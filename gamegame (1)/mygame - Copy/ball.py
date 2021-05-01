import os
import numpy as np
from colorama import init as cinit
from colorama import Fore, Back, Style
import random
from time import monotonic as clock
import math
from random import randrange as rr


import config as conf
import utils
from thing import Thing

class Ball(Thing):
    '''
    coin object
    uses physics inherited from Thing
    '''

    def __init__(self, game_height, game_width, x=0, y=0, on_paddle=False, paddle_delta = 0):
        if type(x) != int or type(y) != int:
            raise ValueError

        if x == 0 and y == 0:
            x = game_height - conf.GND_HEIGHT - 2
            y = game_width/2

        super().__init__(game_height, game_width, np.array([x, y]), np.array([1, 1]))

        self._paddle_delta = paddle_delta 
        self._on_paddle = on_paddle

        if rr(2) == 0:
            self._vel = np.array([-1, 1]) 
        else :
            self._vel = np.array([-1, -1]) 
            
        self._acc = np.array([0, 0])

        color_number = rr(3)
        color = Fore.WHITE
        if color_number == 1:
            color = Fore.MAGENTA
        elif color_number == 2:
            color = Fore.CYAN

        self._repr = np.array([[Style.BRIGHT + color  + 'O']], dtype='object')
    
    
            
    
    def is_out(self):
        '''
        overriden to return false as soon as any part of the object goes off screen, because mandalorian can not go off screen
        '''
        # T, L, B, R
        return (self._pos[0] <= conf.SKY_DEPTH), (self._pos[1] <= conf.SKY_DEPTH), (self._pos[0] + self._size[0] + conf.GND_HEIGHT > self._game_h), (self._pos[1] + self._size[1] + conf.GND_HEIGHT > self._game_w)

    def show(self):
        '''
        overriden to accomodate shield
        '''
        return np.round(self._pos).astype(np.int32), self._size, self._repr

    def release(self):
        self._on_paddle = False 
        self.move()
        pass

    def reset_acc(self):
        '''
        overriden to accomodate gravity and drag force
        '''

        super().reset_acc()

        self._acc[0] += conf.GRAVITY_X
        self._acc[1] += conf.GRAVITY_Y

        # drag force added so that velocity changes due to user inputs do not accumulate
        # drag force tends to align the player's velocities to the game's velocity
        if (self._vel[1] + conf.GAME_SPEED) > 0:
            drag = -conf.DRAG_COEFF * ((self._vel[1] + conf.GAME_SPEED)** 2)
        else:
            drag = conf.DRAG_COEFF * ((self._vel[1] + conf.GAME_SPEED)** 2)
            
        self._acc[1] += drag

    def move(self, paddle = None):
        if self._on_paddle:
            pos, size, represen = paddle.show()
            self._pos[1] = pos[1] + self._paddle_delta 
            return

        super().move()

        t, l, b, r = self.is_out() # don't let it go out

        if l:
            if self._vel[1] < 0:
                self._pos[1] = 0
                self._vel[1] *= -1
            # if self._acc[1] < 0:
            #     self._acc[1] = 0

        if r:
            if self._vel[1] > 0:
                self._pos[1] = self._game_w - self._size[1]
                self._vel[1] *= -1 
            # if self._acc[1] > 0:
            #     self._acc[1] = 0

        if t:
            if self._vel[0] < 0:
                self._pos[0] = 5
                self._vel[0] *= -1

        if b:
            if self._vel[0] > 0:
                self._pos[0] = self._game_h - self._size[0]
                self._vel[0] *= -1 
                return True 

