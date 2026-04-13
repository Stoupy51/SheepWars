
#> sheepwars:v2.4.0/load/check_dependencies
#
# @within	sheepwars:v2.4.0/load/secondary
#

## Check if SheepWars is loadable (dependencies)
scoreboard players set #dependency_error sheepwars.data 0
execute if score #dependency_error sheepwars.data matches 0 unless score #realistic_explosion.major load.status matches 1.. run scoreboard players set #dependency_error sheepwars.data 1
execute if score #dependency_error sheepwars.data matches 0 if score #realistic_explosion.major load.status matches 1 unless score #realistic_explosion.minor load.status matches 2.. run scoreboard players set #dependency_error sheepwars.data 1

