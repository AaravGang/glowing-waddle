from constants import root3
from button import Button
import pygame

# co-ordinates of a regular hexagon, provided center and side length
def hexagon(center, l, flat=False):
    centerx, centery = center

    h = root3 / 2 * l  # (#6 - #2)/2
    x = h / root3  # (#1 – #4)/2

    # flat top hexagon
    """ 
      /#5––––––#6\
     /            \
    /            #1\
    \#4            /
     \            /
      \#3––––––#2/
    """
    if flat:
        return [
            (centerx + l, centery),
            (centerx + x, centery + h),
            (centerx - x, centery + h),
            (centerx - l, centery),
            (centerx - x, centery - h),
            (centerx + x, centery - h),
        ]

    # pointed top hexagon

    #
    #      #1
    #      ／＼
    #     ／  ＼
    #    ／    ＼
    # #2／      ＼#6
    #   |       |
    #   |       |
    #   |       |
    # #3＼      ／#5
    #    ＼    ／
    #     ＼  ／
    #      ＼／
    #      #4

    else:
        return [
            (centerx, centery - l),
            (centerx - h, centery - x),
            (centerx - h, centery + x),
            (centerx, centery + l),
            (centerx + h, centery + x),
            (centerx + h, centery - x),
        ]


class Hex(Button):
    def __init__(self, parent: pygame.Surface, rect, color, function, points, **kwargs):
        super().__init__(
            parent, rect, color, function=function, shape=points, **kwargs,
        )

