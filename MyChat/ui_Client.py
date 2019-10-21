# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_Client.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(424, 445)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.get_msg_label = QtWidgets.QLabel(Dialog)
        self.get_msg_label.setMinimumSize(QtCore.QSize(400, 200))
        self.get_msg_label.setMaximumSize(QtCore.QSize(400, 200))
        self.get_msg_label.setText("")
        self.get_msg_label.setObjectName("get_msg_label")
        self.verticalLayout.addWidget(self.get_msg_label)
        spacerItem = QtWidgets.QSpacerItem(458, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.send_msg = QtWidgets.QTextEdit(Dialog)
        self.send_msg.setMinimumSize(QtCore.QSize(400, 150))
        self.send_msg.setMaximumSize(QtCore.QSize(400, 150))
        self.send_msg.setObjectName("send_msg")
        self.verticalLayout.addWidget(self.send_msg)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.friends_Button = QtWidgets.QPushButton(Dialog)
        self.friends_Button.setObjectName("friends_Button")
        self.horizontalLayout.addWidget(self.friends_Button)
        spacerItem1 = QtWidgets.QSpacerItem(358, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.sign_Button = QtWidgets.QPushButton(Dialog)
        self.sign_Button.setObjectName("sign_Button")
        self.horizontalLayout.addWidget(self.sign_Button)
        self.send_Button = QtWidgets.QPushButton(Dialog)
        self.send_Button.setObjectName("send_Button")
        self.horizontalLayout.addWidget(self.send_Button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Client"))
        self.friends_Button.setText(_translate("Dialog", "Friends"))
        self.sign_Button.setText(_translate("Dialog", "Sign"))
        self.send_Button.setText(_translate("Dialog", "Send"))
