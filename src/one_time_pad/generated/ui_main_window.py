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
    QSizePolicy, QStatusBar, QTabWidget, QTreeView,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(644, 488)
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
        self.encryptKeyfilesLabel = QLabel(self.encryptTab)
        self.encryptKeyfilesLabel.setObjectName(u"encryptKeyfilesLabel")

        self.encryptFileLayout.addWidget(self.encryptKeyfilesLabel)

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
        self.decryptKeyfilesLabel = QLabel(self.decryptTab)
        self.decryptKeyfilesLabel.setObjectName(u"decryptKeyfilesLabel")

        self.decryptFileLayout.addWidget(self.decryptKeyfilesLabel)

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
        self.menubar.setGeometry(QRect(0, 0, 644, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.encryptKeyfilesLabel.setText(QCoreApplication.translate("MainWindow", u"Available keyfiles:", None))
        self.inputMessageLabel.setText(QCoreApplication.translate("MainWindow", u"Input message:", None))
        self.encryptButton.setText(QCoreApplication.translate("MainWindow", u"Encrypt", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.encryptTab), QCoreApplication.translate("MainWindow", u"Encrypt", None))
        self.decryptKeyfilesLabel.setText(QCoreApplication.translate("MainWindow", u"Available keyfiles:", None))
        self.inputCiphertextLabel.setText(QCoreApplication.translate("MainWindow", u"Input ciphertext:", None))
        self.decryptButton.setText(QCoreApplication.translate("MainWindow", u"Decrypt", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.decryptTab), QCoreApplication.translate("MainWindow", u"Decrypt", None))
    # retranslateUi

