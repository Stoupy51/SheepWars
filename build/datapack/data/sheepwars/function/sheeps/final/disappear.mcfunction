
#> sheepwars:sheeps/final/disappear
#
# @executed	as @e[type=sheep,tag=sheepwars.sheep] & at @s
#
# @within	sheepwars:sheeps/final_action
#			sheepwars:sheeps/active/intergalactique/marker_tick [ at @s ]
#			sheepwars:v2.4.2/tick [ as @e[type=husk,tag=sheepwars.chercheur_rider,predicate=!sheepwars:has_vehicle] ]
#
# @description		Remove the sheep from the game.
#

# Unride any rider, keeping it safe from the fall it did not choose
execute on passengers run effect give @s[type=player] slow_falling 10 0 true
execute on passengers run ride @s[type=player] dismount

# Remove the sheep
tp @s 0 -10000 0
kill @s

