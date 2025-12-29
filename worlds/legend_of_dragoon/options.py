from dataclasses import dataclass
from Options import PerGameCommonOptions, Choice, OptionGroup, Toggle


class AdditionRandomization(Choice):
    """
    Controls how character Additions are unlocked.

    Off:
        Additions unlock via in-game events only (vanilla behavior).

    Shuffled (Character):
        Addition unlock events are shuffled within each character.

    Shuffled (Party):
        Addition unlock events are shuffled across all characters.

    Progressive (Character):
        Progressive addition items are added to the item pool
        and unlock additions for their respective character.

    Addition Sanity:
        Each addition unlock is its own item in the item pool
        and can be placed in any world.
    """
    display_name = "Addition Randomization"

    option_off = 0
    option_shuffled_character = 1
    option_shuffled_party = 2
    option_progressive_character = 3
    option_addition_sanity = 4

    default = 0

class RandomStartingAddition(Toggle):
    """Start each character with a random addition unlocked."""
    display_name = "Random Starting Addition"
    rich_text_doc = True


class CompletionCondition(Choice):
    """
    Set the goal for completing the game.
    """
    display_name = "Completion Condition"
    option_stardust_count_25 = 0
    option_stardust_count_50 = 1 # collect all stardust in the game
    option_lavitz =  2# goal after lavitz death
    option_doel = 3 # goal after defeating dragoon doel
    option_lenus2 = 4# goal after defeating lenus w/ regole
    option_faust =  5 # goal after defeating Magician Faust
    option_melbu =  6 # goal after defeating Melbu Frahma
    option_seles_commander = 7
    default = 7


@dataclass
class LegendOfDragoonOptions(PerGameCommonOptions):
    enable_addition_randomizer: AdditionRandomization
    random_starting_addition: RandomStartingAddition
    lod_completion_condition: CompletionCondition

option_groups = [
    OptionGroup("General", [
        AdditionRandomization,
        RandomStartingAddition,
        CompletionCondition,
    ], False)
]

option_presets = {

}