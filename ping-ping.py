from pygame import *
# import os

import random


font.init()
font2 = font.Font(None, 36)
win = font2.render("YOU WIN!", 1, (255,255,0))
lose = font2.render("YOU LOSE.", 1, (255,0,0))

# parent class for other sprites
class GameSprite(sprite.Sprite):
  # class constructor
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # We call the class constructor (Sprite):
        sprite.Sprite.__init__(self)

        # each sprite must store an image property
        # player_image = os.path.join(script_dir, player_image)

        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        # each sprite must store the rect property it is inscribed in
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
  # method that draws the character in the window
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 400:
            self.rect.y += self.speed

    def update2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed

 
 


img_back = 'background3.png'
img_player1 = 'Racket.png'
img_player2 = 'Racket.png'

# Create the window
win_width = 700
win_height = 500

display.set_caption("Ping Pong")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

player1 = Player(img_player1, 30, 200, 20, 100, 10)
player2 = Player(img_player1, 650, 200, 20, 100, 10)


finish = False
run = True
while run:
    # the press the Close button event
    for e in event.get():
        if e.type == QUIT:
            run = False
        # refresh background 
    if not finish:

            window.blit(background,(0,0))
            player1.update()
            player2.update2()
            
            player1.reset()
            player2.reset()
            display.update()

            time.delay(60)
