from typing import Dict, TYPE_CHECKING

from .item_data import LegendOfDragoonItemData, ItemCategory, ItemClassification as IC

dart_spells_table: Dict[str, LegendOfDragoonItemData] = {
    "Dart Flame Shot": LegendOfDragoonItemData(ItemCategory.SPELL, 108_31001, IC.progression),
    "Dart Explosion": LegendOfDragoonItemData(ItemCategory.SPELL, 108_31002, IC.progression),
    "Dart Final Burst": LegendOfDragoonItemData(ItemCategory.SPELL, 108_31003, IC.progression),
    "Dart Red-Eye Dragon": LegendOfDragoonItemData(ItemCategory.SPELL, 108_31004, IC.progression),
    "Dart Divine DG Ball": LegendOfDragoonItemData(ItemCategory.SPELL, 108_31005, IC.progression),
    "Dart Divine DG Cannon": LegendOfDragoonItemData(ItemCategory.SPELL, 108_31006, IC.progression),
}

lavitz_spells_table: Dict[str, LegendOfDragoonItemData] = {
    "Lavitz Wing Blaster": LegendOfDragoonItemData(ItemCategory.SPELL, 108_31011, IC.progression),
    "Lavitz Blossom Storm": LegendOfDragoonItemData(ItemCategory.SPELL, 108_31012, IC.progression),
    "Lavitz Gaspless": LegendOfDragoonItemData(ItemCategory.SPELL, 108_31013, IC.progression),
    "Lavitz Jade Dragon": LegendOfDragoonItemData(ItemCategory.SPELL, 108_31014, IC.progression),
}

rose_spells_table: Dict[str, LegendOfDragoonItemData] = {
    "Rose Astral Drain": LegendOfDragoonItemData(ItemCategory.SPELL, 108_31021, IC.progression),
    "Rose Death Dimension": LegendOfDragoonItemData(ItemCategory.SPELL, 108_31022, IC.progression),
    "Rose Demon's Gate": LegendOfDragoonItemData(ItemCategory.SPELL, 108_31023, IC.progression),
    "Rose Dark Dragon": LegendOfDragoonItemData(ItemCategory.SPELL, 108_31024, IC.progression),
}

shana_spells_table: Dict[str, LegendOfDragoonItemData] = {
    "Shana Moon Light": LegendOfDragoonItemData(ItemCategory.SPELL, 108_31031, IC.progression),
    "Shana Star Children": LegendOfDragoonItemData(ItemCategory.SPELL, 108_31032, IC.progression),
    "Shana Gates of Heaven": LegendOfDragoonItemData(ItemCategory.SPELL, 108_31033, IC.progression),
    "Shana W Silver Dragon": LegendOfDragoonItemData(ItemCategory.SPELL, 108_31034, IC.progression),
}

haschel_spells_table: Dict[str, LegendOfDragoonItemData] = {
    "Haschel Atomic Mind": LegendOfDragoonItemData(ItemCategory.SPELL, 108_31041, IC.progression),
    "Haschel Thunder Kid": LegendOfDragoonItemData(ItemCategory.SPELL, 108_31042, IC.progression),
    "Haschel Thunder God": LegendOfDragoonItemData(ItemCategory.SPELL, 108_31043, IC.progression),
    "Haschel Violet Dragon": LegendOfDragoonItemData(ItemCategory.SPELL, 108_31044, IC.progression),
}

albert_spells_table: Dict[str, LegendOfDragoonItemData] = {
    "Albert Wing Blaster": LegendOfDragoonItemData(ItemCategory.SPELL, 108_31051, IC.progression),
    "Albert Rose Storm": LegendOfDragoonItemData(ItemCategory.SPELL, 108_31052, IC.progression),
    "Albert Gaspless": LegendOfDragoonItemData(ItemCategory.SPELL, 108_31053, IC.progression),
    "Albert Jade Dragon": LegendOfDragoonItemData(ItemCategory.SPELL, 108_31054, IC.progression),
}

