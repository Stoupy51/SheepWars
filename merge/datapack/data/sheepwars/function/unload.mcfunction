
#> sheepwars:unload
#
# @executed			unknown context
#
# @description		Function that unload everything from the SheepWars datapack
#

# Delete all scoreboards
scoreboard objectives remove sheepwars.data
scoreboard objectives remove sheepwars.right_click
scoreboard objectives remove sheepwars.previous_color
scoreboard objectives remove sheepwars.launched_count

# Delete storage
data remove storage sheepwars:main all
data remove storage sheepwars:items all

#define storage sheepwars:main
#define storage sheepwars:items


