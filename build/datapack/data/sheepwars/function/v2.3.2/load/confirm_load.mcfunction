
#> sheepwars:v2.3.2/load/confirm_load
#
# @within	sheepwars:v2.3.2/load/secondary
#

# Confirm load
tellraw @a[tag=convention.debug] {"text":"[Loaded SheepWars v2.3.2]","color":"green"}
scoreboard players set #sheepwars.loaded load.status 1

# Items storage
data modify storage sheepwars:items all set value {}
data modify storage sheepwars:items all.explosif set value {"id": "minecraft:red_wool","count": 1,"components": {"minecraft:item_name": {"text": "Mouton Explosif","color": "red"},"minecraft:consumable": {"consume_seconds": 1024},"minecraft:lore": [["",{"text": "I","color": "white","italic": false,"font": "sheepwars:icons"},{"text": " SheepWars","italic": true,"color": "blue"}]],"minecraft:custom_data": {"sheepwars": {"explosif": true},"smithed": {"ignore": {"functionality": true,"crafting": true}}}}}
data modify storage sheepwars:items all.tenebreux set value {"id": "minecraft:black_wool","count": 1,"components": {"minecraft:item_name": {"text": "Mouton Ténébreux","color": "dark_gray"},"minecraft:consumable": {"consume_seconds": 1024},"minecraft:lore": [["",{"text": "I","color": "white","italic": false,"font": "sheepwars:icons"},{"text": " SheepWars","italic": true,"color": "blue"}]],"minecraft:custom_data": {"sheepwars": {"tenebreux": true},"smithed": {"ignore": {"functionality": true,"crafting": true}}}}}
data modify storage sheepwars:items all.glouton set value {"id": "minecraft:green_wool","count": 1,"components": {"minecraft:item_name": {"text": "Mouton Glouton","color": "green"},"minecraft:consumable": {"consume_seconds": 1024},"minecraft:lore": [["",{"text": "I","color": "white","italic": false,"font": "sheepwars:icons"},{"text": " SheepWars","italic": true,"color": "blue"}]],"minecraft:custom_data": {"sheepwars": {"glouton": true},"smithed": {"ignore": {"functionality": true,"crafting": true}}}}}
data modify storage sheepwars:items all.sismique set value {"id": "minecraft:brown_wool","count": 1,"components": {"minecraft:item_name": {"text": "Mouton Sismique","color": "#B37520"},"minecraft:consumable": {"consume_seconds": 1024},"minecraft:lore": [["",{"text": "I","color": "white","italic": false,"font": "sheepwars:icons"},{"text": " SheepWars","italic": true,"color": "blue"}]],"minecraft:custom_data": {"sheepwars": {"sismique": true},"smithed": {"ignore": {"functionality": true,"crafting": true}}}}}
data modify storage sheepwars:items all.foudroyant set value {"id": "minecraft:yellow_wool","count": 1,"components": {"minecraft:item_name": {"text": "Mouton Foudroyant","color": "yellow"},"minecraft:consumable": {"consume_seconds": 1024},"minecraft:lore": [["",{"text": "I","color": "white","italic": false,"font": "sheepwars:icons"},{"text": " SheepWars","italic": true,"color": "blue"}]],"minecraft:custom_data": {"sheepwars": {"foudroyant": true},"smithed": {"ignore": {"functionality": true,"crafting": true}}}}}
data modify storage sheepwars:items all.incendiaire set value {"id": "minecraft:orange_wool","count": 1,"components": {"minecraft:item_name": {"text": "Mouton Incendiaire","color": "gold"},"minecraft:consumable": {"consume_seconds": 1024},"minecraft:lore": [["",{"text": "I","color": "white","italic": false,"font": "sheepwars:icons"},{"text": " SheepWars","italic": true,"color": "blue"}]],"minecraft:custom_data": {"sheepwars": {"incendiaire": true},"smithed": {"ignore": {"functionality": true,"crafting": true}}}}}
data modify storage sheepwars:items all.glace set value {"id": "minecraft:light_blue_wool","count": 1,"components": {"minecraft:item_name": {"text": "Mouton Glacé","color": "aqua"},"minecraft:consumable": {"consume_seconds": 1024},"minecraft:lore": [["",{"text": "I","color": "white","italic": false,"font": "sheepwars:icons"},{"text": " SheepWars","italic": true,"color": "blue"}]],"minecraft:custom_data": {"sheepwars": {"glace": true},"smithed": {"ignore": {"functionality": true,"crafting": true}}}}}
data modify storage sheepwars:items all.fragmentation set value {"id": "minecraft:light_gray_wool","count": 1,"components": {"minecraft:item_name": {"text": "Mouton Fragmentation","color": "gray"},"minecraft:consumable": {"consume_seconds": 1024},"minecraft:lore": [["",{"text": "I","color": "white","italic": false,"font": "sheepwars:icons"},{"text": " SheepWars","italic": true,"color": "blue"}]],"minecraft:custom_data": {"sheepwars": {"fragmentation": true},"smithed": {"ignore": {"functionality": true,"crafting": true}}}}}
data modify storage sheepwars:items all.chercheur set value {"id": "minecraft:lime_wool","count": 1,"components": {"minecraft:item_name": {"text": "Mouton Chercheur","color": "green"},"minecraft:consumable": {"consume_seconds": 1024},"minecraft:lore": [["",{"text": "I","color": "white","italic": false,"font": "sheepwars:icons"},{"text": " SheepWars","italic": true,"color": "blue"}]],"minecraft:custom_data": {"sheepwars": {"chercheur": true},"smithed": {"ignore": {"functionality": true,"crafting": true}}}}}
data modify storage sheepwars:items all.distorsion set value {"id": "minecraft:purple_wool","count": 1,"components": {"minecraft:item_name": {"text": "Mouton Distorsion","color": "dark_purple"},"minecraft:consumable": {"consume_seconds": 1024},"minecraft:lore": [["",{"text": "I","color": "white","italic": false,"font": "sheepwars:icons"},{"text": " SheepWars","italic": true,"color": "blue"}]],"minecraft:custom_data": {"sheepwars": {"distorsion": true},"smithed": {"ignore": {"functionality": true,"crafting": true}}}}}
data modify storage sheepwars:items all.soutien set value {"id": "minecraft:pink_wool","count": 1,"components": {"minecraft:item_name": {"text": "Mouton de Soutien","color": "#FF69B4"},"minecraft:consumable": {"consume_seconds": 1024},"minecraft:lore": [["",{"text": "I","color": "white","italic": false,"font": "sheepwars:icons"},{"text": " SheepWars","italic": true,"color": "blue"}]],"minecraft:custom_data": {"sheepwars": {"soutien": true},"smithed": {"ignore": {"functionality": true,"crafting": true}}}}}
data modify storage sheepwars:items all.abordage set value {"id": "minecraft:white_wool","count": 1,"components": {"minecraft:item_name": {"text": "Mouton d'Abordage","color": "white"},"minecraft:consumable": {"consume_seconds": 1024},"minecraft:lore": [["",{"text": "I","color": "white","italic": false,"font": "sheepwars:icons"},{"text": " SheepWars","italic": true,"color": "blue"}]],"minecraft:custom_data": {"sheepwars": {"abordage": true},"smithed": {"ignore": {"functionality": true,"crafting": true}}}}}
data modify storage sheepwars:items all.intergalactique set value {"id": "minecraft:blue_wool","count": 1,"components": {"minecraft:item_name": {"text": "Mouton Intergalactique","color": "blue"},"minecraft:consumable": {"consume_seconds": 1024},"minecraft:lore": [["",{"text": "I","color": "white","italic": false,"font": "sheepwars:icons"},{"text": " SheepWars","italic": true,"color": "blue"}]],"minecraft:custom_data": {"sheepwars": {"intergalactique": true},"smithed": {"ignore": {"functionality": true,"crafting": true}}}}}

## Scoreboards
# Delete all scoreboards
scoreboard objectives remove sheepwars.data

# Data scoreboard for math and stuff
scoreboard objectives add sheepwars.data dummy

# Previous color reminder
scoreboard objectives add sheepwars.previous_color dummy

# Additional
scoreboard objectives add sheepwars.launched_count dummy

# Team with no collision
team add sheepwars.sheeps
team modify sheepwars.sheeps collisionRule never

