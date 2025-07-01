
#> sheepwars:sheeps/final/disappear
#
# @within	sheepwars:sheeps/active/intergalactique/marker_tick
#			sheepwars:sheeps/final_action
#			sheepwars:v2.3.2/tick
#
# @executed			as & at the sheep
# 
# @description		Remove the sheep from the game.
#

# Unride any rider
execute on passengers run ride @s[type=player] dismount

# Remove the sheep
tp @s 0 -10000 0
kill @s

