from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.rules import Has, HasAll
from .options import CompletionCondition, AdditionRandomization
from .regions import visualize_world

if TYPE_CHECKING:
    from .world import LegendOfDragoonWorld


def setup_chapter_one(world):
    set_chapter_one_entrance_rules(world)
    set_chapter_one_rules(world)


def setup_chapter_two(world):
    if world.options.lod_completion_condition == CompletionCondition.option_chapter_1:
        return
    set_chapter_two_entrance_rules(world)
    set_chapter_two_rules(world)


def setup_chapter_three(world):
    goal = world.options.lod_completion_condition
    if goal == CompletionCondition.option_chapter_1 or goal == CompletionCondition.option_chapter_2:
        return

    set_chapter_three_entrance_rules(world)
    set_chapter_three_rules(world)


def setup_chapter_four(world):
    goal = world.options.lod_completion_condition
    if goal != CompletionCondition.option_chapter_4:
        return

    set_chapter_four_entrance_rules(world)
    set_chapter_four_rules(world)


def set_all_rules(world: LegendOfDragoonWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)

    setup_chapter_one(world)
    setup_chapter_two(world)
    setup_chapter_three(world)
    setup_chapter_four(world)

    # for debugging purposes:
    # visualize_world(world)


def set_chapter_one_entrance_rules(world):
    seles_to_forest = world.get_entrance("Seles to Forest")
    world.set_rule(seles_to_forest, Has("Commander"))

    forest_to_prairie = world.get_entrance("Forest to Prairie")
    world.set_rule(forest_to_prairie, HasAll("Prison Key", "Fruegel 1"))

    hellena_prison_01_to_forest = world.get_entrance("Hellena Prison 01 to Forest")
    world.set_rule(hellena_prison_01_to_forest, HasAll("Prison Key", "Fruegel 1"))

    hellena_prison_01_to_02 = world.get_entrance("Hellena Prison 01 to 02")
    world.set_rule(hellena_prison_01_to_02, Has("Lloyd 1"))

    prairie_to_limestone_cave = world.get_entrance("Prairie to Limestone Cave")
    world.set_rule(prairie_to_limestone_cave, Has("Axe from the Shack"))

    limestone_cave_to_bale = world.get_entrance("Limestone Cave to Bale")
    world.set_rule(limestone_cave_to_bale, Has("Urobolus"))

    dragons_nest_to_shrine_of_shirley = world.get_entrance("Dragon's Nest to Shrine of Shirley")
    world.set_rule(dragons_nest_to_shrine_of_shirley,
                   HasAll("Life Water", "Water Bottle"))

    forest_to_kazas = world.get_entrance("Forest to Kazas")
    world.set_rule(forest_to_kazas, Has("Fruegel 2"))


def set_chapter_two_entrance_rules(world):
    black_castle_throne_room_to_fletz = world.get_entrance("Black Castle Throne Room to Fletz")
    world.set_rule(black_castle_throne_room_to_fletz, Has("Dragoon Doel"))

    barrens_to_valley = world.get_entrance("Barrens to Valley of Corrupted Gravity")
    world.set_rule(barrens_to_valley, HasAll("Pass for Valley", "Letter from Lynn"))

    valley_to_home_of_giganto = world.get_entrance("Valley of Corrupted Gravity to Home of Giganto")
    world.set_rule(valley_to_home_of_giganto, Has("Valley Virage"))

    donau_to_queen_fury = world.get_entrance("Donau to Queen Fury")
    world.set_rule(donau_to_queen_fury, Has("Gehrich"))

    phantom_ship_to_lidiera = world.get_entrance("Phantom Ship to Lidiera")
    world.set_rule(phantom_ship_to_lidiera, Has("Key to Ship"))


