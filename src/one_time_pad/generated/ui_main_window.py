# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTabWidget,
    QToolButton, QTreeView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.encryptTab = QWidget()
        self.encryptTab.setObjectName(u"encryptTab")
        self.horizontalLayout = QHBoxLayout(self.encryptTab)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.encryptFileLayout = QVBoxLayout()
        self.encryptFileLayout.setObjectName(u"encryptFileLayout")
        self.encryptButtonLayout = QHBoxLayout()
        self.encryptButtonLayout.setObjectName(u"encryptButtonLayout")
        self.encryptKeyfilesLabel = QLabel(self.encryptTab)
        self.encryptKeyfilesLabel.setObjectName(u"encryptKeyfilesLabel")

        self.encryptButtonLayout.addWidget(self.encryptKeyfilesLabel)

        self.encryptButtonSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.encryptButtonLayout.addItem(self.encryptButtonSpacer)

        self.enDeleteButton = QToolButton(self.encryptTab)
        self.enDeleteButton.setObjectName(u"enDeleteButton")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditDelete))
        self.enDeleteButton.setIcon(icon)

        self.encryptButtonLayout.addWidget(self.enDeleteButton)

        self.enGenerateButton = QToolButton(self.encryptTab)
        self.enGenerateButton.setObjectName(u"enGenerateButton")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentNew))
        self.enGenerateButton.setIcon(icon1)

        self.encryptButtonLayout.addWidget(self.enGenerateButton)

        self.enExportButton = QToolButton(self.encryptTab)
        self.enExportButton.setObjectName(u"enExportButton")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoUp))
        self.enExportButton.setIcon(icon2)

        self.encryptButtonLayout.addWidget(self.enExportButton)

        self.enImportButton = QToolButton(self.encryptTab)
        self.enImportButton.setObjectName(u"enImportButton")
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoDown))
        self.enImportButton.setIcon(icon3)
        self.enImportButton.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)

        self.encryptButtonLayout.addWidget(self.enImportButton)


        self.encryptFileLayout.addLayout(self.encryptButtonLayout)

        self.encryptKeyfilesView = QTreeView(self.encryptTab)
        self.encryptKeyfilesView.setObjectName(u"encryptKeyfilesView")

        self.encryptFileLayout.addWidget(self.encryptKeyfilesView)


        self.horizontalLayout.addLayout(self.encryptFileLayout)

        self.encryptLayout = QVBoxLayout()
        self.encryptLayout.setObjectName(u"encryptLayout")
        self.inputMessageLabel = QLabel(self.encryptTab)
        self.inputMessageLabel.setObjectName(u"inputMessageLabel")

        self.encryptLayout.addWidget(self.inputMessageLabel)

        self.inputMessageField = QPlainTextEdit(self.encryptTab)
        self.inputMessageField.setObjectName(u"inputMessageField")

        self.encryptLayout.addWidget(self.inputMessageField)

        self.encryptButton = QPushButton(self.encryptTab)
        self.encryptButton.setObjectName(u"encryptButton")

        self.encryptLayout.addWidget(self.encryptButton)

        self.outputCiphertextField = QPlainTextEdit(self.encryptTab)
        self.outputCiphertextField.setObjectName(u"outputCiphertextField")

        self.encryptLayout.addWidget(self.outputCiphertextField)


        self.horizontalLayout.addLayout(self.encryptLayout)

        self.tabWidget.addTab(self.encryptTab, "")
        self.decryptTab = QWidget()
        self.decryptTab.setObjectName(u"decryptTab")
        self.horizontalLayout_2 = QHBoxLayout(self.decryptTab)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.decryptFileLayout = QVBoxLayout()
        self.decryptFileLayout.setObjectName(u"decryptFileLayout")
        self.decryptButtonLayout = QHBoxLayout()
        self.decryptButtonLayout.setObjectName(u"decryptButtonLayout")
        self.decryptKeyfilesLabel = QLabel(self.decryptTab)
        self.decryptKeyfilesLabel.setObjectName(u"decryptKeyfilesLabel")

        self.decryptButtonLayout.addWidget(self.decryptKeyfilesLabel)

        self.decryptButtonSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.decryptButtonLayout.addItem(self.decryptButtonSpacer)

        self.deDeleteButton = QToolButton(self.decryptTab)
        self.deDeleteButton.setObjectName(u"deDeleteButton")
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListRemove))
        self.deDeleteButton.setIcon(icon4)

        self.decryptButtonLayout.addWidget(self.deDeleteButton)

        self.deAddButton = QToolButton(self.decryptTab)
        self.deAddButton.setObjectName(u"deAddButton")
        icon5 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.deAddButton.setIcon(icon5)
        self.deAddButton.setArrowType(Qt.ArrowType.NoArrow)

        self.decryptButtonLayout.addWidget(self.deAddButton)


        self.decryptFileLayout.addLayout(self.decryptButtonLayout)

        self.decryptKeyfilesView = QTreeView(self.decryptTab)
        self.decryptKeyfilesView.setObjectName(u"decryptKeyfilesView")

        self.decryptFileLayout.addWidget(self.decryptKeyfilesView)


        self.horizontalLayout_2.addLayout(self.decryptFileLayout)

        self.decryptLayout = QVBoxLayout()
        self.decryptLayout.setObjectName(u"decryptLayout")
        self.inputCiphertextLabel = QLabel(self.decryptTab)
        self.inputCiphertextLabel.setObjectName(u"inputCiphertextLabel")

        self.decryptLayout.addWidget(self.inputCiphertextLabel)

        self.inputCiphertextField = QPlainTextEdit(self.decryptTab)
        self.inputCiphertextField.setObjectName(u"inputCiphertextField")

        self.decryptLayout.addWidget(self.inputCiphertextField)

        self.decryptButton = QPushButton(self.decryptTab)
        self.decryptButton.setObjectName(u"decryptButton")

        self.decryptLayout.addWidget(self.decryptButton)

        self.outputMessageField = QPlainTextEdit(self.decryptTab)
        self.outputMessageField.setObjectName(u"outputMessageField")

        self.decryptLayout.addWidget(self.outputMessageField)


        self.horizontalLayout_2.addLayout(self.decryptLayout)

        self.tabWidget.addTab(self.decryptTab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"OTP - Manager", None))
        self.encryptKeyfilesLabel.setText(QCoreApplication.translate("MainWindow", u"Available keyfiles:", None))
