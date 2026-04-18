
#> sheepwars:v2.4.0/unload
#
# @within	#sheepwars:unload
#

# Clear custom items
clear @a *[custom_data~{"sheepwars":{}}]

# Kill entities with custom tags
execute as @e[tag=sheepwars.explode] at @s run function sheepwars:v2.4.0/unload/safe_kill
execute as @e[tag=sheepwars.fragmentation_part] at @s run function sheepwars:v2.4.0/unload/safe_kill
execute as @e[tag=sheepwars.new] at @s run function sheepwars:v2.4.0/unload/safe_kill
execute as @e[tag=sheepwars.sheep] at @s run function sheepwars:v2.4.0/unload/safe_kill

# Remove scoreboard objectives
scoreboard objectives remove load.status
scoreboard objectives remove sheepwars.cooldown
scoreboard objectives remove sheepwars.data
scoreboard objectives remove sheepwars.launched_count
scoreboard objectives remove sheepwars.previous_color

# Clear storages
data remove storage sheepwars:items all
data remove storage sheepwars:main Copy
data remove storage sheepwars:main Items
data remove storage sheepwars:main Motion
data remove storage sheepwars:main Rotation
data remove storage sheepwars:main UUID

