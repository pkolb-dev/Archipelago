from dataclasses import dataclass
from Options import PerGameCommonOptions, Choice, OptionGroup, Toggle, Range, DeathLink


class AdditionRandomization(Choice):
    """
    Controls how character Additions are unlocked.
    Off:
        Additions will not be added to the item pool.

    Progressive (Character):
        Progressive addition items are added to the item pool
        and unlock additions for their respective character.

    Addition Sanity:
        Each addition unlock is its own item in the item pool
        and can be placed in any world.
        Starting additions are randomly chosen.
    """
    display_name = "Addition Randomization"

    option_off = 0
    option_addition_sanity = 1
    option_progressive_character = 2

    default = 0


class Shopsanity(Toggle):
    """
    Toggles all shop items to be locations. This disables vanilla behavior and makes all items one-time purchases.
    Every shop will have randomized prices as well.
    """
    display_name = "Shopsanity"
    default = True


class MinimumShopPrice(Range):
    """
    The minimum gold price for items in shops.
    Raising this could make certain seeds more difficult early on.
    """
    display_name = "Minimum Shop Price"
    range_start = 1
    range_end = 200
    default = 10


class MaximumShopPrice(Range):
    """
    The maximum gold price for items in shops.
    Raising this could make certain seeds more difficult early on.
    """
    display_name = "Maximum Shop Price"
    range_start = 200
    range_end = 2000
    default = 700


class BaleEquipmentShopSlots(Range):
    """For each slot, add a location to the shop"""
    display_name = "Bale Equipment Shop Slots"
    default = 10
    range_end = 20


class BaleItemShopSlots(Range):
    """For each slot, add a location to the shop"""
    display_name = "Bale Item Shop Slots"
    default = 7
    range_end = 20


class LohanEquipmentShopSlots(Range):
    """For each slot, add a location to the shop"""
    display_name = "Lohan Equipment Shop Slots"
    default = 10
    range_end = 20


class LohanItemShopSlots(Range):
    """For each slot, add a location to the shop"""
    display_name = "Lohan Item Shop Slots"
    default = 8
    range_end = 20


class KazasEquipmentShopSlots(Range):
    """For each slot, add a location to the shop"""
    display_name = "Kazas Equipment Shop Slots"
    default = 5
    range_end = 20


class KazasFortEquipmentShopSlots(Range):
    """For each slot, add a location to the shop"""
    display_name = "Kazas Fort Equipment Shop Slots"
    default = 5
    range_end = 20


class KazasFortItemShopSlots(Range):
    """For each slot, add a location to the shop"""
    display_name = "Kazas Fort Item Shop Slots"
    default = 5
    range_end = 20


class FletzEquipmentShopSlots(Range):
    """For each slot, add a location to the shop"""
    display_name = "Fletz Equipment Shop Slots"
    default = 10
    range_end = 20


class FletzItemShopSlots(Range):
    """For each slot, add a location to the shop"""
    display_name = "Fletz Item Shop Slots"
    default = 9
    range_end = 20


class DonauEquipmentShopSlots(Range):
    """For each slot, add a location to the shop"""
    display_name = "Donau Equipment Shop Slots"
    default = 10
    range_end = 20


class DonauItemShopSlots(Range):
    """For each slot, add a location to the shop"""
    display_name = "Donau Item Shop Slots"
    default = 10
    range_end = 20


class QueenFuryEquipmentShopSlots(Range):
    """
    For each slot, add a location to the shop
    WARNING:
        This is a missable location! This is only available
        on the phantom ship!
    """
    display_name = "Queen Fury Equipment Shop Slots"
    default = 10
    range_end = 20


class QueenFuryItemShopSlots(Range):
    """
    For each slot, add a location to the shop
    WARNING:
        This is a missable location! This is only available
        on the phantom ship!
    """
    display_name = "Queen Fury Item Shop Slots"
    default = 10
    range_end = 20


class FuenoEquipmentShopSlots(Range):
    """
    For each slot, add a location to the shop
    """
    display_name = "Fueno Equipment Shop Slots"
    default = 10
    range_end = 20


class FuenoItemShopSlots(Range):
    """
    For each slot, add a location to the shop
    """
    display_name = "Fueno Item Shop Slots"
    default = 10
    range_end = 20


class FurniEquipmentShopSlots(Range):
    """
    For each slot, add a location to the shop
    """
    display_name = "Furni Equipment Shop Slots"
    default = 10
    range_end = 20


class FurniItemShopSlots(Range):
    """
    For each slot, add a location to the shop
    """
    display_name = "Furni Item Shop Slots"
    default = 10
    range_end = 20


class DeningradEquipmentShopSlots(Range):
    """
    For each slot, add a location to the shop
    """
    display_name = "Deningrad Equipment Shop Slots"
    default = 10
    range_end = 20


class DeningradItemShopSlots(Range):
    """
    For each slot, add a location to the shop
    """
    display_name = "Deningrad Item Shop Slots"
    default = 10
    range_end = 20


