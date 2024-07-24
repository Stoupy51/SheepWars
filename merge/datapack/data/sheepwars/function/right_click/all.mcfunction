
# Revoke advancement
advancement revoke @s only sheepwars:using_item

# Copy the player's UUID to the main storage
data modify storage sheepwars:main UUID set from entity @s UUID

## All Sheeps
scoreboard players set #success sheepwars.data 0
execute if score #success sheepwars.data matches 0 if data entity @s SelectedItem.components."minecraft:custom_data".sheepwars.explosif run function sheepwars:sheeps/summon/explosif
execute if score #success sheepwars.data matches 0 if data entity @s SelectedItem.components."minecraft:custom_data".sheepwars.incendiaire run function sheepwars:sheeps/summon/incendiaire
execute if score #success sheepwars.data matches 0 if data entity @s SelectedItem.components."minecraft:custom_data".sheepwars.fragmentation run function sheepwars:sheeps/summon/fragmentation
execute if score #success sheepwars.data matches 0 if data entity @s SelectedItem.components."minecraft:custom_data".sheepwars.glouton run function sheepwars:sheeps/summon/glouton
execute if score #success sheepwars.data matches 0 if data entity @s SelectedItem.components."minecraft:custom_data".sheepwars.chercheur run function sheepwars:sheeps/summon/chercheur
execute if score #success sheepwars.data matches 0 if data entity @s SelectedItem.components."minecraft:custom_data".sheepwars.glace run function sheepwars:sheeps/summon/glace
execute if score #success sheepwars.data matches 0 if data entity @s SelectedItem.components."minecraft:custom_data".sheepwars.foudroyant run function sheepwars:sheeps/summon/foudroyant
execute if score #success sheepwars.data matches 0 if data entity @s SelectedItem.components."minecraft:custom_data".sheepwars.distorsion run function sheepwars:sheeps/summon/distorsion
execute if score #success sheepwars.data matches 0 if data entity @s SelectedItem.components."minecraft:custom_data".sheepwars.tenebreux run function sheepwars:sheeps/summon/tenebreux
execute if score #success sheepwars.data matches 0 if data entity @s SelectedItem.components."minecraft:custom_data".sheepwars.sismique run function sheepwars:sheeps/summon/sismique
execute if score #success sheepwars.data matches 0 if data entity @s SelectedItem.components."minecraft:custom_data".sheepwars.soutien run function sheepwars:sheeps/summon/soutien
execute if score #success sheepwars.data matches 0 if data entity @s SelectedItem.components."minecraft:custom_data".sheepwars.abordage run function sheepwars:sheeps/summon/abordage
execute if score #success sheepwars.data matches 0 if data entity @s SelectedItem.components."minecraft:custom_data".sheepwars.intergalactique run function sheepwars:sheeps/summon/intergalactique

# If success is 1, then remove one count of the item in the player's hand
execute if score #success sheepwars.data matches 1 run item modify entity @s weapon.mainhand sheepwars:remove_one
execute if score #success sheepwars.data matches 1 run scoreboard players add @s sheepwars.launched_count 1

