from __future__ import annotations

from typing import Dict, TYPE_CHECKING

from worlds.legend_of_dragoon.loc.additions import addition_table
from worlds.legend_of_dragoon.loc.chests import chests_table
from worlds.legend_of_dragoon.loc.events import events_table
from worlds.legend_of_dragoon.loc.location_data import LegendOfDragoonLocationData, LegendOfDragoonLocation
from worlds.legend_of_dragoon.loc.shops import shop_table
from .item.item_data import LegendOfDragoonItem

if TYPE_CHECKING:
    from .world import LegendOfDragoonWorld

location_table: Dict[str, LegendOfDragoonLocationData] = {
    **shop_table,
    **addition_table,
    **chests_table,
    **events_table,
}

LOCATION_NAME_TO_ID = {name: data.code for name, data in location_table.items()}

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

def get_locations_by_category(location_category: str) -> Dict[str, LegendOfDragoonLocationData]:
    return {name: data for name, data in location_table.items() if data.category == location_category}

def get_locations_by_category_with_ids(location_category: str) -> Dict[str, int | None]:
    locs: Dict[str,LegendOfDragoonLocationData] = get_locations_by_category(location_category)
    return {location_name: locs[location_name].code for location_name in locs}


def create_all_locations(world: LegendOfDragoonWorld) -> None:
    create_regular_locations(world)
    create_events(world)

def create_regular_locations(world: LegendOfDragoonWorld) -> None:
    menu = world.get_region("Menu")
    additions = world.get_region("Additions")

    seles = world.get_region("Seles")
    forest = world.get_region("Forest")
    hellena_prison = world.get_region("Hellena Prison")
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

    death_frontier = world.get_region("Death Frontier")
    ulara = world.get_region("Ulara")
    rouge = world.get_region("Rouge")
    aglis = world.get_region("Aglis")
    zenebatos = world.get_region("Zenebatos")
    mayfil = world.get_region("Mayfil")
    divine_tree = world.get_region("Divine Tree")
    moon_that_never_sets = world.get_region("Moon That Never Sets")


    # shops
    forest.add_locations(get_locations_by_category_with_ids("Forest"), LegendOfDragoonLocation)
    bale.add_locations(get_locations_by_category_with_ids("Bale"), LegendOfDragoonLocation)
    lohan.add_locations(get_locations_by_category_with_ids("Lohan"), LegendOfDragoonLocation)
    kazas.add_locations(get_locations_by_category_with_ids("Kazas"), LegendOfDragoonLocation)
    fletz.add_locations(get_locations_by_category_with_ids("Fletz"), LegendOfDragoonLocation)
    donau.add_locations(get_locations_by_category_with_ids("Donau"), LegendOfDragoonLocation)
    queen_fury.add_locations(get_locations_by_category_with_ids("Queen Fury"), LegendOfDragoonLocation)
    fueno.add_locations(get_locations_by_category_with_ids("Fueno"), LegendOfDragoonLocation)
    furni.add_locations(get_locations_by_category_with_ids("Furni"), LegendOfDragoonLocation)
    deningrad.add_locations(get_locations_by_category_with_ids("Deningrad"), LegendOfDragoonLocation)
    wingly_forest.add_locations(get_locations_by_category_with_ids("Wingly Forest"), LegendOfDragoonLocation)
    vellweb.add_locations(get_locations_by_category_with_ids("Vellweb"), LegendOfDragoonLocation)
    ulara.add_locations(get_locations_by_category_with_ids("Ulara"), LegendOfDragoonLocation)
    rouge.add_locations(get_locations_by_category_with_ids("Rouge"), LegendOfDragoonLocation)
    moon_that_never_sets.add_locations(get_locations_by_category_with_ids("Moon"), LegendOfDragoonLocation)
    hellena_prison.add_locations(get_locations_by_category_with_ids("Hellena 01"), LegendOfDragoonLocation)
    hellena_prison.add_locations(get_locations_by_category_with_ids("Hellena 02"), LegendOfDragoonLocation)
    kashua_glacier.add_locations(get_locations_by_category_with_ids("Kashua"), LegendOfDragoonLocation)
    volcano_villude.add_locations(get_locations_by_category_with_ids("Volcano"), LegendOfDragoonLocation)
    zenebatos.add_locations(get_locations_by_category_with_ids("Zenebatos"), LegendOfDragoonLocation)

    # additions
    additions.add_locations(get_locations_by_category_with_ids("Dart"), LegendOfDragoonLocation)
    additions.add_locations(get_locations_by_category_with_ids("Lavitz"), LegendOfDragoonLocation)
    additions.add_locations(get_locations_by_category_with_ids("Rose"), LegendOfDragoonLocation)
    additions.add_locations(get_locations_by_category_with_ids("Haschel"), LegendOfDragoonLocation)
    additions.add_locations(get_locations_by_category_with_ids("Albert"), LegendOfDragoonLocation)
    additions.add_locations(get_locations_by_category_with_ids("Meru"), LegendOfDragoonLocation)
    additions.add_locations(get_locations_by_category_with_ids("Kongol"), LegendOfDragoonLocation)


def create_events(world: LegendOfDragoonWorld) -> None:
    if world.options.lod_completion_condition.option_seles_commander:
        seles = world.get_region("Seles")
        seles.add_event("Defeat Commander in Seles", "Victory", location_type=LegendOfDragoonLocation, item_type=LegendOfDragoonItem)
        # world.get_location("Defeat Commander in Seles").place_locked_item(world.create_event("Victory"))
