from .bases import LegendOfDragoonTestBase


class TestShopsanityChapter1(LegendOfDragoonTestBase):
    options = {
        "lod_completion_condition": 1,
        "enable_shopsanity": True
    }
    run_default_tests = False


class TestShopsanityChapter2(LegendOfDragoonTestBase):
    options = {
        "lod_completion_condition": 2,
        "enable_shopsanity": True
    }
    run_default_tests = False


class TestShopsanityChapter3(LegendOfDragoonTestBase):
    options = {
        "lod_completion_condition": 3,
        "enable_shopsanity": True
    }
    run_default_tests = False


class TestShopsanityChapter4(LegendOfDragoonTestBase):
    options = {
        "lod_completion_condition": 4,
        "enable_shopsanity": True
    }
    run_default_tests = False


class TestShopsanityOffChapter1(LegendOfDragoonTestBase):
    options = {
        "lod_completion_condition": 1,
        "addition_randomizer": 1,
        "enable_shopsanity": False
    }
    run_default_tests = False


class TestShopsanityOffChapter2(LegendOfDragoonTestBase):
    options = {
        "lod_completion_condition": 2,
        "addition_randomizer": 1,
        "enable_shopsanity": False
    }
    run_default_tests = False


class TestShopsanityOffChapter3(LegendOfDragoonTestBase):
    options = {
        "lod_completion_condition": 3,
        "addition_randomizer": 1,
        "enable_shopsanity": False
    }
    run_default_tests = False


class TestShopsanityOffChapter4(LegendOfDragoonTestBase):
    options = {
        "lod_completion_condition": 4,
        "addition_randomizer": 1,
        "enable_shopsanity": False
    }
    run_default_tests = False
