from math import sqrt

class Hex:
    hex_size = 50
    def __init__(self, terraintype, dicerollnumber:int, boardid:str):
        self.terrain = terraintype
        self.number = dicerollnumber
        self.pos = boardid

    
def hexagon(center, l, flat=False):
    centerx, centery = center

    root3 = sqrt(3)
    h = root3 / 2 * l
    x = h / root3

    # flat top hexagon
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
    else:
        return [
            (centerx, centery - l),
            (centerx - h, centery - x),
            (centerx - h, centery + x),
            (centerx, centery + l),
            (centerx + h, centery + x),
            (centerx + h, centery - x),
        ]

