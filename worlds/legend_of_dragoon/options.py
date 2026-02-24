from dataclasses import dataclass
from Options import PerGameCommonOptions, Choice, OptionGroup, Toggle


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
    """
    display_name = "Shopsanity"
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


@dataclass
class LegendOfDragoonOptions(PerGameCommonOptions):
    addition_randomizer: AdditionRandomization
    lod_completion_condition: CompletionCondition
    enable_shopsanity: Shopsanity


option_groups = [
    OptionGroup("Goal Requirements", [
        CompletionCondition,
    ], False),
    OptionGroup("Addition Settings", [
        AdditionRandomization,
    ]),
    OptionGroup("Rando Options", [
        Shopsanity
    ], False),
    # OptionGroup("Starting Choices", [
    # ])
]
option_presets = {

}
