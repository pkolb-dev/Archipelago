from .bases import LegendOfDragoonTestBase


class TestDefault(LegendOfDragoonTestBase):
    options = {}


class TestDoel(LegendOfDragoonTestBase):
    options = {
        "lod_completion_condition": 1,
    }
    run_default_tests = False


class TestLenus2(LegendOfDragoonTestBase):
    options = {
        "lod_completion_condition": 2,
    }
    run_default_tests = False


class TestLloyd2(LegendOfDragoonTestBase):
    options = {
        "lod_completion_condition": 3,
    }
    run_default_tests = False


class TestMelbu(LegendOfDragoonTestBase):
    options = {
        "lod_completion_condition": 4,
    }
    run_default_tests = False
