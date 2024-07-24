
# Loot insert
setblock 0 0 0 air
setblock 0 0 0 yellow_shulker_box
loot insert 0 0 0 loot sheepwars:basic_drop
execute if score #number_of_drops sheepwars.data matches 2.. run loot insert 0 0 0 loot sheepwars:basic_drop
execute if score #number_of_drops sheepwars.data matches 3.. run loot insert 0 0 0 loot sheepwars:basic_drop

## Sheep count
# Preparation of the storages
data modify storage sheepwars:main Items set from block 0 0 0 Items

# Get the number of each sheep (starting from the end)
execute store result score #c_intergalactique sheepwars.data run data get storage sheepwars:main Items[{components:{"minecraft:custom_data":{sheepwars:{intergalactique:true}}}}].count
execute store result score #c_abordage sheepwars.data run data get storage sheepwars:main Items[{components:{"minecraft:custom_data":{sheepwars:{abordage:true}}}}].count
execute store result score #c_soutien sheepwars.data run data get storage sheepwars:main Items[{components:{"minecraft:custom_data":{sheepwars:{soutien:true}}}}].count
execute store result score #c_distorsion sheepwars.data run data get storage sheepwars:main Items[{components:{"minecraft:custom_data":{sheepwars:{distorsion:true}}}}].count
execute store result score #c_chercheur sheepwars.data run data get storage sheepwars:main Items[{components:{"minecraft:custom_data":{sheepwars:{chercheur:true}}}}].count
execute store result score #c_fragmentation sheepwars.data run data get storage sheepwars:main Items[{components:{"minecraft:custom_data":{sheepwars:{fragmentation:true}}}}].count
execute store result score #c_glace sheepwars.data run data get storage sheepwars:main Items[{components:{"minecraft:custom_data":{sheepwars:{glace:true}}}}].count
execute store result score #c_incendiaire sheepwars.data run data get storage sheepwars:main Items[{components:{"minecraft:custom_data":{sheepwars:{incendiaire:true}}}}].count
execute store result score #c_foudroyant sheepwars.data run data get storage sheepwars:main Items[{components:{"minecraft:custom_data":{sheepwars:{foudroyant:true}}}}].count
execute store result score #c_sismique sheepwars.data run data get storage sheepwars:main Items[{components:{"minecraft:custom_data":{sheepwars:{sismique:true}}}}].count
execute store result score #c_glouton sheepwars.data run data get storage sheepwars:main Items[{components:{"minecraft:custom_data":{sheepwars:{glouton:true}}}}].count
execute store result score #c_tenebreux sheepwars.data run data get storage sheepwars:main Items[{components:{"minecraft:custom_data":{sheepwars:{tenebreux:true}}}}].count
execute store result score #c_explosif sheepwars.data run data get storage sheepwars:main Items[{components:{"minecraft:custom_data":{sheepwars:{explosif:true}}}}].count

# Tellraw to the player
tellraw @s ["",{"text":"[SheepWars] ","color":"yellow"},{"text":"You got: "}]

# Add a component to the message for each sheep (starting from the end)
execute if score #c_intergalactique sheepwars.data matches 1.. run tellraw @s [{"text":"- x","color":"blue"},{"score":{"name":"#c_intergalactique","objective":"sheepwars.data"}},{"text":" Mouton Intergalactique"}]
execute if score #c_abordage sheepwars.data matches 1.. run tellraw @s [{"text":"- x","color":"white"},{"score":{"name":"#c_abordage","objective":"sheepwars.data"}},{"text":" Mouton d'Abordage"}]
execute if score #c_soutien sheepwars.data matches 1.. run tellraw @s [{"text":"- x","color":"#FF69B4"},{"score":{"name":"#c_soutien","objective":"sheepwars.data"}},{"text":" Mouton de Soutien"}]
execute if score #c_distorsion sheepwars.data matches 1.. run tellraw @s [{"text":"- x","color":"dark_purple"},{"score":{"name":"#c_distorsion","objective":"sheepwars.data"}},{"text":" Mouton Distorsion"}]
execute if score #c_chercheur sheepwars.data matches 1.. run tellraw @s [{"text":"- x","color":"green"},{"score":{"name":"#c_chercheur","objective":"sheepwars.data"}},{"text":" Mouton Chercheur"}]
execute if score #c_fragmentation sheepwars.data matches 1.. run tellraw @s [{"text":"- x","color":"gray"},{"score":{"name":"#c_fragmentation","objective":"sheepwars.data"}},{"text":" Mouton Fragmentation"}]
execute if score #c_glace sheepwars.data matches 1.. run tellraw @s [{"text":"- x","color":"aqua"},{"score":{"name":"#c_glace","objective":"sheepwars.data"}},{"text":" Mouton Glace"}]
execute if score #c_incendiaire sheepwars.data matches 1.. run tellraw @s [{"text":"- x","color":"gold"},{"score":{"name":"#c_incendiaire","objective":"sheepwars.data"}},{"text":" Mouton Incendiaire"}]
execute if score #c_foudroyant sheepwars.data matches 1.. run tellraw @s [{"text":"- x","color":"yellow"},{"score":{"name":"#c_foudroyant","objective":"sheepwars.data"}},{"text":" Mouton Foudroyant"}]
execute if score #c_sismique sheepwars.data matches 1.. run tellraw @s [{"text":"- x","color":"#B37520"},{"score":{"name":"#c_sismique","objective":"sheepwars.data"}},{"text":" Mouton Sismique"}]
execute if score #c_glouton sheepwars.data matches 1.. run tellraw @s [{"text":"- x","color":"dark_green"},{"score":{"name":"#c_glouton","objective":"sheepwars.data"}},{"text":" Mouton Glouton"}]
execute if score #c_tenebreux sheepwars.data matches 1.. run tellraw @s [{"text":"- x","color":"dark_gray"},{"score":{"name":"#c_tenebreux","objective":"sheepwars.data"}},{"text":" Mouton Ténébreux"}]
execute if score #c_explosif sheepwars.data matches 1.. run tellraw @s [{"text":"- x","color":"red"},{"score":{"name":"#c_explosif","objective":"sheepwars.data"}},{"text":" Mouton Explosif"}]
tellraw @s ""

# Reset the counters
scoreboard players reset #c_intergalactique sheepwars.data
scoreboard players reset #c_abordage sheepwars.data
scoreboard players reset #c_soutien sheepwars.data
scoreboard players reset #c_distorsion sheepwars.data
scoreboard players reset #c_chercheur sheepwars.data
scoreboard players reset #c_fragmentation sheepwars.data
scoreboard players reset #c_glace sheepwars.data
scoreboard players reset #c_incendiaire sheepwars.data
scoreboard players reset #c_foudroyant sheepwars.data
scoreboard players reset #c_sismique sheepwars.data
scoreboard players reset #c_glouton sheepwars.data
scoreboard players reset #c_tenebreux sheepwars.data
scoreboard players reset #c_explosif sheepwars.data

# Loot to the player and remove the shulker box
loot give @s mine 0 0 0 stone[custom_data={drop_contents:true}]
setblock 0 0 0 air

# Reset input score
scoreboard players reset #number_of_drops sheepwars.data

