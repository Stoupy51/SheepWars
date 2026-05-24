
#> sheepwars:v2.4.1/load/valid_dependencies
#
# @within	sheepwars:v2.4.1/load/secondary
#			sheepwars:v2.4.1/load/valid_dependencies 1t replace [ scheduled ]
#

# Waiting for a player to get the game version, but stop function if no player found
execute unless entity @p run return run schedule function sheepwars:v2.4.1/load/valid_dependencies 1t replace
execute store result score #game_version sheepwars.data run data get entity @p DataVersion

# Check if the game version is supported
scoreboard players set #mcload_error sheepwars.data 0
execute unless score #game_version sheepwars.data matches 4786.. run scoreboard players set #mcload_error sheepwars.data 1

# Decode errors
execute if score #mcload_error sheepwars.data matches 1 run tellraw @a {"text":"SheepWars Error: This version is made for Minecraft 26.1+.","color":"red"}
execute if score #dependency_error sheepwars.data matches 1 run tellraw @a {"text":"SheepWars Error: Libraries are missing\nplease download the right SheepWars datapack\nor download each of these libraries one by one:","color":"red"}
execute if score #dependency_error sheepwars.data matches 1 unless score #realistic_explosion.major load.status matches 1.. run tellraw @a {"text":"- [RealisticExplosion (v1.2.1+)]","color":"gold","click_event":{"action":"open_url","url":"https://github.com/Stoupy51/RealisticExplosion"}}
execute if score #dependency_error sheepwars.data matches 1 if score #realistic_explosion.major load.status matches 1 unless score #realistic_explosion.minor load.status matches 2.. run tellraw @a {"text":"- [RealisticExplosion (v1.2.1+)]","color":"gold","click_event":{"action":"open_url","url":"https://github.com/Stoupy51/RealisticExplosion"}}
execute if score #dependency_error sheepwars.data matches 1 if score #realistic_explosion.major load.status matches 1 if score #realistic_explosion.minor load.status matches 2 unless score #realistic_explosion.patch load.status matches 1.. run tellraw @a {"text":"- [RealisticExplosion (v1.2.1+)]","color":"gold","click_event":{"action":"open_url","url":"https://github.com/Stoupy51/RealisticExplosion"}}

# Load SheepWars
execute if score #game_version sheepwars.data matches 1.. if score #mcload_error sheepwars.data matches 0 if score #dependency_error sheepwars.data matches 0 run function sheepwars:v2.4.1/load/confirm_load

