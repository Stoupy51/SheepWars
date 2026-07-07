
# ruff: noqa: E501
# Imports
from beet import Context
from stewbeet import write_function


# Setup utils functions
def setup_utils_functions(ctx: Context) -> None:
	ns: str = ctx.project_id

	write_function(f"{ns}:utils/get_marker_motion", f"""
#> {ns}:utils/get_marker_motion
#
# @executed			as & at a non-player entity (sheep, etc.)
#
# @input storage	{ns}:main Rotation : 2D rotation of the entity
# @output storage	{ns}:main Motion : 3D motion of the entity (Position of the marker)
#
# @description		Use this marker to fill the "Motion" storage with the position of the marker
#

# Apply rotation to the entity
data modify entity @s Rotation set from storage {ns}:main Rotation

# Teleport ahead
execute at @s run tp @s ^ ^ ^100

# Fill the "Motion" storage with the position of the entity
data modify storage {ns}:main Motion set from entity @s Pos

# Kill the entity
kill @s
""")

	write_function(f"{ns}:utils/get_player_from_uuid", f"""
#> {ns}:utils/get_player_from_uuid
#
# @executed			as a player
#
# @input storage	{ns}:main UUID : The player UUID that launched the sheep.
# @output player	Tagged player that launched the sheep.
#
# @description		Compare the player UUID with the one stored in the {ns}:main storage.
#

# Copy the player UUID
data modify storage {ns}:main Copy set from storage {ns}:main UUID

# Check for equality
scoreboard players set #replaced {ns}.data 0
execute store success score #replaced {ns}.data run data modify storage {ns}:main Copy set from entity @s UUID

# If the player UUID matches (not replaced), add a tag to the player
execute if score #replaced {ns}.data matches 0 run tag @s add {ns}.owner

""")

	write_function(f"{ns}:utils/launch_entity_in_direction", f"""
#> {ns}:utils/launch_entity_in_direction
#
# @executed			as & at a non-player entity (sheep, etc.)
#
# @input storage	{ns}:main Rotation : 2D rotation of the entity
# @input storage	{ns}:main UUID : UUID of the player who launched the entity
#
# @description		Handles the launch of an entity in a direction, remove "new" tag and store launcher's UUID.
#

# Remove the "new" tag and store the launcher's UUID
function {ns}:utils/new_sheep

## Launch the entity
# Get the motion of the entity by summoning a temporary marker
execute at @s positioned 0 0 0 summon marker at @s run function {ns}:utils/get_marker_motion

# Apply the motion to the entity
execute store result entity @s Motion[0] double 0.04 run data get storage {ns}:main Motion[0]
execute store result entity @s Motion[1] double 0.04 run data get storage {ns}:main Motion[1]
execute store result entity @s Motion[2] double 0.04 run data get storage {ns}:main Motion[2]
""")

	write_function(f"{ns}:utils/new_sheep", f"""
#> {ns}:utils/new_sheep
#
# @executed			as & at a non-player entity (sheep, etc.)
#
# @input storage	{ns}:main Rotation : 2D rotation of the entity
# @input storage	{ns}:main UUID : UUID of the player who launched the entity
#
# @description		Remove "new" tag and store launcher's UUID.
#

# Remove "new" tag
tag @s remove {ns}.new

# Apply rotation to the entity
data modify entity @s Rotation set from storage {ns}:main Rotation

# Store the launcher's UUID
data merge entity @s {{ArmorItems:[{{id:"minecraft:stone",count:1}},{{}},{{}},{{}}],ArmorDropChances:[0.0f,0.0f,0.0f,0.0f]}}
data modify entity @s ArmorItems[0].components."minecraft:custom_data".UUID set from storage {ns}:main UUID

# Join the {ns}.sheeps team (no collisions)
team join {ns}.sheeps

# Give fire resistance
effect give @s fire_resistance infinite 0 true

# Remove fall damage
attribute @s safe_fall_distance base set 1024
""")

	write_function(f"{ns}:utils/player_damaged", f"""
#> {ns}:utils/player_damaged
#
# @executed			as a player
#
# @output victim	The player who has been damaged (executing the function tag)
# @output damager	The owner of the sheep who killed the victim (tagged with "{ns}.owner")
#
# @description		Send a function tag signal if he is dead, and remove the damage tag.
#					The function tag signal can be used to customize the death of the player (message, etc.)
#

# Send a function tag signal
scoreboard players set #health {ns}.data -1
execute store result score #health {ns}.data run data get entity @s Health 1000000
execute if score #health {ns}.data matches ..0 run function #{ns}:signals/player_killed

# Remove the damage tag
tag @s remove {ns}.damaged
""")

	write_function(f"{ns}:utils/random_give", f"""
# Loot insert
setblock 0 0 0 air
setblock 0 0 0 yellow_shulker_box
loot insert 0 0 0 loot {ns}:basic_drop
execute if score #number_of_drops {ns}.data matches 2.. run loot insert 0 0 0 loot {ns}:basic_drop
execute if score #number_of_drops {ns}.data matches 3.. run loot insert 0 0 0 loot {ns}:basic_drop

## Sheep count
# Preparation of the storages
data modify storage {ns}:main Items set from block 0 0 0 Items

# Get the number of each sheep (starting from the end)
execute store result score #c_intergalactique {ns}.data run data get storage {ns}:main Items[{{components:{{"minecraft:custom_data":{{{ns}:{{intergalactique:true}}}}}}}}].count
execute store result score #c_abordage {ns}.data run data get storage {ns}:main Items[{{components:{{"minecraft:custom_data":{{{ns}:{{abordage:true}}}}}}}}].count
execute store result score #c_soutien {ns}.data run data get storage {ns}:main Items[{{components:{{"minecraft:custom_data":{{{ns}:{{soutien:true}}}}}}}}].count
execute store result score #c_distorsion {ns}.data run data get storage {ns}:main Items[{{components:{{"minecraft:custom_data":{{{ns}:{{distorsion:true}}}}}}}}].count
execute store result score #c_chercheur {ns}.data run data get storage {ns}:main Items[{{components:{{"minecraft:custom_data":{{{ns}:{{chercheur:true}}}}}}}}].count
execute store result score #c_fragmentation {ns}.data run data get storage {ns}:main Items[{{components:{{"minecraft:custom_data":{{{ns}:{{fragmentation:true}}}}}}}}].count
execute store result score #c_glace {ns}.data run data get storage {ns}:main Items[{{components:{{"minecraft:custom_data":{{{ns}:{{glace:true}}}}}}}}].count
execute store result score #c_incendiaire {ns}.data run data get storage {ns}:main Items[{{components:{{"minecraft:custom_data":{{{ns}:{{incendiaire:true}}}}}}}}].count
execute store result score #c_foudroyant {ns}.data run data get storage {ns}:main Items[{{components:{{"minecraft:custom_data":{{{ns}:{{foudroyant:true}}}}}}}}].count
execute store result score #c_sismique {ns}.data run data get storage {ns}:main Items[{{components:{{"minecraft:custom_data":{{{ns}:{{sismique:true}}}}}}}}].count
execute store result score #c_glouton {ns}.data run data get storage {ns}:main Items[{{components:{{"minecraft:custom_data":{{{ns}:{{glouton:true}}}}}}}}].count
execute store result score #c_tenebreux {ns}.data run data get storage {ns}:main Items[{{components:{{"minecraft:custom_data":{{{ns}:{{tenebreux:true}}}}}}}}].count
execute store result score #c_explosif {ns}.data run data get storage {ns}:main Items[{{components:{{"minecraft:custom_data":{{{ns}:{{explosif:true}}}}}}}}].count

# Tellraw to the player
tellraw @s ["",{{"text":"[SheepWars] ","color":"yellow"}},{{"text":"You got: "}}]

# Add a component to the message for each sheep (starting from the end)
execute if score #c_intergalactique {ns}.data matches 1.. run tellraw @s [{{"text":"- x","color":"blue"}},{{"score":{{"name":"#c_intergalactique","objective":"{ns}.data"}}}},{{"text":" Mouton Intergalactique"}}]
execute if score #c_abordage {ns}.data matches 1.. run tellraw @s [{{"text":"- x","color":"white"}},{{"score":{{"name":"#c_abordage","objective":"{ns}.data"}}}},{{"text":" Mouton d'Abordage"}}]
execute if score #c_soutien {ns}.data matches 1.. run tellraw @s [{{"text":"- x","color":"#FF69B4"}},{{"score":{{"name":"#c_soutien","objective":"{ns}.data"}}}},{{"text":" Mouton de Soutien"}}]
execute if score #c_distorsion {ns}.data matches 1.. run tellraw @s [{{"text":"- x","color":"dark_purple"}},{{"score":{{"name":"#c_distorsion","objective":"{ns}.data"}}}},{{"text":" Mouton Distorsion"}}]
execute if score #c_chercheur {ns}.data matches 1.. run tellraw @s [{{"text":"- x","color":"green"}},{{"score":{{"name":"#c_chercheur","objective":"{ns}.data"}}}},{{"text":" Mouton Chercheur"}}]
execute if score #c_fragmentation {ns}.data matches 1.. run tellraw @s [{{"text":"- x","color":"gray"}},{{"score":{{"name":"#c_fragmentation","objective":"{ns}.data"}}}},{{"text":" Mouton Fragmentation"}}]
execute if score #c_glace {ns}.data matches 1.. run tellraw @s [{{"text":"- x","color":"aqua"}},{{"score":{{"name":"#c_glace","objective":"{ns}.data"}}}},{{"text":" Mouton Glace"}}]
execute if score #c_incendiaire {ns}.data matches 1.. run tellraw @s [{{"text":"- x","color":"gold"}},{{"score":{{"name":"#c_incendiaire","objective":"{ns}.data"}}}},{{"text":" Mouton Incendiaire"}}]
execute if score #c_foudroyant {ns}.data matches 1.. run tellraw @s [{{"text":"- x","color":"yellow"}},{{"score":{{"name":"#c_foudroyant","objective":"{ns}.data"}}}},{{"text":" Mouton Foudroyant"}}]
execute if score #c_sismique {ns}.data matches 1.. run tellraw @s [{{"text":"- x","color":"#B37520"}},{{"score":{{"name":"#c_sismique","objective":"{ns}.data"}}}},{{"text":" Mouton Sismique"}}]
execute if score #c_glouton {ns}.data matches 1.. run tellraw @s [{{"text":"- x","color":"dark_green"}},{{"score":{{"name":"#c_glouton","objective":"{ns}.data"}}}},{{"text":" Mouton Glouton"}}]
execute if score #c_tenebreux {ns}.data matches 1.. run tellraw @s [{{"text":"- x","color":"dark_gray"}},{{"score":{{"name":"#c_tenebreux","objective":"{ns}.data"}}}},{{"text":" Mouton Ténébreux"}}]
execute if score #c_explosif {ns}.data matches 1.. run tellraw @s [{{"text":"- x","color":"red"}},{{"score":{{"name":"#c_explosif","objective":"{ns}.data"}}}},{{"text":" Mouton Explosif"}}]
tellraw @s ""

# Reset the counters
scoreboard players reset #c_intergalactique {ns}.data
scoreboard players reset #c_abordage {ns}.data
scoreboard players reset #c_soutien {ns}.data
scoreboard players reset #c_distorsion {ns}.data
scoreboard players reset #c_chercheur {ns}.data
scoreboard players reset #c_fragmentation {ns}.data
scoreboard players reset #c_glace {ns}.data
scoreboard players reset #c_incendiaire {ns}.data
scoreboard players reset #c_foudroyant {ns}.data
scoreboard players reset #c_sismique {ns}.data
scoreboard players reset #c_glouton {ns}.data
scoreboard players reset #c_tenebreux {ns}.data
scoreboard players reset #c_explosif {ns}.data

# Loot to the player and remove the shulker box
loot give @s mine 0 0 0 stone[custom_data={{drop_contents:true}}]
setblock 0 0 0 air

# Reset input score
scoreboard players reset #number_of_drops {ns}.data
""")

