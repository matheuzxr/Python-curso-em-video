import pygame
pygame.init()
pygame.mixer.music.load('blue.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()