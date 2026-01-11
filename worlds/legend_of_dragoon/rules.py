from __future__ import annotations

from typing import TYPE_CHECKING

from worlds.generic.Rules import set_rule
from .regions import visualize_world

if TYPE_CHECKING:
    from .world import LegendOfDragoonWorld

def set_all_rules(world: LegendOfDragoonWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)

    # for debugging purposes:
    # visualize_world(world.multiworld)


def set_all_entrance_rules(world: LegendOfDragoonWorld) -> None:
    dart_additions = world.get_entrance("Menu to Dart Additions")
    lavitz_additions = world.get_entrance("Menu to Lavitz Additions")
    rose_additions = world.get_entrance("Menu to Rose Additions")
    haschel_additions = world.get_entrance("Menu to Haschel Additions")
    albert_additions = world.get_entrance("Menu to Albert Additions")
    meru_additions = world.get_entrance("Menu to Meru Additions")
    kongol_additions = world.get_entrance("Menu to Kongol Additions")

    # set_rule(dart_additions, lambda state: state.has("Commander", world.player))
    set_rule(lavitz_additions, lambda state: state.has("Prison Key", world.player))
    set_rule(rose_additions, lambda state: state.has("Kongol 1", world.player))
    set_rule(haschel_additions, lambda state: state.has("Lloyd 1", world.player))
    set_rule(albert_additions, lambda state: state.has("Fruegel 2", world.player))
    set_rule(meru_additions, lambda state: state.has_all(["Mappi Steals Orb","Letter from Lynn"], world.player))
    set_rule(kongol_additions, lambda state: state.has("Gehrich", world.player))

    forest_to_prairie = world.get_entrance("Forest to Prairie")
    set_rule(forest_to_prairie, lambda state: state.has_all(["Prison Key", "Fruegel 1"], world.player))

    hellena_prison_01_to_forest = world.get_entrance("Hellena Prison 01 to Forest")
    set_rule(hellena_prison_01_to_forest, lambda state: state.has_all(["Prison Key", "Fruegel 1"], world.player))

    hellena_prison_01_to_02 = world.get_entrance("Hellena Prison 01 to 02")
    set_rule(hellena_prison_01_to_02, lambda state: state.has("Lloyd 1", world.player))

    prairie_to_limestone_cave = world.get_entrance("Prairie to Limestone Cave")
    set_rule(prairie_to_limestone_cave, lambda state: state.has("Axe from the Shack", world.player))

    bale_to_hoax = world.get_entrance("Bale to Hoax")
    set_rule(bale_to_hoax, lambda state: state.has_all(["Lavitzs Picture", "Fathers Stone"], world.player))

    dragons_nest_to_shrine_of_shirley = world.get_entrance("Dragon's Nest to Shrine of Shirley")
    set_rule(dragons_nest_to_shrine_of_shirley, lambda state: state.has_all(["Life Water", "Water Bottle"], world.player))

    lohan_to_hellena_prison_02 = world.get_entrance("Lohan to Hellena Prison 02")
    set_rule(lohan_to_hellena_prison_02, lambda state: state.has("Lloyd 1", world.player))
    forest_to_kazas = world.get_entrance("Forest to Kazas")
    set_rule(forest_to_kazas, lambda state: state.has("Fruegel 2", world.player))

    black_castle_to_fletz = world.get_entrance("Black Castle to Fletz")
    set_rule(black_castle_to_fletz, lambda state: state.has_all(["Magic Oil", "Red Stone", "Blue Stone", "Yellow Stone"], world.player))

    barrens_to_valley = world.get_entrance("Barrens to Valley of Corrupted Gravity")
    set_rule(barrens_to_valley, lambda state: state.has("Pass for Valley", world.player))

    donau_to_queen_fury = world.get_entrance("Donau to Queen Fury")
    set_rule(donau_to_queen_fury, lambda state: state.has("Lenus 1", world.player))

    phantom_ship_to_lidiera = world.get_entrance("Phantom Ship to Lidiera")
    set_rule(phantom_ship_to_lidiera, lambda state: state.has("Key to Ship", world.player))

    donau_to_furni = world.get_entrance("Donau to Furni")
    set_rule(donau_to_furni, lambda state: state.has_all(["Boat License", "Lenus 2"], world.player))

    vellweb_to_death_frontier = world.get_entrance("Vellweb to Death Frontier")
    set_rule(vellweb_to_death_frontier, lambda state: state.has_all(["Moon Mirror", "Moon Dagger", "Moon Gem"], world.player))

    zenebatos_to_mayfil = world.get_entrance("Zenebatos to Mayfil")
    set_rule(zenebatos_to_mayfil, lambda state: state.has_all(["Law Maker", "Law Output"], world.player))

