from Board import Board
import pygame

pygame.init()
from constants import *

win = pygame.display.set_mode((screen_width, screen_height))
board = Board((400, 400), (screen_height, screen_height))


def draw():
    win.fill(NAVY)
    board.draw(win)

    pygame.display.update()


def main():
    run = True
    while run:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False
                break
            board.check_event(e)

        draw()


if __name__ == "__main__":
    main()
