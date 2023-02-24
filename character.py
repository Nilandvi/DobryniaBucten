from settings import *
from maps import bar
from ban import *
def load_image(name):
    fullname = os.path.join('animation', name)
    image = pygame.image.load(fullname)
    return image

dobrina = pygame.sprite.Group()
char = pygame.sprite.Sprite()
left = right = up = down = False 
dobrina = load_image("dobr.png")
anims = [load_image("d1.png"), load_image("d2.png"), load_image("d3.png"), load_image("d4.png"), load_image("u1.png"),
load_image("u2.png"), load_image("u3.png"), load_image("u4.png"), load_image("l1.png"), load_image("l2.png"), load_image("l3.png"),
load_image("l4.png"), load_image("r1.png"), load_image("r2.png"), load_image("r3.png"), load_image("r4.png")]

clock = pg.time.Clock()
class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0   #скорость перемещения. 0 - стоять на месте
        self.yvel = 0
        self.startX = x # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.image = dobrina
        self.rect = Rect(x, y, 32, 32) # прямоугольный объект

    def update(self, left, right, down, up, platforms):
        if left:
            self.xvel = -MOVE_SPEED
        if right:
            self.xvel = MOVE_SPEED
        if down:
            self.yvel = MOVE_SPEED
        if up:
            self.yvel = -MOVE_SPEED
        if not(left or right or up or down): # стоим, когда нет указаний идти
            self.xvel = 0
            self.yvel = 0

        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms)
    
    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):
                if xvel > 0:                      
                    self.rect.right = p.rect.left 

                if xvel < 0:                      
                    self.rect.left = p.rect.right 

                if yvel > 0:                      
                    self.rect.bottom = p.rect.top 
                    self.onGround = True          
                    self.yvel = 0                 

                if yvel < 0:                      
                    self.rect.top = p.rect.bottom 
                    self.yvel = 0                 

    def draw(self, screen): # Выводим себя на экран
        screen.blit(self.image, (self.rect.x,self.rect.y))

hero = Player(420,500)
