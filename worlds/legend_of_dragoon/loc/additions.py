from typing import Dict
from worlds.legend_of_dragoon.loc.location_data import LegendOfDragoonLocationData, LegendOfDragoonLocationInfo

dart_additions_table: list[str] = [
    "Double Slash",
    "Volcano",
    "Burning Rush",
    "Crush Dance",
    "Madness Hero",
    "Moon Strike",
    "Blazing Dynamo",
]

rose_additions_table: list[str] = [
    "Whip Smack",
    "More and More",
    "Hard Blade",
    "Demon's Dance"
]

lavitz_additions_table: list[str] = [
    "Harpoon",
    "Spinning Cane",
    "Rod Typhoon",
    "Gust Of Wind Dance",
    "Flower Storm"
]

shana_additions_table: list[str] = []

haschel_additions_table: list[str] = [
    "Double Punch",
    "Flurry of Styx",
    "Summon 4 Gods",
    "5-Ring Shattering",
    "Hex Hammer",
    "Omni-Sweep"
]

albert_additions_table: list[str] = [
    "Harpoon",
    "Spinning Cane",
    "Rod Typhoon",
    "Gust Of Wind Dance",
    "Flower Storm"
]

meru_additions_table: list[str] = [
    "Double Smack",
    "Hammer Spin",
    "Cool Boogie",
    "Cat's Cradle",
    "Perky Step"
]

kongol_additions_table: list[str] = [
    "Pursuit",
    "Inferno",
    "Bone Crush"
]

miranda_additions_table: list[str] = []

starting_additions: list[str] = [
    dart_additions_table[0],
    lavitz_additions_table[0],
    rose_additions_table[0],
    # shana_additions_table[0],
    haschel_additions_table[0],
    albert_additions_table[0],
    meru_additions_table[0],
    kongol_additions_table[0],
    # miranda_additions_table[0],
]

all_character_unlocks_table: Dict[str, list[str]] = {
    "Dart": dart_additions_table,
    "Lavitz": lavitz_additions_table,
    "Rose": rose_additions_table,
    "Shana": shana_additions_table,
    "Haschel": haschel_additions_table,
    "Albert": albert_additions_table,
    "Meru": meru_additions_table,
    "Kongol": kongol_additions_table,
    "Miranda": miranda_additions_table,
}

chapter_additions: dict[int, list[str]] = {
    1: [
        "Dart - Double Slash"
        "Dart - Volcano",
        "Dart - Burning Rush",
        "Dart - Crush Dance",
        "Rose - Whip Smack",
        "Rose - More and More",
        "Lavitz - Harpoon",
        "Lavitz - Spinning Cane",
        "Lavitz - Rod Typhoon",
        "Lavitz - Gust Of Wind Dance",
        "Lavitz - Flower Storm",
        "Albert - Harpoon",
        "Albert - Spinning Cane",
        "Albert - Rod Typhoon",
        "Albert - Gust Of Wind Dance",
        "Albert - Flower Storm",
        "Haschel - Double Punch",
        "Haschel - Flurry of Styx",
    ],
    2: [
        "Rose - Hard Blade",
        "Rose - Demon's Dance",
        "Haschel - Summon 4 Gods",
        "Meru - Double Smack",
        "Meru - Hammer Spin",
    ],
    3: [
        "Dart - Madness Hero",
        "Haschel - 5-Ring Shattering",
        "Haschel - Hex Hammer",
        "Haschel - Omni-Sweep",
        "Meru - Cool Boogie",
        "Kongol - Pursuit",
        "Kongol - Inferno",
        "Kongol - Bone Crush",
    ],
    4: [
        "Dart - Moon Strike",
        "Dart - Blazing Dynamo",
        "Meru - Cat's Cradle",
        "Meru - Perky Step",
    ],
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


def get_all_addition_locations() -> Dict[str, LegendOfDragoonLocationData]:
    base_id: int = 108_60000

    unlock_locations: list[LegendOfDragoonLocationInfo] = []
    addition_mastery_locations: list[LegendOfDragoonLocationInfo] = []
    for character, additions in all_character_unlocks_table.items():
        for addition in additions:
            for level in range(1, 5):
                addition_mastery_locations.append(
                    LegendOfDragoonLocationInfo(f"{character} - {addition} Level {level + 1}", character))
            if addition in starting_additions:
                continue
            unlock_locations.append(LegendOfDragoonLocationInfo(f"{character} - {addition} Unlock", character))

    all_locs = {}
    i: int = base_id
    for location in unlock_locations + addition_mastery_locations:
        all_locs.update({location.key: LegendOfDragoonLocationData(location.region, i, "Addition")})
        i += 1

    return all_locs


all_addition_locations_table = get_all_addition_locations()


def build_chapter_unlock_table(chapter: int) -> Dict[str, LegendOfDragoonLocationInfo]:
    active_names = chapter_additions.get(chapter, [])
    table = {}
    for loc_key, loc_data in all_addition_locations_table.items():
        for name in active_names:
            if name in loc_key:
                table[loc_key] = loc_data
    return table


chapter_one_addition_unlock_table = build_chapter_unlock_table(1)
chapter_two_addition_unlock_table = build_chapter_unlock_table(2)
chapter_three_addition_unlock_table = build_chapter_unlock_table(3)
chapter_four_addition_unlock_table = build_chapter_unlock_table(4)
