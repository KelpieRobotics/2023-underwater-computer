import clientClass

client = clientClass.TCPClient("192.168.137.1", 9000)

client.connect()
while True:
    message = input("")
    if message == "quit":
        client.disconnect()
        break
    client.send(message)