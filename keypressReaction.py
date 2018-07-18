#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 22:19:49 2018

@author: diveki
"""

import curses

def moveUp():
    print('Move Up!')
    
def moveDown():
    print('Move Down!')
    
def moveLeft():
    print('Move Left!')

def moveRight():
    print('Move Right!')

actions = {
    curses.KEY_UP:    moveUp,
    curses.KEY_DOWN:  moveDown,
    curses.KEY_LEFT:  moveLeft,
    curses.KEY_RIGHT: moveRight,
    }

def main(window):
    next_key = None
    while True:
        curses.halfdelay(1)
        if next_key is None:
            key = window.getch()
            print(key)
        else:
            key = next_key
            next_key = None
        if key != -1:
            # KEY DOWN
            curses.halfdelay(3)
            action = actions.get(key)
            if action is not None:
                action()
            next_key = key
            while next_key == key:
                next_key = window.getch()
            # KEY UP
            

curses.wrapper(main)