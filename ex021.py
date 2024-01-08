# Tocar um mp3

import pygame
pygame.init()
pygame.mixer.music.load('sincero.mp3')
pygame.mixer.music.play(start=0.5)
pygame.event.wait()
