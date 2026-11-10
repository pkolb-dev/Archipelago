from dataclasses import dataclass
from Options import PerGameCommonOptions, Choice, OptionGroup, Toggle, Range, DeathLink, TextChoice


class AdditionRandomization(Choice):
    """
    Controls how character Additions are unlocked.
   Shuffled:
        Each addition unlock is its own item in the item pool
        and can be placed in any world.
        Starting additions are randomly chosen.

    Progressive:
        Progressive addition items are added to the item pool
        and unlock additions for their respective character.
    """
    display_name = "Addition Randomization"

    option_shuffled = 1
    option_progressive = 2

    default = 2


class DragoonMagicRandomization(Choice):
    """
    Controls how Dragoon Magic are unlocked.

    Progressive:
        Progressive dragoon magic is added to the item pool
        and unlock spells for their respective character.

    Shuffled:
        Each magic spell is its own item in the item pool.
    """
    display_name = "Dragoon Magic Randomization"

    option_progressive = 0
    option_shuffled = 1

    default = 0


class Shopsanity(Toggle):
    """
    Toggles all shop items to be exclusively locations. This disables vanilla behavior and makes all items one-time purchases.
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


class DefaultShopSlots(Range):
    """
    For each slot, add a location to the shop
    This setting targets all shops that are always present
    """
    display_name = "Default Shop Slots"
    default = 10
    range_start = 10
    range_end = 20


class MissableShopSlots(Range):
    """
    For each slot, add a location to the shop
    This setting targets all shops that are missable:
    Shops:
    - Black Castle Item Shop
    - Forest Item Shop
    - Hellena Item Shops (1 & 2)
    - Queen Fury (Phantom ship)
    - Volcano Item Shop
    """
    display_name = "Missable Shop Slots"
    default = 10
    range_start = 10
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


class DragoonMagicLocations(Range):
    """
    Number of magic locations to include in the playthrough.
    """
    display_name = "Dragoon Magic Locations"
    default = 2
    range_end = 4
    range_start = 1


class EnableLloyd(Toggle):
    """
    Allow Lloyd to be part of the multiworld
    This requires the Lloyd Mod to be downloaded and included in the mods folder
    """
    display_name = "Enable Lloyd"
    default = False


class StartingCharacter(TextChoice):
    """
    Choose which character to start with
    Lloyd requires "Enable Lloyd" checked.
    """
    display_name = "Starting Character"
    option_dart = "Dart"
    option_lavitz = "Lavitz"
    option_shana = "Shana"
    option_rose = "Rose"
    option_haschel = "Haschel"
    option_albert = "Albert"
    option_meru = "Meru"
    option_kongol = "Kongol"
    option_miranda = "Miranda"
    option_lloyd = "Lloyd"
    default = "Dart"


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


@dataclass
class LegendOfDragoonOptions(PerGameCommonOptions):
    addition_randomizer: AdditionRandomization
    magic_randomizer: DragoonMagicRandomization
    lod_completion_condition: CompletionCondition
    enable_shopsanity: Shopsanity
    allow_repeat_consumables: AllowRepeatConsumables
    death_link: DeathLink
    minimum_shop_price: MinimumShopPrice
    maximum_shop_price: MaximumShopPrice
    default_shop_slots: DefaultShopSlots
    missable_shop_slots: MissableShopSlots
    magic_slots: DragoonMagicLocations
    starting_character: StartingCharacter
    enable_lloyd: EnableLloyd


option_groups = [
    OptionGroup("Goal Requirements", [
        CompletionCondition,
    ], False),
    OptionGroup("Addition Settings", [
        AdditionRandomization,
    ]),
    OptionGroup("Rando Options", [
        AllowRepeatConsumables,
        DeathLink,
    ], False),
    OptionGroup("Dragoon Magic Settings", [
        DragoonMagicRandomization,
        DragoonMagicLocations,
    ]),
    OptionGroup("Shopsanity", [
        Shopsanity,
        MinimumShopPrice,
        MaximumShopPrice,
        DefaultShopSlots,
        MissableShopSlots,
    ], False),
    OptionGroup("Starting Choices", [
        StartingCharacter
    ])
]
option_presets = {

}
