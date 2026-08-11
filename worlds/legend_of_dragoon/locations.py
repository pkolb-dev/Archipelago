from __future__ import annotations

from typing import Dict, TYPE_CHECKING

from worlds.legend_of_dragoon.loc.additions import all_addition_locations_table, chapter_one_addition_unlock_table, \
    chapter_two_addition_unlock_table, chapter_three_addition_unlock_table, chapter_four_addition_unlock_table
from worlds.legend_of_dragoon.loc.chests import chests_table
from worlds.legend_of_dragoon.loc.enemies import enemy_table
from worlds.legend_of_dragoon.loc.events import events_table
from worlds.legend_of_dragoon.loc.location_data import LegendOfDragoonLocationData, LegendOfDragoonLocation
from worlds.legend_of_dragoon.loc.shops import shop_table, get_all_shops
from .item.item_data import LegendOfDragoonItem
from .loc.goods import goods_location_table
from .loc.magic import all_magic_locations_table, all_character_magic_unlocks_table
from .options import CompletionCondition, AdditionRandomization

import re

if TYPE_CHECKING:
    from .world import LegendOfDragoonWorld

all_location_table: Dict[str, LegendOfDragoonLocationData] = {
    **all_addition_locations_table,
    **chests_table,
    **events_table,
    **enemy_table,
    **goods_location_table,
    **get_all_shops(),
    **all_magic_locations_table,
}

dynamic_location_table: Dict[str, LegendOfDragoonLocationData] = {
    **enemy_table,
    **events_table,
    **chests_table,
}


def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def get_locations_by_category(location_category: str) -> Dict[str, LegendOfDragoonLocationData]:
    return {name: data for name, data in dynamic_location_table.items() if data.category == location_category}


def get_locations_by_category_with_ids(location_category: str) -> Dict[str, int | None]:
    locs: Dict[str, LegendOfDragoonLocationData] = get_locations_by_category(location_category)
    return {location_name: locs[location_name].code for location_name in locs}


def get_locations_by_category_in_chapter(category, table):
    locs: Dict[str, LegendOfDragoonLocationData] = {name: data for name, data in table.items() if
                                                    data.category == category}
    return {location_name: locs[location_name].code for location_name in locs}


def setup_chapter_one(world):
    create_chapter_one_locations(world)
    setup_chapter_one_events(world)


def setup_chapter_two(world):
    if world.options.lod_completion_condition == CompletionCondition.option_chapter_1:
        return

    create_chapter_two_locations(world)
    setup_chapter_two_events(world)


def setup_chapter_three(world):
    goal = world.options.lod_completion_condition
    if goal == CompletionCondition.option_chapter_1 or goal == CompletionCondition.option_chapter_2:
        return

    create_chapter_three_locations(world)
    setup_chapter_three_events(world)


def setup_chapter_four(world):
    goal = world.options.lod_completion_condition
    if goal != CompletionCondition.option_chapter_4:
        return

    create_chapter_four_locations(world)
    setup_chapter_four_events(world)


def setup_addition_locations(world):
    # add guards
    chapter_tables = {
        1: chapter_one_addition_unlock_table,
        2: chapter_two_addition_unlock_table,
        3: chapter_three_addition_unlock_table,
        4: chapter_four_addition_unlock_table,
    }

    regex = r"^([\S]*) - ((\S* *)*)(?: Unlock)"

    for chapter, table in chapter_tables.items():
        categories = {data.category for data in table.values()}

        for category in categories:
            if chapter == 2 and world.options.lod_completion_condition == CompletionCondition.option_chapter_1:
                continue
            if chapter == 3 and world.options.lod_completion_condition in [CompletionCondition.option_chapter_1,
                                                                           CompletionCondition.option_chapter_2]:
                continue
            if chapter == 4 and world.options.lod_completion_condition != CompletionCondition.option_chapter_4:
                continue
            region = world.get_region(f"{category} Additions")
            locations = get_locations_by_category_in_chapter(category, table)

            if world.options.addition_randomizer == AdditionRandomization.option_off:
                for location in locations:
                    match = re.search(regex, location)
                    if match:
                        event_item = f"{match.group(1)} {match.group(2)}".strip()
                        region.add_event(location, event_item,
                                         location_type=LegendOfDragoonLocation,
                                         item_type=LegendOfDragoonItem)
            else:
                region.add_locations(locations, LegendOfDragoonLocation)
    pass


