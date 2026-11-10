from worlds.legend_of_dragoon.loc.location_data import LegendOfDragoonLocationData
from worlds.legend_of_dragoon.options import DefaultShopSlots, MissableShopSlots

perma_shop_table: dict[str, str] = {
    "Bale Equipment Shop": "Bale",
    "Bale Item Shop": "Bale",
    "Lohan Equipment Shop": "Lohan",
    "Lohan Item Shop": "Lohan",
    "Kazas Equipment Shop": "Kazas",
    "Kazas Fort Item Shop": "Kazas",
    "Fletz Equipment Shop": "Fletz",
    "Fletz Item Shop": "Fletz",
    "Donau Equipment Shop": "Donau",
    "Donau Item Shop": "Donau",
    "Fueno Equipment Shop": "Fueno",
    "Fueno Item Shop": "Fueno",
    "Furni Equipment Shop": "Furni",
    "Furni Item Shop": "Furni",
    "Deningrad Equipment Shop": "Deningrad",
    "Deningrad Item Shop": "Deningrad",
    "Wingly Forest Equipment Shop": "Wingly Forest",
    "Wingly Forest Item Shop": "Wingly Forest",
    "Vellweb Equipment Shop": "Vellweb",
    "Vellweb Item Shop": "Vellweb",
    "Ulara Equipment Shop": "Ulara",
    "Ulara Item Shop": "Ulara",
    "Rouge Equipment Shop": "Rouge",
    "Rouge Item Shop": "Rouge",
    "Moon Equipment Shop": "Moon",
    "Moon Item Shop": "Moon",
    "Kashua Equipment Shop": "Kashua Glacier",
    "Kashua Item Shop": "Kashua Glacier",
    "Fletz Accessory Shop": "Fletz",
    "Kazas Fort Equipment Shop": "Kazas",
    "Zenebatos Equipment Shop": "Zenebatos",
    "Zenebatos Item Shop": "Zenebatos",
}

missable_shop_table: dict[str, str] = {
    "Queen Fury Equipment Shop": "Queen Fury",
    "Queen Fury Item Shop": "Queen Fury",
    "Hellena 01 Item Shop": "Hellena Prison 01",
    "Forest Item Shop": "Forest",
    "Volcano Item Shop": "Volcano Villude",
    "Hellena 02 Item Shop": "Hellena Prison 02",
    "Black Castle Item Shop": "Black Castle",
}


def build_all_shops(perma_slots: int, missable_slots: int):
    base_id: int = 108_50000
    all_shops: dict[str, LegendOfDragoonLocationData] = {}

    curr_id = base_id
    for shop, region in perma_shop_table.items():
        for number in range(perma_slots):
            complete_name = shop + " - Slot " + str(number + 1)
            updated_data = LegendOfDragoonLocationData(region, curr_id, "Shop")
            all_shops.update({f"{complete_name}": updated_data})
            curr_id += 1

    for shop, region in missable_shop_table.items():
        for number in range(missable_slots):
            complete_name = shop + " - Slot " + str(number + 1)
            updated_data = LegendOfDragoonLocationData(region, curr_id, "Shop")
            all_shops.update({f"{complete_name}": updated_data})
            curr_id += 1

    return all_shops


def get_all_shops(perma_slots, missable_slots) -> dict[str, LegendOfDragoonLocationData]:
    all_shops: dict[str, LegendOfDragoonLocationData] = {}

    for shop in perma_shop_table.keys():
        for number in range(perma_slots):
            complete_name = shop + " - Slot " + str(number + 1)
            data = all_shops_table.get(complete_name)
            if data is None:
                continue
            all_shops[complete_name] = data

    for shop in missable_shop_table.keys():
        for number in range(missable_slots):
            complete_name = shop + " - Slot " + str(number + 1)
            data = all_shops_table.get(complete_name)
            if data is None:
                continue
            all_shops[complete_name] = data

    return all_shops


all_shops_table: dict[str, LegendOfDragoonLocationData] = build_all_shops(DefaultShopSlots.range_end,
                                                                          MissableShopSlots.range_end)
