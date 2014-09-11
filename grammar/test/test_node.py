from nose.tools import *
from grammar import node

import re

strip_comments_re = re.compile("//.*?$", re.MULTILINE)

def strip_comments(src):
    return re.sub(strip_comments_re, "", src)

def test_track():
    src = strip_comments("""
        node -1 0 none track normal 100.0 1.435 0.15 25.0 20 0 flat vis 
        rail_screw_used1 6 1435mm/tpbps-new2 0.2 0.5 1.1 
        0.396851 0.2 36.1112  -2.5  //point 1
        0.0 0.0 0.0  //control vector 1
        0.0 0.0 0.0  //control vector 2
        0.396825 0.2 136.111  0.0  //point 2
        0
        event2 tdo_rez_SHP 
        endtrack
    """)

    result = node.Track.parseString(src)

def test_track_isolated_event():
    src = strip_comments("""
        node 1100 0 Ozimek_zwr03 track switch 34.0 1.435 0.24 15.0 20 2 flat vis 
        rail_screw_used1 4 rail_screw_used1 0.2 2.75 2.5 
        13064.6 -11.6007 7984.21 0.1 //point 1
        0.0 0.0 0.0 //control vector 1
        0.0 0.0 0.0 //control vector 2
        13097.4 -11.6007 7993.01 -0.1 //point 2
        0 
        13064.6 -11.6007 7984.21 0 //point 1
        10.9482 0.0 2.93359 //control vector 1
        -11.21 0.0 -1.67676 //control vector 2
        13097.8 -11.6007 7991.13 0 //point 2
        300.0 
        isolated ozimek_Zwr
        endtrack
    """)

    result = node.Switch.parseString(src)