def set_chapter_three_entrance_rules(world):
    queen_fury_to_furni = world.get_entrance("Queen Fury to Furni")
    world.set_rule(queen_fury_to_furni, HasAll("Boat License", "Lenus 2"))

    evergreen_forest_to_wingly_forest = world.get_entrance("Evergreen Forest to Wingly Forest")
    world.set_rule(evergreen_forest_to_wingly_forest, Has("Talk to Ute"))

    wingly_forest_to_deningrad = world.get_entrance("Wingly Forest to Deningrad")
    world.set_rule(wingly_forest_to_deningrad, Has("Dragon Blocker"))

    evergreen_forest_to_mortal_dragon_mountain = world.get_entrance("Evergreen Forest to Mortal Dragon Mountain")
    world.set_rule(evergreen_forest_to_mortal_dragon_mountain, Has("Grand Jewel"))

    deningrad_to_kashua_glacier = world.get_entrance("Deningrad to Kashua Glacier")
    world.set_rule(deningrad_to_kashua_glacier, Has("Divine Dragon"))

    kashua_glacier_to_flanvel_tower = world.get_entrance("Kashua Glacier to Tower of Flanvel")
    world.set_rule(kashua_glacier_to_flanvel_tower, Has("Windigo"))

    kashua_glacier_to_snowfield = world.get_entrance("Kashua Glacier to Snowfield")
    world.set_rule(kashua_glacier_to_snowfield, Has("Lloyd 2"))


def set_chapter_four_entrance_rules(world):
    vellweb_to_death_frontier = world.get_entrance("Vellweb to Death Frontier")
    world.set_rule(vellweb_to_death_frontier, Has("Lloyd 2"))

    ulara_to_home_of_giganto = world.get_entrance("Ulara to Home of Giganto")
    home_of_giganto_to_ulara = world.get_entrance("Home of Giganto to Ulara")
    world.set_rule(ulara_to_home_of_giganto, Has("Ulara Teleporter"))
    world.set_rule(home_of_giganto_to_ulara, Has("Ulara Teleporter"))

    queen_fury_to_rouge = world.get_entrance("Queen Fury to Rouge")
    world.set_rule(queen_fury_to_rouge, Has("Ulara Teleporter"))

    aglis_to_zenebatos = world.get_entrance("Aglis to Zenebatos")
    world.set_rule(aglis_to_zenebatos, Has("Kraken"))

    zenebatos_to_mayfil = world.get_entrance("Zenebatos to Mayfil")
    world.set_rule(zenebatos_to_mayfil, HasAll("Law Making License", "Law Launching License"))

    mayfil_to_divine_tree = world.get_entrance("Mayfil to Divine Tree")
    world.set_rule(mayfil_to_divine_tree, Has("Zackwell"))

    divine_tree_to_moon_that_never_sets = world.get_entrance("Divine Tree to Moon That Never Sets")
    world.set_rule(divine_tree_to_moon_that_never_sets, Has("Imago"))


def set_addition_entrance_rules(world) -> None:
    dart_additions = world.get_entrance("Menu to Dart Additions")
    lavitz_additions = world.get_entrance("Menu to Lavitz Additions")
    rose_additions = world.get_entrance("Menu to Rose Additions")
    haschel_additions = world.get_entrance("Menu to Haschel Additions")
    albert_additions = world.get_entrance("Menu to Albert Additions")

    # world.set_rule(dart_additions, Has("Commander"))
    world.set_rule(lavitz_additions, Has("Prison Key"))
    world.set_rule(rose_additions, Has("Kongol 1"))
    world.set_rule(haschel_additions, Has("Lloyd 1"))
    world.set_rule(albert_additions, Has("Fruegel 2"))

    if world.options.lod_completion_condition != CompletionCondition.option_chapter_1:
        meru_additions = world.get_entrance("Menu to Meru Additions")
        kongol_additions = world.get_entrance("Menu to Kongol Additions")
        world.set_rule(meru_additions, HasAll("Mappi Steals Orb", "Letter from Lynn"))
        world.set_rule(kongol_additions, Has("Gehrich"))