def create_all_locations(world: LegendOfDragoonWorld) -> None:
    create_regular_locations(world)
    # create_events(world) - unused atm

    setup_chapter_one(world)
    setup_chapter_two(world)
    setup_chapter_three(world)
    setup_chapter_four(world)

    setup_addition_locations(world)


def create_regular_locations(world: LegendOfDragoonWorld) -> None:
    configure_shopsanity(world)
    configure_magicsanity(world)


def create_magic_location(number_of_slots: int, character_key: str) -> None:
    character_data: Dict[str, LegendOfDragoonLocationData] = all_character_magic_unlocks_table[character_key]

    for number in range(number_of_slots):
        # locations start from level 1
        location_key = f"{character_key} - Magic Level {number + 2} Unlock"
        location_data = character_data.get(location_key)
        if location_data is None:
            continue
        dynamic_location_table[location_key] = location_data


def configure_magicsanity(world: LegendOfDragoonWorld) -> None:
    create_magic_location(world.options.dart_magic_slots.value, "Dart")
    create_magic_location(world.options.dart_magic_slots.value, "Lavitz")
    create_magic_location(world.options.dart_magic_slots.value, "Shana")
    create_magic_location(world.options.dart_magic_slots.value, "Rose")
    create_magic_location(world.options.dart_magic_slots.value, "Haschel")
    create_magic_location(world.options.dart_magic_slots.value, "Albert")
    create_magic_location(world.options.dart_magic_slots.value, "Meru")
    create_magic_location(world.options.dart_magic_slots.value, "Kongol")
    create_magic_location(world.options.dart_magic_slots.value, "Miranda")

    dart_spells = world.get_region("Dart Spells")
    lavitz_spells = world.get_region("Lavitz Spells")
    shana_spells = world.get_region("Shana Spells")
    rose_spells = world.get_region("Rose Spells")
    haschel_spells = world.get_region("Haschel Spells")
    albert_spells = world.get_region("Albert Spells")

    dart_spells.add_locations(get_locations_by_category_with_ids("Dart"))
    lavitz_spells.add_locations(get_locations_by_category_with_ids("Lavitz"))
    shana_spells.add_locations(get_locations_by_category_with_ids("Shana"))
    rose_spells.add_locations(get_locations_by_category_with_ids("Rose"))
    haschel_spells.add_locations(get_locations_by_category_with_ids("Haschel"))
    albert_spells.add_locations(get_locations_by_category_with_ids("Albert"))

    if world.options.lod_completion_condition == CompletionCondition.option_chapter_1:
        return

    meru_spells = world.get_region("Meru Spells")
    kongol_spells = world.get_region("Kongol Spells")

    meru_spells.add_locations(get_locations_by_category_with_ids("Meru"))
    kongol_spells.add_locations(get_locations_by_category_with_ids("Kongol"))

    if world.options.lod_completion_condition == CompletionCondition.option_chapter_2:
        return

    miranda_spells = world.get_region("Miranda Spells")
    miranda_spells.add_locations(get_locations_by_category_with_ids("Miranda"))


