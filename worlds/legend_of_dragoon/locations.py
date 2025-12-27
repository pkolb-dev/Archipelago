from typing import Dict, Set

from worlds.legend_of_dragoon.loc.additions import addition_table
from worlds.legend_of_dragoon.loc.chests import chests_table
from worlds.legend_of_dragoon.loc.events import events_table
from worlds.legend_of_dragoon.loc.location_data import LegendOfDragoonLocationData
from worlds.legend_of_dragoon.loc.shops import shop_table

def get_locations_by_type(location_type: str) -> Dict[str, LegendOfDragoonLocationData]:
    return {name: data for name, data in location_table.items() if data.category == location_type}

location_table: Dict[str, LegendOfDragoonLocationData] = {
    **shop_table,
    **addition_table,
    **chests_table,
    **events_table,
}

#Make location categories
location_name_groups: Dict[str, Set[str]] = {}
for location in location_table.keys():
    category = location_table[location].category
    if category not in location_name_groups.keys():
        location_name_groups[category] = set()
    location_name_groups[category].add(location)