def set_spell_entrance_rules(world: LegendOfDragoonWorld) -> None:
    dart_spells = world.get_entrance("Menu to Dart Spells")
    lavitz_spells = world.get_entrance("Menu to Lavitz Spells")
    shana_spells = world.get_entrance("Menu to Shana Spells")
    rose_spells = world.get_entrance("Menu to Rose Spells")
    haschel_spells = world.get_entrance("Menu to Haschel Spells")
    albert_spells = world.get_entrance("Menu to Albert Spells")

    world.set_rule(dart_spells, HasAll("Red Dragoon Spirit"))
    world.set_rule(lavitz_spells, HasAll("Prison Key", "Jade Dragoon Spirit"))
    world.set_rule(shana_spells, HasAll("Prison Key", "Silver Dragoon Spirit"))
    world.set_rule(rose_spells, HasAll("Kongol 1", "Dark Dragoon Spirit"))
    world.set_rule(haschel_spells, HasAll("Lloyd 1", "Violet Dragoon Spirit"))
    world.set_rule(albert_spells, HasAll("Fruegel 2", "Jade Dragoon Spirit"))

    if world.options.lod_completion_condition == CompletionCondition.option_chapter_1:
        return

    meru_spells = world.get_entrance("Menu to Meru Spells")
    kongol_spells = world.get_entrance("Menu to Kongol Spells")

    world.set_rule(meru_spells, HasAll("Mappi Steals Orb", "Letter from Lynn", "Blue Dragoon Spirit"))
    world.set_rule(kongol_spells, HasAll("Gehrich", "Gold Dragoon Spirit"))

    if world.options.lod_completion_condition == CompletionCondition.option_chapter_2:
        return

    miranda_spells = world.get_entrance("Menu to Miranda Spells")
    world.set_rule(miranda_spells, HasAll("Talk to Ute", "Silver Dragoon Spirit"))


def set_all_entrance_rules(world: LegendOfDragoonWorld) -> None:
    set_addition_entrance_rules(world)
    set_spell_entrance_rules(world)


def set_chapter_one_rules(world):
    fruegel_1 = world.get_location("Fruegel 1")
    fruegel_1_event = world.get_location("Defeat Fruegel 1")
    world.set_rule(fruegel_1, Has("Prison Key"))
    world.set_rule(fruegel_1_event, Has("Prison Key"))

    urobolus_event = world.get_location("Defeat Urobolus")
    world.set_rule(urobolus_event, Has("Fruegel 1"))

    gorgaga = world.get_location("Gorgaga")
    serfius = world.get_location("Serfius")
    atlow = world.get_location("Atlow")
    danton = world.get_location("Danton")
    lloyd_1 = world.get_location("Lloyd 1")
    world.set_rule(gorgaga, Has("Shirley"))
    world.set_rule(serfius, Has("Shirley"))
    world.set_rule(atlow, Has("Shirley"))
    world.set_rule(danton, Has("Shirley"))
    world.set_rule(lloyd_1, Has("Shirley"))

    lloyd_1_event = world.get_location("Lose to Lloyd")
    world.set_rule(lloyd_1_event, Has("Shirley"))

    kongol_2 = world.get_location("Kongol 2")
    kongol_2_event = world.get_location("Defeat Kongol 2")
    world.set_rule(kongol_2,
                   HasAll("Red Stone", "Blue Stone", "Yellow Stone"))
    world.set_rule(kongol_2_event,
                   HasAll("Red Stone", "Blue Stone", "Yellow Stone"))

    doel_event = world.get_location("Defeat Dragoon Doel")
    doel = world.get_location("Dragoon Doel")
    world.set_rule(doel, Has("Kongol 2"))
    world.set_rule(doel_event, Has("Kongol 2"))


def set_chapter_two_rules(world):
    goal = world.options.lod_completion_condition
    if goal == CompletionCondition.option_chapter_1:
        return

    mappi_steals_orb = world.get_location("Mappi Steals Orb")
    world.set_rule(mappi_steals_orb, Has("Red Dragoon Spirit"))

    ghost_commander = world.get_location("Ghost Commander")
    world.set_rule(ghost_commander, Has("Key to Ship"))


def set_chapter_three_rules(world):
    goal = world.options.lod_completion_condition
    if goal == CompletionCondition.option_chapter_1 or goal == CompletionCondition.option_chapter_2:
        return


def set_chapter_four_rules(world):
    goal = world.options.lod_completion_condition
    if goal != CompletionCondition.option_chapter_4:
        return

    kubila = world.get_location("Defeat Kubila")
    selebus = world.get_location("Defeat Selebus")
    vector = world.get_location("Defeat Vector")

    world.set_rule(kubila, HasAll("Law Making License", "Law Launching License"))
    world.set_rule(selebus, HasAll("Law Making License", "Law Launching License"))
    world.set_rule(vector, HasAll("Law Making License", "Law Launching License"))


