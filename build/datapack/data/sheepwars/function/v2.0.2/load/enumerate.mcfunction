
#> sheepwars:v2.0.2/load/enumerate
#
# @within	#sheepwars:enumerate
#

# If current major is too low, set it to the current major
execute unless score #sheepwars.major load.status matches 2.. run scoreboard players set #sheepwars.major load.status 2

# If current minor is too low, set it to the current minor (only if major is correct)
execute if score #sheepwars.major load.status matches 2 unless score #sheepwars.minor load.status matches 0.. run scoreboard players set #sheepwars.minor load.status 0

# If current patch is too low, set it to the current patch (only if major and minor are correct)
execute if score #sheepwars.major load.status matches 2 if score #sheepwars.minor load.status matches 0 unless score #sheepwars.patch load.status matches 2.. run scoreboard players set #sheepwars.patch load.status 2

