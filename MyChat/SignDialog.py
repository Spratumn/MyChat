import sys
from PyQt5.QtWidgets import QDialog,QApplication,QMessageBox
from ui_Sign import Ui_sin_Dialog
class SignDialog(QDialog,Ui_sin_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.uid = ''
        self.password = ''
    def varyfy_uid(self,uid):
        if uid.isdigit() and len(uid)==4:
            return True
        else:
            return False
    def varyfy_password(self,password):
        if password.isalnum():
            return True
        else:
            return False
    def get_info(self):
        if self.varyfy_uid(self.user_id_lineEdit.text()) and self.varyfy_password(self.password_lineEdit.text()):
            self.uid = self.user_id_lineEdit.text()
            self.password = self.password_lineEdit.text()
            return True
        elif not self.varyfy_uid(self.user_id_lineEdit.text()):
            QMessageBox.warning(self, 'Warning', 'invalid user id', QMessageBox.Ok)
            return False
        elif not self.varyfy_password(self.password_lineEdit.text()):
            QMessageBox.warning(self, 'Warning', 'invalid password', QMessageBox.Ok)
            return False
if __name__ == '__main__':
    app = QApplication(sys.argv)
    sign_d = SignDialog()
    flag = False
    while not flag:
        if sign_d.exec() == QDialog.Accepted:
            flag = sign_d.get_info()
            sign_d.close()
        else:
            sign_d.close()
            break
    if sign_d.uid == '' or sign_d.password == '':
        print('canceled')
    else:
        print(sign_d.uid)
        print(sign_d.password)

    sys.exit(app.exec_())
