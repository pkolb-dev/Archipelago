from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from worlds.generic.Rules import add_rule, set_rule

if TYPE_CHECKING:
    from .world import LegendOfDragoonWorld

def set_all_rules(world: LegendOfDragoonWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)


def set_all_entrance_rules(world: LegendOfDragoonWorld) -> None:

    lohan_to_shrine_of_shirley = world.get_entrance("Lohan to Shrine of Shirley")
    set_rule(lohan_to_shrine_of_shirley, lambda state: state.has("Life Water", world.player))

def set_all_location_rules(world: LegendOfDragoonWorld) -> None:
    pass

def set_completion_condition(world: LegendOfDragoonWorld) -> None:
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)
