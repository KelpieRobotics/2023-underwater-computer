import clientClass
import datetime
from datetime import timezone

client = clientClass.TCPClient("127.0.0.1", 9000)

client.connect()
while True:

    message = input("")
    if message == "quit":
        client.disconnect()
        break
    
    client.send(message)