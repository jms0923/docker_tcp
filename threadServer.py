import socket
import threading
import sys
import json


def recv_msg(client_socket, addr):
    # while True:
    message = client_socket.recv(1024).decode()
    jsonObj = makeJsonObject(message)
    # print(type(jsonObj))
    # print(jsonObj)
    print(type(jsonObj))
    print(str(addr) + ' : ', jsonObj)
    disconnect(client_socket)
    print(str(addr) + ' ' + 'disconnected\n')


def makeJsonObject(msg):
    jsonObj = json.loads(msg)
    # jsonObj = json.dumps(msg)
    return jsonObj


def disconnect(client_socket):
    client_socket.close()
    if client_socket in clientList:
        clientList.remove(client_socket)


def main():
    port = 80
    numOfClient = 5
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', port))
    server_socket.listen(numOfClient)
    print('waiting cllient...')


    while True:
        (client_socket, addr) = server_socket.accept()
        if len(clientList) > numOfClient - 1:
            client_socket.close()
            print('too many client')

        else:
            clientList.append(client_socket)
            print(addr[1], ' connected')
            client_socket.send('received successfully'.encode())

            client_thread = threading.Thread(target=recv_msg, args=(client_socket, addr[1]))
            client_thread.setDaemon(True)
            client_thread.start()
            threadList.append(client_thread)

    # server_socket.close()


if __name__ == "__main__":
    clientList = []
    threadList = []
    main()
