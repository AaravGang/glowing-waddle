import math
import pygame

pygame.font.init()


# Math constants
root3 = math.sqrt(3)


# Catan constants
num_hexes = 19
num_terrains = 5

terrain_types = ["desert", "pasture", "fields", "mountains", "forest", "hills"]
terrain_counts = {
    "desert": 1,
    "pasture": 4,
    "fields": 4,
    "mountains": 3,
    "forest": 4,
    "hills": 3,
}
resources = {
    "desert": None,
    "pasture": "wool",
    "fields": "grain",
    "mountains": "ore",
    "forest": "lumber",
    "hills": "brick",
}


# Screen constants
screen_width, screen_height = 1600, 800

# Color constants
BLACK = (0, 0, 0)
MATTE_BLACK = (33, 33, 33)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PINK = (200, 0, 50)
GREEN = (0, 255, 0)
OLIVE_GREEN = (50, 100, 0)
BLUE = (0, 0, 255)
NAVY = (0, 0, 130)
LIGHT_BLUE = (89, 154, 215)
YELLOW = (235, 214, 151)
CYAN = (0, 255, 255)
LIGHT_BROWN = (205, 144, 96)
ORANGE = (206, 11, 43)

# All the fonts
class Fonts:
    default_font_path = "static/fonts"

    chalkduster = pygame.font.Font(f"{default_font_path}/Chalkduster.ttf", 50,)


# Button Styles
DEFAULT_BUTTON_STYLE = {
    "font": Fonts.chalkduster,
    "hover_color": OLIVE_GREEN,
    "clicked_color": CYAN,
    "clicked_font_color": LIGHT_BROWN,
    "hover_font_color": ORANGE,
}

