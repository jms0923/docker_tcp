import socket
from sensor_input import sensing

# data 생성
dstIp = '192.168.150.26'
dstPort = 80
sensors = sensing()
data = sensors.sensing()

# 소켓 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 연결 및 전송
try:
    sock.connect((dstIp, dstPort))
    sock.sendall(data.encode())
    print('send all data')

    recvData = sock.recv(1024)

    print('receive from server : ' + recvData.decode())

except ValueError:
    print(ValueError)

finally:
    sock.close()
    print('socket closed')

# --------------------------------------------------------------------

# import socket
# import sys
# import threading
# import time
#
# is_access_denied = False
#
# def recv_message(message_socket):
#     while True:
#         #if the socket is closed, break the loop(if not, socket.recv() throws an error)
#         if message_socket._closed == True :
#             break
#         message = message_socket.recv(1024)
#         message = message.decode()
#
#         print(message)
#         #If five users are already connected
#         if "Too many users" in message:
#             message_socket.close()
#             break
#
# def is_closed(socket):
#     if socket._closed == True :
#         return True
#     else :
#         return False
#
# def main():
#     dstIp = '192.168.150.26'
#     dstPort = 80
#
#     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client_socket.connect((dstIp, dstPort))
#
#     print('Host connected')
#
#     th = threading.Thread(target=recv_message, args=(client_socket,))
#     th.start()
#     try :
#         while True:
#             time.sleep(1)
#             if is_closed(client_socket) is True: #This is the case when the connection is denied due to a large number of users.
#                 break
#             message = sys.stdin.readline()
#             client_socket.send(message.encode())
#             prompt()
#             if message[0:4].lower() == 'quit':
#                 break
#     except e:
#         print(e)
#         client_socket.send('quit'.encode())
#     finally:
#         if is_closed(client_socket) is False:
#             client_socket.close()
#         th.join()
#         print("disconnected")
#
# if __name__ == "__main__":
#     main()



