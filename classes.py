# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 13:04:33 2018

@author: zdiveki
"""

from random import randint
from time import sleep, time
from tkinter import *

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
        

class GeneralButton:
    def __init__(self, cls):
        self.initializeButton(cls)


class KeyboardButton(GeneralButton):
    def initializeButton(self, cls):
        button = input('Press the button you want to use: ')
        cls.button = button


class GeneralGame(Frame):
    def __init__(self, master, numberPlayer=2, roundNumbers=3, **kw):
        Frame.__init__(self, master)
        self.numberOfPlayers = numberPlayer
        self.numberOfRounds = roundNumbers
        self.maxWait = 5
        self.players = {}
        self.__dict__.update(kw)
        self.initializeGame()
    
    def initializeGame(self):
        for ii in range(self.numberOfPlayers):
            self.players[ii+1] = self.set_players(ii+1)
    
    def startGame(self):
        for ii in range(self.numberOfRounds):
            self.startMessage(ii+1)
            startTime = time()
            self.startSignal()
            
        
class ButtonGame(GeneralGame):
    def __init__(self, master, numberPlayer=2, roundNumbers=3, msg = 'Press', **kw):
        GeneralGame.__init__(self, master, numberPlayer=numberPlayer, roundNumbers=roundNumbers, **kw)
        self.startmsg = msg
        self.master = master
        
        
    def set_players(self, pid):
        name = input('Name of %sth player: ' % pid)
        p = Player(name)
        button = input('Press the button you want to use: ')
        p.set_button(button)
        return p
    
    def startMessage(self, ii):
        print('Round number %s starts when %s appears' % (ii, self.startmsg))

    def startSignal(self):
        sec = randint(1, self.maxWait)
        sleep(sec)
        print(self.startmsg)
        
    
def pressedButton(event):
    print("pressed", repr(event.char))
    

    
if __name__ == '__main__':
    root = Tk()
    game = ButtonGame(root, msg = 'Press')
    root.bind("<Key>", pressedButton)
  #  game.startGame()
    root.mainloop()
    
    
    
    
    
        