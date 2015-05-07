import numpy as np
from matplotlib import pyplot as plt
from collections import namedtuple


swap = lambda x, y, flag: (y, x) if flag else (x, y)
Item = namedtuple('Item', 'xy wh depth')


def get_piet_rectangles(xy=(0., 0.), wh=(1., 1.), depth=0, direction=0):
    """Return a list of named tuples that contain rectangles to be drawn"""
    if depth < 1 or (np.random.random() > 0.2 and depth < 4):
        r = min(max(np.random.normal(0.5, 0.2), 0.2), 0.8)
        for k in range(2):           
            i = Item(
                swap(xy[direction] + k * wh[direction] * r, xy[1 - direction], direction), 
                swap(wh[direction] * (r + (1 - 2 * r) * k), wh[1 - direction], direction), 
                depth + 1
            )
        yield i
        get_piet_rectangles(direction=1 - direction, *i)
    else:
        yield Item(xy, wh, depth + 1)

if __name__ == 'main':
    np.random.seed(8)
    rectangles = list(get_piet_rectangles())
    from pprint import pprint
    pprint(rectangles)