def set_all_location_rules(world: LegendOfDragoonWorld) -> None:
    blazing_dynamo = world.get_location("Dart - Blazing Dynamo Unlock")
    lavitz_blossom_storm = world.get_location("Lavitz - Blossom Storm Unlock")
    demons_dance = world.get_location("Rose - Demon's Dance Unlock")
    omni_sweep = world.get_location("Haschel - Omni-Sweep Unlock")
    albert_blossom_storm = world.get_location("Albert - Blossom Storm Unlock")
    perky_step = world.get_location("Meru - Perky Step Unlock")
    bone_crush = world.get_location("Kongol - Bone Crush Unlock")

    if world.options.enable_addition_randomizer == world.options.enable_addition_randomizer.option_progressive_character:
        set_rule(blazing_dynamo, lambda state: state.has("Dart Progressive Addition", world.player, 6))
        set_rule(lavitz_blossom_storm, lambda state: state.has("Lavitz Progressive Addition", world.player, 4))
        set_rule(demons_dance, lambda state: state.has("Rose Progressive Addition", world.player, 3))
        set_rule(omni_sweep, lambda state: state.has("Haschel Progressive Addition", world.player, 5))
        set_rule(albert_blossom_storm, lambda state: state.has("Albert Progressive Addition", world.player, 4))
        set_rule(perky_step, lambda state: state.has("Meru Progressive Addition", world.player, 4))
        set_rule(bone_crush, lambda state: state.has("Kongol Progressive Addition", world.player, 2))
    else:
        set_rule(
            blazing_dynamo,
            lambda state: (
                state.has_all((
                    "Dart Double Slash",
                    "Dart Volcano",
                    "Dart Burning Rush",
                    "Dart Crush Dance",
                    "Dart Madness Hero",
                    "Dart Moon Strike",
                    ), world.player)
            ),
        )

        set_rule(
            lavitz_blossom_storm,
            lambda state: (
                state.has_all((
                    "Lavitz Harpoon",
                    "Lavitz Spinning Cane",
                    "Lavitz Rod Typhoon",
                    "Lavitz Gust Of Wind Dance",
                ), world.player)
            ),
        )

        set_rule(
            demons_dance,
            lambda state: (
                state.has_all((
                    "Rose Whip Smack",
                    "Rose More More",
                    "Rose Hard Blade",
                ), world.player)
            ),
        )

        set_rule(
            omni_sweep,
            lambda state: (
                state.has_all((
                    "Haschel Double Punch",
                    "Haschel Ferry Of Styx",
                    "Haschel Summon 4 Gods",
                    "Haschel Five Ring Shattering",
                    "Haschel Hex Hammer",
                ), world.player)
            ),
        )

        set_rule(
            albert_blossom_storm,
            lambda state: (
                state.has_all((
                    "Albert Harpoon",
                    "Albert Spinning Cane",
                    "Albert Rod Typhoon",
                    "Albert Gust Of Wind Dance",
                ), world.player)
            ),
        )

        set_rule(
            perky_step,
            lambda state: (
                state.has_all((
                    "Meru Double Smack",
                    "Meru Hammer Spin",
                    "Meru Cool Boogie",
                    "Meru Cats Cradle",
                ), world.player)
            ),
        )

        set_rule(
            bone_crush,
            lambda state: (
                state.has_all((
                    "Kongol Pursuit",
                    "Kongol Inferno",
                ), world.player)
            ),
        )

def set_completion_condition(world: LegendOfDragoonWorld) -> None:
    # set completion conditions
    conditions = world.options.lod_completion_condition

    item = ""
    if conditions.option_fruegel2 == world.options.lod_completion_condition:
        item = "Fruegel 2"

    if conditions.option_doel == world.options.lod_completion_condition:
        item = "Dragoon Doel"

    if conditions.option_lenus2 == world.options.lod_completion_condition:
        item = "Lenus 2"

    if conditions.option_faust == world.options.lod_completion_condition:
        item = "Faust"

    if conditions.option_melbu == world.options.lod_completion_condition:
        item = "Melbu Frahma"

    world.multiworld.completion_condition[world.player] = lambda state: state.has(item, world.player)
