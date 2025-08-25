
#> sheepwars:magic_wool/arrow
#
# @executed	as @e[type=arrow,nbt={inBlockState:{}},distance=..1.69,limit=1]
#
# @within	sheepwars:magic_wool/tick [ as @e[type=arrow,nbt={inBlockState:{}},distance=..1.69,limit=1] ]
#
# @description		Launches a signal (function tag) on the arrow owner (origin) and kill the arrow
#

# Launch a signal on the arrow owner
execute on origin run function #sheepwars:signals/magic_wool_shot

# Kill the arrow
scoreboard players set #success sheepwars.data 1
kill @s

