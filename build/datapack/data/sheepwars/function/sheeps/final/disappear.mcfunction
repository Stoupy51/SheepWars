
#> sheepwars:sheeps/final/disappear
#
# @executed	as @e[type=sheep,tag=sheepwars.sheep] & at @s
#
# @within	sheepwars:sheeps/final_action
#			sheepwars:sheeps/active/intergalactique/marker_tick [ at @s ]
#			sheepwars:v2.4.1/tick [ as @e[type=husk,tag=sheepwars.chercheur_rider,predicate=!sheepwars:has_vehicle] ]
#
# @description		Remove the sheep from the game.
#

# Unride any rider
execute on passengers run ride @s[type=player] dismount

# Remove the sheep
tp @s 0 -10000 0
kill @s

