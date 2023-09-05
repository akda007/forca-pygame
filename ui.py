import pygame as pg
from pygame import draw
from Colors import *
from utils import Coordinate

from pygame.locals import *


def draw_forca(_screen):
    draw.line(_screen, black, (100, 100), (100, 300), 5)
    draw.line(_screen, black, (70, 300), (130, 300), 5)
    draw.line(_screen, black, (100, 100), (160, 100), 5)
    draw.line(_screen, black, (160, 100), (160, 135), 5)

def draw_character(_screen, _lives):
    char = Character(Coordinate(160, 250), _screen)
    char.clear((255, 255, 255))

    if _lives >= 1:
        char.draw_head()
    if _lives >= 2:
        char.draw_body()
    if _lives >= 3:
        char.draw_leftarm()
    if _lives >= 4:
        char.draw_rightarm()
    if _lives >= 5:
        char.draw_rightleg()
    if _lives >= 6:
        char.draw_leftleg()


class Word:
    screen: pg.Surface
    word: str
    word_len: int
    current_pos: Coordinate
    bar_len:int
    spacing: int
    
    char_coords = []
    
    def draw_char(self, char: str):
        for i in range(len(self.word)):
            if self.word[i] == char:
                font = pg.font.Font("freesansbold.ttf", 32)
                text = font.render(char, True, black, white)
                textRect = text.get_rect()
                
                coord = self.char_coords[i]
                x = coord[0][0] + (coord[1][0] - coord[0][0]) / 2
                
                y = self.current_pos.Y - 20
                
                textRect.center = (x, y)
                self.screen.blit(text, textRect)
            

    def draw_underline(self):
        for c in self.word:
            coord = ((self.current_pos.X, self.current_pos.Y), (self.current_pos.X + self.bar_len, self.current_pos.Y))
            
            draw.line(self.screen, black, coord[0], coord[1], 3)
            
            self.char_coords.append(coord)

            self.current_pos.X += self.bar_len + self.spacing
            

    def __init__(self, _word, surface: pg.Surface):
        
        self.word = _word
        self.word_len = len(_word)
        self.screen = surface
        self.current_pos = Coordinate(50, 400)
        self.bar_len = 30
        self.spacing = 10

        pg.display.set_mode((100 + self.bar_len*self.word_len + self.spacing*self.word_len, surface.get_height()))
        surface.fill("white")

        self.draw_underline()


class Character:
    center: Coordinate
    screen: pg.Surface

    def __init__(self, _center: Coordinate, _surface: pg.Surface):
        self.center = _center
        self.screen = _surface


    def clear(self, color):
        draw.rect(self.screen, color,
                  pg.Rect(
                      self.center.X - 50,
                      self.center.Y - 120,
                      self.center.X - 50,
                      self.center.Y - 100 ))


    def draw_head(self):
        draw.circle(self.screen, black, (self.center.X, self.center.Y - 100), 20, 5)


    def draw_leftarm(self):
        draw.line(self.screen, black,
                  (self.center.X, self.center.Y - 75),
                  (self.center.X - 30, self.center.Y - 30), 5)


    def draw_rightarm(self):
        draw.line(self.screen, black,
                  (self.center.X, self.center.Y - 75),
                  (self.center.X + 30, self.center.Y - 30), 5)


    def draw_leftleg(self):
        draw.line(self.screen, black,
                  (self.center.X, self.center.Y - 20),
                  (self.center.X - 25, self.center.Y + 10), 5)


    def draw_rightleg(self):
        draw.line(self.screen, black,
                  (self.center.X, self.center.Y - 20),
                  (self.center.X + 25, self.center.Y + 10), 5)


    def draw_body(self):
        draw.line(self.screen, black, (self.center.X, self.center.Y - 80), (self.center.X, self.center.Y - 20), 5)
