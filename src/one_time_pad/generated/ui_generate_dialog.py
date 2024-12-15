# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'generate_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_GenerateDialog(object):
    def setupUi(self, GenerateDialog):
        if not GenerateDialog.objectName():
            GenerateDialog.setObjectName(u"GenerateDialog")
        GenerateDialog.resize(644, 422)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentNew))
        GenerateDialog.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(GenerateDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titleLabel = QLabel(GenerateDialog)
        self.titleLabel.setObjectName(u"titleLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleLabel.sizePolicy().hasHeightForWidth())
        self.titleLabel.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(24)
        self.titleLabel.setFont(font)

        self.verticalLayout.addWidget(self.titleLabel)

        self.disclaimerGroupBox = QGroupBox(GenerateDialog)
        self.disclaimerGroupBox.setObjectName(u"disclaimerGroupBox")
        self.verticalLayout_2 = QVBoxLayout(self.disclaimerGroupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.disclaimerLabel = QLabel(self.disclaimerGroupBox)
        self.disclaimerLabel.setObjectName(u"disclaimerLabel")
        sizePolicy.setHeightForWidth(self.disclaimerLabel.sizePolicy().hasHeightForWidth())
        self.disclaimerLabel.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(12)
        self.disclaimerLabel.setFont(font1)
        self.disclaimerLabel.setTextFormat(Qt.TextFormat.PlainText)
        self.disclaimerLabel.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.disclaimerLabel)


        self.verticalLayout.addWidget(self.disclaimerGroupBox)

        self.keyfileGroupBox = QGroupBox(GenerateDialog)
        self.keyfileGroupBox.setObjectName(u"keyfileGroupBox")
        self.verticalLayout_3 = QVBoxLayout(self.keyfileGroupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.nameLabel = QLabel(self.keyfileGroupBox)
        self.nameLabel.setObjectName(u"nameLabel")

        self.verticalLayout_3.addWidget(self.nameLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.keyNameEdit = QLineEdit(self.keyfileGroupBox)
        self.keyNameEdit.setObjectName(u"keyNameEdit")

        self.horizontalLayout.addWidget(self.keyNameEdit)

        self.keyEndingLabel = QLabel(self.keyfileGroupBox)
        self.keyEndingLabel.setObjectName(u"keyEndingLabel")

        self.horizontalLayout.addWidget(self.keyEndingLabel)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.sizeLabel = QLabel(self.keyfileGroupBox)
        self.sizeLabel.setObjectName(u"sizeLabel")

        self.verticalLayout_3.addWidget(self.sizeLabel)

        self.keyfileSizeLayout = QHBoxLayout()
        self.keyfileSizeLayout.setObjectName(u"keyfileSizeLayout")
        self.fileSizeEdit = QLineEdit(self.keyfileGroupBox)
        self.fileSizeEdit.setObjectName(u"fileSizeEdit")
        self.fileSizeEdit.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly)

        self.keyfileSizeLayout.addWidget(self.fileSizeEdit)

        self.unitSelect = QComboBox(self.keyfileGroupBox)
        self.unitSelect.addItem("")
        self.unitSelect.addItem("")
        self.unitSelect.addItem("")
        self.unitSelect.addItem("")
        self.unitSelect.setObjectName(u"unitSelect")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.unitSelect.sizePolicy().hasHeightForWidth())
        self.unitSelect.setSizePolicy(sizePolicy1)

        self.keyfileSizeLayout.addWidget(self.unitSelect)

        self.generateButton = QPushButton(self.keyfileGroupBox)
        self.generateButton.setObjectName(u"generateButton")

        self.keyfileSizeLayout.addWidget(self.generateButton)


        self.verticalLayout_3.addLayout(self.keyfileSizeLayout)

        self.generateProgressBar = QProgressBar(self.keyfileGroupBox)
        self.generateProgressBar.setObjectName(u"generateProgressBar")
        self.generateProgressBar.setValue(0)

        self.verticalLayout_3.addWidget(self.generateProgressBar)


        self.verticalLayout.addWidget(self.keyfileGroupBox)

        self.generateDialogSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.generateDialogSpacer)

        self.buttonLayout_2 = QHBoxLayout()
        self.buttonLayout_2.setObjectName(u"buttonLayout_2")
        self.buttonHorizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonLayout_2.addItem(self.buttonHorizontalSpacer)

        self.doneGeneratingButton = QPushButton(GenerateDialog)
        self.doneGeneratingButton.setObjectName(u"doneGeneratingButton")

        self.buttonLayout_2.addWidget(self.doneGeneratingButton)


        self.verticalLayout.addLayout(self.buttonLayout_2)


        self.retranslateUi(GenerateDialog)

        self.unitSelect.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(GenerateDialog)
    # setupUi

    def retranslateUi(self, GenerateDialog):
        GenerateDialog.setWindowTitle(QCoreApplication.translate("GenerateDialog", u"Generate Keyfile", None))
        self.titleLabel.setText(QCoreApplication.translate("GenerateDialog", u"Generate Keyfile", None))
        self.disclaimerGroupBox.setTitle(QCoreApplication.translate("GenerateDialog", u"Disclaimer", None))
        self.disclaimerLabel.setText(QCoreApplication.translate("GenerateDialog", u"This Generator uses the secrets module for generating cryptographically strong random numbers using the highest-quality sources provided by the operating System.\n"
"\n"
"The quality of these random numbers may vary depending on your operating system and hardware, so you are free to use your own keys!", None))
        self.keyfileGroupBox.setTitle(QCoreApplication.translate("GenerateDialog", u"Keyfile Settings", None))
        self.nameLabel.setText(QCoreApplication.translate("GenerateDialog", u"Name:", None))
        self.keyNameEdit.setPlaceholderText(QCoreApplication.translate("GenerateDialog", u"generated", None))
        self.keyEndingLabel.setText(QCoreApplication.translate("GenerateDialog", u".key", None))
        self.sizeLabel.setText(QCoreApplication.translate("GenerateDialog", u"Size: (max: 4 GiB)", None))
        self.fileSizeEdit.setText("")
        self.fileSizeEdit.setPlaceholderText(QCoreApplication.translate("GenerateDialog", u"4", None))
        self.unitSelect.setItemText(0, QCoreApplication.translate("GenerateDialog", u"B", None))
        self.unitSelect.setItemText(1, QCoreApplication.translate("GenerateDialog", u"KiB", None))
        self.unitSelect.setItemText(2, QCoreApplication.translate("GenerateDialog", u"MiB", None))
        self.unitSelect.setItemText(3, QCoreApplication.translate("GenerateDialog", u"GiB", None))

        self.generateButton.setText(QCoreApplication.translate("GenerateDialog", u"Generate", None))
        self.doneGeneratingButton.setText(QCoreApplication.translate("GenerateDialog", u"Done", None))
    # retranslateUi

