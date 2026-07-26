from typing import Dict

from worlds.legend_of_dragoon.loc.location_data import LegendOfDragoonLocationData

dart_magic_unlocks_table: Dict[str, LegendOfDragoonLocationData] = {
    "Dart - Magic Level 1 Unlock": LegendOfDragoonLocationData("Dart", 108_90000, "Magic"),
    "Dart - Magic Level 2 Unlock": LegendOfDragoonLocationData("Dart", 108_90001, "Magic"),
    "Dart - Magic Level 3 Unlock": LegendOfDragoonLocationData("Dart", 108_90002, "Magic"),
    "Dart - Magic Level 4 Unlock": LegendOfDragoonLocationData("Dart", 108_90003, "Magic"),
    "Dart - Magic Level 5 Unlock": LegendOfDragoonLocationData("Dart", 108_90004, "Magic"),
}

lavitz_magic_unlocks_table: Dict[str, LegendOfDragoonLocationData] = {
    "Lavitz - Magic Level 1 Unlock": LegendOfDragoonLocationData("Lavitz", 108_90010, "Magic"),
    "Lavitz - Magic Level 2 Unlock": LegendOfDragoonLocationData("Lavitz", 108_90011, "Magic"),
    "Lavitz - Magic Level 3 Unlock": LegendOfDragoonLocationData("Lavitz", 108_90012, "Magic"),
    "Lavitz - Magic Level 4 Unlock": LegendOfDragoonLocationData("Lavitz", 108_90013, "Magic"),
    "Lavitz - Magic Level 5 Unlock": LegendOfDragoonLocationData("Lavitz", 108_90014, "Magic"),
}

shana_magic_unlocks_table: Dict[str, LegendOfDragoonLocationData] = {
    "Shana - Magic Level 1 Unlock": LegendOfDragoonLocationData("Shana", 108_90020, "Magic"),
    "Shana - Magic Level 2 Unlock": LegendOfDragoonLocationData("Shana", 108_90021, "Magic"),
    "Shana - Magic Level 3 Unlock": LegendOfDragoonLocationData("Shana", 108_90022, "Magic"),
    "Shana - Magic Level 4 Unlock": LegendOfDragoonLocationData("Shana", 108_90023, "Magic"),
    "Shana - Magic Level 5 Unlock": LegendOfDragoonLocationData("Shana", 108_90024, "Magic"),
}

rose_magic_unlocks_table: Dict[str, LegendOfDragoonLocationData] = {
    "Rose - Magic Level 1 Unlock": LegendOfDragoonLocationData("Rose", 108_90030, "Magic"),
    "Rose - Magic Level 2 Unlock": LegendOfDragoonLocationData("Rose", 108_90031, "Magic"),
    "Rose - Magic Level 3 Unlock": LegendOfDragoonLocationData("Rose", 108_90032, "Magic"),
    "Rose - Magic Level 4 Unlock": LegendOfDragoonLocationData("Rose", 108_90033, "Magic"),
    "Rose - Magic Level 5 Unlock": LegendOfDragoonLocationData("Rose", 108_90034, "Magic"),
}

haschel_magic_unlocks_table: Dict[str, LegendOfDragoonLocationData] = {
    "Haschel - Magic Level 1 Unlock": LegendOfDragoonLocationData("Haschel", 108_90040, "Magic"),
    "Haschel - Magic Level 2 Unlock": LegendOfDragoonLocationData("Haschel", 108_90041, "Magic"),
    "Haschel - Magic Level 3 Unlock": LegendOfDragoonLocationData("Haschel", 108_90042, "Magic"),
    "Haschel - Magic Level 4 Unlock": LegendOfDragoonLocationData("Haschel", 108_90043, "Magic"),
    "Haschel - Magic Level 5 Unlock": LegendOfDragoonLocationData("Haschel", 108_90044, "Magic"),
}

