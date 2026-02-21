from .bases import LegendOfDragoonTestBase


# class TestProgressive(LegendOfDragoonTestBase):
#     options = {
#         "addition_randomizer": 3,
#     }

class TestAdditionSanity(LegendOfDragoonTestBase):
    options = {
        "addition_randomizer": 1,
    }


class TestRandomizedAdditionSanity(LegendOfDragoonTestBase):
    options = {
        "addition_randomizer": 1,
        "random_starting_addition": True,
    }
