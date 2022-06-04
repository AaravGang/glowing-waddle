from constants import *
from utils import hexagon
import pygame


class Board:
    def __init__(
        self, center: tuple, size: tuple,
    ):

        # size of the board
        self.size = size
        self.surf = pygame.Surface(self.size)
        # a rect surface with center of the board, relative to the window
        self.rect = self.surf.get_rect(center=center)

        # the center of the board, relative to the board
        self.center = (self.size[0] / 2, self.size[1] / 2)

        # hexagonal border of the board
        hex_side = min(*self.size) / 2 
        self.hex_pts = hexagon(self.center, hex_side, flat=True)
        self.border_width = 20

    def draw(self, win):
        self.surf.fill(WHITE)

        # draw hexaogonal border
        pygame.draw.polygon(self.surf, LIGHT_BLUE, self.hex_pts)

        win.blit(self.surf, self.rect)

