
# ruff: noqa: E501
# Imports
from beet import Context
from stewbeet import write_function


# Setup sheeps summon functions
def setup_sheeps_summon_functions(ctx: Context) -> None:
	ns: str = ctx.project_id

	write_function(f"{ns}:sheeps/summon/abordage", f"""
#> {ns}:sheeps/summon/abordage
#
# @executed			as & at the player
#
# @description		Summons a sheep with tag "abordage" and launches it in the direction the player is looking at.
#

# Summon the sheep
summon sheep ^ ^1 ^1 {{Tags:["{ns}.sheep","{ns}.abordage","{ns}.new","{ns}.to_ride"],Color:0,DeathLootTable:"minecraft:empty"}}

# Store player's rotation
data modify storage {ns}:main Rotation set from entity @s Rotation

# Execute as the sheep the function that will launch it
execute as @e[tag={ns}.new] at @s run function {ns}:utils/launch_entity_in_direction

# Ride the sheep and remove the "to_ride" tag
ride @s dismount
ride @s mount @n[tag={ns}.to_ride]
tag @e[tag={ns}.to_ride] remove {ns}.to_ride

# Success
scoreboard players set #success {ns}.data 1

""")

	write_function(f"{ns}:sheeps/summon/chercheur", f"""
#> {ns}:sheeps/summon/chercheur
#
# @executed			as & at the player
#
# @description		Summons a sheep with tag "chercheur" and launches it in the direction the player is looking at.
#

# Summon the sheep
summon sheep ^ ^1 ^1 {{DeathLootTable:"{ns}:i/chercheur",Color:5b,Tags:["{ns}.sheep","{ns}.explode","{ns}.chercheur","{ns}.new"],Passengers:[{{id:"minecraft:husk",Silent:1b,Invulnerable:1b,NoAI:1b,DeathLootTable:"minecraft:empty",IsBaby:1b,Tags:["{ns}.chercheur_rider"],active_effects:[{{id:"minecraft:invisibility",amplifier:1,duration:20000000,show_particles:0b}}],Attributes:[{{Name:attack_damage,Base:0}}]}}]}}

# Store player's rotation and UUID
data modify storage {ns}:main Rotation set from entity @s Rotation

# Execute as the sheep the function that will launch it
execute as @e[tag={ns}.new] at @s run function {ns}:utils/launch_entity_in_direction

# Success
scoreboard players set #success {ns}.data 1

""")

	write_function(f"{ns}:sheeps/summon/distorsion", f"""
#> {ns}:sheeps/summon/distorsion
#
# @executed			as & at the player
#
# @description		Summons a sheep with tag "distorsion" and launches it in the direction the player is looking at.
#

# Summon the sheep
summon sheep ^ ^1 ^1 {{Tags:["{ns}.sheep","{ns}.distorsion","{ns}.new"],Color:10,DeathLootTable:"{ns}:i/distorsion"}}

# Store player's rotation
data modify storage {ns}:main Rotation set from entity @s Rotation

# Execute as the sheep the function that will launch it
execute as @e[tag={ns}.new] at @s run function {ns}:utils/launch_entity_in_direction

# Success
scoreboard players set #success {ns}.data 1

""")

	write_function(f"{ns}:sheeps/summon/explosif", f"""
#> {ns}:sheeps/summon/explosif
#
# @executed			as & at the player
#
# @description		Summons a sheep with tag "explosif" and launches it in the direction the player is looking at.
#

# Summon the sheep
summon sheep ^ ^1 ^1 {{Tags:["{ns}.sheep","{ns}.explode","{ns}.explosif","{ns}.new"],Color:14,DeathLootTable:"{ns}:i/explosif"}}

# Store player's rotation
data modify storage {ns}:main Rotation set from entity @s Rotation

# Execute as the sheep the function that will launch it
execute as @e[tag={ns}.new] at @s run function {ns}:utils/launch_entity_in_direction

# Success
scoreboard players set #success {ns}.data 1

""")

	write_function(f"{ns}:sheeps/summon/foudroyant", f"""
#> {ns}:sheeps/summon/foudroyant
#
# @executed			as & at the player
#
# @description		Summons a sheep with tag "foudroyant" and launches it in the direction the player is looking at.
#

# Summon the sheep
summon sheep ^ ^1 ^1 {{Tags:["{ns}.sheep","{ns}.foudroyant","{ns}.new"],Color:4,DeathLootTable:"{ns}:i/foudroyant"}}

# Store player's rotation
data modify storage {ns}:main Rotation set from entity @s Rotation

# Execute as the sheep the function that will launch it
execute as @e[tag={ns}.new] at @s run function {ns}:utils/launch_entity_in_direction

# Success
scoreboard players set #success {ns}.data 1

""")

	write_function(f"{ns}:sheeps/summon/fragmentation", f"""
#> {ns}:sheeps/summon/fragmentation
#
# @executed			as & at the player
#
# @description		Summons a sheep with tag "fragmentation" and launches it in the direction the player is looking at.
#

# Summon the sheep
summon sheep ^ ^1 ^1 {{Tags:["{ns}.sheep","{ns}.explode","{ns}.fragmentation","{ns}.new"],Color:8,DeathLootTable:"{ns}:i/fragmentation"}}

# Store player's rotation
data modify storage {ns}:main Rotation set from entity @s Rotation

# Execute as the sheep the function that will launch it
execute as @e[tag={ns}.new] at @s run function {ns}:utils/launch_entity_in_direction

# Success
scoreboard players set #success {ns}.data 1

""")

	write_function(f"{ns}:sheeps/summon/glace", f"""
#> {ns}:sheeps/summon/glace
#
# @executed			as & at the player
#
# @description		Summons a sheep with tag "glace" and launches it in the direction the player is looking at.
#

# Summon the sheep
summon sheep ^ ^1 ^1 {{Tags:["{ns}.sheep","{ns}.glace","{ns}.new"],Color:3,DeathLootTable:"{ns}:i/glace"}}

# Store player's rotation
data modify storage {ns}:main Rotation set from entity @s Rotation

# Execute as the sheep the function that will launch it
execute as @e[tag={ns}.new] at @s run function {ns}:utils/launch_entity_in_direction

# Success
scoreboard players set #success {ns}.data 1

""")

	write_function(f"{ns}:sheeps/summon/glouton", f"""
#> {ns}:sheeps/summon/glouton
#
# @executed			as & at the player
#
# @description		Summons a sheep with tag "glouton" and launches it in the direction the player is looking at.
#

# Summon the sheep
summon sheep ^ ^1 ^1 {{Tags:["{ns}.sheep","{ns}.explode","{ns}.glouton","{ns}.new"],Color:13,DeathLootTable:"{ns}:i/glouton"}}

# Store player's rotation
data modify storage {ns}:main Rotation set from entity @s Rotation

# Execute as the sheep the function that will launch it
execute as @e[tag={ns}.new] at @s run function {ns}:utils/launch_entity_in_direction

# Success
scoreboard players set #success {ns}.data 1

""")

	write_function(f"{ns}:sheeps/summon/incendiaire", f"""
#> {ns}:sheeps/summon/incendiaire
#
# @executed			as & at the player
#
# @description		Summons a sheep with tag "incendiaire" and launches it in the direction the player is looking at.
#

# Summon the sheep
summon sheep ^ ^1 ^1 {{Tags:["{ns}.sheep","{ns}.explode","{ns}.incendiaire","{ns}.new"],Color:1,DeathLootTable:"{ns}:i/incendiaire"}}

# Store player's rotation
data modify storage {ns}:main Rotation set from entity @s Rotation

# Execute as the sheep the function that will launch it
execute as @e[tag={ns}.new] at @s run function {ns}:utils/launch_entity_in_direction

# Success
scoreboard players set #success {ns}.data 1

""")

	write_function(f"{ns}:sheeps/summon/intergalactique", f"""
#> {ns}:sheeps/summon/intergalactique
#
# @executed			as & at the player
#
# @description		Summons a sheep with tag "intergalactique" and launches it in the direction the player is looking at.
#

# Summon the sheep
summon sheep ^ ^1 ^1 {{Tags:["{ns}.sheep","{ns}.intergalactique","{ns}.new"],Color:11,DeathLootTable:"minecraft:empty"}}

# Store player's rotation
data modify storage {ns}:main Rotation set from entity @s Rotation

# Execute as the sheep the function that will launch it
execute as @e[tag={ns}.new] at @s run function {ns}:utils/launch_entity_in_direction

# Success
scoreboard players set #success {ns}.data 1

""")

	write_function(f"{ns}:sheeps/summon/sismique", f"""
#> {ns}:sheeps/summon/sismique
#
# @executed			as & at the player
#
# @description		Summons a sheep with tag "sismique" and launches it in the direction the player is looking at.
#

# Summon the sheep
summon sheep ^ ^1 ^1 {{Tags:["{ns}.sheep","{ns}.sismique","{ns}.new"],Color:12,DeathLootTable:"{ns}:i/sismique"}}

# Store player's rotation
data modify storage {ns}:main Rotation set from entity @s Rotation

# Execute as the sheep the function that will launch it
execute as @e[tag={ns}.new] at @s run function {ns}:utils/launch_entity_in_direction

# Success
scoreboard players set #success {ns}.data 1

""")

	write_function(f"{ns}:sheeps/summon/soutien", f"""
#> {ns}:sheeps/summon/soutien
#
# @executed			as & at the player
#
# @description		Summons a sheep with tag "soutien" and apply NBT changes to it
#

# Summon the sheep
summon sheep ^ ^1 ^1 {{Tags:["{ns}.sheep","{ns}.soutien","{ns}.new"],Color:6,DeathLootTable:"minecraft:empty"}}

# Store player's rotation
data modify storage {ns}:main Rotation set from entity @s Rotation

# Execute as the sheep the function that will apply NBT changes
execute as @e[tag={ns}.new] at @s run function {ns}:utils/new_sheep

# Success
scoreboard players set #success {ns}.data 1

""")

	write_function(f"{ns}:sheeps/summon/tenebreux", f"""
#> {ns}:sheeps/summon/tenebreux
#
# @executed			as & at the player
#
# @description		Summons a sheep with tag "tenebreux" and launches it in the direction the player is looking at.
#

# Summon the sheep
summon sheep ^ ^1 ^1 {{Tags:["{ns}.sheep","{ns}.tenebreux","{ns}.new"],Color:15,DeathLootTable:"{ns}:i/tenebreux"}}

# Store player's rotation
data modify storage {ns}:main Rotation set from entity @s Rotation

# Execute as the sheep the function that will launch it
execute as @e[tag={ns}.new] at @s run function {ns}:utils/launch_entity_in_direction

# Success
scoreboard players set #success {ns}.data 1

""")

