
#> sheepwars:v2.4.0/load/confirm_load
#
# @within	sheepwars:v2.4.0/load/valid_dependencies
#

# Confirm load
tellraw @a[tag=convention.debug] {"text":"[Loaded SheepWars v2.4.0]","color":"green"}
scoreboard players set #sheepwars.loaded load.status 1
function sheepwars:v2.4.0/load/set_items_storage

## Scoreboards
# Data scoreboard for math and stuff
scoreboard objectives add sheepwars.data dummy
scoreboard objectives add sheepwars.cooldown dummy

# Previous color reminder
scoreboard objectives add sheepwars.previous_color dummy

# Additional
scoreboard objectives add sheepwars.launched_count dummy

# Team with no collision
team add sheepwars.sheeps
team modify sheepwars.sheeps collisionRule never

