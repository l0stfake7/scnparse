from pyparsing import *
from common import Identifier, UIntNum, DecimalNum, Position, FileName

# common
NodeTag = CaselessKeyword('node')
Preamble = \
    NodeTag + \
    DecimalNum('max_dist') + \
    DecimalNum('min_dist') + \
    Identifier('Name')

# track
TrackTag = CaselessKeyword('track')
EndTrackTag = CaselessKeyword('endtrack')

Environment = oneOf('flat mountains canyon tunnel')
TrackPrefix = \
    DecimalNum('length') + \
    DecimalNum('width') + \
    DecimalNum('friction') + \
    DecimalNum('sound_dist') + \
    UIntNum('quality') + \
    UIntNum('damage_flag') + \
    Environment('environment') 

TrackSuffix = Each([\
    Optional(CaselessKeyword('velocity') + DecimalNum('velocity')), \
    Optional(CaselessKeyword('event0') + Identifier('event0')), \
    Optional(CaselessKeyword('event1') + Identifier('event1')), \
    Optional(CaselessKeyword('event2') + Identifier('event2')), \
    Optional(CaselessKeyword('isolated') + Identifier('isolated'))
])

VisTag = CaselessKeyword("vis").setParseAction(replaceWith(True))("visibile")
UnvisTag = CaselessKeyword("unvis").setParseAction(replaceWith(False))("visibile")

TrackMaterialParams = \
    Group(
        FileName('tex') + \
        DecimalNum('scale'))('rail') + \
    Group(
        FileName('tex') + \
        DecimalNum('height') + \
        DecimalNum('width') + \
        DecimalNum('slope'))('ballast')

TrackMaterial = (VisTag + TrackMaterialParams("material")) | UnvisTag

TrackGeometry = \
    Position('point') + \
    DecimalNum('roll') + \
    Position('control') + \
    Position('control') + \
    Position('point') + \
    DecimalNum('roll') + \
    DecimalNum('radius')

SwitchGeometry = \
    TrackGeometry + \
    Position('point') + \
    DecimalNum('roll') + \
    Position('control') + \
    Position('control') + \
    DecimalNum('roll') + \
    DecimalNum('radius')

Track = \
    Preamble + \
    TrackTag + \
    CaselessKeyword('normal') + \
    TrackPrefix + \
    TrackMaterial('material') + \
    TrackGeometry + \
    TrackSuffix + \
    EndTrackTag

Switch = \
    Preamble + \
    TrackTag + \
    CaselessKeyword('switch') + \
    TrackPrefix + \
    TrackMaterial + \
    SwitchGeometry + \
    TrackSuffix
