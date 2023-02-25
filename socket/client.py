import socket
import threading
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 6150))

def sendMessage(s):
    while True:
        s.send(input('나 : ').encode('utf-8'))

def receiveMessage(r):
    while True:
        data = r.recv(2048)
        print(f'서버 : {data.decode("utf-8")}')
        print('나 : ', end='')

th1 = threading.Thread(target=receiveMessage, args=(client,))
th2 = threading.Thread(target=sendMessage, args=(client,))

# 프로그램은 메인 쓰레드가 코드의 끝에 도달했을 때 종료
th1.start()
th2.start()

# 프로그램 종료. (너무 빠른 while)
# ~~
while True:
    time.sleep(1.5)
    pass