def configure_shopsanity(world: LegendOfDragoonWorld) -> None:
    if not world.options.enable_shopsanity.value:
        return
    # now we go through each shop and add the number of locations per options.
    create_shop_location(world.options.bale_equipment_shop_slots.value, "Bale Equipment Shop")
    create_shop_location(world.options.serdio_item_shop_slots.value, "Bale Item Shop")
    create_shop_location(world.options.lohan_equipment_shop_slots.value, "Lohan Equipment Shop")
    create_shop_location(world.options.lohan_item_shop_slots.value, "Lohan Item Shop")
    create_shop_location(world.options.kazas_equipment_shop_slots.value, "Kazas Equipment Shop")
    create_shop_location(world.options.kazas_fort_item_shop_slots.value, "Kazas Fort Item Shop")
    create_shop_location(world.options.fletz_equipment_shop_slots.value, "Fletz Equipment Shop")
    create_shop_location(world.options.fletz_item_shop_slots.value, "Fletz Item Shop")
    create_shop_location(world.options.donau_equipment_shop_slots.value, "Donau Equipment Shop")
    create_shop_location(world.options.donau_item_shop_slots.value, "Donau Item Shop")
    create_shop_location(world.options.queen_fury_equipment_shop_slots.value, "Queen Fury Equipment Shop")
    create_shop_location(world.options.queen_fury_item_shop_slots.value, "Queen Fury Item Shop")
    create_shop_location(world.options.fueno_equipment_shop_slots.value, "Fueno Equipment Shop")
    create_shop_location(world.options.fueno_item_shop_slots.value, "Fueno Item Shop")
    create_shop_location(world.options.furni_equipment_shop_slots.value, "Furni Equipment Shop")
    create_shop_location(world.options.furni_item_shop_slots.value, "Furni Item Shop")
    create_shop_location(world.options.deningrad_equipment_shop_slots.value, "Deningrad Equipment Shop")
    create_shop_location(world.options.deningrad_item_shop_slots.value, "Deningrad Item Shop")
    create_shop_location(world.options.wingly_forest_equipment_shop_slots.value, "Wingly Forest Equipment Shop")
    create_shop_location(world.options.wingly_forest_item_shop_slots.value, "Wingly Forest Item Shop")
    create_shop_location(world.options.vellweb_equipment_shop_slots.value, "Vellweb Equipment Shop")
    create_shop_location(world.options.vellweb_item_shop_slots.value, "Vellweb Item Shop")
    create_shop_location(world.options.ulara_equipment_shop_slots.value, "Ulara Equipment Shop")
    create_shop_location(world.options.ulara_item_shop_slots.value, "Ulara Item Shop")
    create_shop_location(world.options.rouge_equipment_shop_slots.value, "Rouge Equipment Shop")
    create_shop_location(world.options.rouge_item_shop_slots.value, "Rouge Item Shop")
    create_shop_location(world.options.moon_equipment_shop_slots.value, "Moon Equipment Shop")
    create_shop_location(world.options.moon_item_shop_slots.value, "Moon Item Shop")
    create_shop_location(world.options.hellena_01_item_shop_slots.value, "Hellena 01 Item Shop")
    create_shop_location(world.options.kashua_equipment_shop_slots.value, "Kashua Equipment Shop")
    create_shop_location(world.options.kashua_item_shop_slots.value, "Kashua Item Shop")
    create_shop_location(world.options.fletz_accessory_shop_slots.value, "Fletz Accessory Shop")
    create_shop_location(world.options.forest_item_shop_slots.value, "Forest Item Shop")
    create_shop_location(world.options.kazas_fort_equipment_shop_slots.value, "Kazas Fort Equipment Shop")
    create_shop_location(world.options.volcano_item_shop_slots.value, "Volcano Item Shop")
    create_shop_location(world.options.zenebatos_equipment_shop_slots.value, "Zenebatos Equipment Shop")
    create_shop_location(world.options.zenebatos_item_shop_slots.value, "Zenebatos Item Shop")
    create_shop_location(world.options.hellena_02_item_shop_slots.value, "Hellena 02 Item Shop")
    create_shop_location(world.options.black_castle_item_shop_slots.value, "Black Castle Item Shop")


def create_shop_location(number_of_slots: int, key: str) -> None:
    base_data = shop_table[key]
    if base_data.code is None:
        return

    for number in range(number_of_slots):
        complete_name = key + " - Slot " + str(number + 1)
        updated_data = LegendOfDragoonLocationData(base_data.category, base_data.code + number + 1, base_data.type)
        dynamic_location_table[complete_name] = updated_data


