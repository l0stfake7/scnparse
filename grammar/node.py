from pyparsing import *
from common import Identifier, UIntNum, DecimalNum, Position, FileName

# common
NodeTag = CaselessKeyword('node')
Name = Keyword('none').setParseAction(replaceWith(None)) | Identifier

Preamble = \
    NodeTag + \
    DecimalNum('max_dist') + \
    DecimalNum('min_dist') + \
    Name('name')

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

TrackSuffix = \
    Optional(CaselessKeyword('velocity') + DecimalNum('velocity')) + \
    Group(Each([
        Optional(CaselessKeyword('event0') + Identifier('event0')), \
        Optional(CaselessKeyword('event1') + Identifier('event1')), \
        Optional(CaselessKeyword('event2') + Identifier('event2')), \
        Optional(CaselessKeyword('isolated') + Identifier('isolated')) \
    ]))('events')

VisTag = CaselessKeyword('vis').setParseAction(replaceWith(True))('visible')
UnvisTag = CaselessKeyword('unvis').setParseAction(replaceWith(False))('visible')

TrackMaterialParams = \
    Group(
        FileName('tex') + \
        DecimalNum('scale'))('rail') + \
    Group(
        FileName('tex') + \
        DecimalNum('height') + \
        DecimalNum('width') + \
        DecimalNum('slope'))('ballast')

TrackMaterial = (VisTag + TrackMaterialParams('material')) | UnvisTag

Point = Position.setResultsName('point', True)
Roll = DecimalNum.setResultsName('roll', True)
Control = Position.setResultsName('control', True)
Radius = DecimalNum.setResultsName('radius', True)

TrackGeometry = Point + Roll + Control + Control + Point + Roll + Radius
SwitchGeometry = TrackGeometry + TrackGeometry

Track = \
    Preamble + \
    TrackTag + \
    CaselessKeyword('normal') + \
    TrackPrefix + \
    TrackMaterial + \
    TrackGeometry('geometry') + \
    TrackSuffix + \
    EndTrackTag

Switch = \
    Preamble + \
    TrackTag + \
    CaselessKeyword('switch') + \
    TrackPrefix + \
    TrackMaterial + \
    SwitchGeometry('geometry') + \
    TrackSuffix + \
    EndTrackTag

Node = Track('track') | Switch('switch')
