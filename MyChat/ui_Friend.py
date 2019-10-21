# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_Friend.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Friend_Dialog(object):
    def setupUi(self, Friend_Dialog):
        Friend_Dialog.setObjectName("Friend_Dialog")
        Friend_Dialog.resize(308, 256)
        self.buttonBox = QtWidgets.QDialogButtonBox(Friend_Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(100, 200, 193, 28))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_3 = QtWidgets.QLabel(Friend_Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 60, 191, 41))
        self.label_3.setStyleSheet("font: 20pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.layoutWidget = QtWidgets.QWidget(Friend_Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 140, 243, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.user_id_lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.user_id_lineEdit.setMinimumSize(QtCore.QSize(170, 20))
        self.user_id_lineEdit.setMaximumSize(QtCore.QSize(170, 20))
        self.user_id_lineEdit.setObjectName("user_id_lineEdit")
        self.horizontalLayout.addWidget(self.user_id_lineEdit)

        self.retranslateUi(Friend_Dialog)
        self.buttonBox.accepted.connect(Friend_Dialog.accept)
        self.buttonBox.rejected.connect(Friend_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Friend_Dialog)

    def retranslateUi(self, Friend_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Friend_Dialog.setWindowTitle(_translate("Friend_Dialog", "Find a friend"))
        self.label_3.setText(_translate("Friend_Dialog", "Find a friend"))
        self.label.setText(_translate("Friend_Dialog", "User ID:"))