def create_chapter_one_locations(world):
    seles = world.get_region("Seles")
    forest = world.get_region("Forest")
    hellena_prison_01 = world.get_region("Hellena Prison 01")
    hellena_prison_02 = world.get_region("Hellena Prison 02")
    prairie = world.get_region("Prairie")
    limestone_cave = world.get_region("Limestone Cave")
    bale = world.get_region("Bale")
    hoax = world.get_region("Hoax")
    marshland = world.get_region("Marshland")
    volcano_villude = world.get_region("Volcano Villude")
    dragons_nest = world.get_region("Dragon's Nest")
    lohan = world.get_region("Lohan")
    shrine_of_shirley = world.get_region("Shrine of Shirley")
    kazas = world.get_region("Kazas")
    black_castle = world.get_region("Black Castle")
    black_castle_throne_room = world.get_region("Black Castle Throne Room")

    seles.add_locations(get_locations_by_category_with_ids("Seles"), LegendOfDragoonLocation)
    forest.add_locations(get_locations_by_category_with_ids("Forest"), LegendOfDragoonLocation)
    prairie.add_locations(get_locations_by_category_with_ids("Prairie"), LegendOfDragoonLocation)
    limestone_cave.add_locations(get_locations_by_category_with_ids("Limestone Cave"), LegendOfDragoonLocation)
    bale.add_locations(get_locations_by_category_with_ids("Bale"), LegendOfDragoonLocation)
    hoax.add_locations(get_locations_by_category_with_ids("Hoax"), LegendOfDragoonLocation)
    marshland.add_locations(get_locations_by_category_with_ids("Marshland"), LegendOfDragoonLocation)
    lohan.add_locations(get_locations_by_category_with_ids("Lohan"), LegendOfDragoonLocation)
    shrine_of_shirley.add_locations(get_locations_by_category_with_ids("Shrine of Shirley"), LegendOfDragoonLocation)
    dragons_nest.add_locations(get_locations_by_category_with_ids("Dragon's Nest"), LegendOfDragoonLocation)
    kazas.add_locations(get_locations_by_category_with_ids("Kazas"), LegendOfDragoonLocation)
    black_castle.add_locations(get_locations_by_category_with_ids("Black Castle"), LegendOfDragoonLocation)
    black_castle_throne_room.add_locations(get_locations_by_category_with_ids("Black Castle Throne Room"),
                                           LegendOfDragoonLocation)

    hellena_prison_01.add_locations(get_locations_by_category_with_ids("Hellena 01"), LegendOfDragoonLocation)
    hellena_prison_02.add_locations(get_locations_by_category_with_ids("Hellena 02"), LegendOfDragoonLocation)
    volcano_villude.add_locations(get_locations_by_category_with_ids("Volcano Villude"), LegendOfDragoonLocation)


def create_chapter_two_locations(world):
    fletz = world.get_region("Fletz")
    barrens = world.get_region("Barrens")
    donau = world.get_region("Donau")
    fletz_castle = world.get_region("Fletz Castle")
    valley_of_corrupted_gravity = world.get_region("Valley of Corrupted Gravity")
    home_of_giganto = world.get_region("Home of Giganto")
    queen_fury = world.get_region("Queen Fury")
    phantom_ship = world.get_region("Phantom Ship")
    lidiera = world.get_region("Lidiera")
    underwater_cavern = world.get_region("Underwater Cavern")
    fueno = world.get_region("Fueno")
    fletz.add_locations(get_locations_by_category_with_ids("Fletz"), LegendOfDragoonLocation)
    fletz_castle.add_locations(get_locations_by_category_with_ids("Fletz Castle"), LegendOfDragoonLocation)
    barrens.add_locations(get_locations_by_category_with_ids("Barrens"), LegendOfDragoonLocation)
    donau.add_locations(get_locations_by_category_with_ids("Donau"), LegendOfDragoonLocation)
    valley_of_corrupted_gravity.add_locations(get_locations_by_category_with_ids("Valley of Corrupted Gravity"),
                                              LegendOfDragoonLocation)
    home_of_giganto.add_locations(get_locations_by_category_with_ids("Home of Giganto"), LegendOfDragoonLocation)
    queen_fury.add_locations(get_locations_by_category_with_ids("Queen Fury"), LegendOfDragoonLocation)
    phantom_ship.add_locations(get_locations_by_category_with_ids("Phantom Ship"), LegendOfDragoonLocation)
    lidiera.add_locations(get_locations_by_category_with_ids("Lidiera"), LegendOfDragoonLocation)
    underwater_cavern.add_locations(get_locations_by_category_with_ids("Underwater Cavern"), LegendOfDragoonLocation)
    fueno.add_locations(get_locations_by_category_with_ids("Fueno"), LegendOfDragoonLocation)


