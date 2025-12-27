from worlds.AutoWorld import World, WebWorld
from BaseClasses import Tutorial

from .game_id import lod_name
from .item.item_data import LegendOfDragoonItem
from .items import get_items_by_category, item_table

# LoD imports
from .options import LegendOfDragoonOptions, lod_option_groups
from .locations import location_table

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
    options_dataclass = options.LegendOfDragoonOptions
    options: options.LegendOfDragoonOptions

    fillers = {}
    fillers.update(get_items_by_category("Consumable"))


    # map items & locations
    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {name: data.code for name, data in location_table.items()}

    def create_item(self, name: str) -> LegendOfDragoonItem:
        data = item_table[name]
        return LegendOfDragoonItem(name, data.classification, data.code, self.player)


    def get_filler_item_name(self) -> str:
        return self.random.choices([filler for filler in self.fillers.keys()])[0]
