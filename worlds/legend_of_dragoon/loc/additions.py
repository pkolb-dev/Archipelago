from typing import Dict

from worlds.legend_of_dragoon.loc.location_data import LegendOfDragoonLocationData

dart_addition_unlocks_table: Dict[str, LegendOfDragoonLocationData] = {
    "Dart - Volcano Unlock": LegendOfDragoonLocationData("Dart", 108_60001, "Addition"),
    "Dart - Burning Rush Unlock": LegendOfDragoonLocationData("Dart", 108_60002, "Addition"),
    "Dart - Crush Dance Unlock": LegendOfDragoonLocationData("Dart", 108_60003, "Addition"),
    "Dart - Madness Hero Unlock": LegendOfDragoonLocationData("Dart", 108_60004, "Addition"),
    "Dart - Moon Strike Unlock": LegendOfDragoonLocationData("Dart", 108_60005, "Addition"),
    "Dart - Blazing Dynamo Unlock": LegendOfDragoonLocationData("Dart", 108_60006, "Addition"),
}

rose_addition_unlocks_table: Dict[str, LegendOfDragoonLocationData] = {
    "Rose - More and More Unlock": LegendOfDragoonLocationData("Rose", 108_60011, "Addition"),
    "Rose - Hard Blade Unlock": LegendOfDragoonLocationData("Rose", 108_60012, "Addition"),
    "Rose - Demon's Dance Unlock": LegendOfDragoonLocationData("Rose", 108_60013, "Addition"),
}

lavitz_addition_unlocks_table: Dict[str, LegendOfDragoonLocationData] = {
    "Lavitz - Spinning Cane Unlock": LegendOfDragoonLocationData("Lavitz", 108_60021, "Addition"),
    "Lavitz - Rod Typhoon Unlock": LegendOfDragoonLocationData("Lavitz", 108_60022, "Addition"),
    "Lavitz - Gust Of Wind Dance Unlock": LegendOfDragoonLocationData("Lavitz", 108_60023, "Addition"),
    "Lavitz - Flower Storm Unlock": LegendOfDragoonLocationData("Lavitz", 108_60024, "Addition"),
}

haschel_addition_unlocks_table: Dict[str, LegendOfDragoonLocationData] = {
    "Haschel - Flurry of Styx Unlock": LegendOfDragoonLocationData("Haschel", 108_60041, "Addition"),
    "Haschel - Summon 4 Gods Unlock": LegendOfDragoonLocationData("Haschel", 108_60042, "Addition"),
    "Haschel - 5-Ring Shattering Unlock": LegendOfDragoonLocationData("Haschel", 108_60043, "Addition"),
    "Haschel - Hex Hammer Unlock": LegendOfDragoonLocationData("Haschel", 108_60044, "Addition"),
    "Haschel - Omni-Sweep Unlock": LegendOfDragoonLocationData("Haschel", 108_60045, "Addition"),
}

albert_addition_unlocks_table: Dict[str, LegendOfDragoonLocationData] = {
    "Albert - Spinning Cane Unlock": LegendOfDragoonLocationData("Albert", 108_60031, "Addition"),
    "Albert - Rod Typhoon Unlock": LegendOfDragoonLocationData("Albert", 108_60032, "Addition"),
    "Albert - Gust Of Wind Dance Unlock": LegendOfDragoonLocationData("Albert", 108_60033, "Addition"),
    "Albert - Flower Storm Unlock": LegendOfDragoonLocationData("Albert", 108_60034, "Addition"),
}

meru_addition_unlocks_table: Dict[str, LegendOfDragoonLocationData] = {
    "Meru - Hammer Spin Unlock": LegendOfDragoonLocationData("Meru", 108_60051, "Addition"),
    "Meru - Cool Boogie Unlock": LegendOfDragoonLocationData("Meru", 108_60052, "Addition"),
    "Meru - Cat's Cradle Unlock": LegendOfDragoonLocationData("Meru", 108_60053, "Addition"),
    "Meru - Perky Step Unlock": LegendOfDragoonLocationData("Meru", 108_60054, "Addition"),
}

kongol_addition_unlocks_table: Dict[str, LegendOfDragoonLocationData] = {
    "Kongol - Inferno Unlock": LegendOfDragoonLocationData("Kongol", 108_60061, "Addition"),
    "Kongol - Bone Crush Unlock": LegendOfDragoonLocationData("Kongol", 108_60062, "Addition"),
}

all_addition_locations_table: Dict[str, LegendOfDragoonLocationData] = {
    **dart_addition_unlocks_table,
    **rose_addition_unlocks_table,
    **lavitz_addition_unlocks_table,
    **albert_addition_unlocks_table,
    **haschel_addition_unlocks_table,
    **meru_addition_unlocks_table,
    **kongol_addition_unlocks_table,
}

all_character_unlocks_table: Dict[str, Dict[str, LegendOfDragoonLocationData]] = {
    "Dart": dart_addition_unlocks_table,
    "Lavitz": lavitz_addition_unlocks_table,
    "Rose": rose_addition_unlocks_table,
    "Haschel": haschel_addition_unlocks_table,
    "Albert": albert_addition_unlocks_table,
    "Meru": meru_addition_unlocks_table,
    "Kongol": kongol_addition_unlocks_table,
}

chapter_unlock_order: dict[int, list[str]] = {
    1: [
        "Dart - Volcano Unlock",
        "Dart - Burning Rush Unlock",
        "Dart - Crush Dance Unlock",
        "Rose - More and More Unlock",
        "Lavitz - Spinning Cane Unlock",
        "Lavitz - Rod Typhoon Unlock",
        "Lavitz - Gust Of Wind Dance Unlock",
        "Lavitz - Flower Storm Unlock",
        "Albert - Spinning Cane Unlock",
        "Albert - Rod Typhoon Unlock",
        "Albert - Gust Of Wind Dance Unlock",
        "Albert - Flower Storm Unlock",
        "Haschel - Flurry of Styx Unlock",
    ],
    2: [
        "Rose - Hard Blade Unlock",
        "Rose - Demon's Dance Unlock",
        "Haschel - Summon 4 Gods Unlock",
        "Meru - Hammer Spin Unlock",
    ],
    3: [
        "Dart - Madness Hero Unlock",
        "Haschel - 5-Ring Shattering Unlock",
        "Haschel - Hex Hammer Unlock",
        "Haschel - Omni-Sweep Unlock",
        "Meru - Cool Boogie Unlock",
        "Kongol - Inferno Unlock",
        "Kongol - Bone Crush Unlock",
    ],
    4: [
        "Dart - Moon Strike Unlock",
        "Dart - Blazing Dynamo Unlock",
        "Meru - Cat's Cradle Unlock",
        "Meru - Perky Step Unlock",
    ],
}


def build_chapter_unlock_table(chapter: int) -> Dict[str, LegendOfDragoonLocationData]:
    active_names = chapter_unlock_order.get(chapter, [])
    table = {}
    for char, char_table in all_character_unlocks_table.items():
        for name, loc_data in char_table.items():
            if name in active_names:
                table[name] = loc_data
    return table


chapter_one_addition_unlock_table = build_chapter_unlock_table(1)
chapter_two_addition_unlock_table = build_chapter_unlock_table(2)
chapter_three_addition_unlock_table = build_chapter_unlock_table(3)
chapter_four_addition_unlock_table = build_chapter_unlock_table(4)
