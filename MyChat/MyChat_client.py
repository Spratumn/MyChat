# -*- coding: utf-8 -*-
import sys
import socket
import myqueue
import threading
from ui_Client import Ui_Dialog
from SignDialog import SignDialog
from FriendDialog import FriendDialog
from PyQt5.QtWidgets import QDialog,QApplication,QMessageBox
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSignal
import struct

class Client(QDialog,Ui_Dialog):
    recv_signal = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        ### 定义属性
        self.user_id = ''
        self.message_que = myqueue.myqueue(10)
        self.text = ""
        self.chatting = False
        ### 设定初始界面属性
        self.send_Button.setDisabled(True)
        self.friends_Button.setDisabled(True)
        ###信号槽绑定
        self.send_Button.clicked.connect(self.send_mssage)
        self.sign_Button.clicked.connect(self.sign)
        self.friends_Button.clicked.connect(self.connect_friend)
        self.recv_signal.connect(self.add_recv_msg)

    def sign(self):
        self.sockt = socket.socket()  # 创建 socket 对象
        self.host = socket.gethostname()  # 获取本地主机名
        self.port = 1234  # 设置端口
        # 设置1s超时关闭
        val = struct.pack("Q", 1000)
        self.sockt.setsockopt(socket.SOL_SOCKET, socket.SO_RCVTIMEO, val)
        self.sockt.connect((self.host, self.port))
        ## 发送用户信息
        sign_d = SignDialog()
        user_info = '0' + ',' + '0'
        flag = False
        while not flag:
            if sign_d.exec() == QDialog.Accepted:
                flag = sign_d.get_info()
                sign_d.close()
            else:
                sign_d.close()
                break
        if sign_d.uid == '' or sign_d.password == '':
            # print('canceled')
            QMessageBox.warning(self, 'Warning', 'sign canceled', QMessageBox.Ok)
        else:
            self.user_id = sign_d.uid
            user_info = str(sign_d.uid)+','+str(sign_d.password)
        self.sockt.send(user_info.encode())
        sign_status = self.sockt.recv(1024).decode()
        if sign_status == 'ok':
            self.setWindowTitle(self.user_id)
            self.send_Button.setDisabled(False)
            self.friends_Button.setDisabled(False)
            self.sign_Button.setVisible(False)
            QMessageBox.information(self, 'OK', 'sign succeed', QMessageBox.Ok)
        else:
            QMessageBox.warning(self, 'Warning', sign_status, QMessageBox.Ok)

    # 开始正式会话后新建一个线程不断接收信息，接收到信息后触发信号
    def recv_msg(self):
        while True:
            try:
                msg = self.sockt.recv(1024).decode()
                self.recv_signal.emit(msg)
            except TimeoutError:
                pass

    def add_recv_msg(self,msg):
        if self.message_que.is_full():
            self.message_que.deque()
        self.message_que.enque(msg)
        self.print_message()

    def send_mssage(self):
        # 尚未正式会话，处于和服务器测试阶段
        if not self.chatting:
            input_msg = self.send_msg.toPlainText()
            if input_msg != '':
                msg = self.user_id + ":" + input_msg +'\n'
                self.send_msg.setText('')
                if self.message_que.is_full():
                    self.message_que.deque()
                self.message_que.enque(msg)
                self.sockt.send(msg.encode())
                receive_msg = self.sockt.recv(1024).decode()
                if receive_msg !='':
                    if self.message_que.is_full():
                        self.message_que.deque()
                    self.message_que.enque("server: "+receive_msg+'\n')
                    self.print_message()
            else:
                QMessageBox.warning(self, 'Warning', 'input is empty', QMessageBox.Ok)
        # 开始会话
        else:
            input_msg = self.send_msg.toPlainText()
            if input_msg != '':
                msg = self.user_id + ":" + input_msg +'\n'
                self.send_msg.setText('')
                if self.message_que.is_full():
                    self.message_que.deque()
                self.message_que.enque(msg)
                self.print_message()
                self.sockt.send(msg.encode())
            else:
                QMessageBox.warning(self, 'Warning', 'input is empty', QMessageBox.Ok)


    def connect_friend(self):
        friend_dialog = FriendDialog()
        flag = False
        user_id = '0'
        while not flag:
            if friend_dialog.exec() == QDialog.Accepted:
                flag = friend_dialog.get_info()
                friend_dialog.close()
            else:
                friend_dialog.close()
                break
        if friend_dialog.uid == '':
            QMessageBox.warning(self, 'Warning', 'find canceled', QMessageBox.Ok)
        else:
            user_id = '....'+friend_dialog.uid+'....'
        self.sockt.send(user_id.encode())

        friend_status = self.sockt.recv(1024).decode()
        if friend_status == '1':
            QMessageBox.information(self, 'OK', 'find you friend', QMessageBox.Ok)
            self.friends_Button.setDisabled(True)
            self.chatting = True
            threading.Thread(target=self.recv_msg).start()
        else:
            QMessageBox.warning(self, 'Warning', 'not exist', QMessageBox.Ok)

    def print_message(self):
        if self.message_que.length>1:
            self.text = ''.join(self.message_que.to_list())
        else:
            self.text = self.message_que.deque()
        self.get_msg_label.setText(self.text)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        msg = self.user_id+': byby'
        self.sockt.send(msg.encode())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Client()
    w.show()
    sys.exit(app.exec_())

