"""Python module for basic otp related functions."""

import base64
from pathlib import Path

import one_time_pad.config as cfg


def read_pos_metadata(file_path: Path) -> int:
    """Return key position from metadata file."""
    path = file_path.parent / (file_path.stem + ".meta")

    if path.exists():
        bytes_val = path.read_bytes()
        return int.from_bytes(bytes_val, cfg.BYTEORDER, signed=False)

    new_value: int = 0
    bytes_val = new_value.to_bytes(4, cfg.BYTEORDER)
    path.write_bytes(bytes_val)
    return new_value


def write_pos_metadata(file_path: Path, position: int) -> None:
    """Write the current position to metadata file."""
    path = file_path.parent / (file_path.stem + ".meta")
    bytes_val = position.to_bytes(4, cfg.BYTEORDER)
    path.write_bytes(bytes_val)


def read_key(key_path: Path, file_pos: int, key_length: int) -> bytes:
    """Return key bytes from keyfile and update position."""
    file_size = key_path.stat().st_size
    if file_size - file_pos < key_length:
        return None
    with key_path.open("rb") as file:
        file.seek(file_pos)
        data = file.read(key_length)
        file_pos = file.tell()
    if file_pos > read_pos_metadata(key_path):
        write_pos_metadata(key_path, file_pos)
    return data


def _xor_bytes(data: bytes, key: bytes) -> bytes:
    return bytes(a ^ b for a, b in zip(data, key, strict=True))


def encode_data(key_path: Path, message: str) -> str:
    """Return encoded ciphertext package."""
    msg_data = message.encode(cfg.ENCODING)

    file_pos = read_pos_metadata(key_path)
    key = read_key(key_path, file_pos, len(msg_data))

    if key is None:
        return None

    encrypted = _xor_bytes(msg_data, key)
    pos_data = file_pos.to_bytes(4, cfg.BYTEORDER)
    package = pos_data + encrypted
    return base64.a85encode(package).decode(cfg.ENCODING)


def decode_data(key_path: Path, ciphertext: str) -> str:
    """Return decoded cleartext message."""
    package = base64.a85decode(ciphertext)
    key_pos = int.from_bytes(package[:4], cfg.BYTEORDER, signed=False)
    msg_data = package[4:]

    key = read_key(key_path, key_pos, len(msg_data))

    if key is None:
        return None

    decrypted = _xor_bytes(msg_data, key)
    return decrypted.decode(cfg.ENCODING)
