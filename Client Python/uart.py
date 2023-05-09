import serial
import clientClass
import threading

baudrate = 115200
statusPin = 16

def start_UART_relay(_serial, _client):
        while True:
            if _serial.in_waiting <= 0: continue
            message = _serial.readline()
            #print(message)
            _client.send(message)

serial_mcu = serial.Serial('/dev/ttyAMA0', baudrate, timeout=1)
debug_mcu = serial.Serial('/dev/ttyAMA1', baudrate, timeout=1)

thread_alive = True

client = clientClass.TCPClient("192.168.2.1", 7000, serial_mcu, statusPin)

## Uncomment for third serial connection, used for debug
# debug = serial.Serial('/dev/serial0', 115200)
# debug_client = clientClass.UART_TCPClient("10.0.0.106", 9000, debug)

client.connect()

receiveThread_Serial = threading.Thread(target=start_UART_relay, args = (serial_mcu, client))
receiveThread_Debug = threading.Thread(target=start_UART_relay, args = (debug_mcu, client))

receiveThread_Serial.start()
receiveThread_Debug.start()