def create_chapter_three_locations(world):
    furni = world.get_region("Furni")
    evergreen_forest = world.get_region("Evergreen Forest")
    deningrad = world.get_region("Deningrad")
    neet = world.get_region("Neet")
    wingly_forest = world.get_region("Wingly Forest")
    forbidden_land = world.get_region("Forbidden Land")
    mortal_dragon_mountain = world.get_region("Mortal Dragon Mountain")
    kashua_glacier = world.get_region("Kashua Glacier")
    tower_of_flanvel = world.get_region("Tower of Flanvel")
    snowfield = world.get_region("Snowfield")
    fort_magrad = world.get_region("Fort Magrad")
    vellweb = world.get_region("Vellweb")

    furni.add_locations(get_locations_by_category_with_ids("Furni"), LegendOfDragoonLocation)
    evergreen_forest.add_locations(get_locations_by_category_with_ids("Evergreen Forest"), LegendOfDragoonLocation)
    deningrad.add_locations(get_locations_by_category_with_ids("Deningrad"), LegendOfDragoonLocation)
    neet.add_locations(get_locations_by_category_with_ids("Neet"), LegendOfDragoonLocation)
    wingly_forest.add_locations(get_locations_by_category_with_ids("Wingly Forest"), LegendOfDragoonLocation)
    forbidden_land.add_locations(get_locations_by_category_with_ids("Forbidden Land"), LegendOfDragoonLocation)
    vellweb.add_locations(get_locations_by_category_with_ids("Vellweb"), LegendOfDragoonLocation)
    mortal_dragon_mountain.add_locations(get_locations_by_category_with_ids("Mortal Dragon Mountain"),
                                         LegendOfDragoonLocation)
    kashua_glacier.add_locations(get_locations_by_category_with_ids("Kashua Glacier"), LegendOfDragoonLocation)
    tower_of_flanvel.add_locations(get_locations_by_category_with_ids("Tower of Flanvel"), LegendOfDragoonLocation)
    snowfield.add_locations(get_locations_by_category_with_ids("Snowfield"), LegendOfDragoonLocation)
    fort_magrad.add_locations(get_locations_by_category_with_ids("Fort Magrad"), LegendOfDragoonLocation)


def create_chapter_four_locations(world):
    death_frontier = world.get_region("Death Frontier")
    ulara = world.get_region("Ulara")
    rouge = world.get_region("Rouge")
    aglis = world.get_region("Aglis")
    zenebatos = world.get_region("Zenebatos")
    mayfil = world.get_region("Mayfil")
    divine_tree = world.get_region("Divine Tree")
    moon_that_never_sets = world.get_region("Moon That Never Sets")

    death_frontier.add_locations(get_locations_by_category_with_ids("Death Frontier"), LegendOfDragoonLocation)
    ulara.add_locations(get_locations_by_category_with_ids("Ulara"), LegendOfDragoonLocation)
    rouge.add_locations(get_locations_by_category_with_ids("Rouge"), LegendOfDragoonLocation)
    aglis.add_locations(get_locations_by_category_with_ids("Aglis"), LegendOfDragoonLocation)
    zenebatos.add_locations(get_locations_by_category_with_ids("Zenebatos"), LegendOfDragoonLocation)
    mayfil.add_locations(get_locations_by_category_with_ids("Mayfil"), LegendOfDragoonLocation)
    divine_tree.add_locations(get_locations_by_category_with_ids("Divine Tree"), LegendOfDragoonLocation)
    moon_that_never_sets.add_locations(get_locations_by_category_with_ids("Moon"), LegendOfDragoonLocation)


