
#> sheepwars:v2.4.0/unload/safe_kill
#
# @executed	as @e[tag=sheepwars.explode] & at @s
#
# @within	sheepwars:v2.4.0/unload [ as @e[tag=sheepwars.explode] & at @s ]
#			sheepwars:v2.4.0/unload [ as @e[tag=sheepwars.fragmentation_part] & at @s ]
#			sheepwars:v2.4.0/unload [ as @e[tag=sheepwars.new] & at @s ]
#			sheepwars:v2.4.0/unload [ as @e[tag=sheepwars.sheep] & at @s ]
#

# This function is used to safely kill entities by teleporting them to the void before killing them to prevent item drops
tp @s ~ -10000 ~
kill @s

