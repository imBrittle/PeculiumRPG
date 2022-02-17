# Peculium RPG Game Menu
import pygame, sys

# Setup Pygame
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Peculium Alpha')
screen = pygame.display.set_mode((640, 480), pygame.RESIZABLE)

font = pygame.font.SysFont(None, 20)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

click = False

def main_menu():
    while True:

        screen.fill((0,0,0))
        draw_text('Main Menu', font, (255, 255, 255), screen, 20, 20)

        mx, my = pygame.mouse.get_pos()

        button_game = pygame.Rect(210, 100, 200, 50)
        button_options = pygame.Rect(210, 200, 200, 50)
        button_quit = pygame.Rect(210, 400, 200, 50)
        if button_game.collidepoint((mx, my)):
            if click:
                game()
        if button_options.collidepoint((mx, my)):
            if click:
                options()
        if button_quit.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()
        pygame.draw.rect(screen, (255, 0, 0), button_game)
        pygame.draw.rect(screen, (255, 0, 0), button_options)
        pygame.draw.rect(screen, (255, 0, 0), button_quit)

        # Button Text
        draw_text('Play', font, (255, 255, 255), screen, 295, 115)
        draw_text('Options', font, (255, 255, 255), screen, 285, 215)
        draw_text('Quit', font, (255, 255, 255), screen, 295, 415)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

def game():
    running = True

    playerX = 300
    playerY = 300
    playerVelocity = 5
    player = Rect(playerX, playerY, 50, 50)

    enemy = Rect(150, 150, 50, 50)
    while running:
        screen.fill((0,0,0))

        draw_text('Game', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        # Character Movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            playerX -= playerVelocity
        if keys[pygame.K_d]:
            playerX += playerVelocity
        if keys[pygame.K_w]:
            playerY -= playerVelocity
        if keys[pygame.K_s]:
            playerY += playerVelocity

        pygame.draw.rect(screen, (255, 0, 0), enemy, 1)
        pygame.draw.rect(screen, (255, 0, 255), (playerX, playerY, 50, 50))

        pygame.display.update()
        mainClock.tick(60)

def options():
    running = True
    while running:
        screen.fill((0,0,0))

        draw_text('Options', font, (255, 255, 255), screen, 20, 20)

        mx, my = pygame.mouse.get_pos()

        button_video = pygame.Rect(210, 100, 200, 50)
        button_audio = pygame.Rect(210, 200, 200, 50)
        button_other = pygame.Rect(210, 300, 200, 50)
        if button_video.collidepoint((mx, my)):
            if click:
                video_options()
        if button_audio.collidepoint((mx, my)):
            if click:
                pass
        if button_other.collidepoint((mx, my)):
            if click:
                pass
        pygame.draw.rect(screen, (255, 0, 0), button_video)
        pygame.draw.rect(screen, (255, 0, 0), button_audio)
        pygame.draw.rect(screen, (255, 0, 0), button_other)

        # Button Text
        draw_text('Video', font, (255, 255, 255), screen, 290, 115)
        draw_text('Audio', font, (255, 255, 255), screen, 290, 215)
        draw_text('Other', font, (255, 255, 255), screen, 290, 315)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)

def video_options():
    running = True
    while running:
        screen.fill((0,0,0))

        draw_text('Video', font, (255, 255, 255), screen, 20, 20)

        mx, my = pygame.mouse.get_pos()

        button_videotest1 = pygame.Rect(210, 100, 200, 50)
        button_videotest2 = pygame.Rect(210, 200, 200, 50)
        button_videotest3 = pygame.Rect(210, 300, 200, 50)

        if button_videotest1.collidepoint((mx, my)):
            if click:
                pass
        if button_videotest2.collidepoint((mx, my)):
            if click:
                pass
        if button_videotest3.collidepoint((mx, my)):
            if click:
                pass
        pygame.draw.rect(screen, (255, 0, 0), button_videotest1)
        pygame.draw.rect(screen, (255, 0, 0), button_videotest2)
        pygame.draw.rect(screen, (255, 0, 0), button_videotest3)

        # Button Text
        draw_text('Resolution', font, (255, 255, 255), screen, 290, 115)
        draw_text('Test', font, (255, 255, 255), screen, 290, 215)
        draw_text('Test', font, (255, 255, 255), screen, 290, 315)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)

main_menu()