albert_magic_unlocks_table: Dict[str, LegendOfDragoonLocationData] = {
    "Albert - Magic Level 1 Unlock": LegendOfDragoonLocationData("Albert", 108_90050, "Magic"),
    "Albert - Magic Level 2 Unlock": LegendOfDragoonLocationData("Albert", 108_90051, "Magic"),
    "Albert - Magic Level 3 Unlock": LegendOfDragoonLocationData("Albert", 108_90052, "Magic"),
    "Albert - Magic Level 4 Unlock": LegendOfDragoonLocationData("Albert", 108_90053, "Magic"),
    "Albert - Magic Level 5 Unlock": LegendOfDragoonLocationData("Albert", 108_90054, "Magic"),
}

meru_magic_unlocks_table: Dict[str, LegendOfDragoonLocationData] = {
    "Meru - Magic Level 1 Unlock": LegendOfDragoonLocationData("Meru", 108_90060, "Magic"),
    "Meru - Magic Level 2 Unlock": LegendOfDragoonLocationData("Meru", 108_90061, "Magic"),
    "Meru - Magic Level 3 Unlock": LegendOfDragoonLocationData("Meru", 108_90062, "Magic"),
    "Meru - Magic Level 4 Unlock": LegendOfDragoonLocationData("Meru", 108_90063, "Magic"),
    "Meru - Magic Level 5 Unlock": LegendOfDragoonLocationData("Meru", 108_90064, "Magic"),
}

kongol_magic_unlocks_table: Dict[str, LegendOfDragoonLocationData] = {
    "Kongol - Magic Level 1 Unlock": LegendOfDragoonLocationData("Kongol", 108_90070, "Magic"),
    "Kongol - Magic Level 2 Unlock": LegendOfDragoonLocationData("Kongol", 108_90071, "Magic"),
    "Kongol - Magic Level 3 Unlock": LegendOfDragoonLocationData("Kongol", 108_90072, "Magic"),
    "Kongol - Magic Level 4 Unlock": LegendOfDragoonLocationData("Kongol", 108_90073, "Magic"),
    "Kongol - Magic Level 5 Unlock": LegendOfDragoonLocationData("Kongol", 108_90074, "Magic"),
}

miranda_magic_unlocks_table: Dict[str, LegendOfDragoonLocationData] = {
    "Miranda - Magic Level 1 Unlock": LegendOfDragoonLocationData("Miranda", 108_90080, "Magic"),
    "Miranda - Magic Level 2 Unlock": LegendOfDragoonLocationData("Miranda", 108_90081, "Magic"),
    "Miranda - Magic Level 3 Unlock": LegendOfDragoonLocationData("Miranda", 108_90082, "Magic"),
    "Miranda - Magic Level 4 Unlock": LegendOfDragoonLocationData("Miranda", 108_90083, "Magic"),
    "Miranda - Magic Level 5 Unlock": LegendOfDragoonLocationData("Miranda", 108_90084, "Magic"),
}

all_magic_locations_table: Dict[str, LegendOfDragoonLocationData] = {
    **dart_magic_unlocks_table,
    **lavitz_magic_unlocks_table,
    **shana_magic_unlocks_table,
    **rose_magic_unlocks_table,
    **albert_magic_unlocks_table,
    **haschel_magic_unlocks_table,
    **meru_magic_unlocks_table,
    **kongol_magic_unlocks_table,
    **miranda_magic_unlocks_table,
}

all_character_magic_unlocks_table: Dict[str, Dict[str, LegendOfDragoonLocationData]] = {
    "Dart": dart_magic_unlocks_table,
    "Lavitz": lavitz_magic_unlocks_table,
    "Shana": shana_magic_unlocks_table,
    "Rose": rose_magic_unlocks_table,
    "Haschel": haschel_magic_unlocks_table,
    "Albert": albert_magic_unlocks_table,
    "Meru": meru_magic_unlocks_table,
    "Kongol": kongol_magic_unlocks_table,
    "Miranda": miranda_magic_unlocks_table,
}
