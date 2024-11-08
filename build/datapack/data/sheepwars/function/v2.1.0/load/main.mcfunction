
#> sheepwars:v2.1.0/load/main
#
# @within	sheepwars:v2.1.0/load/resolve
#

# Avoiding multiple executions of the same load function
execute unless score #sheepwars.loaded load.status matches 1 run function sheepwars:v2.1.0/load/secondary

