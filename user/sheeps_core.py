
# ruff: noqa: E501
# Imports
from beet import Context
from stewbeet import write_function


# Setup sheeps core functions
def setup_sheeps_core_functions(ctx: Context) -> None:
	ns: str = ctx.project_id

	write_function(f"{ns}:sheeps/blink", f"""
#> {ns}:sheeps/blink
#
# @executed			as & at the sheep (that can explode)
#
# @description		Score {ns}.data is supposed to be at least 90 (ticks).
#

# Remembers the sheep color
execute if score @s {ns}.data matches 90 store result score @s {ns}.previous_color run data get entity @s Color

## Makes the sheep blink (Explode at 9.5s : 190 ticks)
# Normal
execute if score @s {ns}.data matches 90 run data modify entity @s Color set value 0
execute if score @s {ns}.data matches 100 store result entity @s Color byte 1 run scoreboard players get @s {ns}.previous_color
execute if score @s {ns}.data matches 110 run data modify entity @s Color set value 0
execute if score @s {ns}.data matches 120 store result entity @s Color byte 1 run scoreboard players get @s {ns}.previous_color
execute if score @s {ns}.data matches 130 run data modify entity @s Color set value 0
execute if score @s {ns}.data matches 140 store result entity @s Color byte 1 run scoreboard players get @s {ns}.previous_color

# Fast
execute if score @s {ns}.data matches 145 run data modify entity @s Color set value 0
execute if score @s {ns}.data matches 150 store result entity @s Color byte 1 run scoreboard players get @s {ns}.previous_color
execute if score @s {ns}.data matches 155 run data modify entity @s Color set value 0
execute if score @s {ns}.data matches 160 store result entity @s Color byte 1 run scoreboard players get @s {ns}.previous_color
execute if score @s {ns}.data matches 165 run data modify entity @s Color set value 0

# Very fast
execute if score @s {ns}.data matches 167 run data modify entity @s Color set value 0
execute if score @s {ns}.data matches 169 store result entity @s Color byte 1 run scoreboard players get @s {ns}.previous_color
execute if score @s {ns}.data matches 171 run data modify entity @s Color set value 0
execute if score @s {ns}.data matches 173 store result entity @s Color byte 1 run scoreboard players get @s {ns}.previous_color
execute if score @s {ns}.data matches 175 run data modify entity @s Color set value 0
execute if score @s {ns}.data matches 177 store result entity @s Color byte 1 run scoreboard players get @s {ns}.previous_color
execute if score @s {ns}.data matches 179 run data modify entity @s Color set value 0
execute if score @s {ns}.data matches 181 store result entity @s Color byte 1 run scoreboard players get @s {ns}.previous_color
execute if score @s {ns}.data matches 183 run data modify entity @s Color set value 0
execute if score @s {ns}.data matches 185 store result entity @s Color byte 1 run scoreboard players get @s {ns}.previous_color
execute if score @s {ns}.data matches 187 run data modify entity @s Color set value 0
execute if score @s {ns}.data matches 189 store result entity @s Color byte 1 run scoreboard players get @s {ns}.previous_color

# Do nothing at 190 ticks in this function
""")

	write_function(f"{ns}:sheeps/final_action", f"""
#> {ns}:sheeps/final_action
#
# @executed			as & at the sheep
#
# @description		Manages the final action of the sheep.
#

# Depending on the sheep type, run appropriate functions
scoreboard players set #success {ns}.data 0
execute store success score #success {ns}.data if score #success {ns}.data matches 0 if entity @s[tag={ns}.explosif] run function {ns}:sheeps/final/normal_explosion
execute store success score #success {ns}.data if score #success {ns}.data matches 0 if entity @s[tag={ns}.incendiaire] run function {ns}:sheeps/final/fire_explosion
execute store success score #success {ns}.data if score #success {ns}.data matches 0 if entity @s[tag={ns}.fragmentation] run function {ns}:sheeps/final/fragmentation
execute store success score #success {ns}.data if score #success {ns}.data matches 0 if entity @s[tag={ns}.fragmentation_part] run function {ns}:sheeps/final/normal_explosion
execute store success score #success {ns}.data if score #success {ns}.data matches 0 if entity @s[tag={ns}.glouton] run function {ns}:sheeps/final/normal_explosion
execute store success score #success {ns}.data if score #success {ns}.data matches 0 if entity @s[tag={ns}.chercheur] run function {ns}:sheeps/final/normal_explosion

# In all cases, remove the sheep
function {ns}:sheeps/final/disappear
""")

	write_function(f"{ns}:sheeps/give_levitation", f"""
# Give levitation
effect give @s levitation 1 8 true

# Add the launched tag
tag @s add {ns}.launched_in_air
""")

	write_function(f"{ns}:sheeps/passive_action", f"""
#> {ns}:sheeps/passive_action
#
# @executed			as & at the sheep
#
# @description		Manages the sheep passive actions depending on the sheep type
#

## Apply the sheep passive action
# Abordage
execute if entity @s[tag={ns}.abordage] on passengers run effect give @s slow_falling 1 0 true

# Tenebreux
execute if entity @s[tag={ns}.tenebreux] run effect give @a[gamemode=!spectator,distance=..6] darkness 1 0 true
execute if entity @s[tag={ns}.tenebreux] run particle dust{{color:[0,0,0],scale:1}} ~ ~ ~ 6 6 6 0 10

# Glouton
data modify entity @s[tag={ns}.glouton,scores={{{ns}.data=40}}] NoAI set value 1b
execute if entity @s[tag={ns}.glouton,scores={{{ns}.data=40..}}] run tp @s ^ ^ ^0.1
execute if entity @s[tag={ns}.glouton,scores={{{ns}.data=40..}}] run fill ~-1 ~ ~-1 ~1 ~2 ~1 air destroy
execute if entity @s[tag={ns}.glouton,scores={{{ns}.data=40..}}] run particle block{{block_state:"lime_terracotta"}} ~ ~1 ~ 1 1 1 0 10

# Sismique
execute if entity @s[tag={ns}.sismique] as @a[gamemode=!spectator,distance=..6] at @s unless block ~ ~-.1 ~ air run function {ns}:sheeps/give_levitation
execute if entity @s[tag={ns}.sismique] run particle block{{block_state:"brown_terracotta"}} ~ ~ ~ 6 .5 6 0 10

# Foudroyant
execute if entity @s[tag={ns}.foudroyant,scores={{{ns}.data=41}}] at @a[gamemode=!spectator,distance=..6] run summon lightning_bolt
execute if entity @s[tag={ns}.foudroyant,scores={{{ns}.data=10}}] at @a[gamemode=!spectator,distance=..6] run summon lightning_bolt
execute if entity @s[tag={ns}.foudroyant,scores={{{ns}.data=160}}] at @a[gamemode=!spectator,distance=..6] run summon lightning_bolt
execute if entity @s[tag={ns}.foudroyant,scores={{{ns}.data=41}}] run summon lightning_bolt ~ ~-9 ~
execute if entity @s[tag={ns}.foudroyant,scores={{{ns}.data=100}}] run summon lightning_bolt ~ ~-9 ~
execute if entity @s[tag={ns}.foudroyant,scores={{{ns}.data=160}}] run summon lightning_bolt ~ ~-9 ~

# Glace
execute if entity @s[tag={ns}.glace] run effect give @a[gamemode=!spectator,distance=..6] slowness 1 2 true
execute if entity @s[tag={ns}.glace,scores={{{ns}.data=41}}] run function {ns}:sheeps/active/glace/main
execute if entity @s[tag={ns}.glace,scores={{{ns}.data=44}}] run function {ns}:sheeps/active/glace/main
execute if entity @s[tag={ns}.glace,scores={{{ns}.data=48}}] run function {ns}:sheeps/active/glace/main
execute if entity @s[tag={ns}.glace,scores={{{ns}.data=52}}] run function {ns}:sheeps/active/glace/main
execute if entity @s[tag={ns}.glace,scores={{{ns}.data=56}}] run function {ns}:sheeps/active/glace/main
execute if entity @s[tag={ns}.glace,scores={{{ns}.data=60}}] run function {ns}:sheeps/active/glace/main
execute if entity @s[tag={ns}.glace,scores={{{ns}.data=64}}] run function {ns}:sheeps/active/glace/main
execute if entity @s[tag={ns}.glace,scores={{{ns}.data=68}}] run function {ns}:sheeps/active/glace/main

# Chercheur
execute if entity @s[tag={ns}.chercheur] on passengers run data modify entity @s NoAI set value 0b
execute if entity @s[tag={ns}.chercheur] if entity @p[gamemode=!spectator,distance=..2] run scoreboard players set @s {ns}.data 100000

# Distorsion
execute if entity @s[tag={ns}.distorsion,scores={{{ns}.data=50}}] positioned ~ ~1 ~ run function realistic_explosion:explode
execute if entity @s[tag={ns}.distorsion,scores={{{ns}.data=90}}] positioned ~ ~1 ~ run function realistic_explosion:explode
execute if entity @s[tag={ns}.distorsion,scores={{{ns}.data=120}}] positioned ~ ~1 ~ run function realistic_explosion:explode
execute if entity @s[tag={ns}.distorsion,scores={{{ns}.data=140}}] positioned ~ ~1 ~ run function realistic_explosion:explode
execute if entity @s[tag={ns}.distorsion,scores={{{ns}.data=170}}] positioned ~ ~1 ~ run function realistic_explosion:explode
execute if entity @s[tag={ns}.distorsion] run particle dust{{color:[0.5,0.0,0.5],scale:1}} ~ ~ ~ 2 2 2 0 10

# Soutien
execute if entity @s[tag={ns}.soutien] run effect give @a[gamemode=!spectator,distance=..3,nbt=!{{ActiveEffects:[{{Id:10}}]}}] regeneration 4 2 true
execute if entity @s[tag={ns}.soutien] run particle heart ~ ~ ~ 3 3 3 0 5

# Intergalactique
execute if entity @s[tag={ns}.intergalactique,scores={{{ns}.data=50}}] run function {ns}:sheeps/active/intergalactique/main
execute if entity @s[tag={ns}.intergalactique,scores={{{ns}.data=70}}] run function {ns}:sheeps/active/intergalactique/main
execute if entity @s[tag={ns}.intergalactique,scores={{{ns}.data=90}}] run function {ns}:sheeps/active/intergalactique/main
execute if entity @s[tag={ns}.intergalactique,scores={{{ns}.data=110}}] run function {ns}:sheeps/active/intergalactique/main
execute if entity @s[tag={ns}.intergalactique,scores={{{ns}.data=130}}] run function {ns}:sheeps/active/intergalactique/main

""")

	write_function(f"{ns}:sheeps/tick_sheep", f"""
#> {ns}:sheeps/tick_sheep
#
# @executed			as & at the sheep
#
# @description		Manages the sheep actions
#

# Increment the sheep timer
scoreboard players add @s {ns}.data 1

# Manages sheep blinking for sheeps that can explode
execute if score @s[tag={ns}.explode] {ns}.data matches 90.. run function {ns}:sheeps/blink

# Sheep passive actions
execute if score @s {ns}.data matches 40.. run function {ns}:sheeps/passive_action

# Fragmentation parts
execute if score @s {ns}.data matches 20.. if entity @s[tag={ns}.fragmentation_part] run function {ns}:sheeps/final_action

# Final action of the sheep (Explosion, fire, disappear, etc.)
execute if score @s {ns}.data matches 190.. run function {ns}:sheeps/final_action
""")

