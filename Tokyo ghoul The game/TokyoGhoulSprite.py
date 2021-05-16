import pygame

from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()
fps = 60

screen_width = 1920
screen_height = 1080


screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Tokyo Ghoul")


def draw_grid():
    for line in range(1, 33):
        pygame.draw.line(
            screen,
            (255, 255, 255),
            (0, line * tile_size),
            (screen_width, line * tile_size),
        )
        pygame.draw.line(
            screen,
            (255, 255, 255),
            (line * tile_size, 0),
            (line * tile_size, screen_height),
        )


# load images
bg_img = pygame.image.load("img/bg_img.png")
background = pygame.transform.scale(bg_img, (screen_width, screen_height))

# define game variables
run = True
tile_size = 60
game_over = 0


class Player:
    def __init__(self, x, y):
        self.images_right_idle = []
        self.images_left_idle = []
        self.images_right_run = []
        self.images_left_run = []
        self.images_right_jump = []
        self.images_left_jump = []
        self.index = 0
        self.counter = 0
        self.jump_counter = 0
        self.jump_index = 0

        for num in range(1, 3):
            img_right_idle = pygame.image.load(f"img/idle{num}.png")
            img_right_idle = pygame.transform.scale(img_right_idle, (40, 80))
            img_left_idle = pygame.transform.flip(img_right_idle, True, False)
            self.images_right_idle.append(img_right_idle)
            self.images_left_idle.append(img_left_idle)
        for num in range(1, 12):
            img_right_run = pygame.image.load(f"img/run{num}.png")
            img_right_run = pygame.transform.scale(img_right_run, (40, 80))
            img_left_run = pygame.transform.flip(img_right_run, True, False)
            self.images_right_run.append(img_right_run)
            self.images_left_run.append(img_left_run)
        for num in range(1, 7):
            img_right_jump = pygame.image.load(f"img/jump{num}.png")
            img_right_jump = pygame.transform.scale(img_right_jump, (40, 80))
            img_left_jump = pygame.transform.flip(img_right_jump, True, False)
            self.images_right_jump.append(img_right_jump)
            self.images_left_jump.append(img_left_jump)

        self.image = self.images_right_idle[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 1
        self.in_air = True

    def update(self, game_over):
        dx = 0
        dy = 0
        walk_cooldown = 2
        jump_cooldown = 2
        col_thresh = 20

        if game_over == 0:
            # get keypresses
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE] and self.jumped == False and self.in_air == False:
                self.vel_y = -15
                self.jumped = True

            if key[pygame.K_SPACE] == False:
                self.jumped = False

            if key[pygame.K_LEFT]:
                dx -= 5
                self.counter += 1
                
                self.direction = -1

            if key[pygame.K_RIGHT]:
                dx += 5
                self.counter += 1
                self.direction = 1

            if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
                self.counter = 0
                self.index = 0
                if self.direction == 1:
                    self.image = self.images_right_idle[self.index]
                if self.direction == -1:
                    self.image = self.images_left_idle[self.index]

            # handle animations

            if self.counter > walk_cooldown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images_right_run):
                    self.index = 0
                if self.direction == 1:
                    self.image = self.images_right_run[self.index]
                if self.direction == -1:
                    self.image = self.images_left_run[self.index]
            if self.in_air == True:
                    self.jump_index = 0
                    self.jump_index += 1
                    if self.jump_index >= len(self.images_right_jump):
                        self.jump_index = 0
                    if self.direction == 1:
                        self.image = self.images_right_jump[self.jump_index]
                    if self.direction == -1:
                        self.image = self.images_left_jump[self.jump_index]

            # add gravity
            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10
            dy += self.vel_y

            # check for collision
            self.in_air = True

            for tile in world.tile_list:
                # check for collision in x direction
                if tile[2] != False:

                    if tile[1].colliderect(
                        self.rect.x + dx, self.rect.y, self.width, self.height
                    ):
                        dx = 0

                    # check for collision in y direction
                    if tile[1].colliderect(
                        self.rect.x, self.rect.y + dy, self.width, self.height
                    ):
                        # check if below the ground i.e. jumping
                        if self.vel_y < 0:
                            dy = tile[1].bottom - self.rect.top
                            self.vel_y = 0

                        # check if above the ground i.e. falling
                        elif self.vel_y >= 0:
                            dy = tile[1].top - self.rect.bottom
                            self.vel_y = 0
                            self.in_air = False

            # update player co ordinates
            self.rect.x += dx
            self.rect.y += dy

        # draw player onto the screen
        screen.blit(self.image, self.rect)
        #pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)


