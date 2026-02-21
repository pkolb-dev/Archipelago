from .bases import LegendOfDragoonTestBase

class TestDefault(LegendOfDragoonTestBase):
    options = {}


class TestDoel(LegendOfDragoonTestBase):
    options = {
        "lod_completion_condition": 1,
    }


class TestLenus2(LegendOfDragoonTestBase):
    options = {
        "lod_completion_condition": 2,
    }

class TestLloyd2(LegendOfDragoonTestBase):
    options = {
        "lod_completion_condition": 3,
    }

class TestMelbu(LegendOfDragoonTestBase):
    options = {
        "lod_completion_condition": 4,
    }