class WinglyForestEquipmentShopSlots(Range):
    """
    For each slot, add a location to the shop
    """
    display_name = "Wingly Forest Equipment Shop Slots"
    default = 10
    range_end = 20


class WinglyForestItemShopSlots(Range):
    """
    For each slot, add a location to the shop
    """
    display_name = "Wingly Forest Item Shop Slots"
    default = 10
    range_end = 20


class VellwebEquipmentShopSlots(Range):
    """
    For each slot, add a location to the shop
    """
    display_name = "Vellweb Equipment Shop Slots"
    default = 10
    range_end = 20


class VellwebItemShopSlots(Range):
    """
    For each slot, add a location to the shop
    """
    display_name = "Vellweb Item Shop Slots"
    default = 10
    range_end = 20


class UlaraEquipmentShopSlots(Range):
    """
    For each slot, add a location to the shop
    """
    display_name = "Ulara Equipment Shop Slots"
    default = 10
    range_end = 20


class UlaraItemShopSlots(Range):
    """
    For each slot, add a location to the shop
    """
    display_name = "Ulara Item Shop Slots"
    default = 10
    range_end = 20


class RougeEquipmentShopSlots(Range):
    """
    For each slot, add a location to the shop
    """
    display_name = "Rouge Equipment Shop Slots"
    default = 10
    range_end = 20


class RougeItemShopSlots(Range):
    """
    For each slot, add a location to the shop
    """
    display_name = "Rouge Item Shop Slots"
    default = 10
    range_end = 20


class MoonEquipmentShopSlots(Range):
    """
    For each slot, add a location to the shop
    """
    display_name = "Moon Equipment Shop Slots"
    default = 10
    range_end = 20


class MoonItemShopSlots(Range):
    """
    For each slot, add a location to the shop
    """
    display_name = "Moon Item Shop Slots"
    default = 10
    range_end = 20


class Hellena01ItemShopSlots(Range):
    """
    For each slot, add a location to the shop.
    WARNING:
        This is a missable location!
    """
    display_name = "Hellena (First Visit) Item Shop Slots"
    default = 4
    range_end = 20


class Hellena02ItemShopSlots(Range):
    """
    For each slot, add a location to the shop
    WARNING:
        This is a missable location!
    """
    display_name = "Hellena (Second Visit) Item Shop Slots"
    default = 10
    range_end = 20


class KashuaEquipmentShopSlots(Range):
    """
    For each slot, add a location to the shop
    """
    display_name = "Kashua Equipment Shop Slots"
    default = 10
    range_end = 20


class KashuaItemShopSlots(Range):
    """
    For each slot, add a location to the shop
    """
    display_name = "Kashua Item Shop Slots"
    default = 10
    range_end = 20


class FletzAccessoryShopSlots(Range):
    """
    For each slot, add a location to the shop
    """
    display_name = "Fletz Accessory Shop Slots"
    default = 10
    range_end = 20


class ForestItemShopSlots(Range):
    """
    For each slot, add a location to the shop
    WARNING:
        This is a missable location!
    """
    display_name = "Forest Item Shop Slots"
    default = 5
    range_end = 20


class VolcanoItemShopSlots(Range):
    """
    For each slot, add a location to the shop
    """
    display_name = "Volcano Item Shop Slots"
    default = 10
    range_end = 20


class ZenebatosEquipmentShopSlots(Range):
    """
    For each slot, add a location to the shop
    """
    display_name = "Zenebatos Equipment Shop Slots"
    default = 10
    range_end = 20


class ZenebatosItemShopSlots(Range):
    """
    For each slot, add a location to the shop
    """
    display_name = "Zenebatos Item Shop Slots"
    default = 10
    range_end = 20


class BlackCastleItemShopSlots(Range):
    """
    For each slot, add a location to the shop
    WARNING:
        This is a missable location!
    """
    display_name = "Black Castle Item Shop Slots"
    default = 10
    range_end = 20


class AllowRepeatConsumables(Toggle):
    """
    Toggles all shops having four basic repeatable purchases:
    - Angel's Prayer
    - Healing Potion
    - Mind Purifier
    - Body Purifier
    """
    display_name = "Allow Repeat Consumables"
    default = True


class CompletionCondition(Choice):
    """
    Set the goal for completing the game.
    - Chapter 1: Goal after defeating Dragoon Doel
    - Chapter 2: Goal after defeating Lenus & Regole
    - Chapter 3: Goal after defeating Lloyd 2
    - Chapter 4: Goal after defeating Melbu Frahma
    """
    display_name = "Completion Condition"
    option_chapter_1 = 1
    option_chapter_2 = 2
    option_chapter_3 = 3
    option_chapter_4 = 4
    default = 1


class LegendOfDragoonDeathLink(DeathLink):
    __doc__ = DeathLink.__doc__ + "\n\n    Note: this will set every character's HP value to 0 instead of game over when receiving a deathlink trigger."


