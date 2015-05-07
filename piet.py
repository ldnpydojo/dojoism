import numpy as np
from matplotlib import pyplot as plt
from collections import namedtuple
from itertools import cycle


WHITE = '#f2f2e9'
pietColors = cycle([WHITE, '#bf0000', WHITE, '#0500ef', WHITE, '#fff700',])
swap = lambda x, y, flag: (y, x) if flag else (x, y)
Item = namedtuple('Item', 'xy wh depth')


def get_piet_rectangles(xy=(0., 0.), wh=(1., 1.), depth=0, direction=0):
    """Return a list of named tuples that contain rectangles to be drawn"""
    if depth < 1 or (np.random.random() > 0.2 and depth < 4):
        r = min(max(np.random.normal(0.5, 0.2), 0.2), 0.8)
        res = []
        for k in range(2):           
            i = Item(
                swap(xy[direction] + k * wh[direction] * r, xy[1 - direction], direction), 
                swap(wh[direction] * (r + (1 - 2 * r) * k), wh[1 - direction], direction), 
                depth + 1
            )
            res.append(i)
            res = res + get_piet_rectangles(direction=1 - direction, *i)
        return res
    else:
        return [Item(xy, wh, depth + 1)]

if __name__ == '__main__':
    np.random.seed(8)
    rectangles = get_piet_rectangles()
    rectangles = sorted(rectangles, key=lambda x: x.depth)

    fig = plt.figure(figsize=(16, 12))
    ax = plt.subplot(111)
    ax.axis('off')
    plt.ion()
    for r in rectangles:
        ax.add_patch(plt.Rectangle(r.xy, *r.wh, fc=pietColors.next() if min(r.wh)<0.1 or np.product(r.wh)<0.2 else WHITE, ec='k', lw=10))
    plt.savefig('test.png')
    
    from pprint import pprint
    pprint(rectangles)
