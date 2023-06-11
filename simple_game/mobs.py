import pygame

class Inos(pygame.sprite.Sprite): #класс 1 пришельца

    def __init__(self, screen): #инициализируем и задаем начальное положение

        super(Inos, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('mob1.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.x = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self): #вывод мобов на экран
        self.screen.blit(self.image, self.rect)


    def update(self): #перемещение врагов
        self.y += 0.05
        self.rect.y = self.y
