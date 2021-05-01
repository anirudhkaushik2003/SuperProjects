import os
import numpy as np
from colorama import init as cinit
from colorama import Fore, Back, Style
import random
from time import monotonic as clock, sleep

# RANDOM TESTING for debugging

abc = np.array([' ', Fore.CYAN + Style.BRIGHT + '#', Fore.GREEN + '-',
                Fore.GREEN + '-', Fore.GREEN + '-', Fore.GREEN + '-', Fore.GREEN + '-', Fore.GREEN + '-', Fore.GREEN + '-', Fore.GREEN + '-',
                Fore.GREEN + '-', Fore.GREEN + '-', Fore.CYAN + Style.BRIGHT + '#', ' '], dtype='object')
abc = np.array([' ', Fore.CYAN + Style.BRIGHT + '#', Fore.GREEN + '--------', Fore.CYAN + Style.BRIGHT + '#', ' '], dtype='object')

for i in abc:
    print(i, end='')