def setup_chapter_one_events(world):
    seles = world.get_region("Seles")
    hellena_prison_01 = world.get_region("Hellena Prison 01")
    hellena_prison_02 = world.get_region("Hellena Prison 02")
    limestone_cave = world.get_region("Limestone Cave")
    hoax = world.get_region("Hoax")
    volcano_villude = world.get_region("Volcano Villude")
    dragons_nest = world.get_region("Dragon's Nest")
    lohan = world.get_region("Lohan")
    shrine_of_shirley = world.get_region("Shrine of Shirley")
    black_castle = world.get_region("Black Castle")
    black_castle_throne_room = world.get_region("Black Castle Throne Room")

    seles.add_event("Defeat Commander", "Commander", location_type=LegendOfDragoonLocation,
                    item_type=LegendOfDragoonItem)
    hellena_prison_01.add_event("Defeat Fruegel 1", "Fruegel 1",
                                location_type=LegendOfDragoonLocation,
                                item_type=LegendOfDragoonItem)
    limestone_cave.add_event("Defeat Urobolus", "Urobolus", location_type=LegendOfDragoonLocation,
                             item_type=LegendOfDragoonItem)
    hoax.add_event("Defeat Kongol 1", "Kongol 1", location_type=LegendOfDragoonLocation, item_type=LegendOfDragoonItem)
    volcano_villude.add_event("Defeat Volcano Virage", "Volcano Virage", location_type=LegendOfDragoonLocation,
                              item_type=LegendOfDragoonItem)
    volcano_villude.add_event("Defeat Firebird", "Firebird", location_type=LegendOfDragoonLocation,
                              item_type=LegendOfDragoonItem)
    dragons_nest.add_event("Defeat Greham", "Greham", location_type=LegendOfDragoonLocation,
                           item_type=LegendOfDragoonItem)
    shrine_of_shirley.add_event("Defeat Shirley", "Shirley", location_type=LegendOfDragoonLocation,
                                item_type=LegendOfDragoonItem)
    lohan.add_event("Lose to Lloyd", "Lloyd 1", location_type=LegendOfDragoonLocation, item_type=LegendOfDragoonItem)
    hellena_prison_02.add_event("Defeat Fruegel 2", "Fruegel 2", location_type=LegendOfDragoonLocation,
                                item_type=LegendOfDragoonItem)
    black_castle.add_event("Defeat Kongol 2", "Kongol 2", location_type=LegendOfDragoonLocation,
                           item_type=LegendOfDragoonItem)
    black_castle_throne_room.add_event("Defeat Dragoon Doel", "Dragoon Doel", location_type=LegendOfDragoonLocation,
                                       item_type=LegendOfDragoonItem)


def setup_chapter_two_events(world):
    fletz = world.get_region("Fletz")
    barrens = world.get_region("Barrens")
    donau = world.get_region("Donau")
    fletz_castle = world.get_region("Fletz Castle")
    valley_of_corrupted_gravity = world.get_region("Valley of Corrupted Gravity")
    home_of_giganto = world.get_region("Home of Giganto")
    queen_fury = world.get_region("Queen Fury")
    phantom_ship = world.get_region("Phantom Ship")
    lidiera = world.get_region("Lidiera")
    underwater_cavern = world.get_region("Underwater Cavern")
    fueno = world.get_region("Fueno")

    barrens.add_event("Mappi Steals Orb", "Mappi Steals Orb", location_type=LegendOfDragoonLocation,
                      item_type=LegendOfDragoonItem)
    valley_of_corrupted_gravity.add_event("Defeat Valley Virage", "Valley Virage",
                                          location_type=LegendOfDragoonLocation, item_type=LegendOfDragoonItem)
    home_of_giganto.add_event("Defeat Gehrich", "Gehrich", location_type=LegendOfDragoonLocation,
                              item_type=LegendOfDragoonItem)
    fletz_castle.add_event("Defeat Lenus 1", "Lenus 1", location_type=LegendOfDragoonLocation,
                           item_type=LegendOfDragoonItem)
    phantom_ship.add_event("Defeat Ghost Commander", "Ghost Commander", location_type=LegendOfDragoonLocation,
                           item_type=LegendOfDragoonItem)
    underwater_cavern.add_event("Defeat Lenus & Regole", "Lenus 2", location_type=LegendOfDragoonLocation,
                                item_type=LegendOfDragoonItem)


