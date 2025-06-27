import pygame
import sys
import random
from time import time
from buttons import Buttons
from message import Message
from score import Scoreboard

class Guess_Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.screen_rect = self.screen.get_rect()
        self.screen_width = self.screen_rect.width
        self.screen_hieght = self.screen_rect.height
        self.buttons = Buttons(self)
        self.message = Message(self)
        self.number = random.randint(1,10)
        self.waiting = False
        self.now = time()
        self.length = 0
        self.new_message = "ok"
        self.score = 0
        self.board = Scoreboard(self)
    
    def run(self):
        while True:
            self.check_events()
            self.message.text()
            self.wait(self.now, self.length, self.new_message)
            self.board.text()
            self.update_screen()
    
    def update_screen(self):
        self.screen.fill("white")
        self.buttons.draw()
        self.message.draw()
        self.board.draw()
        pygame.display.flip()
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_downs(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                self.check_mouse(pos)
    
    def correct(self):
        self.number = random.randint(1,10)
        self.message.message = "That's Right!"
        self.waiting = True
        self.length = 1
        self.new_message = "I'm thinking of another number 1 through 10"
        self.now = time()
        self.score += 1
    
    def incorrect(self):
        self.message.message = f"Thats Wrong! It was {self.number}"
        self.number = random.randint(1,10)
        self.waiting = True
        self.length = 1.5
        self.new_message = "I'm thinking of another number 1 through 10. Can you guess it?"
        self.now = time()

    def check_mouse(self, pos):
        if self.buttons.but1.collidepoint(pos):
            if self.number == 1:
                self.correct()
            else:
                self.incorrect()
        if self.buttons.but2.collidepoint(pos):
            if self.number == 2:
                self.correct()
            else:
                self.incorrect()
        if self.buttons.but3.collidepoint(pos):
            if self.number == 3:
                self.correct()
            else:
                self.incorrect()
        if self.buttons.but4.collidepoint(pos):
            if self.number == 4:
                self.correct()
            else:
                self.incorrect()
        if self.buttons.but5.collidepoint(pos):
            if self.number == 5:
                self.correct()
            else:
                self.incorrect()
        if self.buttons.but6.collidepoint(pos):
            if self.number == 6:
                self.correct()
            else:
                self.incorrect()
        if self.buttons.but7.collidepoint(pos):
            if self.number == 7:
                self.correct()
            else:
                self.incorrect()
        if self.buttons.but8.collidepoint(pos):
            if self.number == 8:
                self.correct()
            else:
                self.incorrect()
        if self.buttons.but9.collidepoint(pos):
            if self.number == 9:
                self.correct()
            else:
                self.incorrect()
        if self.buttons.but10.collidepoint(pos):
            if self.number == 10:
                self.correct()
            else:
                self.incorrect()
        
    def wait(self, start, length, message):
        if self.waiting:
            now = time()
            if round((now - start),2) == length:
                self.message.message = message
        

    def check_downs(self, event):
        if event.key == pygame.K_q:
            sys.exit()

guess = Guess_Game()
guess.run()