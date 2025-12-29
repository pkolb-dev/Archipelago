from typing import Mapping, Any

from worlds.AutoWorld import World
from . import items, locations, regions, rules, web_world, options as lod_options
from .game_id import lod_name
from .item.item_data import LegendOfDragoonItem


class LegendOfDragoonWorld(World):
    """
    The Legend of Dragoon is a role-playing game developed and published by Sony Computer Entertainment for the video game console PlayStation.
    It was first released in Japan on December 2, 1999, in North America on June 11, 2000, and on January 19, 2001 in Europe.
    It was re-released in PlayStation Network December 22, 2010 in Japan and May 1, 2012 in North America.
    The game follows a young man, Dart Feld, on his journey through a world of magic, where ancient dragon warriors
    called Dragoons exist, to fight against evil forces who are threatening to destroy the world.
    """

    game = lod_name
    web = web_world.LegendOfDragoonWebWorld()

    # Options
    options_dataclass = lod_options.LegendOfDragoonOptions
    options: lod_options.LegendOfDragoonOptions

    # fillers = {}
    # fillers.update(get_items_by_category("Consumable"))


    # map items & locations

    # item_name_to_id = {name: data.code for name, data in item_table.items()}
    # location_name_to_id = {name: data.code for name, data in location_table.items()}
    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = "Menu"

    def create_regions(self):
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)
        # create_regions(self)

    def set_rules(self):
        rules.set_all_rules(self)
        # set_rules(self)

    def create_item(self, name: str) -> LegendOfDragoonItem:
        return items.create_item(self, name)

    def create_items(self):
        items.create_all_items(self)


    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)


    # def fill_slot_data(self) -> Mapping[str, Any]:
    #     # TODO: send shop data here?
    #     return self.options.as_dict()
