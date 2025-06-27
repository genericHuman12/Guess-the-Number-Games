import pygame

class Scoreboard:
    def __init__(self, game):
        self.screen = game.screen
        self.game = game
        self.font = pygame.font.SysFont("Times New Roman", 40)
    
    def text(self):
        self.tex = f"{self.game.score}"
        self.img = self.font.render(self.tex, 0, "black", "white")
        self.rect = self.img.get_rect()
        self.rect.x, self.rect.y = 10, 10

    def draw(self):
        self.screen.blit(self.img, self.rect)