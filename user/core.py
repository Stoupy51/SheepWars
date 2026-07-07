
# ruff: noqa: E501
# Imports
from beet import Context
from stewbeet import write_function


# Setup core functions
def setup_core_functions(ctx: Context) -> None:
	ns: str = ctx.project_id

	write_function(f"{ns}:unload", f"""
#> {ns}:unload
#
# @executed			unknown context
#
# @description		Function that unload everything from the SheepWars datapack
#

# Delete all scoreboards
scoreboard objectives remove {ns}.data
scoreboard objectives remove {ns}.right_click
scoreboard objectives remove {ns}.previous_color
scoreboard objectives remove {ns}.launched_count

# Delete storage
data remove storage {ns}:main all
data remove storage {ns}:items all

#define storage {ns}:main
#define storage {ns}:items


""")

	write_function(f"{ns}:right_click/all", f"""
# Revoke advancement
advancement revoke @s only {ns}:using_item

# 4 ticks cooldown to prevent multiple summons when right-clicking fast
execute if score @s {ns}.cooldown > #global_tick {ns}.data run return fail
scoreboard players operation @s {ns}.cooldown = #global_tick {ns}.data
scoreboard players add @s {ns}.cooldown 4

# Copy the player's UUID to the main storage
data modify storage {ns}:main UUID set from entity @s UUID

## All Sheeps
scoreboard players set #success {ns}.data 0
execute if score #success {ns}.data matches 0 if data entity @s SelectedItem.components."minecraft:custom_data".{ns}.explosif run function {ns}:sheeps/summon/explosif
execute if score #success {ns}.data matches 0 if data entity @s SelectedItem.components."minecraft:custom_data".{ns}.incendiaire run function {ns}:sheeps/summon/incendiaire
execute if score #success {ns}.data matches 0 if data entity @s SelectedItem.components."minecraft:custom_data".{ns}.fragmentation run function {ns}:sheeps/summon/fragmentation
execute if score #success {ns}.data matches 0 if data entity @s SelectedItem.components."minecraft:custom_data".{ns}.glouton run function {ns}:sheeps/summon/glouton
execute if score #success {ns}.data matches 0 if data entity @s SelectedItem.components."minecraft:custom_data".{ns}.chercheur run function {ns}:sheeps/summon/chercheur
execute if score #success {ns}.data matches 0 if data entity @s SelectedItem.components."minecraft:custom_data".{ns}.glace run function {ns}:sheeps/summon/glace
execute if score #success {ns}.data matches 0 if data entity @s SelectedItem.components."minecraft:custom_data".{ns}.foudroyant run function {ns}:sheeps/summon/foudroyant
execute if score #success {ns}.data matches 0 if data entity @s SelectedItem.components."minecraft:custom_data".{ns}.distorsion run function {ns}:sheeps/summon/distorsion
execute if score #success {ns}.data matches 0 if data entity @s SelectedItem.components."minecraft:custom_data".{ns}.tenebreux run function {ns}:sheeps/summon/tenebreux
execute if score #success {ns}.data matches 0 if data entity @s SelectedItem.components."minecraft:custom_data".{ns}.sismique run function {ns}:sheeps/summon/sismique
execute if score #success {ns}.data matches 0 if data entity @s SelectedItem.components."minecraft:custom_data".{ns}.soutien run function {ns}:sheeps/summon/soutien
execute if score #success {ns}.data matches 0 if data entity @s SelectedItem.components."minecraft:custom_data".{ns}.abordage run function {ns}:sheeps/summon/abordage
execute if score #success {ns}.data matches 0 if data entity @s SelectedItem.components."minecraft:custom_data".{ns}.intergalactique run function {ns}:sheeps/summon/intergalactique

# If success is 1, then remove one count of the item in the player's hand
execute if score #success {ns}.data matches 1 run item modify entity @s weapon.mainhand {ns}:remove_one
execute if score #success {ns}.data matches 1 run scoreboard players add @s {ns}.launched_count 1

""")

