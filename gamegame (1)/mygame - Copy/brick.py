import os
import numpy as np
from colorama import init as cinit
from colorama import Fore, Back, Style
import random
from time import monotonic as clock
import math

import config as conf
import utils
from thing import Thing

class Brick(Thing):
    '''
    coin object
    uses physics inherited from Thing
    '''

    def __init__(self, game_height, game_width, power, x=0, y=0):
        if type(x) != int or type(y) != int:
            raise ValueError

        super().__init__(game_height, game_width, np.array([x, y], dtype='float32'), np.array([conf.BRICK_ROW, conf.BRICK_COL]))

        self._strength = power 
        self._repr = utils.make_brick(power)
        self.unbreakable = 0
        # self._disappear = False 
        # self._exploding = power == 4 

        if power >= conf.UNBREAKABLE:
            self.unbreakable = 1 

    def hit(self, through_ball = 0):
        if through_ball:
            self._strength = 0
            return 1 

        if self.unbreakable:
            return 
            
        self._strength -= 1
        self._repr = utils.make_brick(self._strength)
        return self._strength <= 0