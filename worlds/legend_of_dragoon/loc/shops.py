from typing import Dict

from worlds.legend_of_dragoon.loc.location_data import LegendOfDragoonLocationData

shop_table: Dict[str, LegendOfDragoonLocationData] = {
    "Bale Equipment Shop": LegendOfDragoonLocationData("Bale", 108_50000, "Shop"),
    "Bale Item Shop": LegendOfDragoonLocationData("Bale", 108_50100, "Shop"),
    "Lohan Equipment Shop": LegendOfDragoonLocationData("Lohan", 108_50200, "Shop"),
    "Lohan Item Shop": LegendOfDragoonLocationData("Lohan", 108_50300, "Shop"),
    "Kazas Equipment Shop": LegendOfDragoonLocationData("Kazas", 108_50400, "Shop"),
    "Kazas Fort Item Shop": LegendOfDragoonLocationData("Kazas", 108_50500, "Shop"),
    "Fletz Equipment Shop": LegendOfDragoonLocationData("Fletz", 108_50600, "Shop"),
    "Fletz Item Shop": LegendOfDragoonLocationData("Fletz", 108_50700, "Shop"),
    "Donau Equipment Shop": LegendOfDragoonLocationData("Donau", 108_50800, "Shop"),
    "Donau Item Shop": LegendOfDragoonLocationData("Donau", 108_50900, "Shop"),
    "Queen Fury Equipment Shop": LegendOfDragoonLocationData("Queen Fury", 108_51000, "Shop"),
    "Queen Fury Item Shop": LegendOfDragoonLocationData("Queen Fury", 108_51100, "Shop"),
    "Fueno Equipment Shop": LegendOfDragoonLocationData("Fueno", 108_51200, "Shop"),
    "Fueno Item Shop": LegendOfDragoonLocationData("Fueno", 108_51300, "Shop"),
    "Furni Equipment Shop": LegendOfDragoonLocationData("Furni", 108_51400, "Shop"),
    "Furni Item Shop": LegendOfDragoonLocationData("Furni", 108_51500, "Shop"),
    "Deningrad Equipment Shop": LegendOfDragoonLocationData("Deningrad", 108_51600, "Shop"),
    "Deningrad Item Shop": LegendOfDragoonLocationData("Deningrad", 108_51700, "Shop"),
    "Wingly Forest Equipment Shop": LegendOfDragoonLocationData("Wingly Forest", 108_51800, "Shop"),
    "Wingly Forest Item Shop": LegendOfDragoonLocationData("Wingly Forest", 108_51900, "Shop"),
    "Vellweb Equipment Shop": LegendOfDragoonLocationData("Vellweb", 108_52000, "Shop"),
    "Vellweb Item Shop": LegendOfDragoonLocationData("Vellweb", 108_52100, "Shop"),
    "Ulara Equipment Shop": LegendOfDragoonLocationData("Ulara", 108_52200, "Shop"),
    "Ulara Item Shop": LegendOfDragoonLocationData("Ulara", 108_52300, "Shop"),
    "Rouge Equipment Shop": LegendOfDragoonLocationData("Rouge", 108_52400, "Shop"),
    "Rouge Item Shop": LegendOfDragoonLocationData("Rouge", 108_52500, "Shop"),
    "Moon Equipment Shop": LegendOfDragoonLocationData("Moon", 108_52600, "Shop"),
    "Moon Item Shop": LegendOfDragoonLocationData("Moon", 108_52700, "Shop"),
    "Hellena 01 Item Shop": LegendOfDragoonLocationData("Hellena 01", 108_52800, "Shop"),
    "Kashua Equipment Shop": LegendOfDragoonLocationData("Kashua Glacier", 108_52900, "Shop"),
    "Kashua Item Shop": LegendOfDragoonLocationData("Kashua Glacier", 108_53000, "Shop"),
    "Fletz Accessory Shop": LegendOfDragoonLocationData("Fletz", 108_53100, "Shop"),
    "Forest Item Shop": LegendOfDragoonLocationData("Forest", 108_53200, "Shop"),
    "Kazas Fort Equipment Shop": LegendOfDragoonLocationData("Kazas", 108_53300, "Shop"),
    "Volcano Item Shop": LegendOfDragoonLocationData("Volcano Villude", 108_53400, "Shop"),
    "Zenebatos Equipment Shop": LegendOfDragoonLocationData("Zenebatos", 108_53500, "Shop"),
    "Zenebatos Item Shop": LegendOfDragoonLocationData("Zenebatos", 108_53600, "Shop"),
    "Hellena 02 Item Shop": LegendOfDragoonLocationData("Hellena 02", 108_53700, "Shop"),
    "Black Castle Item Shop": LegendOfDragoonLocationData("Black Castle", 108_53800, "Shop"),
}


def get_all_shops():
    all_shops: Dict[str, LegendOfDragoonLocationData] = {}

    for key, value in shop_table.items():
        if value.code is None:
            continue

        for number in range(20):
            complete_name = key + " - Slot " + str(number + 1)
            updated_data = LegendOfDragoonLocationData(value.category, value.code + number + 1, value.type)
            all_shops.update({f"{complete_name}": updated_data})

    return all_shops
