from .bases import LegendOfDragoonTestBase

class TestDefault(LegendOfDragoonTestBase):
    options = {}


class TestFruegel2(LegendOfDragoonTestBase):
    options = {
        "lod_completion_condition": 2,
    }

class TestDoel(LegendOfDragoonTestBase):
    options = {
        "lod_completion_condition": 3,
    }

class TestLenus2(LegendOfDragoonTestBase):
    options = {
        "lod_completion_condition": 4,
    }

class TestFaust(LegendOfDragoonTestBase):
    options = {
        "lod_completion_condition": 5,
    }

class TestMelbu(LegendOfDragoonTestBase):
    options = {
        "lod_completion_condition": 6,
    }

