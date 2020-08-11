#Faça um programa em python que abra e reproduza o áudio de um arquivo mp3.
import pygame
#print('Curta o SOM :D ')
pygame.init()
pygame.mixer.load('aindatoai.mp3')
pygame.mixer.music.play()
pygame.event.wait()
