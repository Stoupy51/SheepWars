
#> sheepwars:sheeps/final/disappear
#
# @executed	at @s
#
# @within	sheepwars:sheeps/active/intergalactique/marker_tick [ at @s ]
#			sheepwars:sheeps/final_action
#			sheepwars:v2.3.3/tick [ as @e[type=husk,tag=sheepwars.chercheur_rider,predicate=!sheepwars:has_vehicle] ]
#
# @description		Remove the sheep from the game.
#

# Unride any rider
execute on passengers run ride @s[type=player] dismount

# Remove the sheep
tp @s 0 -10000 0
kill @s

