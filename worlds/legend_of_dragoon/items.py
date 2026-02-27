from __future__ import annotations

from typing import Dict, Set, TYPE_CHECKING, List

from BaseClasses import ItemClassification
from worlds.legend_of_dragoon.item.additions import progressive_additions_table, get_active_characters, \
    all_addition_items, chapter_two_addition_item_table, chapter_one_addition_item_table, \
    chapter_three_addition_item_table, chapter_four_addition_item_table
from worlds.legend_of_dragoon.item.consumables import consumables_table
from worlds.legend_of_dragoon.item.equipment import equipment_table
from worlds.legend_of_dragoon.item.goods import goods_table, all_goods_table, chapter_one_table, chapter_two_table, \
    chapter_three_table, chapter_four_table
from .item.item_data import LegendOfDragoonItemData, LegendOfDragoonItem
from .options import AdditionRandomization

if TYPE_CHECKING:
    from .world import LegendOfDragoonWorld


def get_items_by_category(item_category: str) -> Dict[str, LegendOfDragoonItemData]:
    return {name: data for name, data in lookup_table.items() if data.category == item_category}


lookup_table: Dict[str, LegendOfDragoonItemData] = {
    **all_addition_items,
    **progressive_additions_table,
    **consumables_table,
    **equipment_table,
    **all_goods_table,
}

ITEM_NAME_TO_ID = {name: data.code for name, data in lookup_table.items()}


def get_random_filler_item_name(world: LegendOfDragoonWorld):
    filtered_dict = {key: value for key, value in lookup_table.items() if
                     value.classification == ItemClassification.filler}
    return world.random.choices([filler for filler in filtered_dict.keys()])[0]


def create_item(world: LegendOfDragoonWorld, name: str):
    data = lookup_table[name]
    return LegendOfDragoonItem(name, data.classification, data.code, world.player)


def setup_additions(world):
    if world.options.addition_randomizer == AdditionRandomization.option_off:
        return []

    active_characters = get_active_characters(world)
    itempool = []

    # Determine allowed additions based on chapters
    allowed_additions = set()
    chapter_tables = [
        chapter_one_addition_item_table,
        chapter_two_addition_item_table,
        chapter_three_addition_item_table,
        chapter_four_addition_item_table,
    ]
    chapter_count = min(world.options.lod_completion_condition.value, len(chapter_tables))
    for table in chapter_tables[:chapter_count]:
        allowed_additions.update(table.keys())

    if world.options.addition_randomizer == AdditionRandomization.option_progressive_character:
        for [character_name, table] in active_characters.items():
            for addition_name in table.keys():
                if addition_name in allowed_additions:
                    progressive_name = f"{character_name} Progressive Addition"
                    itempool.append(world.create_item(progressive_name))

    elif world.options.addition_randomizer == AdditionRandomization.option_addition_sanity:
        for table in active_characters.values():
            for addition_name in table.keys():
                if addition_name in allowed_additions:
                    itempool.append(world.create_item(addition_name))

    return itempool


def configure_starting_additions(world, itempool):
    active_characters = get_active_characters(world)
    chapter_tables = [
        chapter_one_addition_item_table,
        chapter_two_addition_item_table,
        chapter_three_addition_item_table,
        chapter_four_addition_item_table,
    ]
    chapter_count = min(world.options.lod_completion_condition.value, len(chapter_tables))
    allowed_additions = set()
    for table in chapter_tables[:chapter_count]:
        allowed_additions.update(table.keys())

    if world.options.addition_randomizer == AdditionRandomization.option_off:
        # Give each character their base addition if it's in allowed chapters
        for table in active_characters.values():
            base_addition_name = next(iter(table))
            if base_addition_name in allowed_additions:
                item = world.create_item(base_addition_name)
                if item in itempool:
                    itempool.remove(item)
                    world.push_precollected(item)
        return

    if world.options.addition_randomizer == AdditionRandomization.option_progressive_character:
        for character_name in active_characters.keys():
            progressive_name = f"{character_name} Progressive Addition"
            if progressive_name in allowed_additions:
                item = world.create_item(progressive_name)
                if item in itempool:
                    itempool.remove(item)
                    world.push_precollected(item)
        return

    if world.options.addition_randomizer == AdditionRandomization.option_addition_sanity:
        for table in active_characters.values():
            # Filter additions by allowed chapters
            valid_additions = [name for name in table if name in allowed_additions]
            if not valid_additions:
                continue  # skip if none are valid
            addition_name = world.random.choice(valid_additions)
            item = world.create_item(addition_name)
            if item in itempool:
                itempool.remove(item)
                world.push_precollected(item)


def setup_equipment(world, itempool):
    if not world.options.enable_shopsanity:
        return

    number_of_items = len(itempool)
    number_of_equipment = len(equipment_table)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    needed_number_of_equipment_items = min(number_of_unfilled_locations - number_of_items, number_of_equipment)
    for _ in range(needed_number_of_equipment_items):
        equipment_map = map(world.create_item, equipment_table)
        itempool.append(world.random.choice(list(equipment_map)))


def create_all_items(world: LegendOfDragoonWorld):
    itempool: List[LegendOfDragoonItem] = []

    # set up goods
    lenStart = len(world.multiworld.get_unfilled_locations(world.player))
    goods_pool = get_chapter_goods(world)
    for lod_item in map(world.create_item, goods_pool):
        if not lod_item.classification.filler:
            itempool.append(lod_item)

    itempool += setup_additions(world)

    configure_starting_additions(world, itempool)

    setup_equipment(world, itempool)

    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool


def get_chapter_goods(world: LegendOfDragoonWorld) -> Dict[str, LegendOfDragoonItemData]:
    chapter_tables = [
        chapter_one_table,
        chapter_two_table,
        chapter_three_table,
        chapter_four_table,
    ]

    chapter_count = min(
        world.options.lod_completion_condition.value,
        len(chapter_tables)
    )

    chapter_goods: Dict[str, LegendOfDragoonItemData] = {}
    chapter_goods.update(goods_table)
    for table in chapter_tables[:chapter_count]:
        chapter_goods.update(table)

    return chapter_goods


# Make item categories
item_name_groups: Dict[str, Set[str]] = {}
for item in lookup_table.keys():
    category = lookup_table[item].category
    if category not in item_name_groups.keys():
        item_name_groups[category] = set()
    item_name_groups[category].add(item)
