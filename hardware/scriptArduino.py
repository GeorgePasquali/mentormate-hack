import serial

ser = serial.Serial('COM6',baudrate = 9600, timeout=1)

def getValues():
    ser.write(b'g')
    arduinoData = ser.readline()
    return arduinoData

while 1:
  
    print(getValues())
