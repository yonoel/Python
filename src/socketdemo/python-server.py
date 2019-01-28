import socket
import time

def Main():
    try:
        host = "127.0.0.1"
        port = 5001
        mySocket = socket.socket()
        mySocket.bind((host,port))

        mySocket.listen(1)
        conn,addr = mySocket.accept()
        print ("server start,connection from",str(addr))

        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            print ("from connected  user: " + str(data))

            data = str(data)
            print ("Received from User: " + str(data))

            data = input("?")
            conn.send(data.encode())

        conn.close()
    except Exception as e:
        print ("has error",e)

if __name__ == "__main__":
    Main()
