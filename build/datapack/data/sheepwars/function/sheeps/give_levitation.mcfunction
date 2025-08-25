
#> sheepwars:sheeps/give_levitation
#
# @executed	as @a[gamemode=!spectator,distance=..6] & at @s
#
# @within	sheepwars:sheeps/passive_action [ as @a[gamemode=!spectator,distance=..6] & at @s ]
#

# Give levitation
effect give @s levitation 1 8 true

# Add the launched tag
tag @s add sheepwars.launched_in_air

