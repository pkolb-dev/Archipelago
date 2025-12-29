from __future__ import annotations
from typing import Dict, Set, TYPE_CHECKING, List

from worlds.legend_of_dragoon.item.additions import additions_table
from worlds.legend_of_dragoon.item.consumables import  consumables_table
from worlds.legend_of_dragoon.item.equipment import  equipment_table
from worlds.legend_of_dragoon.item.goods import goods_table
from .item.item_data import LegendOfDragoonItemData, LegendOfDragoonItem

if TYPE_CHECKING:
    from .world import LegendOfDragoonWorld

def get_items_by_category(item_category: str) -> Dict[str, LegendOfDragoonItemData]:
    return {name: data for name, data in item_table.items() if data.category == item_category}

# TODO: not sure if needed
# event_item_table: Dict[str, LegendOfDragoonItemData] = {
#     "Victory":       LegendOfDragoonItemData(ItemCategory.EVENT, None, ItemClassification.progression),
# }

item_table: Dict[str, LegendOfDragoonItemData] = {
    **consumables_table,
    **equipment_table,
    **additions_table,
    **goods_table,
}

ITEM_NAME_TO_ID = {name: data.code for name, data in item_table.items()}

def get_random_filler_item_name(world: LegendOfDragoonWorld):
    return world.random.choices([filler for filler in consumables_table.keys()])[0]

def create_item(world: LegendOfDragoonWorld, name: str):
    data = item_table[name]
    return LegendOfDragoonItem(name, data.classification, data.code, world.player)

def create_all_items(world: LegendOfDragoonWorld):
    itempool: List[LegendOfDragoonItem] = []
    for item in map(world.create_item, item_table):
        itempool.append(item)

    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool

    # TODO: starting inventory TBD:
    # if world.options.<SOME OPTION>:
    #    item_to_start_with = world.create_item("ITEM NAME")
    #    world.push_precollected(item_to_start_with)

# Make item categories
item_name_groups: Dict[str, Set[str]] = {}
for item in item_table.keys():
    category = item_table[item].category
    if category not in item_name_groups.keys():
        item_name_groups[category] = set()
    item_name_groups[category].add(item)
