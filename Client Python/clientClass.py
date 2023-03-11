import socket
import threading
import time
import datetime
from datetime import timezone

class TCPClient:


    def __init__(self, host, port):
       self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       self.connected = False
       self.receiveThread = threading.Thread(target=self.receive)
       self.host = host
       self.port = port
       self.disconnectFlag = False
    
    def intializeSocket(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        while True:
            try:
                print("Connecting...")
                self.intializeSocket()
                self.client.connect((self.host, self.port))
                self.connected = True
                print("Connected.")
                if self.receiveThread.is_alive():
                    return
                self.receiveThread.start()
                return
            except Exception as e:
                print(e)
                self.intializeSocket()
                self.connected = False
                #print("Connecting Failed. Trying again in 5 seconds...")
                time.sleep(0.5)

        
    def disconnect(self):
        if self.connected == False:
            print("Not connected.")
            return
        
        self.client.close()
        self.disconnectFlag = True
        print("Disconnected.")

    def send(self, data):
        if self.connected == False:
            print("Not connected.")
            return
        try:    
            self.client.sendall(data)
        except Exception:
            print("Error on send.")


    def receive(self):
        while(True):
            if self.disconnectFlag:
                break

            try:
                #self.client.settimeout()
                message = self.client.recv(1024)
                message = message.decode().strip()
                print(message)
            except Exception as e:
                print(e)
                print("Lost host. Trying to reconnect...")
                
                self.disconnect()
                self.connected = False
                self.connect()
                continue
            #except Exception as e:
            #    print("Error on receive.")
            #    print(e)
            #    break 

            



