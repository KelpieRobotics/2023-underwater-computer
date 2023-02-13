import serial
import clientClass

client = clientClass.TCPClient("10.0.0.106", 9000)
ser = serial.Serial('/dev/serial0', 115200)

client.connect()
try:
    while True:
        message = ser.readline()
        #print(message.decode())
        client.send(message)
except KeyboardInterrupt:
    client.disconnect()
    ser.close()
