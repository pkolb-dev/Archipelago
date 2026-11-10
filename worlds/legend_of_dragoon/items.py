from __future__ import annotations

from typing import Dict, TYPE_CHECKING, List

from BaseClasses import ItemClassification
from worlds.legend_of_dragoon.item.additions import progressive_additions_table, \
    all_addition_items, all_character_addition_items, addition_item_table
from worlds.legend_of_dragoon.item.consumables import consumables_table
from worlds.legend_of_dragoon.item.equipment import equipment_table
from worlds.legend_of_dragoon.item.goods import all_goods_table, chapter_one_table, chapter_two_table, \
    chapter_three_table, chapter_four_table
from .item.characters import characters_table
from .item.item_data import LegendOfDragoonItemData, LegendOfDragoonItem
from .item.spells import progressive_spells_table, all_spell_items, all_character_spell_items
from .options import AdditionRandomization, DragoonMagicRandomization, CompletionCondition

if TYPE_CHECKING:
    from .world import LegendOfDragoonWorld


def get_items_by_category(item_category: str) -> Dict[str, LegendOfDragoonItemData]:
    return {name: data for name, data in lookup_table.items() if data.category == item_category}


lookup_table: Dict[str, LegendOfDragoonItemData] = {
    **all_addition_items,
    **all_spell_items,
    **progressive_additions_table,
    **progressive_spells_table,
    **consumables_table,
    **equipment_table,
    **all_goods_table,
    **characters_table,
}

ITEM_NAME_TO_ID = {name: data.code for name, data in lookup_table.items()}


def get_random_filler_item_name(world: LegendOfDragoonWorld):
    filtered_dict = {key: value for key, value in lookup_table.items() if
                     value.classification == ItemClassification.filler}
    return world.random.choices([filler for filler in filtered_dict.keys()])[0]


def create_item(world: LegendOfDragoonWorld, name: str):
    data = lookup_table[name]
    return LegendOfDragoonItem(name, data.classification, data.code, world.player)


def setup_additions(world) -> list[LegendOfDragoonItem]:
    active_characters = all_character_addition_items.copy()
    itempool = []

    allowed_additions = addition_item_table.keys()

    if world.options.addition_randomizer == AdditionRandomization.option_progressive:
        for [character_name, table] in active_characters.items():
            for addition_name in table.keys():
                if addition_name in allowed_additions:
                    progressive_name = f"{character_name} Progressive Addition"
                    itempool.append(world.create_item(progressive_name))

    elif world.options.addition_randomizer == AdditionRandomization.option_shuffled:
        for table in active_characters.values():
            for addition_name in table.keys():
                if addition_name in allowed_additions:
                    itempool.append(world.create_item(addition_name))

    return itempool


def setup_spells(world: LegendOfDragoonWorld) -> list[LegendOfDragoonItem]:
    active_characters = all_character_spell_items.copy()
    itempool = []
    option_value = world.options.magic_randomizer
    if option_value == DragoonMagicRandomization.option_shuffled:
        for character, table in active_characters.items():
            if not world.options.enable_lloyd and character == "Lloyd":
                continue
            for spell_name in table.keys():
                itempool.append(world.create_item(spell_name))

        if world.options.enable_lloyd:
            lloyd_spell = world.create_item("Lloyd Running Slash")
            itempool.remove(lloyd_spell)
            world.push_precollected(lloyd_spell)
    elif option_value == DragoonMagicRandomization.option_progressive:
        for [character_name, table] in active_characters.items():
            if not world.options.enable_lloyd and character_name == "Lloyd":
                continue
            for _spell_name in table.keys():
                progressive_name = f"{character_name} Progressive Spell"
                itempool.append(world.create_item(progressive_name))
        if world.options.enable_lloyd:
            lloyd_spell = world.create_item("Lloyd Progressive Spell")
            itempool.remove(lloyd_spell)
            world.push_precollected(lloyd_spell)

    return itempool


def configure_starting_character(world, itempool):
    character_name = world.options.starting_character.value
    character_item = world.create_item(character_name)
    if character_item in itempool:
        itempool.remove(character_item)
        world.push_precollected(character_item)


def configure_starting_additions(world, itempool):
    active_characters = all_character_addition_items.copy()
    allowed_additions = addition_item_table.keys()

    if world.options.addition_randomizer == AdditionRandomization.option_progressive:
        for character_name in active_characters.keys():
            progressive_name = f"{character_name} Progressive Addition"
            progressive_item = world.create_item(progressive_name)
            if progressive_item in itempool:
                itempool.remove(progressive_item)
                world.push_precollected(progressive_item)
        return

    elif world.options.addition_randomizer == AdditionRandomization.option_shuffled:
        for table in active_characters.values():
            # Filter additions by allowed chapters
            valid_additions = [name for name in table if name in allowed_additions]
            if not valid_additions:
                continue  # skip if none are valid
            addition_name = world.random.choice(valid_additions)
            addition_item = world.create_item(addition_name)
            if addition_item in itempool:
                itempool.remove(addition_item)
                world.push_precollected(addition_item)


def setup_equipment(world, itempool):
    if not world.options.enable_shopsanity:
        return

    number_of_items = len(itempool)
    number_of_equipment = len(equipment_table)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    needed_number_of_equipment_items = min(number_of_unfilled_locations - number_of_items, number_of_equipment)
    for _ in range(needed_number_of_equipment_items):
        equipment_map = map(world.create_item,
                            filter(
                                lambda equip_item: equipment_table[
                                                       equip_item].classification != ItemClassification.filler,
                                equipment_table))
        itempool.append(world.random.choice(list(equipment_map)))


def get_goods(world) -> list[LegendOfDragoonItem]:
    itempool: list[LegendOfDragoonItem] = [world.create_item("Dart Progressive Spirit"),
                                           world.create_item("Dart Progressive Spirit"),
                                           world.create_item("Dart Progressive Spirit")]

    goods_list: list[str] = get_chapter_goods(world)

    for good_name in goods_list:
        if not world.options.enable_lloyd and good_name == "Chaos Divine Dragoon Spirit":
            continue
        itempool.append(world.create_item(good_name))

    return itempool


def get_characters(world) -> list[LegendOfDragoonItem]:
    itempool: List[LegendOfDragoonItem] = []
    for char_name in characters_table.keys():
        if not world.options.enable_lloyd and char_name == "Lloyd":
            continue
        itempool.append(world.create_item(char_name))

    return itempool


def create_all_items(world: LegendOfDragoonWorld):
    itempool: List[LegendOfDragoonItem] = []

    itempool += get_goods(world)
    itempool += setup_additions(world)
    itempool += setup_spells(world)
    itempool += get_characters(world)

    configure_starting_character(world, itempool)

    configure_starting_additions(world, itempool)

    setup_equipment(world, itempool)

    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool


def get_chapter_goods(world: LegendOfDragoonWorld) -> list[str]:
    goods_list = list(chapter_one_table.keys())

    option_value = world.options.lod_completion_condition
    if option_value == CompletionCondition.option_chapter_1:
        return goods_list

    goods_list.extend(chapter_two_table.keys())
    if option_value == CompletionCondition.option_chapter_2:
        return goods_list

    goods_list.extend(chapter_three_table.keys())
    if option_value == CompletionCondition.option_chapter_3:
        return goods_list

    goods_list.extend(chapter_four_table.keys())

    return goods_list


# Make item categories
item_name_groups: Dict[str, str] = {}
for item in lookup_table.keys():
    category = lookup_table[item].category
    item_name_groups[category] = item
