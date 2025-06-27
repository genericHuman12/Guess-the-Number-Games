import pygame

class Buttons:
    def __init__(self, game):
        self.screen = game.screen
        self.image = pygame.image.load(r"Guess_num\images\buttons.bmp")
        self.image = pygame.transform.scale(self.image, (600, 195*(600/538)))
        #538, 195
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen.get_rect().midbottom
        self.rect.y -= 10
        x = 47
        s = 80
        h = 7
        self.but1 = pygame.rect.Rect(self.rect.left+h, self.rect.top+h, s, s)
        self.but2 = pygame.rect.Rect(self.but1.right+x, self.rect.top+h, s, s)
        self.but3 = pygame.rect.Rect(self.but2.right+x, self.rect.top+h, s, s)
        self.but4 = pygame.rect.Rect(self.but3.right+x, self.rect.top+h, s, s)
        self.but5 = pygame.rect.Rect(self.but4.right+x, self.rect.top+h, s, s)
        self.but6 = pygame.rect.Rect(self.rect.left+h, self.but1.bottom+x, s, s)
        self.but7 = pygame.rect.Rect(self.but6.right+x, self.but2.bottom+x, s, s)
        self.but8 = pygame.rect.Rect(self.but7.right+x, self.but3.bottom+x, s, s)
        self.but9 = pygame.rect.Rect(self.but8.right+x, self.but4.bottom+x, s, s)
        self.but10 = pygame.rect.Rect(self.but9.right+x, self.but5.bottom+x, s, s)
    
    def draw(self):
        pygame.draw.rect(self.screen, "blue", self.but1)
        pygame.draw.rect(self.screen, "blue", self.but2)
        pygame.draw.rect(self.screen, "blue", self.but3)
        pygame.draw.rect(self.screen, "blue", self.but4)
        pygame.draw.rect(self.screen, "blue", self.but5)
        pygame.draw.rect(self.screen, "blue", self.but6)
        pygame.draw.rect(self.screen, "blue", self.but7)
        pygame.draw.rect(self.screen, "blue", self.but8)
        pygame.draw.rect(self.screen, "blue", self.but9)
        pygame.draw.rect(self.screen, "blue", self.but10)
        self.screen.blit(self.image, self.rect)
