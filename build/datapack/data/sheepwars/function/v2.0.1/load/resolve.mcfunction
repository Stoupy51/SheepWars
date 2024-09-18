
#> sheepwars:v2.0.1/load/resolve
#
# @within	#sheepwars:resolve
#

# If correct version, load the datapack
execute if score #sheepwars.major load.status matches 2 if score #sheepwars.minor load.status matches 0 if score #sheepwars.patch load.status matches 1 run function sheepwars:v2.0.1/load/main

