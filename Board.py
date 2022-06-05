from constants import *
from utils import *
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
        self.origin = (self.size[0] / 2, self.size[1] / 2)

        # hexagonal border of the board
        self.border_side_length = min(*self.size) / 2
        self.border_pts = hexagon(self.origin, self.border_side_length, flat=True)

        # hexagonal hexes
        self.hexgrid, self.hexmap = [], {}
        self.hexgrid, self.hexmap = self.hex_grid(5)

    # a row of hexes
    def hex_row(self, count, center, hex_width, buffer=0):
        hexes = []
        shapes = []

        centerx, centery = center

        # centerx of leftmost hex
        startx = (
            centerx - (count // 2) * hex_width
            if count % 2 == 1
            else centerx - (count // 2 - 1 / 2) * hex_width
        )
        # side length of each hex
        side_length = (hex_width - buffer) / root3

        # a default hex with top left as (0,0)
        default_hex = hexagon((hex_width / 2, side_length), side_length, flat=False)

        # callback function to call when a hex is clicked
        def foo(button):
            for hex in self.hexmap.values():
                hex.selected = False

            button.selected = True

        # add count number of hexes
        for i in range(count):
            # the points for the hexagon
            hex = hexagon((startx + i * (hex_width), centery), side_length, flat=False,)

            shapes.append(hex)
            hexes.append(
                Hex(
                    self.surf,
                    (
                        startx - hex_width / 2 + i * hex_width,
                        centery - side_length,
                        hex_width,
                        2 * side_length,
                    ),
                    YELLOW,
                    function=foo,
                    points=default_hex,
                    **DEFAULT_BUTTON_STYLE
                )
            )

        return hexes

    # create a hex grid of hexes
    def hex_grid(
        self, n_rows,
    ):
        hexgrid = []
        hexmap = {}

        # dynamically determine the width and side length of each hex
        hex_width = 2 * self.border_side_length / (n_rows + 1)
        side_length = root3 / 2 * hex_width
        self.road_width = hex_width / 10

        # create rows of hexes
        for i in range(-n_rows // 2 + 1, n_rows // 2 + 1):
            n_hexes = n_rows - abs(i)

            hexgrid.append(
                self.hex_row(
                    n_hexes,
                    (self.origin[0], self.origin[1] + i * side_length),
                    hex_width,
                    buffer=self.road_width,
                )
            )

        # hexes mapped to keys
        hexmap = dict(enumerate([hex for row in hexgrid for hex in row]))

        return hexgrid, hexmap

    def draw(self, win):
        self.surf.fill(WHITE)

        # draw hexaogonal border
        pygame.draw.polygon(self.surf, LIGHT_BLUE, self.border_pts)

        # draw hexes
        for hex in self.hexmap.values():
            hex.update()

        win.blit(self.surf, self.rect)

    # check for user events
    def check_event(self, e):
        for hex in self.hexmap.values():
            hex.check_event(e)

