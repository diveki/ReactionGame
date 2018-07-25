import tkinter as tk
import time
import random

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
    
    def determineRoundPlayerNames(self):
        for pid in range(len(self.players)):
            player = self.players[pid+1]
            for ii, item in enumerate(self.results[self.roundCount]):
                if player.get_button() == item[0]:
                    self.results[self.roundCount][ii].append(player.name)
        for ii, item in enumerate(self.results[self.roundCount]):
            if len(item) < 3:
                self.results[self.roundCount][ii].append('Invalid')
    
    def getRoundWinner(self):
        names = list(map(lambda x: x[2], self.results[self.roundCount]))
        names = list(filter(lambda x: x != 'Invalid', names))
        if names == []:
            print('Nobody pressed the right button')
            return 'Nobody'
        else:
            return names[0]
        
                    
            
            
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
            self.results[self.roundCount] = [[pressedKey, delta]]
        else:
            self.results[self.roundCount].append([pressedKey, delta])

        if self.pressNum >= self.playerNum:
            self.text.unbind('<Key>')
            self.determineRoundPlayerNames()
            print('Winner is: %s' % self.getRoundWinner())
            if self.roundCount >= self.roundnum:
                self.text.unbind('<Key>')
                print('End of game')
            else:
                #print(self.results[self.roundCount])
                self.roundCount = self.roundCount + 1
                self.pressNum = 0
                print('Next round starts soon')
                self.startGame()
    
    def startGame(self):
        self.text.bind('<Key>', self.callback)
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