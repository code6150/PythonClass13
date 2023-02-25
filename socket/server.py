import socket
import threading
import time

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 포트는 외부에서 클라이언트가 이 서버에 접속할 때 사용할 포트
# 이미 사용되고 있는 포트는 피해서 사용.
# 80 -> http
# 443 -> https
# 3306 -> db ... 이런것들 ...

server.bind(('', 6150))
server.listen(1)

# accept -> tuple(연결된 소켓, 연결된 주소)
clientSocket, address = server.accept()

def sendMessage(s):
    while True:
        s.send(input('나 : ').encode('utf-8'))

def receiveMessage(r):
    while True:
        data = r.recv(2048)
        print(f'클라이언트 : {data.decode("utf-8")}')

th1 = threading.Thread(target=sendMessage, args=(clientSocket,))
th2 = threading.Thread(target=receiveMessage(), args=(clientSocket,))
th1.start()
th2.start()

while True:
    time.sleep(1.5)
    pass
