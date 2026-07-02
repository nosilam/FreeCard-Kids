import FreeCAD as App
import Part

from .config import *


class Card:

    def __init__(self):

        self.doc = App.ActiveDocument

        if self.doc is None:
            self.doc = App.newDocument("FreeCard")

    def create_base(self):

        plate = Part.makeBox(
            CARD_WIDTH,
            CARD_HEIGHT,
            BASE_HEIGHT
        )

        return plate
      
