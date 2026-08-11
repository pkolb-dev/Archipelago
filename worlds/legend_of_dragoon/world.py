from typing import Mapping, Any

import Utils
from BaseClasses import CollectionState, MultiWorld
from rule_builder.cached_world import CachedRuleBuilderWorld
from worlds.AutoWorld import World
from . import items, locations, regions, rules, web_world, options as lod_options
from .game_id import lod_name
from .item.additions import dart_additions_table, lavitz_additions_table, rose_additions_table, haschel_additions_table, \
    albert_additions_table, meru_additions_table, kongol_additions_table
from .item.item_data import LegendOfDragoonItem
from .options import CompletionCondition


class LegendOfDragoonWorld(CachedRuleBuilderWorld):
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

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = "Menu"

    def create_regions(self):
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self):
        rules.set_all_rules(self)

    def create_item(self, name: str) -> LegendOfDragoonItem:
        return items.create_item(self, name)

    def create_items(self):
        items.create_all_items(self)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        # If you need access to the player's chosen options on the client side, there is a helper for that.
        return {
            "addition_randomizer": self.options.addition_randomizer.value,
            "magic_randomizer": self.options.magic_randomizer.value,
            "lod_completion_condition": self.options.lod_completion_condition.value,
            "enable_shop_sanity": self.options.enable_shopsanity.value,
            "world_version": self.world_version,
            "maximum_shop_price": self.options.maximum_shop_price.value,
            "minimum_shop_price": self.options.minimum_shop_price.value,
            "allow_repeat_consumables": self.options.allow_repeat_consumables.value,
            "death_link": self.options.death_link.value,
            "bale_equipment_shop_slots": self.options.bale_equipment_shop_slots.value,
            "serdio_item_shop_slots": self.options.serdio_item_shop_slots.value,
            "lohan_equipment_shop_slots": self.options.lohan_equipment_shop_slots.value,
            "lohan_item_shop_slots": self.options.lohan_item_shop_slots.value,
            "kazas_equipment_shop_slots": self.options.kazas_equipment_shop_slots.value,
            "kazas_fort_item_shop_slots": self.options.kazas_fort_item_shop_slots.value,
            "fletz_equipment_shop_slots": self.options.fletz_equipment_shop_slots.value,
            "fletz_item_shop_slots": self.options.fletz_item_shop_slots.value,
            "donau_equipment_shop_slots": self.options.donau_equipment_shop_slots.value,
            "donau_item_shop_slots": self.options.donau_item_shop_slots.value,
            "queen_fury_equipment_shop_slots": self.options.queen_fury_equipment_shop_slots.value,
            "queen_fury_item_shop_slots": self.options.queen_fury_item_shop_slots.value,
            "fueno_equipment_shop_slots": self.options.fueno_equipment_shop_slots.value,
            "fueno_item_shop_slots": self.options.fueno_item_shop_slots.value,
            "furni_equipment_shop_slots": self.options.furni_equipment_shop_slots.value,
            "furni_item_shop_slots": self.options.furni_item_shop_slots.value,
            "deningrad_equipment_shop_slots": self.options.deningrad_equipment_shop_slots.value,
            "deningrad_item_shop_slots": self.options.deningrad_item_shop_slots.value,
            "wingly_forest_equipment_shop_slots": self.options.wingly_forest_equipment_shop_slots.value,
            "wingly_forest_item_shop_slots": self.options.wingly_forest_item_shop_slots.value,
            "vellweb_equipment_shop_slots": self.options.vellweb_equipment_shop_slots.value,
            "vellweb_item_shop_slots": self.options.vellweb_item_shop_slots.value,
            "ulara_equipment_shop_slots": self.options.ulara_equipment_shop_slots.value,
            "ulara_item_shop_slots": self.options.ulara_item_shop_slots.value,
            "rouge_equipment_shop_slots": self.options.rouge_equipment_shop_slots.value,
            "rouge_item_shop_slots": self.options.rouge_item_shop_slots.value,
            "moon_equipment_shop_slots": self.options.moon_equipment_shop_slots.value,
            "moon_item_shop_slots": self.options.moon_item_shop_slots.value,
            "hellena_01_item_shop_slots": self.options.hellena_01_item_shop_slots.value,
            "kashua_equipment_shop_slots": self.options.kashua_equipment_shop_slots.value,
            "kashua_item_shop_slots": self.options.kashua_item_shop_slots.value,
            "fletz_accessory_shop_slots": self.options.fletz_accessory_shop_slots.value,
            "forest_item_shop_slots": self.options.forest_item_shop_slots.value,
            "kazas_fort_equipment_shop_slots": self.options.kazas_fort_equipment_shop_slots.value,
            "volcano_item_shop_slots": self.options.volcano_item_shop_slots.value,
            "zenebatos_equipment_shop_slots": self.options.zenebatos_equipment_shop_slots.value,
            "zenebatos_item_shop_slots": self.options.zenebatos_item_shop_slots.value,
            "hellena_02_item_shop_slots": self.options.hellena_02_item_shop_slots.value,
            "black_castle_item_shop_slots": self.options.black_castle_item_shop_slots.value,
        }
