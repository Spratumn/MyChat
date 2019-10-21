import myqueue
import threading
import socket
import time
import re
import struct
def find_connection():
    while not clients.is_full():
        ## 验证用户或注册用户

        client, addr = sockt.accept()  # 建立客户端连接
        #print('find a new sign request')

        # while循环实现阻塞
        recv_flag = False
        while not recv_flag:
            try:
                user_info = client.recv(1024).decode()
                recv_flag = True
            except TimeoutError:
                pass
        user_id,password = user_info.split(',')

        if user_id =='0' and password == '0':
            print('sign canceled')
            client.send('sign canceled'.encode())
            client.close()
        elif user_id in runing_clients:
            if password==client_info[user_id]:
                client.send('Aalerady signed in'.encode())
            else:
                client.send('password error'.encode())
        else:
            if user_id in client_info:
                if password == client_info[user_id]:
                    client.send('ok'.encode())
                    clients.enque((client, addr,user_id))
                    runing_clients.add(user_id)
                    print('current thread count: ',threading.active_count())
                else:
                    client.send('password error'.encode())
                    client.close()
            else:
                client_info[user_id]=password
                client.send('ok'.encode())
                print('current thread count: ',threading.active_count())
                clients.enque((client, addr,user_id))
                runing_clients.add(user_id)

def communicate():
        client,addr,user_id = clients.deque()
        #print('find connection at address: '+ str(addr))
        print(user_id,' signed in')
        chatting = False
        friend_id = ''
        while True:
            ### 与服务器沟通测试连接情况以及配置功能
            if not chatting:
                # while循环实现阻塞
                recv_flag = False
                while not recv_flag:
                    try:
                        msg = client.recv(1024).decode()
                        recv_flag = True
                    except TimeoutError:
                        pass
                # 根据收到的msg判断是否是要查找好友
                friend_match = re.match("....\d{4}....", msg)
                if friend_match:
                    friend_id = re.findall('\d+', friend_match.string)[0]
                    if friend_id in client_info and friend_id != user_id:
                        # 告诉客户端正式会话开始
                        print('find friend id: ', friend_id)
                        client.send('1'.encode())
                        chatting = True
                    else:
                        client.send('0'.encode())
                # 正常的连接测试
                else:
                    if msg == 'byby':
                        client.close()
                        runing_clients.remove(user_id)
                        #print(str(addr) + 'closed')
                        print(user_id, ' signed out')
                        break
                    else:
                        words = 'You said:%s' % msg
                        client.send(words.encode())

            ### 开始会话
            else:
                # 消息队列不为空时，将消息发给客户端
                if user_id in unread_msg and unread_msg[user_id].length>0:
                    for i in range(unread_msg[user_id].length):
                        mssg = unread_msg[user_id].deque()
                        client.send(mssg.encode())
                try:
                    # 接受信息
                    msg = client.recv(1024).decode()
                    # 消息入缓存队列
                    if friend_id not in unread_msg:
                        unread_msg[friend_id] = myqueue.myqueue(10)
                    unread_msg[friend_id].enque(msg)
                    # 说了再见
                    if 'byby' in msg:
                        client.close()
                        runing_clients.remove(user_id)
                        print(user_id, ' signed out')
                        break
                # 接受信息超时（未收到信息）
                except TimeoutError:
                    pass

def delay_warning():
    client, addr,user_id = clients.deque()
    words= ''
    client.send(words.encode())
    time.sleep(2)
    client.close()
if __name__ == '__main__':
    ### 保存客户端信息,字典存储,关机时存到文件 用户id：密码
    client_info = dict()

    ### 保存沟通记录，字典存储，关机时存到文件 用户id相连：内容字符串
    chat_countent = dict()

    ### 消息缓存，字典存储，键是用户id，值是消息队列（最长缓存200条信息）
    #当消息队列不为空且用户在线时，将消息队列逐条发给对应的用户
    # 关机时若消息队列不为空，则存入文件，开机时读入
    unread_msg = dict()

    ### 记录已登录的用户id
    runing_clients = set()

    ### 建立socket并监听
    max_connection = 5  # 最大连接个数
    clients = myqueue.myqueue(max_connection)
    sockt = socket.socket()  # 创建 socket 对象
    host = socket.gethostname()  # 获取本地主机名
    port = 1234  # 设置端口
    sockt.bind((host, port))  # 绑定端口
    sockt.listen(max_connection)  # 等待客户端连接

    # 设置1s超时
    val = struct.pack("Q", 1000)
    sockt.setsockopt(socket.SOL_SOCKET, socket.SO_RCVTIMEO, val)

    get_connect = threading.Thread(target=find_connection)
    get_connect.start()
    # print('current thread count: ',threading.active_count())
    while True:
        thread_count = threading.active_count()
        if not clients.is_empty() and thread_count < max_connection+2:
            threading.Thread(target=communicate).start()
        elif not clients.is_empty() and thread_count == max_connection+2:
            threading.Thread(target=delay_warning).start()


