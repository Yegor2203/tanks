from pygame import *

img_bullet = 'bullet.png'

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = image.load(player_image)
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
        
    def fire_r(self):
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)

    def fire_l(self):
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)

class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill() 

back = (200, 255, 255)
win_width = 600
win_height = 500
display.set_caption("Tanks")
window = display.set_mode((win_width, win_height))
window.fill(back)

tank = Player("tank.png", 30, 200, 2, 50, 150)
tank1 = Player("tank1.png", 520, 200, 2, 50, 150)
bullet = Bullet("bullet.png", 200, 200, 1, 50, 50)

finish = False
game = True
clock = time.Clock()

font.init()
Myfont = font.Font(None, 36)
lose1 = Myfont.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = Myfont.render('PLAYER 2 LOE!', True, (180, 0, 0))

class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill() 
            
            def fire(self):
                bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -15)
                bullets.add(bullet) 

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)
        tank.update_l()
        tank1.update_r()
        
        tank.reset()
        tank1.reset()

    display.update()
    clock.tick(40)
