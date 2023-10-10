from notify.app import main
import socket
import os
import time
SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 # send 4096 bytes each time step
        
host = "IP"
port = 5001
        
s = socket.socket()
s.connect((host, port))
s.send("Null".encode())    
#while True:
#    s.send("Null".encode())

if __name__ == '__main__': 
    count = 2
    while count%2 == 0:
        s.send("Null".encode())
        count +=1
    main().main_loop()

