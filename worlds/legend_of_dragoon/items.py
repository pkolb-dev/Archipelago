from typing import Dict, Set

from BaseClasses import ItemClassification
from worlds.legend_of_dragoon.item.additions import additions_table
from worlds.legend_of_dragoon.item.consumables import  consumables_table
from worlds.legend_of_dragoon.item.equipment import  equipment_table
from worlds.legend_of_dragoon.item.goods import goods_table
from .item.item_data import LegendOfDragoonItemData, ItemCategory


def get_items_by_category(item_category: str) -> Dict[str, LegendOfDragoonItemData]:
    return {name: data for name, data in item_table.items() if data.category == item_category}

item_table: Dict[str, LegendOfDragoonItemData] = {
    **consumables_table,
    **equipment_table,
    **additions_table,
    **goods_table,
}

event_item_table: Dict[str, LegendOfDragoonItemData] = {
    "Victory":       LegendOfDragoonItemData(ItemCategory.EVENT, None, ItemClassification.progression),
}

# Make item categories
item_name_groups: Dict[str, Set[str]] = {}
for item in item_table.keys():
    category = item_table[item].category
    if category not in item_name_groups.keys():
        item_name_groups[category] = set()
    item_name_groups[category].add(item)
