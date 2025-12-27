from ..generic.Rules import set_rule, add_rule
from ..AutoWorld import World

def lod_set_rule(lod_world: World, location: str, rule):
    player = lod_world.player

    locations = lod_world.created_multi_locations.get(location)
    if locations is None:
        try:
            locations = [lod_world.multiworld.get_location(location, player)]
        except KeyError:
            return

    for location in locations:
        set_rule(location, rule)

def set_rules(lod_world: World):
    player = lod_world.player
    multiworld = lod_world.multiworld
    options = lod_world.options

    multiworld.completion_condition[player] = lambda state: state.has("Defeat Commander in Seles", player)
