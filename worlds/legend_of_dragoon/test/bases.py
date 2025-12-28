from test.bases import WorldTestBase
from worlds.legend_of_dragoon import LegendOfDragoonWorld, lod_name
from worlds.legend_of_dragoon.options import LegendOfDragoonOptions

class LegendOfDragoonTestBase(WorldTestBase):
    game = lod_name
    world = LegendOfDragoonWorld
    options = {}
