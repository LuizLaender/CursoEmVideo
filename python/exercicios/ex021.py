import pygame
import glob
from random import choice

allmusic = glob.glob('*.mp3')
played = choice(allmusic)

print(played)
pygame.mixer.init()

pygame.mixer.music.load(played)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pass
