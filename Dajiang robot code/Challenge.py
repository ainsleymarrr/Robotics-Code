import pygame,sys,random
from pygame.locals import *
pygame.init()
s=pygame.display.set_mode([600,400])
s.fill([110,230,250])
pygame.display.set_caption('hi')
#pygame.draw.rect(s,[50,100,200],a,5)
i=pygame.image.load("OIP-C.jpg")
img_rect=i.get_rect()
x=random.randint(0,5)
y=random.randint(0,5)
a=pygame.Rect(x,y,50,50)
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    pygame.time.delay(100)
    s.fill([110,230,250])
    pygame.draw.rect(s, [50, 100, 200], a, 25)
    if a.left < 0 or a.right>s.get_width():
        x=-x
    elif a.top<0 or a.bottom>s.get_height():
        y=-y
    a.move_ip(x,y)
    pygame.display.update()
