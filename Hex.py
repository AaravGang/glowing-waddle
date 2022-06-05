from utils import hexagon
import pygame


class Hex:
    def __init__(self, center, side_length):
        self.side_length = side_length
        self.center = center

        self.surf = pygame.Surface((2 * self.side_length, 2 * self.side_length))
        self.rect = self.surf.get_rect(center=center)

        self.origin = (self.side_length, self.side_length)
        self.hex_pts = hexagon(self.origin, self.side_length, flat=False)

    
    def draw(self,win)