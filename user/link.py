
# Imports
from python_datapack.utils.database_helper import *

# Main function is run just before making finalyzing the build process (zip, headers, lang, ...)
def main(config: dict) -> None:
	ns: str = config["namespace"]
	
	# Add scoreboard objectives
	write_to_load_file(config, f"""
## Scoreboards
# Delete all scoreboards
scoreboard objectives remove {ns}.data

# Data scoreboard for math and stuff
scoreboard objectives add {ns}.data dummy

# Previous color reminder
scoreboard objectives add {ns}.previous_color dummy

# Additional
scoreboard objectives add {ns}.launched_count dummy

# Team with no collision
team add {ns}.sheeps
team modify {ns}.sheeps collisionRule never
""")
	
	# Write tick
	write_to_versioned_function(config, "tick", f"""
# Make disappear vehicle less "chercheur_rider"
execute as @e[type=husk,tag={ns}.chercheur_rider,predicate=!{ns}:has_vehicle] run function {ns}:sheeps/final/disappear

# Remove levitation effect if no sheep is nearby and has been launched up
execute as @a[tag={ns}.launched_in_air,nbt={{active_effects:[{{id:"minecraft:levitation"}}]}}] at @s unless entity @e[tag={ns}.sismique,distance=..6] run function {ns}:sheeps/final/remove_levitation

# Sheep management
execute as @e[type=sheep,tag={ns}.sheep] at @s run function {ns}:sheeps/tick_sheep

# Intergalactique markers
execute as @e[type=marker,tag={ns}.intergalactique_marker] at @s run function {ns}:sheeps/active/intergalactique/marker_tick

# Magic wools
execute as @e[type=marker,tag={ns}.magic_wool] at @s run function {ns}:magic_wool/tick
""")
	
	# Write remove levitation function
	write_to_function(config, f"{ns}:sheeps/final/remove_levitation", f"""
# Remove levitation effect
effect clear @s levitation

# Remove tag
tag @s remove {ns}.launched_in_air
""")

	pass