def setup_chapter_three_events(world):
    furni = world.get_region("Furni")
    evergreen_forest = world.get_region("Evergreen Forest")
    deningrad = world.get_region("Deningrad")
    neet = world.get_region("Neet")
    wingly_forest = world.get_region("Wingly Forest")
    forbidden_land = world.get_region("Forbidden Land")
    mortal_dragon_mountain = world.get_region("Mortal Dragon Mountain")
    kashua_glacier = world.get_region("Kashua Glacier")
    tower_of_flanvel = world.get_region("Tower of Flanvel")
    snowfield = world.get_region("Snowfield")
    fort_magrad = world.get_region("Fort Magrad")
    vellweb = world.get_region("Vellweb")

    evergreen_forest.add_event("Defeat Kamuy", "Kamuy", location_type=LegendOfDragoonLocation,
                               item_type=LegendOfDragoonItem)
    deningrad.add_event("Talk to Ute", "Talk to Ute", location_type=LegendOfDragoonLocation,
                        item_type=LegendOfDragoonItem)
    forbidden_land.add_event("Defeat Kadessa Virage", "Kadessa Virage", location_type=LegendOfDragoonLocation,
                             item_type=LegendOfDragoonItem)
    forbidden_land.add_event("Defeat Grand Jewel", "Grand Jewel", location_type=LegendOfDragoonLocation,
                             item_type=LegendOfDragoonItem)
    mortal_dragon_mountain.add_event("Defeat Divine Dragon", "Divine Dragon", location_type=LegendOfDragoonLocation,
                                     item_type=LegendOfDragoonItem)
    kashua_glacier.add_event("Defeat Windigo", "Windigo", location_type=LegendOfDragoonLocation,
                             item_type=LegendOfDragoonItem)
    tower_of_flanvel.add_event("Defeat Lloyd", "Lloyd 2", location_type=LegendOfDragoonLocation,
                               item_type=LegendOfDragoonItem)
    tower_of_flanvel.add_event("Defeat Magician Faust", "Faust", location_type=LegendOfDragoonLocation,
                               item_type=LegendOfDragoonItem)
    snowfield.add_event("Defeat Polter", "Polter", location_type=LegendOfDragoonLocation, item_type=LegendOfDragoonItem)


def setup_chapter_four_events(world):
    death_frontier = world.get_region("Death Frontier")
    ulara = world.get_region("Ulara")
    rouge = world.get_region("Rouge")
    aglis = world.get_region("Aglis")
    zenebatos = world.get_region("Zenebatos")
    mayfil = world.get_region("Mayfil")
    divine_tree = world.get_region("Divine Tree")
    moon_that_never_sets = world.get_region("Moon That Never Sets")

    ulara.add_event("Unlock Ulara Teleporter", "Ulara Teleporter", location_type=LegendOfDragoonLocation,
                    item_type=LegendOfDragoonItem)
    aglis.add_event("Defeat Kraken", "Kraken", location_type=LegendOfDragoonLocation, item_type=LegendOfDragoonItem)

    zenebatos.add_event("Defeat Vector", "Vector", location_type=LegendOfDragoonLocation, item_type=LegendOfDragoonItem)
    zenebatos.add_event("Defeat Kubila", "Kubila", location_type=LegendOfDragoonLocation, item_type=LegendOfDragoonItem)
    zenebatos.add_event("Defeat Selebus", "Selebus", location_type=LegendOfDragoonLocation,
                        item_type=LegendOfDragoonItem)
    mayfil.add_event("Defeat Feyrbrand", "Feyrbrand", location_type=LegendOfDragoonLocation,
                     item_type=LegendOfDragoonItem)
    mayfil.add_event("Defeat Regole", "Regole", location_type=LegendOfDragoonLocation, item_type=LegendOfDragoonItem)
    mayfil.add_event("Defeat Divine Dragon Ghost", "Divine Dragon Ghost", location_type=LegendOfDragoonLocation,
                     item_type=LegendOfDragoonItem)
    mayfil.add_event("Defeat Zackwell", "Zackwell", location_type=LegendOfDragoonLocation,
                     item_type=LegendOfDragoonItem)
    divine_tree.add_event("Defeat Imago", "Imago", location_type=LegendOfDragoonLocation, item_type=LegendOfDragoonItem)
    moon_that_never_sets.add_event("Defeat Moon Virage", "Moon Virage", location_type=LegendOfDragoonLocation,
                                   item_type=LegendOfDragoonItem)
    moon_that_never_sets.add_event("Defeat Zieg", "Zieg", location_type=LegendOfDragoonLocation,
                                   item_type=LegendOfDragoonItem)
    moon_that_never_sets.add_event("Defeat Melbu Frahma", "Melbu Frahma", location_type=LegendOfDragoonLocation,
                                   item_type=LegendOfDragoonItem)


def create_events(world: LegendOfDragoonWorld) -> None:
    pass


LOCATION_NAME_TO_ID = {name: data.code for name, data in all_location_table.items()}