def set_all_location_rules(world: LegendOfDragoonWorld) -> None:
    set_addition_unlock_rules(world)


def set_completion_condition(world: LegendOfDragoonWorld) -> None:
    # set completion conditions
    conditions = world.options.lod_completion_condition

    item = ""
    if conditions.option_chapter_1 == world.options.lod_completion_condition:
        item = "Dragoon Doel"

    if conditions.option_chapter_2 == world.options.lod_completion_condition:
        item = "Lenus 2"

    if conditions.option_chapter_3 == world.options.lod_completion_condition:
        item = "Lloyd 2"

    if conditions.option_chapter_4 == world.options.lod_completion_condition:
        item = "Melbu Frahma"

    world.set_completion_rule(Has(item))


def set_chapter_one_addition_unlock_rules(world):
    dart_burning_rush = world.get_location("Dart - Burning Rush Unlock")
    dart_crush_dance = world.get_location("Dart - Crush Dance Unlock")

    rose_more_more = world.get_location("Rose - More and More Unlock")
    lavitz_spinning_cane = world.get_location("Lavitz - Spinning Cane Unlock")
    lavitz_rod_typhoon = world.get_location("Lavitz - Rod Typhoon Unlock")
    lavitz_gust_of_wind_dance = world.get_location("Lavitz - Gust Of Wind Dance Unlock")
    lavitz_blossom_storm = world.get_location("Lavitz - Flower Storm Unlock")
    albert_spinning_cane = world.get_location("Albert - Spinning Cane Unlock")
    albert_rod_typhoon = world.get_location("Albert - Rod Typhoon Unlock")
    albert_gust_of_wind_dance = world.get_location("Albert - Gust Of Wind Dance Unlock")
    albert_blossom_storm = world.get_location("Albert - Flower Storm Unlock")
    haschel_flurry_of_styx = world.get_location("Haschel - Flurry of Styx Unlock")

    world.set_rule(dart_burning_rush, Has("Kongol 1"))
    world.set_rule(dart_crush_dance, Has("Dragoon Doel"))
    world.set_rule(rose_more_more, Has("Dragoon Doel"))
    world.set_rule(lavitz_spinning_cane, Has("Axe from the Shack"))
    world.set_rule(lavitz_rod_typhoon, Has("Kongol 1"))
    world.set_rule(lavitz_gust_of_wind_dance, Has("Shirley"))
    world.set_rule(albert_spinning_cane, Has("Axe from the Shack"))
    world.set_rule(albert_rod_typhoon, Has("Kongol 1"))
    world.set_rule(albert_gust_of_wind_dance, Has("Shirley"))
    world.set_rule(haschel_flurry_of_styx, Has("Dragoon Doel"))

    if world.options.addition_randomizer == world.options.addition_randomizer.option_progressive_character:
        world.set_rule(lavitz_blossom_storm, Has("Lavitz Progressive Addition", 4))
        world.set_rule(albert_blossom_storm, Has("Albert Progressive Addition", 4))
    elif world.options.addition_randomizer == world.options.addition_randomizer.option_addition_sanity:
        world.set_rule(
            lavitz_blossom_storm,
            HasAll(
                "Lavitz Harpoon",
                "Lavitz Spinning Cane",
                "Lavitz Rod Typhoon",
                "Lavitz Gust Of Wind Dance",
            )
        )
        world.set_rule(
            albert_blossom_storm,
            HasAll(
                "Albert Harpoon",
                "Albert Spinning Cane",
                "Albert Rod Typhoon",
                "Albert Gust Of Wind Dance",
            )
        )


