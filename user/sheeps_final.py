
# ruff: noqa: E501
# Imports
from beet import Context
from stewbeet import write_function


# Setup sheeps final functions
def setup_sheeps_final_functions(ctx: Context) -> None:
	ns: str = ctx.project_id

	write_function(f"{ns}:sheeps/final/disappear", f"""
#> {ns}:sheeps/final/disappear
#
# @executed			as & at the sheep
#
# @description		Remove the sheep from the game.
#

# Unride any rider
execute on passengers run ride @s[type=player] dismount

# Remove the sheep
tp @s 0 -10000 0
kill @s

""")

	write_function(f"{ns}:sheeps/final/fire_explosion", f"""
#> {ns}:sheeps/final/fire_explosion
#
# @executed			as & at the sheep
#
# @description		Explode the sheep with an explosion that creates fire
#

# Particles and sound
particle explosion_emitter ~ ~ ~ 0.5 0.5 0.5 0.1 1
playsound entity.generic.explode block @a[distance=..42] ~ ~ ~ 1 1 0.3

## Tag the player that launched the sheep
# Get player UUID
data modify storage {ns}:main UUID set from entity @s ArmorItems[0].components."minecraft:custom_data".UUID
# Search for the player with this UUID
execute as @a run function {ns}:utils/get_player_from_uuid

## Damage nearby entities
# Damage nearby entities that have a brain
execute as @e[type=!player,tag=!{ns}.sheep,distance=..1,nbt={{Brain:{{}}}},nbt=!{{Invulnerable:1b}}] run damage @s 28 player_explosion by @p[tag={ns}.owner] from @p[tag={ns}.owner]
execute as @e[type=!player,tag=!{ns}.sheep,distance=..2,nbt={{Brain:{{}}}},nbt=!{{Invulnerable:1b}}] run damage @s 20 player_explosion by @p[tag={ns}.owner] from @p[tag={ns}.owner]
execute as @e[type=!player,tag=!{ns}.sheep,distance=..3,nbt={{Brain:{{}}}},nbt=!{{Invulnerable:1b}}] run damage @s 12 player_explosion by @p[tag={ns}.owner] from @p[tag={ns}.owner]
execute as @e[type=!player,tag=!{ns}.sheep,distance=..4,nbt={{Brain:{{}}}},nbt=!{{Invulnerable:1b}}] run damage @s 8 player_explosion by @p[tag={ns}.owner] from @p[tag={ns}.owner]
execute as @e[type=!player,tag=!{ns}.sheep,distance=..5,nbt={{Brain:{{}}}},nbt=!{{Invulnerable:1b}}] run damage @s 4 player_explosion by @p[tag={ns}.owner] from @p[tag={ns}.owner]
execute as @e[type=!player,tag=!{ns}.sheep,distance=..6,nbt={{Brain:{{}}}},nbt=!{{Invulnerable:1b}}] run damage @s 2 player_explosion by @p[tag={ns}.owner] from @p[tag={ns}.owner]

# Damage nearby players
tag @a[gamemode=!creative,gamemode=!spectator,distance=..6] add {ns}.damaged
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..1] run damage @s 28 player_explosion by @p[tag={ns}.owner] from @p[tag={ns}.owner]
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..2] run damage @s 20 player_explosion by @p[tag={ns}.owner] from @p[tag={ns}.owner]
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..3] run damage @s 12 player_explosion by @p[tag={ns}.owner] from @p[tag={ns}.owner]
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..4] run damage @s 8 player_explosion by @p[tag={ns}.owner] from @p[tag={ns}.owner]
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..5] run damage @s 4 player_explosion by @p[tag={ns}.owner] from @p[tag={ns}.owner]
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..6] run damage @s 2 player_explosion by @p[tag={ns}.owner] from @p[tag={ns}.owner]
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..1] run damage @s[tag={ns}.owner] 28 explosion
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..2] run damage @s[tag={ns}.owner] 20 explosion
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..3] run damage @s[tag={ns}.owner] 12 explosion
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..4] run damage @s[tag={ns}.owner] 8 explosion
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..5] run damage @s[tag={ns}.owner] 4 explosion
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..6] run damage @s[tag={ns}.owner] 2 explosion

# For each player, check if the damage killed him
execute as @a[tag={ns}.damaged] run function {ns}:utils/player_damaged

## Break blocks using Realistic Explosion Library
scoreboard players set #falling_fire realistic_explosion.data 1
execute positioned ~1 ~1 ~1 run function realistic_explosion:explode
execute positioned ~-1 ~1 ~1 run function realistic_explosion:explode
execute positioned ~1 ~1 ~-1 run function realistic_explosion:explode
execute positioned ~-1 ~1 ~-1 run function realistic_explosion:explode
execute positioned ~1 ~-1 ~1 run function realistic_explosion:explode
execute positioned ~-1 ~-1 ~1 run function realistic_explosion:explode
execute positioned ~1 ~-1 ~-1 run function realistic_explosion:explode
execute positioned ~-1 ~-1 ~-1 run function realistic_explosion:explode
scoreboard players reset #falling_fire realistic_explosion.data

# Remove the tag from the owner
tag @a[tag={ns}.owner] remove {ns}.owner


""")

	write_function(f"{ns}:sheeps/final/fragmentation", f"""
#> {ns}:sheeps/final/fragmentation
#
# @executed			as & at the sheep
#
# @description		Explode the sheep with a normal explosion and summon 4 new sheeps that will explode after 1 second.
#

# Particles and sound
particle explosion_emitter ~ ~ ~ 0.5 0.5 0.5 0.1 1
playsound entity.generic.explode block @a[distance=..42] ~ ~ ~ 1 1 0.3

## Tag the player that launched the sheep
# Get player UUID
data modify storage {ns}:main UUID set from entity @s ArmorItems[0].components."minecraft:custom_data".UUID
# Search for the player with this UUID
execute as @a run function {ns}:utils/get_player_from_uuid

## Damage nearby entities
# Damage nearby entities that have a brain
execute as @e[type=!player,tag=!{ns}.sheep,distance=..1,nbt={{Brain:{{}}}},nbt=!{{Invulnerable:1b}}] run damage @s 28 player_explosion by @p[tag={ns}.owner] from @p[tag={ns}.owner]
execute as @e[type=!player,tag=!{ns}.sheep,distance=..2,nbt={{Brain:{{}}}},nbt=!{{Invulnerable:1b}}] run damage @s 20 player_explosion by @p[tag={ns}.owner] from @p[tag={ns}.owner]
execute as @e[type=!player,tag=!{ns}.sheep,distance=..3,nbt={{Brain:{{}}}},nbt=!{{Invulnerable:1b}}] run damage @s 12 player_explosion by @p[tag={ns}.owner] from @p[tag={ns}.owner]
execute as @e[type=!player,tag=!{ns}.sheep,distance=..4,nbt={{Brain:{{}}}},nbt=!{{Invulnerable:1b}}] run damage @s 8 player_explosion by @p[tag={ns}.owner] from @p[tag={ns}.owner]
execute as @e[type=!player,tag=!{ns}.sheep,distance=..5,nbt={{Brain:{{}}}},nbt=!{{Invulnerable:1b}}] run damage @s 4 player_explosion by @p[tag={ns}.owner] from @p[tag={ns}.owner]
execute as @e[type=!player,tag=!{ns}.sheep,distance=..6,nbt={{Brain:{{}}}},nbt=!{{Invulnerable:1b}}] run damage @s 2 player_explosion by @p[tag={ns}.owner] from @p[tag={ns}.owner]

# Damage nearby players
tag @a[gamemode=!creative,gamemode=!spectator,distance=..6] add {ns}.damaged
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..1] run damage @s 28 player_explosion by @p[tag={ns}.owner] from @p[tag={ns}.owner]
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..2] run damage @s 20 player_explosion by @p[tag={ns}.owner] from @p[tag={ns}.owner]
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..3] run damage @s 12 player_explosion by @p[tag={ns}.owner] from @p[tag={ns}.owner]
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..4] run damage @s 8 player_explosion by @p[tag={ns}.owner] from @p[tag={ns}.owner]
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..5] run damage @s 4 player_explosion by @p[tag={ns}.owner] from @p[tag={ns}.owner]
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..6] run damage @s 2 player_explosion by @p[tag={ns}.owner] from @p[tag={ns}.owner]
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..1] run damage @s[tag={ns}.owner] 28 explosion
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..2] run damage @s[tag={ns}.owner] 20 explosion
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..3] run damage @s[tag={ns}.owner] 12 explosion
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..4] run damage @s[tag={ns}.owner] 8 explosion
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..5] run damage @s[tag={ns}.owner] 4 explosion
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..6] run damage @s[tag={ns}.owner] 2 explosion

# For each player, check if the damage killed him
execute as @a[tag={ns}.damaged] run function {ns}:utils/player_damaged

## Break blocks using Realistic Explosion Library
function realistic_explosion:explode

## Summon 4 new sheeps
summon sheep ~1 ~ ~1 {{Tags:["{ns}.sheep","{ns}.explode","{ns}.fragmentation_part","{ns}.new"],Color:8,DeathLootTable:"minecraft:empty",Age:-1200s,Motion:[0.2d,0.5d,0.2d]}}
summon sheep ~1 ~ ~-1 {{Tags:["{ns}.sheep","{ns}.explode","{ns}.fragmentation_part","{ns}.new"],Color:8,DeathLootTable:"minecraft:empty",Age:-1200s,Motion:[0.2d,0.5d,-0.2d]}}
summon sheep ~-1 ~ ~1 {{Tags:["{ns}.sheep","{ns}.explode","{ns}.fragmentation_part","{ns}.new"],Color:8,DeathLootTable:"minecraft:empty",Age:-1200s,Motion:[-0.2d,0.5d,0.2d]}}
summon sheep ~-1 ~ ~-1 {{Tags:["{ns}.sheep","{ns}.explode","{ns}.fragmentation_part","{ns}.new"],Color:8,DeathLootTable:"minecraft:empty",Age:-1200s,Motion:[-0.2d,0.5d,-0.2d]}}
execute as @e[type=sheep,tag={ns}.new] run function {ns}:utils/new_sheep

# Remove the tag from the owner
tag @a[tag={ns}.owner] remove {ns}.owner


""")

	write_function(f"{ns}:sheeps/final/normal_explosion", f"""
#> {ns}:sheeps/final/normal_explosion
#
# @executed			as & at the sheep
#
# @description		Explode the sheep with a normal explosion
#

# Particles and sound
particle explosion_emitter ~ ~ ~ 0.5 0.5 0.5 0.1 1
playsound entity.generic.explode block @a[distance=..42] ~ ~ ~ 1 1 0.3

## Tag the player that launched the sheep
# Get player UUID
data modify storage {ns}:main UUID set from entity @s[type=sheep] ArmorItems[0].components."minecraft:custom_data".UUID
data modify storage {ns}:main UUID set from entity @s[type=marker] data.UUID
# Search for the player with this UUID
execute as @a run function {ns}:utils/get_player_from_uuid

## Damage nearby entities
# Damage nearby entities that have a brain
execute as @e[type=!player,tag=!{ns}.sheep,distance=..1,nbt={{Brain:{{}}}},nbt=!{{Invulnerable:1b}}] run damage @s 28 player_explosion by @p[tag={ns}.owner] from @p[tag={ns}.owner]
execute as @e[type=!player,tag=!{ns}.sheep,distance=..2,nbt={{Brain:{{}}}},nbt=!{{Invulnerable:1b}}] run damage @s 20 player_explosion by @p[tag={ns}.owner] from @p[tag={ns}.owner]
execute as @e[type=!player,tag=!{ns}.sheep,distance=..3,nbt={{Brain:{{}}}},nbt=!{{Invulnerable:1b}}] run damage @s 12 player_explosion by @p[tag={ns}.owner] from @p[tag={ns}.owner]
execute as @e[type=!player,tag=!{ns}.sheep,distance=..4,nbt={{Brain:{{}}}},nbt=!{{Invulnerable:1b}}] run damage @s 8 player_explosion by @p[tag={ns}.owner] from @p[tag={ns}.owner]
execute as @e[type=!player,tag=!{ns}.sheep,distance=..5,nbt={{Brain:{{}}}},nbt=!{{Invulnerable:1b}}] run damage @s 4 player_explosion by @p[tag={ns}.owner] from @p[tag={ns}.owner]
execute as @e[type=!player,tag=!{ns}.sheep,distance=..6,nbt={{Brain:{{}}}},nbt=!{{Invulnerable:1b}}] run damage @s 2 player_explosion by @p[tag={ns}.owner] from @p[tag={ns}.owner]

# Damage nearby players
tag @a[gamemode=!creative,gamemode=!spectator,distance=..6] add {ns}.damaged
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..1] run damage @s 28 player_explosion by @p[tag={ns}.owner] from @p[tag={ns}.owner]
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..2] run damage @s 20 player_explosion by @p[tag={ns}.owner] from @p[tag={ns}.owner]
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..3] run damage @s 12 player_explosion by @p[tag={ns}.owner] from @p[tag={ns}.owner]
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..4] run damage @s 8 player_explosion by @p[tag={ns}.owner] from @p[tag={ns}.owner]
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..5] run damage @s 4 player_explosion by @p[tag={ns}.owner] from @p[tag={ns}.owner]
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..6] run damage @s 2 player_explosion by @p[tag={ns}.owner] from @p[tag={ns}.owner]
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..1] run damage @s[tag={ns}.owner] 28 explosion
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..2] run damage @s[tag={ns}.owner] 20 explosion
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..3] run damage @s[tag={ns}.owner] 12 explosion
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..4] run damage @s[tag={ns}.owner] 8 explosion
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..5] run damage @s[tag={ns}.owner] 4 explosion
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..6] run damage @s[tag={ns}.owner] 2 explosion


# For each player, check if the damage killed him
execute as @a[tag={ns}.damaged] run function {ns}:utils/player_damaged

## Break blocks using Realistic Explosion Library
function realistic_explosion:explode

# Remove the tag from the owner
tag @a[tag={ns}.owner] remove {ns}.owner


""")

