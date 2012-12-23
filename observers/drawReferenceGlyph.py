"""
An example script of adding an observers and do *something* 

It draws a simple unicode reference of an existing installed font.
"""

from mojo.events import addObserver
from mojo.drawingTools import *

class DrawReferenceGlyph(object):
    
    def __init__(self):
        addObserver(self, "drawReferenceGlyph", "draw")

    def drawReferenceGlyph(self, info):
        
        glyph = info["glyph"]
        
        r = 0
        g = 0
        b = 0
        a = .5
        
        #if glyph is not None and glyph.unicode is not None:
        if glyph.unicode is not None:
            t = unichr(glyph.unicode)
            font("Georgia", 100)
            stroke(None)
            fill(r, g, b, a)
            text(t, (glyph.width + 25, -110))
        
            
DrawReferenceGlyph()