def set_chapter_two_addition_unlock_rules(world):
    if world.options.lod_completion_condition == CompletionCondition.option_chapter_1:
        return

    rose_hard_blade = world.get_location("Rose - Hard Blade Unlock")
    haschel_summon_4_gods = world.get_location("Haschel - Summon 4 Gods Unlock")
    meru_hammer_spin = world.get_location("Meru - Hammer Spin Unlock")
    demons_dance = world.get_location("Rose - Demon's Dance Unlock")

    world.set_rule(rose_hard_blade, Has("Gehrich and Mappi"))
    world.set_rule(haschel_summon_4_gods, Has("Gehrich"))
    world.set_rule(meru_hammer_spin, Has("Lenus 2"))

    if world.options.addition_randomizer == world.options.addition_randomizer.option_progressive_character:
        world.set_rule(demons_dance, Has("Rose Progressive Addition", 3))
    elif world.options.addition_randomizer == world.options.addition_randomizer.option_addition_sanity:
        world.set_rule(
            demons_dance,
            HasAll(
                "Rose Whip Smack",
                "Rose More More",
                "Rose Hard Blade",
            )
        )


def set_chapter_three_addition_unlock_rules(world):
    goal = world.options.lod_completion_condition
    if goal == CompletionCondition.option_chapter_1 or goal == CompletionCondition.option_chapter_2:
        return

    dart_madness_hero = world.get_location("Dart - Madness Hero Unlock")
    haschel_5_ring_shattering = world.get_location("Haschel - 5-Ring Shattering Unlock")
    haschel_hex_hammer = world.get_location("Haschel - Hex Hammer Unlock")
    omni_sweep = world.get_location("Haschel - Omni-Sweep Unlock")
    meru_cool_boogie = world.get_location("Meru - Cool Boogie Unlock")
    kongol_inferno = world.get_location("Kongol - Inferno Unlock")
    bone_crush = world.get_location("Kongol - Bone Crush Unlock")

    world.set_rule(dart_madness_hero, Has("Kamuy"))
    world.set_rule(haschel_5_ring_shattering, Has("Kamuy"))
    world.set_rule(haschel_hex_hammer, Has("Polter"))
    world.set_rule(meru_cool_boogie, Has("Polter"))

    world.set_rule(kongol_inferno, Has("Divine Dragon"))

    if world.options.addition_randomizer == world.options.addition_randomizer.option_progressive_character:
        world.set_rule(omni_sweep, Has("Haschel Progressive Addition", 5))
        world.set_rule(bone_crush, Has("Kongol Progressive Addition", 2))
    elif world.options.addition_randomizer == world.options.addition_randomizer.option_addition_sanity:
        world.set_rule(
            omni_sweep,
            HasAll(
                "Haschel Double Punch",
                "Haschel Ferry Of Styx",
                "Haschel Summon 4 Gods",
                "Haschel Five Ring Shattering",
                "Haschel Hex Hammer",
            )
        )

        world.set_rule(
            bone_crush,
            HasAll(
                "Kongol Pursuit",
                "Kongol Inferno",
            )
        )


def set_chapter_four_addition_unlock_rules(world):
    if world.options.lod_completion_condition != CompletionCondition.option_chapter_4:
        return

    dart_moon_strike = world.get_location("Dart - Moon Strike Unlock")
    blazing_dynamo = world.get_location("Dart - Blazing Dynamo Unlock")
    meru_cats_cradle = world.get_location("Meru - Cat's Cradle Unlock")
    perky_step = world.get_location("Meru - Perky Step Unlock")

    world.set_rule(dart_moon_strike, Has("Lloyd 2"))
    world.set_rule(meru_cats_cradle, Has("Kraken"))

    if world.options.addition_randomizer == AdditionRandomization.option_progressive_character:
        world.set_rule(blazing_dynamo, Has("Dart Progressive Addition", 6))
        world.set_rule(perky_step, Has("Meru Progressive Addition", 4))
    elif world.options.addition_randomizer == world.options.addition_randomizer.option_addition_sanity:
        world.set_rule(blazing_dynamo,
                       HasAll("Dart Double Slash", "Dart Volcano", "Dart Burning Rush", "Dart Crush Dance",
                              "Dart Madness Hero", "Dart Moon Strike"))

        world.set_rule(perky_step,
                       HasAll("Meru Double Smack", "Meru Hammer Spin", "Meru Cool Boogie", "Meru Cats Cradle"))


def set_addition_unlock_rules(world: LegendOfDragoonWorld) -> None:
    set_chapter_one_addition_unlock_rules(world)
    set_chapter_two_addition_unlock_rules(world)
    set_chapter_three_addition_unlock_rules(world)
    set_chapter_four_addition_unlock_rules(world)
