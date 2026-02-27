from .bases import LegendOfDragoonTestBase
from ..item.additions import chapter_one_addition_item_table, all_addition_items, chapter_two_addition_item_table, \
    chapter_three_addition_item_table, chapter_four_addition_item_table


class TestOptionOffChapter1(LegendOfDragoonTestBase):
    options = {
        "addition_randomizer": 0,
        "lod_completion_condition": 1,
    }
    run_default_tests = False

    def test_additions_dont_exist(self) -> None:
        present = self.get_items_by_name(list(all_addition_items.keys()))
        self.assertFalse(len(present))
        self.assertEqual(0, len(present))


class TestOptionOffChapter2(LegendOfDragoonTestBase):
    options = {
        "addition_randomizer": 0,
        "lod_completion_condition": 2,
    }
    run_default_tests = False

    def test_additions_dont_exist(self) -> None:
        present = self.get_items_by_name(list(all_addition_items.keys()))
        self.assertFalse(len(present))
        self.assertEqual(0, len(present))


class TestOptionOffChapter3(LegendOfDragoonTestBase):
    options = {
        "addition_randomizer": 0,
        "lod_completion_condition": 3,
    }
    run_default_tests = False

    def test_additions_dont_exist(self) -> None:
        present = self.get_items_by_name(list(all_addition_items.keys()))
        self.assertFalse(len(present))
        self.assertEqual(0, len(present))


class TestOptionOffChapter4(LegendOfDragoonTestBase):
    options = {
        "addition_randomizer": 0,
        "lod_completion_condition": 4,
    }
    run_default_tests = False

    def test_additions_dont_exist(self) -> None:
        present = self.get_items_by_name(list(all_addition_items.keys()))
        self.assertFalse(len(present))
        self.assertEqual(0, len(present))


class TestAdditionSanityChapter1(LegendOfDragoonTestBase):
    options = {
        "addition_randomizer": 1,
        "lod_completion_condition": 1,
    }
    run_default_tests = False

    def test_additions_are_present(self) -> None:
        present = self.get_items_by_name(list(chapter_one_addition_item_table.keys()))
        self.assertTrue(len(present))


class TestAdditionSanityChapter2(LegendOfDragoonTestBase):
    options = {
        "addition_randomizer": 1,
        "lod_completion_condition": 2,
    }
    run_default_tests = False

    def test_additions_are_present(self) -> None:
        items = {
            **chapter_one_addition_item_table,
            **chapter_two_addition_item_table
        }
        present = self.get_items_by_name(list(items.keys()))
        self.assertTrue(len(present))


class TestAdditionSanityChapter3(LegendOfDragoonTestBase):
    options = {
        "addition_randomizer": 1,
        "lod_completion_condition": 3,
    }
    run_default_tests = False

    def test_additions_are_present(self) -> None:
        items = {
            **chapter_one_addition_item_table,
            **chapter_two_addition_item_table,
            **chapter_three_addition_item_table,
        }
        present = self.get_items_by_name(list(items.keys()))
        self.assertTrue(len(present))


class TestAdditionSanityChapter4(LegendOfDragoonTestBase):
    options = {
        "addition_randomizer": 1,
        "lod_completion_condition": 4,
    }
    run_default_tests = False

    def test_additions_are_present(self) -> None:
        items = {
            **chapter_one_addition_item_table,
            **chapter_two_addition_item_table,
            **chapter_three_addition_item_table,
            **chapter_four_addition_item_table,
        }
        present = self.get_items_by_name(list(items.keys()))
        self.assertTrue(len(present))


class TestProgressiveAdditionsChapter1(LegendOfDragoonTestBase):
    options = {
        "addition_randomizer": 2,
        "lod_completion_condition": 1,
    }
    run_default_tests = False

    def test_progressive_additions_are_present(self) -> None:
        items = {
            **chapter_one_addition_item_table
        }

        # list should be empty - replaced by progressive items
        empty = self.get_items_by_name(list(items.keys()))
        self.assertFalse(len(empty))

        dart_progressive_additions = self.get_items_by_name("Dart Progressive Addition")
        lavitz_progressive_additions = self.get_items_by_name("Lavitz Progressive Addition")
        rose_progressive_additions = self.get_items_by_name("Rose Progressive Addition")
        haschel_progressive_additions = self.get_items_by_name("Haschel Progressive Addition")
        albert_progressive_additions = self.get_items_by_name("Albert Progressive Addition")
        meru_progressive_additions = self.get_items_by_name("Meru Progressive Addition")
        kongol_progressive_additions = self.get_items_by_name("Kongol Progressive Addition")
        total_progressive_additions = len(dart_progressive_additions) + len(lavitz_progressive_additions) + len(
            rose_progressive_additions) + len(haschel_progressive_additions) + len(albert_progressive_additions) + len(
            meru_progressive_additions) + len(kongol_progressive_additions)

        self.assertEqual(len(dart_progressive_additions), 4)
        self.assertEqual(len(lavitz_progressive_additions), 5)
        self.assertEqual(len(rose_progressive_additions), 2)
        self.assertEqual(len(haschel_progressive_additions), 2)
        self.assertEqual(len(albert_progressive_additions), 5)
        self.assertEqual(len(meru_progressive_additions), 0)
        self.assertEqual(len(kongol_progressive_additions), 0)
        self.assertEqual(total_progressive_additions, len(items.keys()))


