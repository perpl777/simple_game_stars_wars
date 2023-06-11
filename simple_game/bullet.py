import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun): #пушка в текущей позиции пушки
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 3, 15) #появляется в координатах 0, 0, ширина 2 высота 12 пикселей
        self.color = 205, 85, 207
        self.speed = 5
        self.rect.centerx = gun.rect.centerx #появление пули в координате х пушки
        self.rect.top = gun.rect.top #появление пули верху пушки
        self.y = float(self.rect.y)

    def update(self): #премещение пули вверх
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self): #рисуем пулю на экране
        pygame.draw.rect(self.screen, self.color, self.rect)
