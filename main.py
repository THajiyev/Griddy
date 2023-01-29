import pygame
import json
import time
import os

pygame.init()
screen = pygame.display.set_mode((505,705))
pygame.display.set_caption("Griddy")
font = pygame.font.Font("Anonymous.ttf", 7)

music_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "griddy.wav")
if os.path.exists(music_path):
    from pygame.locals import *
    from pygame import mixer
    mixer.init()
    mixer.music.load(music_path)
    mixer.music.play(-1)

data = json.load(open("griddy.json"))
index=0

purple = (138,43,226)
white = (255,255,255)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(purple)
    for i, line in enumerate(data[str(index%71)]):
        text = font.render(line, True, white)
        screen.blit(text, (2, 3+(i * 7)))
    index+=1
    time.sleep(.1)
    pygame.display.flip()
    
pygame.quit()
