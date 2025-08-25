
#> sheepwars:v2.3.4/load/tick_verification
#
# @within	#minecraft:tick
#

execute if score #sheepwars.major load.status matches 2 if score #sheepwars.minor load.status matches 3 if score #sheepwars.patch load.status matches 4 run function sheepwars:v2.3.4/tick

