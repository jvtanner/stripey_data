#!/usr/bin/env python3

"""
Stanford CS106A Stripey Data Project
"""

import sys
from drawcanvas import DrawCanvas


DELTA = 127
BASE = 127


def draw_stripes(width, height, fracs, title):
    """
    Create a canvas of the given width and height.
    Draw the fracs data and title on the canvas.
    """
    canvas = DrawCanvas(width, height, title='Stripey')

    rec_width = width // len(fracs)
    for p in range(len(fracs)):
        start_x = (rec_width * p - (rec_width - 1))

        # color red
        blue = ((fracs[p] * (-1)) + 1) * DELTA
        green = BASE
        red = (fracs[p] + 1) * DELTA
        canvas.fill_rect(start_x, 0, rec_width, height, color=(red, green, blue))
    canvas.draw_string(5, 5, title, color='white')


def read_fracs(filename):
    """
    (provided)
    Given filename, read in and return a list
    of the "fracs" data values.
    Oddity: the index-0 element is the
    string title of this data set,
    the rest of the elements are the float values.
    """
    fracs = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        # First line is title
        fracs.append(lines.pop(0))
        # Process other lines as floats
        for line in lines:
            fracs.append(float(line))
        return fracs


def main():
    # (provided)
    args = sys.argv[1:]

    # Default window size is 800 by 400
    # Optionally command line can have width height numbers to override
    width = 800
    height = 400
    if len(args) == 3:
        width = int(args[len(args) - 2])
        height = int(args[len(args) - 1])

    if len(args) >= 1:
        fracs = read_fracs(args[0])
        title = fracs.pop(0)
        draw_stripes(width, height, fracs, title)

    DrawCanvas.mainloop()


if __name__ == '__main__':
    main()
