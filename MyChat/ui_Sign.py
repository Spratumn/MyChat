# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_Sign.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_sin_Dialog(object):
    def setupUi(self, sin_Dialog):
        sin_Dialog.setObjectName("sin_Dialog")
        sin_Dialog.resize(308, 256)
        self.buttonBox = QtWidgets.QDialogButtonBox(sin_Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(100, 200, 193, 28))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_3 = QtWidgets.QLabel(sin_Dialog)
        self.label_3.setGeometry(QtCore.QRect(100, 40, 171, 41))
        self.label_3.setStyleSheet("font: 20pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.widget = QtWidgets.QWidget(sin_Dialog)
        self.widget.setGeometry(QtCore.QRect(40, 100, 253, 53))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.user_id_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.user_id_lineEdit.setMinimumSize(QtCore.QSize(170, 20))
        self.user_id_lineEdit.setMaximumSize(QtCore.QSize(170, 20))
        self.user_id_lineEdit.setObjectName("user_id_lineEdit")
        self.horizontalLayout.addWidget(self.user_id_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.password_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.password_lineEdit.setMinimumSize(QtCore.QSize(170, 20))
        self.password_lineEdit.setMaximumSize(QtCore.QSize(170, 20))
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.horizontalLayout_2.addWidget(self.password_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(sin_Dialog)
        self.buttonBox.accepted.connect(sin_Dialog.accept)
        self.buttonBox.rejected.connect(sin_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(sin_Dialog)

    def retranslateUi(self, sin_Dialog):
        _translate = QtCore.QCoreApplication.translate
        sin_Dialog.setWindowTitle(_translate("sin_Dialog", "MyChat"))
        self.label_3.setText(_translate("sin_Dialog", "MyChat"))
        self.label.setText(_translate("sin_Dialog", "User ID:"))
        self.label_2.setText(_translate("sin_Dialog", "Password:"))
