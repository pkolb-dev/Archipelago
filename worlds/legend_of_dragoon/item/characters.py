from typing import Dict
from .item_data import LegendOfDragoonItemData, ItemCategory, ItemClassification as IC

characters_table: Dict[str, LegendOfDragoonItemData] = {
    "Dart": LegendOfDragoonItemData(ItemCategory.CHARACTER, 108_32001, IC.progression),
    "Lavitz": LegendOfDragoonItemData(ItemCategory.CHARACTER, 108_32002, IC.progression),
    "Shana": LegendOfDragoonItemData(ItemCategory.CHARACTER, 108_32003, IC.progression),
    "Rose": LegendOfDragoonItemData(ItemCategory.CHARACTER, 108_32004, IC.progression),
    "Haschel": LegendOfDragoonItemData(ItemCategory.CHARACTER, 108_32005, IC.progression),
    "Albert": LegendOfDragoonItemData(ItemCategory.CHARACTER, 108_32006, IC.progression),
    "Meru": LegendOfDragoonItemData(ItemCategory.CHARACTER, 108_32007, IC.progression),
    "Kongol": LegendOfDragoonItemData(ItemCategory.CHARACTER, 108_32008, IC.progression),
    "Miranda": LegendOfDragoonItemData(ItemCategory.CHARACTER, 108_32009, IC.progression),
    "Lloyd": LegendOfDragoonItemData(ItemCategory.CHARACTER, 108_32010, IC.progression),
}
