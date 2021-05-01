import os
import numpy as np
from random import randrange as rr
from colorama import init as cinit
from colorama import Fore, Back, Style
import random
from time import monotonic as clock, sleep
import math

from screen import Screen
import config as conf
from thing import Thing
from kbhit import KBHit
import utils
from paddle import Paddle
from brick import Brick
from ball import Ball

#    |
#  --+-----> Y
#    |
#    |
#    V
#    X

class Game:
    '''
    encapsulates the entire game logic
    '''

    PLAY_KEYS = ('a', 'd','f')
    CONTROL_KEYS = ('q', )
    shield_time = 0
    shield_time2 = 0
    def __init__(self):
        rows, cols = os.popen('stty size', 'r').read().split()
        self._height = int(rows) - conf.BUFFER_DOWN
        self._width = int(cols) - conf.BUFFER_RIGHT
        
        if self._height < conf.MIN_HEIGHT or self._width < conf.MIN_WIDTH:
            print(Fore.RED + 'Fatal Error: Not enough room. Try playing with a larger terminal window.')
            raise SystemExit

        self._screen = Screen(self._height, self._width)
        self._keyboard = KBHit()
        self._frame_count = 0

        self._shield = False
        

        self._lives = conf.MAX_LIVES
        self._score = 0
        self._init_time = clock()
        self._money = 0
        
        self._paddle = Paddle(self._height, self._width)
        self._paddle_time = clock()
        self._bricks = []
        self.place_bricks()
        self._balls = []
        self._ball = Ball(self._height, self._width)
        self.initialize_ball()

    def initialize_ball(self):
        pos, size, represen = self._paddle.show()
        
        size = list(map(int, size))
        pos = list(map(int, pos))

        delta = rr(2, size[1] - 2)
        # print(delta)

        ball = Ball(self._height, self._width, pos[0], pos[1] + delta, True, delta)

        self._balls.append(ball)
        pass

    def place_bricks(self):
        '''
        places random bricks on the screen 
        '''
        rows = self._height//7 
        # print(rows)
        INIT_X = 3
        INIT_Y = self._width // 2 

        DELTA_X = conf.BRICK_ROW
        DELTA_Y = conf.BRICK_COL
        
        cnt = 1
        last_col = 0
        for i in range(rows):
            for j in range(cnt):
                col = rr(1, 5)
                while col == last_col:
                    col = rr(1, 5)
                self._bricks.append(Brick(self._height, self._width, col, INIT_X + DELTA_X * i, INIT_Y + DELTA_Y * (j - i)) )
                last_col = col
            cnt += 2

    
        for j in range(cnt):
            col = rr(1, 5)
            while col == last_col:
                col = rr(1, 5)
            self._bricks.append(Brick(self._height, self._width, col, INIT_X + DELTA_X * rows, INIT_Y + DELTA_Y * (j - rows)) )
            last_col = col

    
        for i in range(rows - 1, -1, -1):
            cnt -= 2
            for j in range(cnt - 1, -1, -1):
                col = rr(1, 5)
                while col == last_col:
                    col = rr(1, 5)
                self._bricks.append(Brick(self._height, self._width, col, INIT_X + DELTA_X * (rows + + rows - i), INIT_Y - DELTA_Y * (j - i) ))
                last_col = col
        
        # self._bricks.append(Brick(self._height, self._width, 2, INIT_X, INIT_Y))
        # self._bricks.append(Brick(self._height, self._width, 3, INIT_X + DELTA_X, INIT_Y))

        pass


    def build_world(self):
        '''
        build the various things
        '''

    def deflect_ball(self, ball, brick):
        '''
        deflects the ball according to which side of the brick it has hit
        '''

        # print("ballllll velocity:", ball._vel)
        bump, area = self.check_collision(ball, brick, True, True, True) #, [0, 0, 0, 0]

        # no collision so no need for deflection
        if not bump :
            return False 

        brick_pos, brick_size, rep = brick.show()
        # print(brick_pos, brick_size)
        ball_pos, __, ____ = ball.show()
        print("brick pos:", brick_pos, "ball pos:", ball_pos)
        print("velocity before:", ball._vel,)

        x, y = ball_pos 

        brick_x_low = brick_pos[0]
        brick_x_high = brick_pos[0] + brick_size[0] - 1
        brick_y_low = brick_pos[1]
        brick_y_high = brick_pos[1] + brick_size[1] - 1

        # if (x == brick_x_low and y == brick_y_low)
        #  (x == brick_x_low and y == brick_y_high) 

        #         (x == brick_x_high and y == brick_y_high) 
        #          (x == brick_x_high and y == brick_y_low):
        #         ball._vel[0] *= -1
        #         ball._vel[1] *= -1 
        #         return True


        if x == brick_x_low - 1 and y == brick_y_low - 1 and ball._vel[0] > 0 and ball._vel[1] > 0:
            ball._vel[0] *= -1
            ball._vel[1] *= -1 
            return True
            
        elif x == brick_x_high + 1 and y == brick_y_low - 1 and ball._vel[0] < 0 and ball._vel[1] > 0:
            ball._vel[0] *= -1
            ball._vel[1] *= -1 
            return True
            
        elif x == brick_x_low - 1 and y == brick_y_high + 1 and ball._vel[0] > 0 and ball._vel[1] < 0:
            ball._vel[0] *= -1
            ball._vel[1] *= -1 
            return True
            
        elif x == brick_x_high + 1 and y == brick_y_high + 1 and ball._vel[0] < 0 and ball._vel[1] < 0:
            ball._vel[0] *= -1
            ball._vel[1] *= -1 
            return True

        for yy in range(brick_y_low + 1, brick_y_high):
            if (ball_pos[0] <= brick_x_low or ball_pos[0] >= brick_x_high) and ball_pos[1] == yy :
                ball._vel[0] *= -1 
                return True 

        # L
        if y <= brick_y_low:
            ball._vel[1] *= -1 
        # R
        elif y >= brick_y_high:
            ball._vel[1] *= -1 
        # T
        elif x < brick_x_low :
            ball._vel[0] *= -1 
        # B
        elif x > brick_x_high :
            ball._vel[0] *= -1 
        else :
            print("WOOPSIE")
            
            for yy in range(brick_y_low + 1, brick_y_high):
                if (ball_pos[0] == brick_x_low or ball_pos[0] == brick_x_high) and ball_pos[1] == yy :
                    ball._vel[0] *= -1 
                    return True 
            print(brick_pos, brick_size, brick._strength)
            print(ball_pos, ball._vel)
            print(area)
            raise SystemExit

        # # T
        # if x <= brick_x_low and not ( x == brick_x_low and (y == brick_y_low or y == brick_y_high) and ( (ball._vel[0] > 0 and ball._vel[1] > 0) or (ball._vel[0] > 0 and ball._vel[1] < 0 ) ) )  :
        #     ball._vel[0] *= -1 
        # # B
        # elif x >= brick_x_high and not ( x == brick_x_high and (y == brick_y_low or y == brick_y_high) and ( (ball._vel[0] > 0 and ball._vel[1] > 0) or (ball._vel[0] > 0 and ball._vel[1] < 0 ) ) ) :
        #     ball._vel[0] *= -1 
        # # L
        # elif y <= brick_y_low:
        #     ball._vel[1] *= -1 
        # # R
        # elif y >= brick_y_high:
        #     ball._vel[1] *= -1 
        # else :
        #     print("WOOPSIE")
        #     print(brick_pos, brick_size, brick._strength)
        #     print(ball_pos, ball._vel)
        #     print(area)
        #     raise SystemExit
        
        print("velocity after:", ball._vel)
        return True 
        pass

    def handle_paddle_collision(self, ball):
        '''
        checks collision with paddle 
        '''
        # check with paddle
        bump, area = self.check_collision(self._paddle, ball, True, True, True)
        if bump:
            # ball._vel[0] *= -1 
            # return 
            # paddle_pos, paddle_size, _ = self._paddle.show()
            # ball_pos, ball_size, __ = ball.show()

            # delta_pos = ball_pos - paddle_pos
            # length = pow( pow(delta_pos[0], 2) + pow(delta_pos[1], 2), 0.5 )

            # normalized = [_/length for _ in delta_pos]  
            # speed = pow( pow(ball._vel[0], 2) + pow(ball._vel[1], 2), 0.5)
            # ball._vel = [_ * speed for _ in normalized]


            # print(ball._vel)

            paddle_pos, paddle_size, _ = self._paddle.show()
            ball_pos, ball_size, __ = ball.show()

            delta_pos = ball_pos[1] - paddle_pos[1] - conf.PADDLE_WIDTH/2 
            normalized_delta = delta_pos/ (conf.PADDLE_WIDTH/2.0)

            if abs(normalized_delta) < 0.5 :
                ball._vel[0] *= -1 
                return 

            bounce_angle = normalized_delta * conf.MAX_BOUNCE_ANGLE

            speed = pow( pow(ball._vel[0], 2) + pow(ball._vel[1], 2), 0.5)
            ball._vel = [speed * - math.cos(bounce_angle), speed * math.sin(bounce_angle) ]
            
            # ball._vel = [speed * - math.sin(bounce_angle), speed * math.cos(bounce_angle)]

            print(normalized_delta, bounce_angle, ball._vel)
            # raise SystemExit

            # ball._vel[0] *= -1 
            return 

    def handle_collisions(self):
        '''
        handle collisions between various things
        '''
        for ball in self._balls:
            if not ball._on_paddle:
                self.handle_paddle_collision(ball)

            for b in self._bricks:
                bump = self.deflect_ball(ball, b)

                if bump:
                    if not b.unbreakable:
                        self._score += 10 
                    if b.hit():
                        self._bricks.remove(b)
                    break 
        pass


    def paint_objs(self):
        '''
        add everything to the screen
        '''
        self._screen.add(self._paddle)
        for b in self._bricks:
            self._screen.add(b)
        for ball in self._balls:
            self._screen.add(ball)

    def move_objs(self):
        '''
        move everything
        '''
        self._paddle.move()
        empty = False 

        for ball in self._balls:
            if ball.move(self._paddle) == True:
                if len(self._balls) == 1:
                    empty = True 
                self._balls.remove(ball)

        if empty:
            self._lives -= 1 
            if self._lives <= 0:
                self.game_over()

            self.initialize_ball()

    def reset_acc_objs(self):
        '''
        reset acceralations of all objects, as accelarations are computed in each frame
        '''
        self._paddle.reset_acc()

    def done(self):
        print('done')   

    def handle_input(self):
        if self._keyboard.kbhit():
            inp = self._keyboard.getch()

            if inp in self.PLAY_KEYS:
                self._paddle.nudge(inp)
            elif inp == 'e':
                self._paddle.nudge('e')
                
            elif inp == 'p':
                self._ball._vel = np.array([-1, -1]) + 100
                self.done()
                   
                
                
    
                    
            # elif inp == 'e':
            #     self.fire()

            elif inp == 'q':
                self.game_over(won=False)
            
            #elif inp == 'e':
                #self._repr = np.array([[' ', Fore.WHITE + Style.BRIGHT + '#', Fore.WHITE + '=',
                # Fore.WHITE + '=', Fore.WHITE + '=', Fore.WHITE + '=', Fore.WHITE + '=', Fore.WHITE + '=', Fore.WHITE + '', Fore.WHITE + '',
                # Fore.WHITE + '', Fore.WHITE + '', Fore.WHITE + Style.BRIGHT + '#', ' ']], dtype='object')
            
            elif inp == 'x':
                for b in self._balls:
                    if b._on_paddle:
                        b.release()

            self._keyboard.flush() # to prevent keystrokes being piled up as input rate is faster than frame rate

    def game_over(self, won=False):
        sleep(1)
        self._screen.game_over(won, self._score, int(clock() - self._init_time))
        while (True):
            if self._keyboard.kbhit():
                if self._keyboard.getch() == 'f':
                    break
        self._keyboard.set_normal_term()
        raise SystemExit
    
    def setup_paddle(self):
        '''
        clear the rest of the objects, disable dragon and show the boss
        '''

        if self._boss is not None:
            return

        # if clock() - self._init_time <= conf.BOSS_ARRIVAL_TIME:
        #     return

        # self._screen.flash(Back.YELLOW + ' ', self._frame_count)

        
    def check_collision(self, obj_a, obj_b, cheap=False, buffer=False, get_area = False):
        '''
        check collisions between two objects
        for small objects, add option of buffering (increasing size of objects) to prevent false negatives
        at high velocities
        for rectangular objects, or when there are many of a type, cheap detection only checks their bounding boxes
        '''


        if buffer and not cheap:
            raise ValueError

        a_pos, a_size, a_repr = obj_a.show()
        b_pos, b_size, b_repr = obj_b.show()

        

        a_rec = [a_pos[0], a_pos[0] + a_size[0] - 1, a_pos[1], a_pos[1] + a_size[1] - 1]
        if buffer: # add extra padding to small object b
            b_rec = [b_pos[0] - 1, b_pos[0] + b_size[0], b_pos[1] - 1, b_pos[1] + b_size[1]]
        else:
            b_rec = [b_pos[0], b_pos[0] + b_size[0] - 1, b_pos[1], b_pos[1] + b_size[1] - 1]

        bump, common = utils.intersect(a_rec, b_rec) # bounding box check
        
        if cheap or buffer:
            if get_area:
                return bump, common
            return bump
        
        if not bump:
            return False

        a_idx = [common[0] - a_pos[0], common[1] - a_pos[0] + 1, common[2] - a_pos[1], common[3] - a_pos[1] + 1]
        b_idx = [common[0] - b_pos[0], common[1] - b_pos[0] + 1, common[2] - b_pos[1], common[3] - b_pos[1] + 1]

        # check in common region if any cell has both of them as non whitespace
        for i in range(common[1] + 1 - common[0]):
            for j in range(common[3] + 1 - common[2]):
                a_i = a_idx[0] + i
                a_j = a_idx[2] + j

                b_i = b_idx[0] + i
                b_j = b_idx[2] + j

                if a_repr[a_i][a_j] != ' ' and b_repr[b_i][b_j] != ' ':
                    return True

        return False

    def print_info(self):
        '''
        print the info below the screen
        '''
        # TODO: should be in screen class: but requires a lot of information being passed

        print(Style.RESET_ALL + Style.BRIGHT, end='')
        print('\033[0K', end='')
        print('LIVES:', str(self._lives).rjust(1), end='\t')
        # print('COINS:', str(self._money).rjust(3), end='\t')
        print('SCORE:', str(self._score).rjust(5), end='\t')
        time = int(clock() - self._init_time)
        print('TIME:', str(time).rjust(5), end='\t')
       

    def start_shield(self):
        if (5-(clock() - self.shield_time) >= 0):
               print('shield power up time remaining = ',5 -(clock()/1 - self.shield_time/1))
        if (self._paddle.shield_condition == True):
            self.shield_time = clock()
             
            self._paddle.shield_condition = False
    def start_shield2(self):
        if (5-(clock() - self.shield_time2) >= 0):
               print('shield power up2 time remaining = ',5 -(clock()/1 - self.shield_time2/1))
        if (self._paddle.shield_condition2 == True):
            self.shield_time2 = clock()
             
            self._paddle.shield_condition2 = False
    def poop(self):
        print('power up time remaining = ',5-(clock() - self.shield_time)) 
       
    def play(self):
        while True:
            start_time = clock()
            self.start_shield()
            if ((clock() - self.shield_time >= 5) and (clock() - self.shield_time <= 5.1)):
                self._paddle._repr = np.array([[' ', Fore.WHITE + Style.BRIGHT + '#', Fore.WHITE + '=',
                Fore.WHITE + '=', Fore.WHITE + '=', Fore.WHITE + '=', Fore.WHITE + '=', Fore.WHITE + '=', Fore.WHITE + '=', Fore.WHITE + '=',
                Fore.WHITE + '=', Fore.WHITE + '=', Fore.WHITE + Style.BRIGHT + '#', ' ']], dtype='object')
            #self.poop()
            self.start_shield2()
            if ((clock() - self.shield_time2 >= 5) and (clock() - self.shield_time2 <= 5.1)):
                self._paddle._repr = np.array([[' ', Fore.WHITE + Style.BRIGHT + '#', Fore.WHITE + '=',
                Fore.WHITE + '=', Fore.WHITE + '=', Fore.WHITE + '=', Fore.WHITE + '=', Fore.WHITE + '=', Fore.WHITE + '=', Fore.WHITE + '=',
                Fore.WHITE + '=', Fore.WHITE + '=', Fore.WHITE + Style.BRIGHT + '#', ' ']], dtype='object')
            
               
            # internal logic
            #self.build_world()
            self.reset_acc_objs()
            self.handle_input()
            self.move_objs()
            self.handle_collisions()
            
            # show to user
            self._screen.clear()
            self.paint_objs()
            
            
            self._screen.print_board(self._frame_count)
            self._frame_count += 1
            while clock() - start_time < 0.1: # frame rate
                pass
            

