
#> sheepwars:magic_wool/arrow
#
# @executed	as @e[type=arrow,distance=..1.69,sort=nearest]
#
# @within	sheepwars:magic_wool/tick [ as @e[type=arrow,distance=..1.69,sort=nearest] ]
#
# @description		Launches a signal (function tag) on the arrow owner (origin) and kill the arrow
#

# Launch a signal on the arrow owner
execute on origin run function #sheepwars:signals/magic_wool_shot

# Kill the arrow
scoreboard players set #success sheepwars.data 1
kill @s

