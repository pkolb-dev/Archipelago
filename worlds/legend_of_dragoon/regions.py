from typing import Dict, List, NamedTuple, Optional

from BaseClasses import MultiWorld, Region, Entrance
from .loc.additions import addition_table
from .loc.location_data import LegendOfDragoonLocation
from .locations import location_table, location_name_groups


class LegendOfDragoonRegionData(NamedTuple):
    locations: List[str]
    region_exits: Optional[List[str]]


def create_regions(legend_of_dragoon_world):
    multiworld = legend_of_dragoon_world.multiworld
    player     = legend_of_dragoon_world.player
    options    = legend_of_dragoon_world.options

    regions: Dict[str, LegendOfDragoonRegionData] = {
        "Menu":                         LegendOfDragoonRegionData([], ["Seles", "Additions"]),
        "Additions":                    LegendOfDragoonRegionData(list(addition_table), []),

        # SERDIO
        "Seles":                        LegendOfDragoonRegionData([],   ["Forest"]),
        "Forest":                       LegendOfDragoonRegionData([],   ["Hellena Prison"]),
        "Hellena Prison":               LegendOfDragoonRegionData([],   ["Prairie"]),
        "Prairie":                      LegendOfDragoonRegionData([],   ["Limestone Cave"]),
        "Limestone Cave":               LegendOfDragoonRegionData([],   ["Bale"]),
        "Bale":                         LegendOfDragoonRegionData([],   ["Hoax"]),
        "Hoax":                         LegendOfDragoonRegionData([],   ["Marshland"]),
        "Marshland":                    LegendOfDragoonRegionData([],   ["Volcano Villude"]),
        "Volcano Villude":              LegendOfDragoonRegionData([],   ["Nest of Dragon"]),
        "Nest of Dragon":               LegendOfDragoonRegionData([],   ["Lohan"]),
        "Lohan":                        LegendOfDragoonRegionData([],   ["Shrine of Shirley"]),
        "Shrine of Shirley":            LegendOfDragoonRegionData([],   ["Kazas"]),
        "Kazas":                        LegendOfDragoonRegionData([],   ["Black Castle"]),
        "Black Castle":                 LegendOfDragoonRegionData([],   ["Queen Fury"]),

        # TIBEROA
        "Queen Fury":                   LegendOfDragoonRegionData([],   ["Fletz Castle", "Phantom Ship"]),
        "Phantom Ship":                 LegendOfDragoonRegionData([],   []),
        "Fletz Castle":                 LegendOfDragoonRegionData([],   ["Barrens"]),
        "Barrens":                      LegendOfDragoonRegionData([],   ["Donau"]),
        "Donau":                        LegendOfDragoonRegionData([],   ["Valley of Corrupted Gravity"]),
        "Valley of Corrupted Gravity":  LegendOfDragoonRegionData([],   ["Home of Giganto"]),
        "Home of Giganto":              LegendOfDragoonRegionData([],   ['Lidiera']),

        # MILLE SESEAU
        "Lidiera":                      LegendOfDragoonRegionData([],   ['Undersea Cavern']),
        "Undersea Cavern":              LegendOfDragoonRegionData([],   ['Prison Island']),
        "Prison Island":                LegendOfDragoonRegionData([],   ['Fueno']),
        "Fueno":                        LegendOfDragoonRegionData([],   ['Furni']),
        "Furni":                        LegendOfDragoonRegionData([],   ['Evergreen Forest']),
        "Evergreen Forest":             LegendOfDragoonRegionData([],   ['Deningrad']),
        "Deningrad":                    LegendOfDragoonRegionData([],   ['Neet']),
        "Neet":                         LegendOfDragoonRegionData([],   ['Wingly Forest']),
        "Wingly Forest":                LegendOfDragoonRegionData([],   ['Kadessa']),
        "Kadessa":                      LegendOfDragoonRegionData([],   ['Mountain of Mortal Dragon']),
        "Mountain of Mortal Dragon":    LegendOfDragoonRegionData([],   ['Kashua Glacier']),

        # GLORIANO & BROKEN ISLANDS
        "Kashua Glacier":               LegendOfDragoonRegionData([],   ['Tower of Flanvel']),
        "Tower of Flanvel":             LegendOfDragoonRegionData([],   ['Snowfield']),
        "Snowfield":                    LegendOfDragoonRegionData([],   ['Fort Magrad']),
        "Fort Magrad":                  LegendOfDragoonRegionData([],   ['Vellweb']),
        "Vellweb":                      LegendOfDragoonRegionData([],   ['Death Frontier']),
        "Death Frontier":               LegendOfDragoonRegionData([],   ['Ulara']),
        "Ulara":                        LegendOfDragoonRegionData([],   ['Rouge']),
        "Rouge":                        LegendOfDragoonRegionData([],   ['Aglis']),
        "Aglis":                        LegendOfDragoonRegionData([],   ['Zenebatos']),
        "Zenebatos":                    LegendOfDragoonRegionData([],   ['Mayfil']),
        "Mayfil":                       LegendOfDragoonRegionData([],   ['Divine Tree']),
        "Divine Tree":                  LegendOfDragoonRegionData([],   ['Moon That Never Sets']),
        "Moon That Never Sets":         LegendOfDragoonRegionData([],   []),
    }


    # Set up locations

    # shops
    for shop_loc in location_name_groups["Bale"]:
        regions["Bale"].locations.append(shop_loc)

    for shop_loc in location_name_groups["Lohan"]:
        regions["Lohan"].locations.append(shop_loc)

    for shop_loc in location_name_groups["Kazas"]:
        regions["Kazas"].locations.append(shop_loc)

    for shop_loc in location_name_groups["Fletz"]:
        regions["Fletz Castle"].locations.append(shop_loc)

    for shop_loc in location_name_groups["Donau"]:
        regions["Donau"].locations.append(shop_loc)

    for shop_loc in location_name_groups["Queen Fury"]:
        regions["Queen Fury"].locations.append(shop_loc)

    for shop_loc in location_name_groups["Fueno"]:
        regions["Fueno"].locations.append(shop_loc)

    for shop_loc in location_name_groups["Furni"]:
        regions["Furni"].locations.append(shop_loc)

    for shop_loc in location_name_groups["Deningrad"]:
        regions["Deningrad"].locations.append(shop_loc)

    for shop_loc in location_name_groups["Wingly Forest"]:
        regions["Wingly Forest"].locations.append(shop_loc)

    for shop_loc in location_name_groups["Vellweb"]:
        regions["Vellweb"].locations.append(shop_loc)

    for shop_loc in location_name_groups["Ulara"]:
        regions["Ulara"].locations.append(shop_loc)

    for shop_loc in location_name_groups["Rouge"]:
        regions["Rouge"].locations.append(shop_loc)

    for shop_loc in location_name_groups["Moon"]:
        regions["Moon That Never Sets"].locations.append(shop_loc)

    for shop_loc in location_name_groups["Hellena 01"]:
        regions["Hellena Prison"].locations.append(shop_loc)

    for shop_loc in location_name_groups["Hellena 02"]:
        regions["Hellena Prison"].locations.append(shop_loc)

    for shop_loc in location_name_groups["Kashua"]:
        regions["Kashua Glacier"].locations.append(shop_loc)

    for shop_loc in location_name_groups["Forest"]:
        regions["Forest"].locations.append(shop_loc)

    for shop_loc in location_name_groups["Volcano"]:
        regions["Volcano Villude"].locations.append(shop_loc)

    for shop_loc in location_name_groups["Zenebatos"]:
        regions["Zenebatos"].locations.append(shop_loc)

    # add events
    regions["Seles"].locations.append("Defeat Commander in Seles")

    # Set up the regions correctly.
    for name, data in regions.items():
        multiworld.regions.append(create_region(multiworld, player, name, data))

def connect_entrances(lod_world):
    multiworld = lod_world.multiworld
    player     = lod_world.player
    options    = lod_world.options

    for region in multiworld.regions:
        if region.player != player:
            continue
        for entrance in region.exits:
            target_region = multiworld.get_region(entrance.name, player)
            entrance.connect(target_region)


def create_region(multiworld: MultiWorld, player: int, name: str, data: LegendOfDragoonRegionData):
    region = Region(name, player, multiworld)
    if data.locations:
        for loc_name in data.locations:
            loc_data = location_table.get(loc_name)
            location = LegendOfDragoonLocation(player, loc_name, loc_data.code if loc_data else None, region)
            if loc_data and loc_data.type == "Event":
                location.address = None
                location.event = True
            region.locations.append(location)

    if data.region_exits:
        for region_exit in data.region_exits:
            entrance = Entrance(player, region_exit, region)
            region.exits.append(entrance)

    return region
