import toga




"""
Legally stream music!
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import socket
import os
import time


SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 # send 4096 bytes each time step

host = "IP"
port = 5001

s = socket.socket()
s.connect((host, port))
doneCommand = False
s.send("Null".encode())

class Notify(toga.App):

    def startup(self):

        s = socket.socket()
        s.connect((host, port))
        main_box = toga.Box(style=Pack(direction=COLUMN))
        
        connectBtn = toga.Button(
            "CONNECT",
            on_press=self.runConnect,
            style=Pack(padding=5)
        )
        shuffleBtn = toga.Button(
            "SHUFFLE",
            on_press=self.sendMessage_shuffle,
            style=Pack(padding=5)
        )
        playBtn = toga.Button(
            "PLAY / STOP",
            on_press=self.sendMessage_play,
            style=Pack(padding=5)
        )
        
        nextBtn = toga.Button(
            ">>",
            on_press=self.sendMessage_next,
            style=Pack(padding=5)
        )
        
        backBtn = toga.Button(
            "<<",
            on_press=self.sendMessage_back,
            style=Pack(padding=5)
        )
        
        upBtn = toga.Button(
            "+",
            on_press=self.sendMessage_up,
            style=Pack(padding=5)
        )
        
        downBtn = toga.Button(
            "-",
            on_press=self.sendMessage_down,
            style=Pack(padding=5)
        )
        
        muteBtn = toga.Button(
            "MUTE",
            on_press=self.sendMessage_mute,
            style=Pack(padding=5)
        )
        
        forwardBtn = toga.Button(
            ">|",
            on_press=self.sendMessage_forward,
            style=Pack(padding=5)
        )
        
        backwardBtn = toga.Button(
            "|<",
            on_press=self.sendMessage_backward,
            style=Pack(padding=5)
        )


        

       #main_box.add(connectBtn)                
        main_box.add(playBtn)
        main_box.add(nextBtn)
        main_box.add(backBtn)
        main_box.add(upBtn)
        main_box.add(downBtn)
        main_box.add(muteBtn)
        main_box.add(forwardBtn)
        main_box.add(backwardBtn)
        main_box.add(shuffleBtn)

        
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

        return main_box

    def sendMessage_seek(self, widget):

    
        temp  = seekSlider.get()
        s.send("TEST".encode())  

    
    def sendMessage_play(self, widget):
        
        print("PLAY")
        s.send("play".encode())
        time.sleep(0.05)
        s.send("play".encode())
        time.sleep(0.05)

        doneCommand = True

    def sendMessage_next(self, widget):
        print("NEXT")
        s.send("forward".encode())
        time.sleep(0.05)
        s.send("forward".encode())
        time.sleep(0.05)

        doneCommand = True        
    def sendMessage_back(self, widget):
        print("BACK")
        s.send("backward".encode())
        time.sleep(0.05)
        s.send("backward".encode())
        time.sleep(0.05)

        doneCommand = True           
    def sendMessage_up(self, widget):
        print("UP")
        s.send("up_volume".encode())
        time.sleep(0.05)
        s.send("up_volume".encode())
        time.sleep(0.05)

        doneCommand = True           
    def sendMessage_down(self, widget):
        print("DOWN")
        s.send("down_volume".encode())
        time.sleep(0.05)
        s.send("down_volume".encode())
        time.sleep(0.05)

                   
    def sendMessage_mute(self, widget):
        print("MUTE")
        s.send("mute".encode())
        time.sleep(0.05)
        s.send("mute".encode())
        time.sleep(0.05)

        doneCommand = True           
    def sendMessage_forward(self, widget):
        print("FORWARD")
        s.send("skip".encode())
        time.sleep(0.05)
        s.send("skip".encode())
        time.sleep(0.05)

        doneCommand = True          
    def sendMessage_backward(self, widget):
        print("BACKWARD")
        s.send("previous".encode())
        time.sleep(0.05)
        s.send("previous".encode())
        time.sleep(0.05)

        doneCommand = True           
    def runConnect(self,widget):
        s.connect((host, port))
        s.send("connection_request".encode())
        time.sleep(0.05)
        s.send("connection_request".encode())
        time.sleep(0.05)
  
        doneCommand = True
            
    def sendMessage_shuffle(self, widget):
        print("shuffle")
        s.send("shuffle".encode()) 
        time.sleep(0.05)
        s.send("shuffle".encode())
        time.sleep(0.05)

        doneCommand = True

    


def main():
    return Notify()

if __name__ == '__main__':
    while True:
        main()
    main().main_loop()  
    