class TestProgressiveAdditionsChapter2(LegendOfDragoonTestBase):
    options = {
        "addition_randomizer": 2,
        "lod_completion_condition": 2,
    }
    run_default_tests = False

    def test_progressive_additions_are_present(self) -> None:
        items = {
            **chapter_one_addition_item_table,
            **chapter_two_addition_item_table,
        }

        empty = self.get_items_by_name(list(items.keys()))
        self.assertFalse(len(empty))

        dart_progressive_additions = self.get_items_by_name("Dart Progressive Addition")
        lavitz_progressive_additions = self.get_items_by_name("Lavitz Progressive Addition")
        rose_progressive_additions = self.get_items_by_name("Rose Progressive Addition")
        haschel_progressive_additions = self.get_items_by_name("Haschel Progressive Addition")
        albert_progressive_additions = self.get_items_by_name("Albert Progressive Addition")
        meru_progressive_additions = self.get_items_by_name("Meru Progressive Addition")
        kongol_progressive_additions = self.get_items_by_name("Kongol Progressive Addition")
        total_progressive_additions = len(dart_progressive_additions) + len(lavitz_progressive_additions) + len(
            rose_progressive_additions) + len(haschel_progressive_additions) + len(albert_progressive_additions) + len(
            meru_progressive_additions) + len(kongol_progressive_additions)

        self.assertEqual(len(dart_progressive_additions), 4)
        self.assertEqual(len(lavitz_progressive_additions), 5)
        self.assertEqual(len(rose_progressive_additions), 4)
        self.assertEqual(len(haschel_progressive_additions), 3)
        self.assertEqual(len(albert_progressive_additions), 5)
        self.assertEqual(len(meru_progressive_additions), 2)
        self.assertEqual(len(kongol_progressive_additions), 1)
        self.assertEqual(total_progressive_additions, len(items.keys()))


class TestProgressiveAdditionsChapter3(LegendOfDragoonTestBase):
    options = {
        "addition_randomizer": 2,
        "lod_completion_condition": 3,
    }
    run_default_tests = False

    def test_progressive_additions_are_present(self) -> None:
        items = {
            **chapter_one_addition_item_table,
            **chapter_two_addition_item_table,
            **chapter_three_addition_item_table,
        }

        empty = self.get_items_by_name(list(items.keys()))
        self.assertFalse(len(empty))

        dart_progressive_additions = self.get_items_by_name("Dart Progressive Addition")
        lavitz_progressive_additions = self.get_items_by_name("Lavitz Progressive Addition")
        rose_progressive_additions = self.get_items_by_name("Rose Progressive Addition")
        haschel_progressive_additions = self.get_items_by_name("Haschel Progressive Addition")
        albert_progressive_additions = self.get_items_by_name("Albert Progressive Addition")
        meru_progressive_additions = self.get_items_by_name("Meru Progressive Addition")
        kongol_progressive_additions = self.get_items_by_name("Kongol Progressive Addition")
        total_progressive_additions = len(dart_progressive_additions) + len(lavitz_progressive_additions) + len(
            rose_progressive_additions) + len(haschel_progressive_additions) + len(albert_progressive_additions) + len(
            meru_progressive_additions) + len(kongol_progressive_additions)

        self.assertEqual(len(dart_progressive_additions), 5)
        self.assertEqual(len(lavitz_progressive_additions), 5)
        self.assertEqual(len(rose_progressive_additions), 4)
        self.assertEqual(len(haschel_progressive_additions), 6)
        self.assertEqual(len(albert_progressive_additions), 5)
        self.assertEqual(len(meru_progressive_additions), 3)
        self.assertEqual(len(kongol_progressive_additions), 3)
        self.assertEqual(total_progressive_additions, len(items.keys()))


class TestProgressiveAdditionsChapter4(LegendOfDragoonTestBase):
    options = {
        "addition_randomizer": 2,
        "lod_completion_condition": 4,
    }
    run_default_tests = False

    def test_progressive_additions_are_present(self) -> None:
        items = {
            **chapter_one_addition_item_table,
            **chapter_two_addition_item_table,
            **chapter_three_addition_item_table,
            **chapter_four_addition_item_table,
        }

        empty = self.get_items_by_name(list(items.keys()))
        self.assertFalse(len(empty))

        dart_progressive_additions = self.get_items_by_name("Dart Progressive Addition")
        lavitz_progressive_additions = self.get_items_by_name("Lavitz Progressive Addition")
        rose_progressive_additions = self.get_items_by_name("Rose Progressive Addition")
        haschel_progressive_additions = self.get_items_by_name("Haschel Progressive Addition")
        albert_progressive_additions = self.get_items_by_name("Albert Progressive Addition")
        meru_progressive_additions = self.get_items_by_name("Meru Progressive Addition")
        kongol_progressive_additions = self.get_items_by_name("Kongol Progressive Addition")
        total_progressive_additions = len(dart_progressive_additions) + len(lavitz_progressive_additions) + len(
            rose_progressive_additions) + len(haschel_progressive_additions) + len(albert_progressive_additions) + len(
            meru_progressive_additions) + len(kongol_progressive_additions)

        self.assertEqual(len(dart_progressive_additions), 7)
        self.assertEqual(len(lavitz_progressive_additions), 5)
        self.assertEqual(len(rose_progressive_additions), 4)
        self.assertEqual(len(haschel_progressive_additions), 6)
        self.assertEqual(len(albert_progressive_additions), 5)
        self.assertEqual(len(meru_progressive_additions), 5)
        self.assertEqual(len(kongol_progressive_additions), 3)
        self.assertEqual(total_progressive_additions, len(items.keys()))
