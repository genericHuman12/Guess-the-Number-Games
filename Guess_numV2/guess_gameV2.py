import pygame
import sys
import random
from time import time
from message import Message
from score import Scoreboard
#You try and guess a number.
#Use the number keys and press enter to guess.
#HAVE FUN!

class Guess_Game:
    def __init__(self):
        #initializes everything
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.screen_rect = self.screen.get_rect()
        self.screen_width = self.screen_rect.width
        self.screen_hieght = self.screen_rect.height
        self.message = Message(self)
        self.number = random.randint(1,100)
        self.waiting = False
        self.now = time()
        self.length = 0
        self.inpt = ""
        self.nums = "1234567890"
        self.new_message = "ok"
        self.score = 0
        self.chances = 6
        self.board = Scoreboard(self)
    
    def run(self):
        while True:
            #Does everything in the game
            self.check_events()
            self.message.text()
            self.message.input_txt()
            self.wait(self.now, self.length, self.new_message)
            self.board.text()
            self.update_screen()
    
    def update_screen(self):
        #Draws the things on the screen
        self.screen.fill("white")
        self.message.draw()
        self.board.draw()
        pygame.display.flip()
    
    def check_events(self):
        #Checks the type of event and does the thing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_downs(event)
    
    def correct(self):
        #Decides what happens if you are wrong
        self.number = random.randint(1,100)
        self.message.message = "That's Right!"
        self.waiting = True
        self.length = 1
        self.new_message = "I'm thinking of another number 1 through 100"
        self.now = time()
        self.score += 1
        self.chances = 6
    
    def incorrect(self):
        #Decides what happens if you are wrong
        if int(self.inpt) > self.number:
            self.message.message = "That's too high!"
        elif int(self.inpt) < self.number:
            self.message.message = "That's too low!"
        self.chances -= 1
        if self.chances > 0:
            self.waiting = True
            self.length = 1.5
            self.new_message = "Try Again"
            self.now = time()
        else:
            self.lose()
    
    def lose(self):
        #Decides what happens if you lose
        self.message.message = f"You Lost! The number was {self.number}"
        self.new_message = "I'm thinking of a new number. Can you guess it?"
        self.now = time()
        self.chances = 6
        self.number = random.randint(1, 100)

    def check_downs(self, event):
        #checks what keys are pressed and does the thing that it is supposed to do
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_BACKSPACE:
            new = self.inpt[:-1]
            self.inpt = new
        elif event.key == pygame.K_RETURN:
            if int(self.inpt) == self.number:
                self.correct()
            else:
                self.incorrect()
            self.inpt = ""
        for n in self.nums:
            if event.unicode== n:
                self.inpt += n
    
    def wait(self, start, length, message):
        #Checks the elapsed time and if it equals the length, it changes the message.
        if self.waiting:
            now = time()
            if round((now - start),2) == length:
                self.message.message = message
        

guess = Guess_Game()
guess.run()