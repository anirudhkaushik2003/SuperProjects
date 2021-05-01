import os
import numpy as np
from colorama import init as cinit
from colorama import Fore, Back, Style
import random
from time import monotonic as clock
import random
import math

import config as conf

def intersect(rec_a, rec_b):
    '''
    checks if two rectangles intersect and returns their intersection area
    '''

    if type(rec_a) != list or type(rec_b) != list or len(rec_a) != 4 or len(rec_b) != 4:
        raise ValueError

    # rectangle representation: [x_start, x_end, y_start, y_end]

    x_start = max(rec_a[0], rec_b[0])
    x_end = min(rec_a[1], rec_b[1])
    y_start = max(rec_a[2], rec_b[2])
    y_end = min(rec_a[3], rec_b[3])

    if x_start > x_end or y_start > y_end:
        return False, [0, 0, 0, 0]
    else:
        return True, [x_start, x_end, y_start, y_end]

def get_art(path):
    '''
    reads the art text file and returns an np array
    '''

    path = os.path.join(conf.ART_BASE_PATH, path)
    arr = []
    try:
        with open(path, 'r') as f:
            for line in f:
                arr.append(list(line.strip('\n')))
    except FileNotFoundError as e:
        return None

    return np.array(arr, dtype='object')

def make_brick(power):
    '''
    makes a brick of specified color depending upon the strength
    '''
    # TODO: Make brick array dimension of BRICK_ROW * BRICK_COL instead of hardtyping 
    
    color = Fore.MAGENTA
    if power == 1:
        color = Fore.YELLOW
    elif power == 2:
        color = Fore.GREEN
    elif power == 3:
        color = Fore.BLUE
    elif power == 4:
        color = Fore.RED

    color += Style.BRIGHT
    representation = np.array([ [ color + '#' for _ in range(conf.BRICK_COL) ] for __ in range(conf.BRICK_ROW) ], dtype='object')
    # representation = np.array([[color + '#', color + '#', color + '#', color + '#', color + '#'],
    #                         [color + '#', color + '#', color + '#', color + '#', color + '#', ]], dtype='object')
    return representation 

def vector_decompose(mag, start, end):
    '''
    decomposes a vector of magnitude mag along direction start to end and returns its 2D components
    '''

    if type(start) != np.ndarray or type(end) != np.ndarray:
        raise ValueError

    x_cap = abs(start[0] - end[0])
    y_cap = abs(start[1] - end[1])

    theta = math.atan2(x_cap, y_cap)
    x_force = abs(mag * math.sin(theta))
    y_force = abs(mag * math.cos(theta))

    if end[0] < start[0]:
        x_force = -x_force

    if end[1] < start[1]:
        y_force = -y_force

    return [x_force, y_force]

def get_bar(length, left, total):
    '''
    generates a loading bar and returns a string representation
    '''
    
    if left >= total:
        return Style.BRIGHT + Back.RED + (' ' * length)
    if left <= 0:
        return Style.BRIGHT + Back.GREEN + (' ' * length)
    perc = int(round((left / total) * length))
    s = Style.BRIGHT + Back.RED + (' ' * perc)
    s += Back.GREEN + (' ' * (length - perc))
    return s
