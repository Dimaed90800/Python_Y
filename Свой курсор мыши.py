import os
import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image

class Bomb(pygame.sprite.Sprite, load_image):
    image = load_image("arrow.png")
    
    def __init__(self, group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно!!!
        super().__init__(group)
        self.image = Bomb.image
        self.rect = self.image.get_rect()
    
    
    def update(self):
        self.rect = self.rect.move(event.pos)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False        
    screen.fill((0, 0, 0))
    pygame.display.flip()
pygame.quit()