#if QT_CONFIG(tooltip)
        self.enDeleteButton.setToolTip(QCoreApplication.translate("MainWindow", u"Delete Keyfile", None))
#endif // QT_CONFIG(tooltip)
        self.enDeleteButton.setText(QCoreApplication.translate("MainWindow", u"-", None))
#if QT_CONFIG(tooltip)
        self.enGenerateButton.setToolTip(QCoreApplication.translate("MainWindow", u"Generate Keyfile", None))
#endif // QT_CONFIG(tooltip)
        self.enGenerateButton.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(tooltip)
        self.enExportButton.setToolTip(QCoreApplication.translate("MainWindow", u"Export keyfile", None))
#endif // QT_CONFIG(tooltip)
        self.enExportButton.setText(QCoreApplication.translate("MainWindow", u"-", None))
#if QT_CONFIG(tooltip)
        self.enImportButton.setToolTip(QCoreApplication.translate("MainWindow", u"Import keyfile", None))
#endif // QT_CONFIG(tooltip)
        self.enImportButton.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.inputMessageLabel.setText(QCoreApplication.translate("MainWindow", u"Input message:", None))
        self.encryptButton.setText(QCoreApplication.translate("MainWindow", u"Encrypt", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.encryptTab), QCoreApplication.translate("MainWindow", u"Encrypt", None))
        self.decryptKeyfilesLabel.setText(QCoreApplication.translate("MainWindow", u"Available keyfiles:", None))
#if QT_CONFIG(tooltip)
        self.deDeleteButton.setToolTip(QCoreApplication.translate("MainWindow", u"Remove Keyfile", None))
#endif // QT_CONFIG(tooltip)
        self.deDeleteButton.setText(QCoreApplication.translate("MainWindow", u"-", None))
#if QT_CONFIG(tooltip)
        self.deAddButton.setToolTip(QCoreApplication.translate("MainWindow", u"Add Keyfile", None))
#endif // QT_CONFIG(tooltip)
        self.deAddButton.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.inputCiphertextLabel.setText(QCoreApplication.translate("MainWindow", u"Input ciphertext:", None))
        self.decryptButton.setText(QCoreApplication.translate("MainWindow", u"Decrypt", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.decryptTab), QCoreApplication.translate("MainWindow", u"Decrypt", None))
    # retranslateUi

