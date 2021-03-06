from pyparsing import *
from decimal import Decimal

from common import DecimalNum, Identifier, Position

# common 
EventTag = CaselessKeyword('event')
EndEventTag = CaselessKeyword('endevent')
CommandValue = DecimalNum | Keyword('*')

# lights event
LightState = oneOf('0 1 2')
LightState.setParseAction(lambda tokens: int(tokens[0]))

Lights = \
    EventTag + \
    Identifier('name') + \
    CaselessKeyword('lights') + \
    DecimalNum('delay') + \
    Identifier('target') + \
    OneOrMore(LightState)('state') + \
    EndEventTag

# animation event
Animation = \
    EventTag + \
    Identifier('name') + \
    CaselessKeyword('animation') + \
    DecimalNum('delay') + \
    Identifier('target') + \
    oneOf('rotate translate', caseless=True)('kind') + \
    Identifier('submodel') + \
    Position('position') + \
    DecimalNum('speed') + \
    EndEventTag

# track velocity event
TrackVel = \
    EventTag + \
    Identifier('name') + \
    CaselessKeyword('trackvel') + \
    DecimalNum('delay') + \
    Identifier('target') + \
    DecimalNum('velocity') + \
    EndEventTag

# update values event
UpdateValues = \
    EventTag + \
    Identifier('name') + \
    CaselessKeyword('updatevalues') + \
    DecimalNum('delay') + \
    Identifier('target') + \
    Identifier('command') + \
    CommandValue('first') + \
    CommandValue('second') + \
    EndEventTag

# get values event
GetValues = \
    EventTag + \
    Identifier('name') + \
    CaselessKeyword('getvalues') + \
    DecimalNum('delay') + \
    Identifier('target') + \
    EndEventTag

# put values
#putValuesEvent = \

# multiple event
ConditionTag = CaselessKeyword('condition')

MemcompareCondition = CaselessKeyword('memcompare')('condition') + Identifier('command') + CommandValue('first') + CommandValue('second')
ProbabilityCondition = CaselessKeyword('probability')('condition') + DecimalNum('probability')
Condition = CaselessKeyword('trackoccupied')('condition') | CaselessKeyword('trackfree')('condition') | ProbabilityCondition | MemcompareCondition 

Multiple = \
    EventTag + \
    Identifier('name') + \
    CaselessKeyword('multiple') + \
    DecimalNum('delay') + \
    Identifier('target') + \
    Group(OneOrMore(~EndEventTag + ~ConditionTag + Identifier))('events') + \
    Optional(ConditionTag + Condition) + \
    EndEventTag

# switch event
SwitchState = oneOf('0 1').setParseAction(lambda t: int(t[0]))

Switch = \
    EventTag + \
    Identifier('name') + \
    CaselessKeyword('switch') + \
    DecimalNum('delay') + \
    Identifier('target') + \
    SwitchState('state') + \
    EndEventTag

# sound event
PlayStatus = oneOf('-1 0 1').setParseAction(lambda t: int(t[0]))

Sound = \
    EventTag + \
    Identifier('name') + \
    CaselessKeyword('sound') + \
    DecimalNum('delay') + \
    Identifier('target') + \
    PlayStatus('state') + \
    EndEventTag
