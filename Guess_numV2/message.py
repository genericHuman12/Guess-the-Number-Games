import pygame

class Message:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.message = "I am thinking of a Number 1 through 100"
        self.font = pygame.font.SysFont("Times New Roman", 40)

    def text(self):
        #defines the text, creates images, and puts them in the right spot
        chances = f"Chances: {self.game.chances}"
        self.message = self.message
        self.img = self.font.render(self.message, 0, "black", "white")
        self.rect = self.img.get_rect()
        self.rect.center = self.screen.get_rect().center
        self.chance_img = self.font.render(chances, 0, "black", "white")
        self.chance_rect = self.chance_img.get_rect()
        self.chance_rect.topright = self.screen.get_rect().topright

    def input_txt(self):
        #Same thing as text()
        ipt = "Input:"
        txt = f"{self.game.inpt}"
        self.ipt_img = self.font.render(ipt, 0, "black", "white")
        self.ipt_rect = self.ipt_img.get_rect()
        self.ipt_rect.centerx = self.screen.get_rect().centerx
        self.ipt_rect.centery = self.screen.get_rect().height * 0.75
        self.txt_img = self.font.render(txt, 0, "black", "white")
        self.txt_rect = self.txt_img.get_rect()
        self.txt_rect.midtop = self.ipt_rect.midbottom
    
    def draw(self):
        #draws the things
        self.screen.blit(self.img, self.rect)
        self.screen.blit(self.chance_img, self.chance_rect)
        self.screen.blit(self.ipt_img, self.ipt_rect)
        self.screen.blit(self.txt_img, self.txt_rect)