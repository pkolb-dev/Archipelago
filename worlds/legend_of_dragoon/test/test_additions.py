from .bases import LegendOfDragoonTestBase


class TestOptionOffChapter1(LegendOfDragoonTestBase):
    options = {
        "addition_randomizer": 0,
        "lod_completion_condition": 1,
    }


class TestOptionOffChapter2(LegendOfDragoonTestBase):
    options = {
        "addition_randomizer": 0,
        "lod_completion_condition": 2,
    }


class TestOptionOffChapter3(LegendOfDragoonTestBase):
    options = {
        "addition_randomizer": 0,
        "lod_completion_condition": 3,
    }


class TestOptionOffChapter4(LegendOfDragoonTestBase):
    options = {
        "addition_randomizer": 0,
        "lod_completion_condition": 4,
    }


class TestAdditionSanityChapter1(LegendOfDragoonTestBase):
    options = {
        "addition_randomizer": 1,
        "lod_completion_condition": 1,
    }


class TestAdditionSanityChapter2(LegendOfDragoonTestBase):
    options = {
        "addition_randomizer": 1,
        "lod_completion_condition": 2,
    }


class TestAdditionSanityChapter3(LegendOfDragoonTestBase):
    options = {
        "addition_randomizer": 1,
        "lod_completion_condition": 3,
    }


class TestAdditionSanityChapter4(LegendOfDragoonTestBase):
    options = {
        "addition_randomizer": 1,
        "lod_completion_condition": 4,
    }


class TestProgressiveAdditionsChapter1(LegendOfDragoonTestBase):
    options = {
        "addition_randomizer": 2,
        "lod_completion_condition": 1,
    }


class TestProgressiveAdditionsChapter2(LegendOfDragoonTestBase):
    options = {
        "addition_randomizer": 2,
        "lod_completion_condition": 2,
    }


class TestProgressiveAdditionsChapter3(LegendOfDragoonTestBase):
    options = {
        "addition_randomizer": 2,
        "lod_completion_condition": 3,
    }


class TestProgressiveAdditionsChapter4(LegendOfDragoonTestBase):
    options = {
        "addition_randomizer": 2,
        "lod_completion_condition": 4,
    }
