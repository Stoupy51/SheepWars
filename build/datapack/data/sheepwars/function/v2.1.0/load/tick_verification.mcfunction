
#> sheepwars:v2.1.0/load/tick_verification
#
# @within	#minecraft:tick
#

execute if score #sheepwars.major load.status matches 2 if score #sheepwars.minor load.status matches 1 if score #sheepwars.patch load.status matches 0 run function sheepwars:v2.1.0/tick

