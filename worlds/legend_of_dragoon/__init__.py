from typing import List

from worlds.AutoWorld import World, WebWorld
from BaseClasses import Tutorial, ItemClassification, Item

from .game_id import lod_name
from .item.item_data import LegendOfDragoonItem
from .items import get_items_by_category, item_table, event_item_table

# LoD imports
from .options import LegendOfDragoonOptions, lod_option_groups
from .locations import location_table
from .regions import create_regions, connect_entrances
from .rules import set_rules

class LegendOfDragoonWebWorld(WebWorld):
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up ArchiDragoon (Archipelago on Severed Chains)",
        "English",
        "en_setup.md",
        "setup/en",
        ["pkolb-dev"]
    )

    tutorials = [setup_en]
    bug_report_page = "https://github.com/pkolb-dev/Archipelago/issues"
    option_groups = lod_option_groups
    options_presets = {}


class LegendOfDragoonWorld(World):
    """
    The Legend of Dragoon is a role-playing game developed and published by Sony Computer Entertainment for the video game console PlayStation.
    It was first released in Japan on December 2, 1999, in North America on June 11, 2000, and on January 19, 2001 in Europe.
    It was re-released in PlayStation Network December 22, 2010 in Japan and May 1, 2012 in North America.
    The game follows a young man, Dart Feld, on his journey through a world of magic, where ancient dragon warriors
    called Dragoons exist, to fight against evil forces who are threatening to destroy the world. 
    """

    # ID, name, version
    game = lod_name
    required_client_version = (0, 6, 0)

    # Web world
    web = LegendOfDragoonWebWorld()

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Severed Chains.",
        "English",
        "setup_en.md",
        "setup/en",
        ["pkolb-dev"]
    )

    tutorials = [setup_en]

    # Options
    options_dataclass = LegendOfDragoonOptions
    options: LegendOfDragoonOptions

    fillers = {}
    fillers.update(get_items_by_category("Consumable"))


    # map items & locations
    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {name: data.code for name, data in location_table.items()}

    def create_regions(self):
        create_regions(self)

    def set_rules(self):
        set_rules(self)

    def connect_entrances(self):
        connect_entrances(self)

    def create_items(self):
        """
        Populate the MultiWorld itempool with all items, including progression, filler, and events.
        By the end of this function, all items that exist in the world should be added to self.multiworld.itempool.
        """
        item_pool: List[LegendOfDragoonItem] = []
        if self.options.lod_completion_condition.option_seles_commander:
            self.get_location("Defeat Commander in Seles").place_locked_item(self.create_event("Victory"))


            # self.multiworld.get_location("Defeat Commander in Seles", self.player).place_locked_item(victory_item)
        total_locations = len(self.multiworld.get_unfilled_locations(self.player))
        for item in map(self.create_item, item_table):
            if item.name == "Victory":
                continue
            item_pool.append(item)


        while len(item_pool) < total_locations:
            item_pool.append(self.create_filler())

        self.multiworld.itempool += item_pool

    def create_item(self, name: str) -> LegendOfDragoonItem:
        data = item_table[name]
        return LegendOfDragoonItem(name, data.classification, data.code, self.player)

    def create_event(self, name: str) -> LegendOfDragoonItem:
        data = event_item_table[name]
        return LegendOfDragoonItem(name, data.classification, data.code, self.player)

    def create_filler(self) -> LegendOfDragoonItem:
        return self.create_item(self.get_filler_item_name())

    def get_filler_item_name(self) -> str:
            return self.random.choices([filler for filler in self.fillers.keys()])[0]
