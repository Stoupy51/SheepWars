
#> sheepwars:v2.0.1/load/tick_verification
#
# @within	#minecraft:tick
#

execute if score #sheepwars.major load.status matches 2 if score #sheepwars.minor load.status matches 0 if score #sheepwars.patch load.status matches 1 run function sheepwars:v2.0.1/tick

