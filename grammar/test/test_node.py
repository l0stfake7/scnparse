from nose.tools import *
from grammar import node

import re

strip_comments = re.compile("//.*?$", re.MULTILINE)

def test_track():
    src = re.sub(strip_comments, "", """
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
