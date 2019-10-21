import sys
from PyQt5.QtWidgets import QDialog,QApplication,QMessageBox
from ui_Friend import Ui_Friend_Dialog
class FriendDialog(QDialog,Ui_Friend_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.uid = ''
    def varyfy_uid(self,uid):
        if uid.isdigit() and len(uid)==4:
            return True
        else:
            return False
    def get_info(self):
        if self.varyfy_uid(self.user_id_lineEdit.text()):
            self.uid = self.user_id_lineEdit.text()
            return True
        else:
            QMessageBox.warning(self, 'Warning', 'invalid user id', QMessageBox.Ok)
            return False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    friend_dialog = FriendDialog()
    flag = False
    while not flag:
        if friend_dialog.exec() == QDialog.Accepted:
            flag = friend_dialog.get_info()
            friend_dialog.close()
        else:
            friend_dialog.close()
            break
    if friend_dialog.uid == '':
        print('canceled')
    else:
        print(friend_dialog.uid)
    sys.exit(app.exec_())
