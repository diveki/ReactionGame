import tkinter as tk
import time
import random
import pandas as pd
import numpy as np

t = 0

class Player:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name
    
    def get_name(self):
        return self.name
    
    def get_button(self):
        return self.button
    
    def set_button(self, button):
        self.button = button
    
    
class GeneralGame(tk.Frame):
    def __init__(self, master, numberPlayer=2, roundNumbers=3, **kw):
        tk.Frame.__init__(self, master)
        self.playerNum = numberPlayer
        self.roundnum = roundNumbers
        self.pressNum = 0
        self.roundCount = 1
        self.maxWait = 5
        self.players = {}
        self.results = {}
        self.resultsContainer = pd.DataFrame(columns=['Round', 'Position', 'Button', 'Delay', 'Name'])
        self.__dict__.update(kw)
        self.initializeGame()
    
    def initializeGame(self):
        for ii in range(self.playerNum):
            self.players[ii+1] = self.set_players(ii+1)
    
    def startGame(self):
        for ii in range(self.numberOfRounds):
            self.startMessage(ii+1)
            startTime = time()
            self.startSignal()
    
    def getPlayerName(self, pressedKey):
        for pid in range(len(self.players)):
            player = self.players[pid+1]
            if player.get_button() == pressedKey:
                return player.name
    
    def getRoundWinner(self):
        names = list(map(lambda x: x[2], self.results[self.roundCount]))
        names = list(filter(lambda x: x != 'Invalid', names))
        if names == []:
            print('Nobody pressed the right button')
            return 'Nobody'
        else:
            return names[0]
    
    def addResult2Container(self):
        rounds = []
        positions = []
        button = []
        delay = []
        name = []
        for pos, item in enumerate(self.results[self.roundCount]):
            positions.append(pos)
            rounds.append(self.roundCount)
            button.append(item[0])
            delay.append(item[1])
            name.append(item[2])
        self.resultsContainer = pd.concat([self.resultsContainer, pd.DataFrame(np.array([rounds, positions, button, delay, name]).T, columns = ['Round', 'Position', 'Button', 'Delay', 'Name'])])
        self.resultsContainer.reset_index()
            
        
        
                    
            
            
class MyApp(GeneralGame):
    def __init__(self, master, numberPlayer=2, roundNumbers=3):
        GeneralGame.__init__(self, master, numberPlayer=numberPlayer, roundNumbers=roundNumbers)
        self.text = tk.Text(master)
        self.text.pack()
        self.text.focus()
        self.startGame()

    def callback(self, event):
        delta = time.time() - self.t
        pressedKey = event.char
        self.pressNum = self.pressNum + 1
        if self.pressNum == 1:
            self.results[self.roundCount] = [[pressedKey, delta, self.getPlayerName(pressedKey)]]
        else:
            self.results[self.roundCount].append([pressedKey, delta, self.getPlayerName(pressedKey)])
        self.text.unbind(event.char)
        if self.pressNum >= self.playerNum:
            self.addResult2Container()
            print('Winner is: %s, with seconds delay!' % (self.getRoundWinner()))
            if self.roundCount >= self.roundnum:
                print('End of game')
            else:
                self.roundCount = self.roundCount + 1
                self.pressNum = 0
                print('Next round starts soon')
                self.startGame()
    
    def startGame(self):
        self.text.bind(self.players[1].button, self.callback)
        self.text.bind(self.players[2].button, self.callback)
        time.sleep(random.randint(1,5))
        print('Turn %s, Press button now!' % self.roundCount)
        self.t = time.time()     
                    
    def set_players(self, pid):
        name = input('Name of %sth player: ' % pid)
        p = Player(name)
        button = input('Press the button you want to use: ')
        p.set_button(button)
        return p
        
        

root = tk.Tk()
app = MyApp(root)
root.mainloop()