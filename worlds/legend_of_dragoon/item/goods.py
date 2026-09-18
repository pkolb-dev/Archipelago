from typing import Dict

from .item_data import LegendOfDragoonItemData, ItemCategory, ItemClassification as IC

chapter_one_table: Dict[str, LegendOfDragoonItemData] = {
    "Jade Dragoon Spirit": LegendOfDragoonItemData(ItemCategory.GOOD, 108_20003, IC.progression),
    "Violet Dragoon Spirit": LegendOfDragoonItemData(ItemCategory.GOOD, 108_20005, IC.progression),
    "Silver Dragoon Spirit": LegendOfDragoonItemData(ItemCategory.GOOD, 108_20006, IC.progression),
    "Dark Dragoon Spirit": LegendOfDragoonItemData(ItemCategory.GOOD, 108_20007, IC.progression),
    "Prison Key": LegendOfDragoonItemData(ItemCategory.GOOD, 108_20011, IC.progression),
    "Axe from the Shack": LegendOfDragoonItemData(ItemCategory.GOOD, 108_20012, IC.progression),
    "Good Spirits": LegendOfDragoonItemData(ItemCategory.GOOD, 108_20013, IC.useful),
    "Water Bottle": LegendOfDragoonItemData(ItemCategory.GOOD, 108_20015, IC.progression),
    "Life Water": LegendOfDragoonItemData(ItemCategory.GOOD, 108_20016, IC.progression),
    "Magic Oil": LegendOfDragoonItemData(ItemCategory.GOOD, 108_20017, IC.progression),
    "Yellow Stone": LegendOfDragoonItemData(ItemCategory.GOOD, 108_20018, IC.progression),
    "Blue Stone": LegendOfDragoonItemData(ItemCategory.GOOD, 108_20019, IC.progression),
    "Red Stone": LegendOfDragoonItemData(ItemCategory.GOOD, 108_20020, IC.progression),
    "Lavitzs Picture": LegendOfDragoonItemData(ItemCategory.GOOD, 108_20037, IC.useful),
}

chapter_two_table: Dict[str, LegendOfDragoonItemData] = {
    "Letter from Lynn": LegendOfDragoonItemData(ItemCategory.GOOD, 108_20021, IC.progression),
    "Pass for Valley": LegendOfDragoonItemData(ItemCategory.GOOD, 108_20022, IC.progression),
    "Kates Bouquet": LegendOfDragoonItemData(ItemCategory.GOOD, 108_20023, IC.useful),
    "Key to Ship": LegendOfDragoonItemData(ItemCategory.GOOD, 108_20024, IC.progression),
    "Gold Dragoon Spirit": LegendOfDragoonItemData(ItemCategory.GOOD, 108_20004, IC.progression),
    "Blue Dragoon Spirit": LegendOfDragoonItemData(ItemCategory.GOOD, 108_20002, IC.progression),
}

chapter_three_table: Dict[str, LegendOfDragoonItemData] = {
    "Boat License": LegendOfDragoonItemData(ItemCategory.GOOD, 108_20025, IC.progression),
    "Dragon Blocker": LegendOfDragoonItemData(ItemCategory.GOOD, 108_20026, IC.progression),
    "Vanishing Stone": LegendOfDragoonItemData(ItemCategory.GOOD, 108_20036, IC.progression),
    "Moon Gem": LegendOfDragoonItemData(ItemCategory.GOOD, 108_20027, IC.useful),
    "Moon Dagger": LegendOfDragoonItemData(ItemCategory.GOOD, 108_20028, IC.useful),
    "Moon Mirror": LegendOfDragoonItemData(ItemCategory.GOOD, 108_20029, IC.useful),
}

chapter_four_table: Dict[str, LegendOfDragoonItemData] = {
    "Law Making License": LegendOfDragoonItemData(ItemCategory.GOOD, 108_20032, IC.progression),
    "Law Launching License": LegendOfDragoonItemData(ItemCategory.GOOD, 108_20033, IC.progression),
}

progressive_spirit_table: Dict[str, LegendOfDragoonItemData] = {
    "Dart Progressive Spirit": LegendOfDragoonItemData(ItemCategory.GOOD, 108_20040, IC.progression)
}

all_goods_table: Dict[str, LegendOfDragoonItemData] = {
    **progressive_spirit_table,
    **chapter_one_table,
    **chapter_two_table,
    **chapter_three_table,
    **chapter_four_table,
}
