from collections import namedtuple

Point = namedtuple('Point', 'x y z')

def parse_points(src):
    return [Point(*p) for p in src]

