import socket
import time


def Main():
    try:
        host = "192.168.1.143"
        port = 8080
        mySocket = socket.socket()
        mySocket.connect((host, port))
        print("2")
        message = input("?")

        print("server start")

        while message != "q":
            mySocket.send(message.encode())
            data = mySocket.recv(1024).decode()

            print("receive data:", str(data))
            message = input("?")

        mySocket.close()

    except Exception as e:
        print("has error", e)


if __name__ == "__main__":
    Main()
