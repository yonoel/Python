import socket
import time

def Main():
    try:
        host = "127.0.0.1"
        port = 5001
        mySocket = socket.socket()
        mySocket.connect((host,port))

        message = input("?")

        print ("server start")

        while message != "q":
            mySocket.send(message.encode())
            data = mySocket.recv(1024).decode()

            print ("receive data:",str(data))
            message = input("?")

        mySocket.close()

    except Exception as e :
        print ("has error",e)

if __name__ == "__main__":
    Main()
