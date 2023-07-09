from pygame import *

mixer.init()
fire_sound = mixer.Sound('fire.ogg')
fire_sound.set_volume(0.3)

font.init()
font2 = font.SysFont('Arial', 90)
font_finall = font.Font(None, 90)
win = font_finall.render("You win", True, (9, 184, 228))


img_bullet = 'bullet.png'
img_superbullet = 'superbullet.png'

HP = 100
HP_l = 100

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
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x = self.rect.x - self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x = self.rect.x + self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
        if keys[K_a] and self.rect.x > 5:
            self.rect.x = self.rect.x - self.speed
        if keys[K_d] and self.rect.x < win_width - 80:
            self.rect.x = self.rect.x + self.speed
        
    def fire_r(self):
        bullet = Bullet_1(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets_r.add(bullet)

    def fire_l(self):
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 585, 20, -15)
        bullets_l.add(bullet)

    def superfire_r(self):
        bullet = Super_Bullet_1(img_superbullet, self.rect.centerx, self.rect.top, 15, 20, -15)
        superbullets_r.add(bullet)

    def superfire_l(self):
        bullet = Super_Bullet(img_superbullet, self.rect.centerx, self.rect.top, 585, 20, -15)
        superbullets_l.add(bullet)

class Bullet(GameSprite):
    def update(self):
        self.rect.x -= self.speed
        if self.rect.x < 0:
            self.kill()

class Bullet_1(GameSprite):
    def update(self):
        self.rect.x += self.speed
        if self.rect.x < 0:
            self.kill()

class Super_Bullet(GameSprite):
    def update(self):
        self.rect.x -= self.speed
        if self.rect.x < 0:
            self.kill()

class Super_Bullet_1(GameSprite):
    def update(self):
        self.rect.x += self.speed
        if self.rect.x < 0:
            self.kill()

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, x, y, widht, height):
        super().__init__
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.widht = widht
        self.height = height
        self.x = x
        self.y = y

        self.image = Surface((self.widht, self.height))
        self.image.fill((color_1, color_2, color_3))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


back = (200, 255, 255)
win_width = 600
win_height = 500
display.set_caption("Tanks")
window = display.set_mode((win_width, win_height))
window.fill(back)

tank = Player("tank.png", 30, 200, 2, 50, 10)
tank1 = Player("tank1.png", 520, 200, 2, 50, 10)
bullets_l = sprite.Group()
bullets_r = sprite.Group()
superbullets_l = sprite.Group()
superbullets_r = sprite.Group()
finish = False
game = True
clock = time.Clock()


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
        if e.type == KEYDOWN:
            if e.key == K_1:
                fire_sound.play()
                tank.fire_l()
            if e.key == K_9:
                fire_sound.play()
                tank1.fire_r()
            if e.key == K_3:
                fire_sound.play()
                tank.superfire_l()
            if e.key == K_7:
                fire_sound.play()
                tank1.superfire_r()
    if not finish:  
                     
        if sprite.spritecollide(tank1, bullets_l, True) or sprite.spritecollide(tank1, bullets_l, False):
            HP = HP - 20
            print(HP)
        
        if sprite.spritecollide(tank, bullets_r, True) or sprite.spritecollide(tank, bullets_r, False):
            HP = HP - 20
            print(HP)
        
        if sprite.spritecollide(tank, superbullets_r, True) or sprite.spritecollide(tank, superbullets_r, False):
            HP = HP - 50
            print(HP)
        if sprite.spritecollide(tank1, superbullets_l, True) or sprite.spritecollide(tank1, superbullets_l, False):
            HP_l = HP_l - 50
            print(HP_l)

    
        if HP == 0:
            win = font2.render("Player 1 win", True, (9, 184, 228))
            window.blit(win, (100, 100))
            finish = True
            
        if HP == 0:
            win = font2.render("Player 2 win", True, (9, 184, 228))
            window.blit(win, (100, 100))
            finish = Tru
        
        
        
    if finish != True:
        window.fill(back)
        tank.update_l()
        tank1.update_r()
        bullets_l.update()
        bullets_r.update()
        superbullets_r.update()
        superbullets_l.update()

        bullets_r.draw(window)
        tank.reset()
        tank1.reset()
        bullets_l.draw(window)
        superbullets_r.draw(window)
        superbullets_l.draw(window)
        
        text_hp = font2.render("HP: " + str(HP), True, (139, 0, 0))
        window.blit(text_hp, (10, 20))
        
        text_hp_l = font2.render("HP: " + str(HP_l), True, (139, 0, 0))
        window.blit(text_hp_l, (330, 20))
        
    display.update()
    clock.tick(60)
