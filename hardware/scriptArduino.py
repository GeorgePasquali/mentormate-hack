import serial
import urllib
import re
import string
from pprint import pprint
import requests


ser = serial.Serial('COM6',baudrate = 9600, timeout=1)

def getValues():
    ser.write(b'g')
    arduinoData = ser.readline()
    return arduinoData


condition = False


while 1:

    
    cValue = getValues()
    strVal = cValue.decode("UTF-8")
    #print(int.from_bytes(cValue, "big"))
    #ival = strVal.rstrip('\r\n')
    #print(len(strVal))
    #print(type(cValue.decode("UTF-8")))

   
   
   
    strValnew = re.findall(r'\d+',strVal)

    if len(strValnew) != 0:
        #print(len(strValnew))
        #print(strValnew.index(0))
        print(int(strValnew[0]))

    


    if condition == False and cValue < b"13":
        condition = True

    
    
    if condition == True and cValue > b"13":
        condition = False
        
   # print(getValues())
    
    
    
    
