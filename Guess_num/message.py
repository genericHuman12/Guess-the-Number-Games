import pygame

class Message:
    def __init__(self, game):
        self.screen = game.screen
        self.message = "I am thinking of a Number 1 through 10"
        self.font = pygame.font.SysFont("Times New Roman", 40)

    def text(self):
        self.message = self.message
        self.img = self.font.render(self.message, 0, "black", "white")
        self.rect = self.img.get_rect()
        self.rect.center = self.screen.get_rect().center
    
    def draw(self):
        self.screen.blit(self.img, self.rect)