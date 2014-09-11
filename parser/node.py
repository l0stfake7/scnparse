from collections import namedtuple

import grammar.node
from common import parse_points

track_nested_fields = 'material geometry events'.split(' ')
track_fields = 'name min_dist max_dist length width friction sound_dist quality damage_flag visible velocity'.split(' ')

Track = namedtuple('Track', track_fields + track_nested_fields)
Switch = namedtuple('Switch', track_fields + track_nested_fields)


def parse_node(src):
    node = grammar.node.Node.parseString(src)
    name = node.getName()

    if name == 'track':
        return Track(**__parse_track(node))
    elif name == 'switch':
        return Switch(**__parse_track(node))


def __parse_track(src):
    kwargs = {k: src.get(k) for k in track_fields}
    kwargs.update({
        'material': {
            'rail': src['material']['rail'].asDict(),
            'ballast': src['material']['ballast'].asDict()
        },
        'geometry': {
            'point': parse_points(src['geometry']['point']),
            'control': parse_points(src['geometry']['control']),
            'roll': src['geometry']['roll'].asList()
        },
        'events': src['events'].asDict()
    })

    return kwargs

