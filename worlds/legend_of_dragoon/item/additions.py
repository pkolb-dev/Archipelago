from typing import Dict, TYPE_CHECKING

from .item_data import LegendOfDragoonItemData, ItemCategory, ItemClassification as IC
from ..options import CompletionCondition

dart_additions_table: Dict[str, LegendOfDragoonItemData] = {
    "Dart Double Slash": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30002, IC.progression),
    "Dart Volcano": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30003, IC.progression),
    "Dart Burning Rush": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30004, IC.progression),
    "Dart Crush Dance": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30005, IC.progression),
    "Dart Madness Hero": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30006, IC.progression),
    "Dart Moon Strike": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30007, IC.progression),
    "Dart Blazing Dynamo": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30008, IC.progression),
}

lavitz_additions_table: Dict[str, LegendOfDragoonItemData] = {
    "Lavitz Harpoon": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30010, IC.progression),
    "Lavitz Spinning Cane": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30011, IC.progression),
    "Lavitz Rod Typhoon": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30012, IC.progression),
    "Lavitz Gust Of Wind Dance": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30013, IC.progression),
    "Lavitz Flower Storm": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30014, IC.progression),
}

rose_additions_table: Dict[str, LegendOfDragoonItemData] = {
    "Rose Whip Smack": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30016, IC.progression),
    "Rose More More": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30017, IC.progression),
    "Rose Hard Blade": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30018, IC.progression),
    "Rose Demons Dance": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30019, IC.progression),
}

haschel_additions_table: Dict[str, LegendOfDragoonItemData] = {
    "Haschel Double Punch": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30021, IC.progression),
    "Haschel Ferry Of Styx": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30022, IC.progression),
    "Haschel Summon 4 Gods": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30023, IC.progression),
    "Haschel Five Ring Shattering": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30024, IC.progression),
    "Haschel Hex Hammer": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30025, IC.progression),
    "Haschel Omni Sweep": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30026, IC.progression),
}

albert_additions_table: Dict[str, LegendOfDragoonItemData] = {
    "Albert Harpoon": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30028, IC.progression),
    "Albert Spinning Cane": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30029, IC.progression),
    "Albert Rod Typhoon": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30030, IC.progression),
    "Albert Gust Of Wind Dance": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30031, IC.progression),
    "Albert Flower Storm": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30032, IC.progression),
}

meru_additions_table: Dict[str, LegendOfDragoonItemData] = {
    "Meru Double Smack": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30034, IC.progression),
    "Meru Hammer Spin": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30035, IC.progression),
    "Meru Cool Boogie": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30036, IC.progression),
    "Meru Cats Cradle": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30037, IC.progression),
    "Meru Perky Step": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30038, IC.progression),
}

kongol_additions_table: Dict[str, LegendOfDragoonItemData] = {
    "Kongol Pursuit": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30040, IC.progression),
    "Kongol Inferno": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30041, IC.progression),
    "Kongol Bone Crush": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30042, IC.progression),
}

all_character_addition_items: Dict[str, Dict[str, LegendOfDragoonItemData]] = {
    "Dart": dart_additions_table,
    "Lavitz": lavitz_additions_table,
    "Rose": rose_additions_table,
    "Haschel": haschel_additions_table,
    "Albert": albert_additions_table,
    "Meru": meru_additions_table,
    "Kongol": kongol_additions_table,
}

all_addition_items: Dict[str, LegendOfDragoonItemData] = {
    **dart_additions_table,
    **lavitz_additions_table,
    **rose_additions_table,
    **haschel_additions_table,
    **albert_additions_table,
    **meru_additions_table,
    **kongol_additions_table,
}

progressive_additions_table: Dict[str, LegendOfDragoonItemData] = {
    "Dart Progressive Addition": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30001, IC.progression, 7),
    "Lavitz Progressive Addition": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30009, IC.progression, 5),
    "Rose Progressive Addition": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30015, IC.progression, 4),
    "Haschel Progressive Addition": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30020, IC.progression, 6),
    "Albert Progressive Addition": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30027, IC.progression, 5),
    "Meru Progressive Addition": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30033, IC.progression, 5),
    "Kongol Progressive Addition": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30039, IC.progression, 3),
}


def get_active_characters(world) -> Dict[str, Dict[str, LegendOfDragoonItemData]]:
    """Return the character addition tables for the current completion goal."""
    characters = all_character_addition_items.copy()

    if world.options.lod_completion_condition == CompletionCondition.option_chapter_1:
        characters.pop("Meru")
        characters.pop("Kongol")

    return characters


chapter_addition_order: dict[int, list[str]] = {
    1: [
        "Dart Double Slash",
        "Dart Volcano",
        "Dart Burning Rush",
        "Dart Crush Dance",
        "Rose Whip Smack",
        "Rose More More",
        "Lavitz Harpoon",
        "Lavitz Spinning Cane",
        "Lavitz Rod Typhoon",
        "Lavitz Gust Of Wind Dance",
        "Lavitz Flower Storm",
        "Albert Harpoon",
        "Albert Spinning Cane",
        "Albert Rod Typhoon",
        "Albert Gust Of Wind Dance",
        "Albert Flower Storm",
        "Haschel Double Punch",
        "Haschel Ferry Of Styx"
    ],
    2: [
        "Rose Hard Blade",
        "Rose Demons Dance",
        "Haschel Summon 4 Gods",
        "Meru Double Smack",
        "Meru Hammer Spin",
        "Kongol Pursuit"
    ],
    3: [
        "Dart Madness Hero",
        "Haschel Five Ring Shattering",
        "Haschel Hex Hammer",
        "Haschel Omni Sweep",
        "Meru Cool Boogie",
        "Kongol Inferno",
        "Kongol Bone Crush",
    ],
    4: [
        "Dart Moon Strike",
        "Dart Blazing Dynamo",
        "Meru Cats Cradle",
        "Meru Perky Step",
    ],
}


def build_chapter_addition_item_table(chapter: int) -> Dict[str, LegendOfDragoonItemData]:
    """Return a dict of additions for a specific chapter."""
    active_names = chapter_addition_order.get(chapter, [])
    table: Dict[str, LegendOfDragoonItemData] = {}
    for char, char_table in all_character_addition_items.items():
        for name, item_data in char_table.items():
            if name in active_names:
                table[name] = item_data
    return table


chapter_one_addition_item_table = build_chapter_addition_item_table(1)
chapter_two_addition_item_table = build_chapter_addition_item_table(2)
chapter_three_addition_item_table = build_chapter_addition_item_table(3)
chapter_four_addition_item_table = build_chapter_addition_item_table(4)
