import tkinter as tk
import time
import random

t = 0

class MyApp(object):
    def __init__(self, master):
        self.playerCount = 1
        self.playerNum = 2
        self.roundnum = 3
        self.pressNum = 0
        self.roundCount = 1
        self.text = tk.Text(master)
        #self.text.bind('<Key>', self.callback)
        self.text.pack()
        self.text.focus()
        self.startGame()

    def callback(self, event):
        delta = time.time() - self.t
        print('{}'.format(delta))
        self.pressNum = self.pressNum + 1
        if self.pressNum >= self.playerNum:
            self.text.unbind('<Key>')
            if self.roundCount >= self.roundnum:
                self.text.unbind('<Key>')
                print('End of game')
            else:
                self.roundCount = self.roundCount + 1
                self.pressNum = 0
                print('Next round starts soon')
                self.startGame()
            
    
    def startGame(self):
        self.text.bind('<Key>', self.callback)
        time.sleep(random.randint(1,5))
        print('Turn %s, Press button now!' % self.roundCount)
        self.t = time.time()        
                    
        
        

root = tk.Tk()
app = MyApp(root)
root.mainloop()