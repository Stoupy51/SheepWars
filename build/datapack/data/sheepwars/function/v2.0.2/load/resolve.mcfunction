
#> sheepwars:v2.0.2/load/resolve
#
# @within	#sheepwars:resolve
#

# If correct version, load the datapack
execute if score #sheepwars.major load.status matches 2 if score #sheepwars.minor load.status matches 0 if score #sheepwars.patch load.status matches 2 run function sheepwars:v2.0.2/load/main
