from typing import Dict

from worlds.legend_of_dragoon.loc.location_data import LegendOfDragoonLocationData

events_table: Dict[str, LegendOfDragoonLocationData] = {
    # TODO more events exist, will add as I find them
    "Defeat Commander in Seles": LegendOfDragoonLocationData("Seles",   108_70001,  "Event"),
}