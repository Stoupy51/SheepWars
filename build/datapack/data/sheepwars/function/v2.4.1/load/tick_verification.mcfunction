
#> sheepwars:v2.4.1/load/tick_verification
#
# @within	#minecraft:tick
#

execute if score #sheepwars.major load.status matches 2 if score #sheepwars.minor load.status matches 4 if score #sheepwars.patch load.status matches 1 run function sheepwars:v2.4.1/tick

