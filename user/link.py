
# Imports
from python_datapack.utils.database_helper import *

# Main function is run just before making finalyzing the build process (zip, headers, lang, ...)
def main(config: dict) -> None:
	namespace: str = config["namespace"]
	
	# Add scoreboard objectives
	write_to_load_file(config, f"""
## Scoreboards
# Delete all scoreboards
scoreboard objectives remove {namespace}.data

# Data scoreboard for math and stuff
scoreboard objectives add {namespace}.data dummy

# Previous color reminder
scoreboard objectives add {namespace}.previous_color dummy

# Additional
scoreboard objectives add {namespace}.launched_count dummy

# Team with no collision
team add sheepwars.sheeps
team modify sheepwars.sheeps collisionRule never
""")
	
	# Write tick
	write_to_versioned_file(config, "tick", f"""
# Make disappear vehicle less "chercheur_rider"
execute as @e[type=husk,tag=sheepwars.chercheur_rider,predicate=!sheepwars:has_vehicle] run function sheepwars:sheeps/final/disappear

# Remove levitation effect if no sheep is nearby
execute as @a[gamemode=!spectator,nbt={{active_effects:[{{id:"minecraft:levitation"}}]}}] at @s unless entity @e[tag=sheepwars.sismique,distance=..6] run effect clear @s

# Sheep management
execute as @e[type=sheep,tag=sheepwars.sheep] at @s run function sheepwars:sheeps/tick_sheep

# Intergalactique markers
execute as @e[type=marker,tag=sheepwars.intergalactique_marker] at @s run function sheepwars:sheeps/active/intergalactique/marker_tick

# Magic wools
execute as @e[type=marker,tag=sheepwars.magic_wool] at @s run function sheepwars:magic_wool/tick
""")

	pass

