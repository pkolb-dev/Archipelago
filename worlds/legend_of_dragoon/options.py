from dataclasses import dataclass
from Options import PerGameCommonOptions, Choice, OptionGroup, Toggle, Range


class AdditionRandomization(Choice):
    """
    Controls how character Additions are unlocked.

    Progressive (Character):
        Progressive addition items are added to the item pool
        and unlock additions for their respective character.

    Addition Sanity:
        Each addition unlock is its own item in the item pool
        and can be placed in any world.
    """
    display_name = "Addition Randomization"

    # these will be added later.
    option_off = 0
    # option_shuffled_character = 1
    # option_shuffled_party = 2
    # option_progressive_character = 3
    option_addition_sanity = 1

    default = 0

class Shopsanity(Toggle):
    """
    Toggles all shop items to be locations. This disables vanilla behavior and makes all items one-time purchases.
    """
    display_name = "Shopsanity"
    default = True

class RandomStartingAddition(Toggle):
    """Start each character with a random addition unlocked."""
    display_name = "Random Starting Addition"
    rich_text_doc = True


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
    option_chapter_4 =  4
    default = 1

@dataclass
class LegendOfDragoonOptions(PerGameCommonOptions):
    addition_randomizer: AdditionRandomization
    random_starting_addition: RandomStartingAddition
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
    OptionGroup("Starting Choices", [
        RandomStartingAddition
    ])
]
option_presets = {

}