meru_spells_table: Dict[str, LegendOfDragoonItemData] = {
    "Meru Freezing Ring": LegendOfDragoonItemData(ItemCategory.SPELL, 108_31061, IC.progression),
    "Meru Rainbow Breath": LegendOfDragoonItemData(ItemCategory.SPELL, 108_31062, IC.progression),
    "Meru Diamond Dust": LegendOfDragoonItemData(ItemCategory.SPELL, 108_31063, IC.progression),
    "Meru Blue Sea Dragon": LegendOfDragoonItemData(ItemCategory.SPELL, 108_31064, IC.progression),
}

kongol_spells_table: Dict[str, LegendOfDragoonItemData] = {
    "Kongol Grand Stream": LegendOfDragoonItemData(ItemCategory.SPELL, 108_31071, IC.progression),
    "Kongol Meteor Strike": LegendOfDragoonItemData(ItemCategory.SPELL, 108_31072, IC.progression),
    "Kongol Golden Dragon": LegendOfDragoonItemData(ItemCategory.SPELL, 108_31073, IC.progression),
}

miranda_spells_table: Dict[str, LegendOfDragoonItemData] = {
    "Miranda Moon Light": LegendOfDragoonItemData(ItemCategory.SPELL, 108_31081, IC.progression),
    "Miranda Star Children": LegendOfDragoonItemData(ItemCategory.SPELL, 108_31082, IC.progression),
    "Miranda Gates of Heaven": LegendOfDragoonItemData(ItemCategory.SPELL, 108_31083, IC.progression),
    "Miranda W Silver Dragon": LegendOfDragoonItemData(ItemCategory.SPELL, 108_31084, IC.progression),
}

all_character_spell_items: Dict[str, Dict[str, LegendOfDragoonItemData]] = {
    "Dart": dart_spells_table,
    "Lavitz": lavitz_spells_table,
    "Shana": shana_spells_table,
    "Rose": rose_spells_table,
    "Haschel": haschel_spells_table,
    "Albert": albert_spells_table,
    "Meru": meru_spells_table,
    "Kongol": kongol_spells_table,
    "Miranda": miranda_spells_table,
}

all_spell_items: Dict[str, LegendOfDragoonItemData] = {
    **dart_spells_table,
    **lavitz_spells_table,
    **shana_spells_table,
    **rose_spells_table,
    **haschel_spells_table,
    **albert_spells_table,
    **meru_spells_table,
    **kongol_spells_table,
    **miranda_spells_table,
}

progressive_spells_table: Dict[str, LegendOfDragoonItemData] = {
    "Dart Progressive Spell": LegendOfDragoonItemData(ItemCategory.SPELL, 108_31000, IC.progression, 6),
    "Lavitz Progressive Spell": LegendOfDragoonItemData(ItemCategory.SPELL, 108_31010, IC.progression, 4),
    "Shana Progressive Spell": LegendOfDragoonItemData(ItemCategory.SPELL, 108_31020, IC.progression, 4),
    "Rose Progressive Spell": LegendOfDragoonItemData(ItemCategory.SPELL, 108_31030, IC.progression, 4),
    "Haschel Progressive Spell": LegendOfDragoonItemData(ItemCategory.SPELL, 108_31040, IC.progression, 4),
    "Albert Progressive Spell": LegendOfDragoonItemData(ItemCategory.SPELL, 108_31050, IC.progression, 4),
    "Meru Progressive Spell": LegendOfDragoonItemData(ItemCategory.SPELL, 108_31060, IC.progression, 4),
    "Kongol Progressive Spell": LegendOfDragoonItemData(ItemCategory.SPELL, 108_31070, IC.progression, 3),
    "Miranda Progressive Spell": LegendOfDragoonItemData(ItemCategory.SPELL, 108_31080, IC.progression, 4),
}
