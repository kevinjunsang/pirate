import pygame
import sys
import time
import random

from cannon_settings import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

board = pygame.image.load("assets/images/bg_wood.png").convert()
board.set_colorkey(BLACK)
water1 = pygame.image.load("assets/images/water1.png").convert()
water1.set_colorkey(BLACK)
water2 = pygame.image.load("assets/images/water2.png").convert()
water2.set_colorkey(BLACK)
screen.fill(SKY_COLOR)

background_board = screen.copy()
background_ocean = screen.copy()


# create the board background
def create_background_board():
    for i in range(SCREEN_WIDTH // BOARD_SIZE):
        background_board.blit(board,
                              (BOARD_SIZE * i,
                               SCREEN_HEIGHT - TILE_SIZE))
        background_board.blit(board,
                              (BOARD_SIZE * i,
                               -3 * TILE_SIZE))
    for j in range(SCREEN_HEIGHT // BOARD_SIZE):
        background_board.blit(board,
                              (SCREEN_WIDTH - TILE_SIZE,
                               BOARD_SIZE * j))
        background_board.blit(board,
                              (-3 * TILE_SIZE,
                               BOARD_SIZE * j))
    pygame.display.flip()


create_background_board()


# create the ocean background
def create_background_ocean():
    for i in range(SCREEN_WIDTH // WATER_WIDTH):
        background_ocean.blit(water1,
                              (2 * i * WATER_WIDTH,
                               SCREEN_HEIGHT - 2 * TILE_SIZE))
        background_ocean.blit(water2,
                              ((2 * i + 1) * WATER_WIDTH,
                               SCREEN_HEIGHT - 2 * TILE_SIZE))
    pygame.display.flip()


create_background_ocean()
screen.blit(background_ocean, (0, 0))
screen.blit(background_board, (0, 0))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