@dataclass
class LegendOfDragoonOptions(PerGameCommonOptions):
    addition_randomizer: AdditionRandomization
    lod_completion_condition: CompletionCondition
    enable_shopsanity: Shopsanity
    allow_repeat_consumables: AllowRepeatConsumables
    death_link: LegendOfDragoonDeathLink
    minimum_shop_price: MinimumShopPrice
    maximum_shop_price: MaximumShopPrice
    bale_equipment_shop_slots: BaleEquipmentShopSlots
    serdio_item_shop_slots: BaleItemShopSlots
    lohan_equipment_shop_slots: LohanEquipmentShopSlots
    lohan_item_shop_slots: LohanItemShopSlots
    kazas_equipment_shop_slots: KazasEquipmentShopSlots
    kazas_fort_item_shop_slots: KazasFortItemShopSlots
    fletz_equipment_shop_slots: FletzEquipmentShopSlots
    fletz_item_shop_slots: FletzItemShopSlots
    donau_equipment_shop_slots: DonauEquipmentShopSlots
    donau_item_shop_slots: DonauItemShopSlots
    queen_fury_equipment_shop_slots: QueenFuryEquipmentShopSlots
    queen_fury_item_shop_slots: QueenFuryItemShopSlots
    fueno_equipment_shop_slots: FuenoEquipmentShopSlots
    fueno_item_shop_slots: FuenoItemShopSlots
    furni_equipment_shop_slots: FurniEquipmentShopSlots
    furni_item_shop_slots: FurniItemShopSlots
    deningrad_equipment_shop_slots: DeningradEquipmentShopSlots
    deningrad_item_shop_slots: DeningradItemShopSlots
    wingly_forest_equipment_shop_slots: WinglyForestEquipmentShopSlots
    wingly_forest_item_shop_slots: WinglyForestItemShopSlots
    vellweb_equipment_shop_slots: VellwebEquipmentShopSlots
    vellweb_item_shop_slots: VellwebItemShopSlots
    ulara_equipment_shop_slots: UlaraEquipmentShopSlots
    ulara_item_shop_slots: UlaraItemShopSlots
    rouge_equipment_shop_slots: RougeEquipmentShopSlots
    rouge_item_shop_slots: RougeItemShopSlots
    moon_equipment_shop_slots: MoonEquipmentShopSlots
    moon_item_shop_slots: MoonItemShopSlots
    hellena_01_item_shop_slots: Hellena01ItemShopSlots
    kashua_equipment_shop_slots: KashuaEquipmentShopSlots
    kashua_item_shop_slots: KashuaItemShopSlots
    fletz_accessory_shop_slots: FletzAccessoryShopSlots
    forest_item_shop_slots: ForestItemShopSlots
    kazas_fort_equipment_shop_slots: KazasFortEquipmentShopSlots
    volcano_item_shop_slots: VolcanoItemShopSlots
    zenebatos_equipment_shop_slots: ZenebatosEquipmentShopSlots
    zenebatos_item_shop_slots: ZenebatosItemShopSlots
    hellena_02_item_shop_slots: Hellena02ItemShopSlots
    black_castle_item_shop_slots: BlackCastleItemShopSlots


option_groups = [
    OptionGroup("Goal Requirements", [
        CompletionCondition,
    ], False),
    OptionGroup("Addition Settings", [
        AdditionRandomization,
    ]),
    OptionGroup("Rando Options", [
        AllowRepeatConsumables,
        LegendOfDragoonDeathLink,
    ], False),
    OptionGroup("Shopsanity", [
        Shopsanity,
        MinimumShopPrice,
        MaximumShopPrice,
        BaleEquipmentShopSlots,
        BaleItemShopSlots,
        LohanEquipmentShopSlots,
        LohanItemShopSlots,
        KazasEquipmentShopSlots,
        KazasFortEquipmentShopSlots,
        KazasFortItemShopSlots,
        FletzEquipmentShopSlots,
        FletzItemShopSlots,
        DonauEquipmentShopSlots,
        DonauItemShopSlots,
        QueenFuryEquipmentShopSlots,
        QueenFuryItemShopSlots,
        FuenoEquipmentShopSlots,
        FuenoItemShopSlots,
        FurniEquipmentShopSlots,
        FurniItemShopSlots,
        DeningradEquipmentShopSlots,
        DeningradItemShopSlots,
        WinglyForestEquipmentShopSlots,
        WinglyForestItemShopSlots,
        VellwebEquipmentShopSlots,
        VellwebItemShopSlots,
        UlaraEquipmentShopSlots,
        UlaraItemShopSlots,
        RougeEquipmentShopSlots,
        RougeItemShopSlots,
        MoonEquipmentShopSlots,
        MoonItemShopSlots,
        Hellena01ItemShopSlots,
        Hellena02ItemShopSlots,
        KashuaEquipmentShopSlots,
        KashuaItemShopSlots,
        FletzAccessoryShopSlots,
        ForestItemShopSlots,
        VolcanoItemShopSlots,
        ZenebatosEquipmentShopSlots,
        ZenebatosItemShopSlots,
        BlackCastleItemShopSlots,
    ], False)
    # OptionGroup("Starting Choices", [
    # ])
]
option_presets = {

}
