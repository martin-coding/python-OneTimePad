"""one-time-pad package."""
import argparse
import base64
from pathlib import Path

from platformdirs import user_data_dir

BYTEORDER = "big"

def read_or_initialize_metadata(file_path: Path) -> int:
    """Return next key position of keyfile."""
    path = file_path.parent / (file_path.stem + ".meta")

    if path.exists():
        bytes_val = path.read_bytes()
        return int.from_bytes(bytes_val, BYTEORDER, signed=False)

    new_value: int = 0
    bytes_val = new_value.to_bytes(4, BYTEORDER)
    path.write_bytes(bytes_val)
    return new_value

def write_pos_metadata(file_path: Path, position: int) -> None:
    """Write the current position in metadata file."""
    path = file_path.parent / (file_path.stem + ".meta")
    bytes_val = position.to_bytes(4, BYTEORDER)
    path.write_bytes(bytes_val)

def read_key(key_path: Path, file_pos: int, key_length: int) -> bytes:
    """Return key bytes from keyfile."""
    file_size = key_path.stat().st_size
    if file_size - file_pos < key_length:
        return None
    with key_path.open("rb") as file:
        file.seek(file_pos)
        data = file.read(key_length)
        file_pos = file.tell()
    write_pos_metadata(key_path, file_pos)
    return data

def xor_bytes(data: bytes, key: bytes) -> bytes:
    """Return the xored bytes."""
    return bytes(a ^ b for a, b in zip(data, key, strict=True))

def encode_package(key_path: Path, msg_data: bytes) -> bytes:
    """Encrypt and Encode data for transmission."""
    file_pos = read_or_initialize_metadata(key_path)
    key = read_key(key_path, file_pos, len(msg_data))

    if key is None:
        return None

    encrypted = xor_bytes(msg_data, key)
    pos_data = file_pos.to_bytes(4, BYTEORDER)
    return pos_data + encrypted

def decode_package(key_path: Path, msg_data: bytes) -> bytes:
    """Decode and Decrypt received data."""
    file_pos_msg = int.from_bytes(msg_data[:4], BYTEORDER, signed=False)

    data = msg_data[4:]
    key = read_key(key_path, file_pos_msg, len(data))

    if key is None:
        return None

    return xor_bytes(data, key)

def main() -> None:
    """Jump in point."""
    parser = argparse.ArgumentParser(description="Read mode and message to be encrypted.")
    parser.add_argument("mode", type=str, help="Mode: 'encrypt' or 'decrypt'")
    parser.add_argument("message", type=str, help="Message: Message to be encrypted.")
    args = parser.parse_args()

    mode: str = args.mode
    message: str = args.message

    keys_dir = Path(user_data_dir("one-time-pad", "martin-coding")) / "keystore"
    keys_dir.mkdir(parents=True, exist_ok=True)

    if mode == "encrypt":
        key_path = keys_dir / "send.key"
        if not key_path.exists():
            print("Cannot encrypt without key:", key_path.as_posix())
            return
        msg_data = message.encode("utf-8")
        package = encode_package(key_path, msg_data)
        if package is None:
            print("Remaining bytes from keyfile to small")
            return
        print(base64.b64encode(package).decode("utf-8"))
    elif mode == "decrypt":
        key_path = keys_dir / "receive.key"
        if not key_path.exists():
            print("Cannot decrypt without key:", key_path.as_posix())
            return
        package = base64.b64decode(message)
        decrypted = decode_package(key_path, package)
        if decrypted is None:
            print("Remaining bytes from keyfile to small")
            return
        try:
            print(decrypted.decode("utf-8"))
        except UnicodeDecodeError:
            print("UnicodeDecodeError: You most likely used the wrong key for decryption")

if __name__ == "__main__":
    main()
