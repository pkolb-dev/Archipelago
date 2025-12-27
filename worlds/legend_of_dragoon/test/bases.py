from test.bases import WorldTestBase
from worlds.legend_of_dragoon import LegendOfDragoonWorld, lod_name

class LegendOfDragoonTestBase(WorldTestBase):
    game = lod_name
    world = LegendOfDragoonWorld