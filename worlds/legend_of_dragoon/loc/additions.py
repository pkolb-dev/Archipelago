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
    "Lavitz - Blossom Storm Unlock": LegendOfDragoonLocationData("Lavitz", 108_60024, "Addition"),
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
    "Albert - Blossom Storm Unlock": LegendOfDragoonLocationData("Albert", 108_60034, "Addition"),
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

chapter_one_addition_unlock_table: Dict[str, LegendOfDragoonLocationData] = {
    "Dart - Volcano Unlock": LegendOfDragoonLocationData("Dart", 108_60001, "Addition"),
    "Dart - Burning Rush Unlock": LegendOfDragoonLocationData("Dart", 108_60002, "Addition"),
    "Dart - Crush Dance Unlock": LegendOfDragoonLocationData("Dart", 108_60003, "Addition"),
    "Rose - More and More Unlock": LegendOfDragoonLocationData("Rose", 108_60011, "Addition"),
    "Lavitz - Spinning Cane Unlock": LegendOfDragoonLocationData("Lavitz", 108_60021, "Addition"),
    "Lavitz - Rod Typhoon Unlock": LegendOfDragoonLocationData("Lavitz", 108_60022, "Addition"),
    "Lavitz - Gust Of Wind Dance Unlock": LegendOfDragoonLocationData("Lavitz", 108_60023, "Addition"),
    "Lavitz - Blossom Storm Unlock": LegendOfDragoonLocationData("Lavitz", 108_60024, "Addition"),
    "Albert - Spinning Cane Unlock": LegendOfDragoonLocationData("Albert", 108_60031, "Addition"),
    "Albert - Rod Typhoon Unlock": LegendOfDragoonLocationData("Albert", 108_60032, "Addition"),
    "Albert - Gust Of Wind Dance Unlock": LegendOfDragoonLocationData("Albert", 108_60033, "Addition"),
    "Albert - Blossom Storm Unlock": LegendOfDragoonLocationData("Albert", 108_60034, "Addition"),
    "Haschel - Flurry of Styx Unlock": LegendOfDragoonLocationData("Haschel", 108_60041, "Addition"),
}

chapter_two_addition_unlock_table: Dict[str, LegendOfDragoonLocationData] = {
    "Rose - Hard Blade Unlock": LegendOfDragoonLocationData("Rose", 108_60012, "Addition"),
    "Rose - Demon's Dance Unlock": LegendOfDragoonLocationData("Rose", 108_60013, "Addition"),
    "Haschel - Summon 4 Gods Unlock": LegendOfDragoonLocationData("Haschel", 108_60042, "Addition"),
    "Meru - Hammer Spin Unlock": LegendOfDragoonLocationData("Meru", 108_60051, "Addition"),
}

chapter_three_addition_unlock_table: Dict[str, LegendOfDragoonLocationData] = {
    "Dart - Madness Hero Unlock": LegendOfDragoonLocationData("Dart", 108_60004, "Addition"),
    "Haschel - 5-Ring Shattering Unlock": LegendOfDragoonLocationData("Haschel", 108_60043, "Addition"),
    "Haschel - Hex Hammer Unlock": LegendOfDragoonLocationData("Haschel", 108_60044, "Addition"),
    "Haschel - Omni-Sweep Unlock": LegendOfDragoonLocationData("Haschel", 108_60045, "Addition"),
    "Meru - Cool Boogie Unlock": LegendOfDragoonLocationData("Meru", 108_60052, "Addition"),
    "Kongol - Inferno Unlock": LegendOfDragoonLocationData("Kongol", 108_60061, "Addition"),
    "Kongol - Bone Crush Unlock": LegendOfDragoonLocationData("Kongol", 108_60062, "Addition"),
}

chapter_four_addition_unlock_table: Dict[str, LegendOfDragoonLocationData] = {
    "Dart - Moon Strike Unlock": LegendOfDragoonLocationData("Dart", 108_60005, "Addition"),
    "Dart - Blazing Dynamo Unlock": LegendOfDragoonLocationData("Dart", 108_60006, "Addition"),
    "Meru - Cat's Cradle Unlock": LegendOfDragoonLocationData("Meru", 108_60053, "Addition"),
    "Meru - Perky Step Unlock": LegendOfDragoonLocationData("Meru", 108_60054, "Addition"),
}
