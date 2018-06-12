# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 13:04:33 2018

@author: zdiveki
"""

from random import randint
from time import sleep, time

class Player:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name
    
    def get_name(self):
        return self.name
    
    def get_button(self):
        return self.button
        

class GeneralButton:
    def __init__(self, cls):
        self.initializeButton(cls)

class KeyboardButton(GeneralButton):
    def initializeButton(self, cls):
        button = input('Press the button you want to use: ')
        cls.button = button
    
    

class Game:
    def __init__(self, numberPlayer, buttonType, roundNumbers=3, msg = 'Press'):
        self.numberOfPlayers = numberPlayer
        self.buttonClass = buttonType
        self.numberOfRounds = roundNumbers
        self.startmsg = msg
        self.maxWait = 5
        self.players = {}
        self.initializeGame()
        
    def initializeGame(self):
        for ii in range(self.numberOfPlayers):
            self.players[ii+1] = self.set_players(ii+1)
            #self.set_buttons()
    
    def set_players(self, pid):
        name = input('Name of %sth player: ' % pid)
        p = Player(name)
        self.buttonClass(p)
        return p
        
    def startGame(self):
        for ii in range(self.numberOfRounds):
            self.startMessage(ii+1)
            startTime = time()
            self.startSignal()
            
    def startMessage(self, ii):
        print('Round number %s starts when %s appears' % (ii, self.startmsg))
    
    def startSignal(self):
        sec = randint(1, self.maxWait)
        sleep(sec)
        print(self.startmsg)
        
    
    
if __name__ == '__main__':
    game = Game(2, KeyboardButton, roundNumbers=3)
    game.startGame()
    
    
    
    
    
        