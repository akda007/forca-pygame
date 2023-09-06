import pygame, ui, Keys, time
import logic.forca as f
import logic.words as words
from Colors import *

from tkinter import *
from tkinter import messagebox


def update():
    pygame.display.flip()

#initialize
pygame.init()
pygame.display.set_caption("Jogo da Forca!")

screen = pygame.display.set_mode((600, 500))
clock = pygame.time.Clock()

running = True

while running:
    forca = f.Forca(words.get_random_word("words.txt"), 6)
    ui_guessed = ui.GussedChars(screen, screen.get_width() - ui.GussedChars.hor_spacing * 8, 0, 30, 0)
    ui_word = ui.Word(forca.word, screen)

    #main loop
    while True:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.KEYUP:
                key_code = Keys.key_handler(event.key)
                
                if key_code != None:
                    if forca.guess(key_code):
                        ui_word.draw_char(key_code)
                        ui_guessed.add_char(key_code)
                        update()
    
        ui.draw_forca(screen)
        ui.draw_character(screen, forca.lives)
        
        clock.tick(30)
        update()
        
        if forca.lives == 0:
            
            res = messagebox.askyesno("GAME OVER!", f"Voce perdeu...\nA palavra era {forca.word}\nJogar novamente?")
            running = res

            del(forca)
            del(ui_word)
        
            break
            
        
        if forca.verify():
            res = messagebox.askyesno("Parabens!", f"Voce adivinhou a palavra: {forca.word} corretamente!\nJogar novamente!")
            running = res
            
            del(forca)
            del(ui_word)
            
            break

pygame.quit()