class World:
    def __init__(self, data):
        self.tile_list = []
        # load images
        ground_img = pygame.image.load("img/ground.png")
        tree_img = pygame.image.load("img/tree.png")
        box_img = pygame.image.load("img/box.png")
        scarecrow_img = pygame.image.load("img/scarecrow.png")
        logs_img = pygame.image.load("img/logs.png")
        table_img = pygame.image.load("img/table.png")
        well_img = pygame.image.load("img/well.png")
        surface_img = pygame.image.load("img/surface.png")
        obstacle_img = pygame.image.load("img/obstacle.png")
        cart_img = pygame.image.load("img/cart.png")
        wheel_img = pygame.image.load("img/wheel.png")
        bush1 = pygame.image.load("img/bush1.png")
        bush2 = pygame.image.load("img/bush2.png")
        bush3 = pygame.image.load("img/bush3.png")

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 20:
                    img = pygame.transform.scale(bush1, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size +2
                    tile = (img, img_rect, False)
                    self.tile_list.append(tile)
                if tile == 18:
                    img = pygame.transform.scale(bush2, (int(tile_size*1.5), int(tile_size*1.5)))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size +2 - int(tile_size*0.5)
                    tile = (img, img_rect, False)
                    self.tile_list.append(tile)
                if tile == 19:
                    img = pygame.transform.scale(bush3, (tile_size*2, int(tile_size*1.5)))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size +2 - int(tile_size*0.5)
                    tile = (img, img_rect, False)
                    self.tile_list.append(tile)
                if tile == 1:
                    img = pygame.transform.scale(ground_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size +2
                    tile = (img, img_rect, True)
                    self.tile_list.append(tile)
                if tile == 14:
                    img = pygame.transform.scale(cart_img, (tile_size*3, int(tile_size*1.5)))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size +2 - int(tile_size*0.5)
                    tile = (img, img_rect, False)
                    self.tile_list.append(tile)
                if tile == 15:
                    img = pygame.transform.scale(wheel_img, (int(tile_size // 1.5), int(tile_size // 1.5)))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size - 30
                    img_rect.y = row_count * tile_size + 2 + 20
                    tile = (img, img_rect, False)
                    self.tile_list.append(tile)
                if tile == 12:
                    img = pygame.transform.scale(surface_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size 
                    tile = (img, img_rect, True)
                    self.tile_list.append(tile)
                if tile == 7:
                    img = pygame.transform.scale(obstacle_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size 
                    tile = (img, img_rect, True)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(
                        tree_img, (tile_size * 4, tile_size * 6)
                    )
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size - tile_size * 5 +2
                    tile = (img, img_rect, False)
                    self.tile_list.append(tile)
                if tile == 3:
                    img = pygame.transform.scale(
                        box_img, (tile_size , tile_size)
                    )
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size +2
                    tile = (img, img_rect, True)
                    self.tile_list.append(tile)
                if tile == 4:
                    img = pygame.transform.scale(
                        scarecrow_img, (tile_size , tile_size + 30)
                    )
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size - 30 +2
                    tile = (img, img_rect, False)
                    self.tile_list.append(tile)
                if tile == 5:
                    img = pygame.transform.scale(
                        logs_img, (tile_size *2, tile_size)
                    )
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size +2
                    tile = (img, img_rect, True)
                    self.tile_list.append(tile)
                if tile == 6:
                    img = pygame.transform.scale(
                        well_img, (tile_size*2 , tile_size*2)
                    )
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size 
                    img_rect.y = row_count * tile_size - tile_size * 1 +2
                    tile = (img, img_rect, False)
                    self.tile_list.append(tile)
                
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
            #pygame.draw.rect(screen, (255, 255, 255), tile[1], 2)


world_data = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [20,0,14,15,18,20,3,19,18,2,20,18,3,0,0,4,19,6,0,20,5,0,2,0,0,0,7,0,0,7,0,0],
    [12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

world = World(world_data)
player = Player(100, screen_height - 260)

while run:

    clock.tick(fps)
    screen.blit(background, (0, 0))

    # draw_grid()

    world.draw()
    player.update(game_over)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()
