
#> sheepwars:sheeps/final/fragmentation
#
# @within	sheepwars:sheeps/final_action
#

#> sheepwars:sheeps/final/fragmentation
#
# @within			sheepwars:sheeps/final_action
# @executed			as & at the sheep
#
# @description		Explode the sheep with a normal explosion and summon 4 new sheeps that will explode after 1 second.
#

# Particles and sound
particle explosion_emitter ~ ~ ~ 0.5 0.5 0.5 0.1 1
playsound entity.generic.explode block @a ~ ~ ~ 1 1 0.3

## Tag the player that launched the sheep
# Get player UUID
data modify storage sheepwars:main UUID set from entity @s ArmorItems[0].components."minecraft:custom_data".UUID
# Search for the player with this UUID
execute as @a run function sheepwars:utils/get_player_from_uuid

## Damage nearby entities
# Damage nearby entities that have a brain
execute as @e[type=!player,tag=!sheepwars.sheep,distance=..1,nbt={Brain:{}},nbt=!{Invulnerable:1b}] run damage @s 28 player_explosion by @p[tag=sheepwars.owner] from @p[tag=sheepwars.owner]
execute as @e[type=!player,tag=!sheepwars.sheep,distance=..2,nbt={Brain:{}},nbt=!{Invulnerable:1b}] run damage @s 20 player_explosion by @p[tag=sheepwars.owner] from @p[tag=sheepwars.owner]
execute as @e[type=!player,tag=!sheepwars.sheep,distance=..3,nbt={Brain:{}},nbt=!{Invulnerable:1b}] run damage @s 12 player_explosion by @p[tag=sheepwars.owner] from @p[tag=sheepwars.owner]
execute as @e[type=!player,tag=!sheepwars.sheep,distance=..4,nbt={Brain:{}},nbt=!{Invulnerable:1b}] run damage @s 8 player_explosion by @p[tag=sheepwars.owner] from @p[tag=sheepwars.owner]
execute as @e[type=!player,tag=!sheepwars.sheep,distance=..5,nbt={Brain:{}},nbt=!{Invulnerable:1b}] run damage @s 4 player_explosion by @p[tag=sheepwars.owner] from @p[tag=sheepwars.owner]
execute as @e[type=!player,tag=!sheepwars.sheep,distance=..6,nbt={Brain:{}},nbt=!{Invulnerable:1b}] run damage @s 2 player_explosion by @p[tag=sheepwars.owner] from @p[tag=sheepwars.owner]

# Damage nearby players
tag @a[gamemode=!creative,gamemode=!spectator,distance=..6] add sheepwars.damaged
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..1] run damage @s 28 player_explosion by @p[tag=sheepwars.owner] from @p[tag=sheepwars.owner]
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..2] run damage @s 20 player_explosion by @p[tag=sheepwars.owner] from @p[tag=sheepwars.owner]
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..3] run damage @s 12 player_explosion by @p[tag=sheepwars.owner] from @p[tag=sheepwars.owner]
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..4] run damage @s 8 player_explosion by @p[tag=sheepwars.owner] from @p[tag=sheepwars.owner]
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..5] run damage @s 4 player_explosion by @p[tag=sheepwars.owner] from @p[tag=sheepwars.owner]
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..6] run damage @s 2 player_explosion by @p[tag=sheepwars.owner] from @p[tag=sheepwars.owner]
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..1] run damage @s[tag=sheepwars.owner] 28 explosion
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..2] run damage @s[tag=sheepwars.owner] 20 explosion
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..3] run damage @s[tag=sheepwars.owner] 12 explosion
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..4] run damage @s[tag=sheepwars.owner] 8 explosion
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..5] run damage @s[tag=sheepwars.owner] 4 explosion
execute as @a[gamemode=!creative,gamemode=!spectator,distance=..6] run damage @s[tag=sheepwars.owner] 2 explosion

# For each player, check if the damage killed him
execute as @a[tag=sheepwars.damaged] run function sheepwars:utils/player_damaged

## Break blocks using Realistic Explosion Library
function realistic_explosion:explode

## Summon 4 new sheeps
summon sheep ~1 ~ ~1 {Tags:["sheepwars.sheep","sheepwars.explode","sheepwars.fragmentation_part","sheepwars.new"],Color:8,DeathLootTable:"minecraft:empty",Age:-1200s,Motion:[0.2d,0.5d,0.2d]}
summon sheep ~1 ~ ~-1 {Tags:["sheepwars.sheep","sheepwars.explode","sheepwars.fragmentation_part","sheepwars.new"],Color:8,DeathLootTable:"minecraft:empty",Age:-1200s,Motion:[0.2d,0.5d,-0.2d]}
summon sheep ~-1 ~ ~1 {Tags:["sheepwars.sheep","sheepwars.explode","sheepwars.fragmentation_part","sheepwars.new"],Color:8,DeathLootTable:"minecraft:empty",Age:-1200s,Motion:[-0.2d,0.5d,0.2d]}
summon sheep ~-1 ~ ~-1 {Tags:["sheepwars.sheep","sheepwars.explode","sheepwars.fragmentation_part","sheepwars.new"],Color:8,DeathLootTable:"minecraft:empty",Age:-1200s,Motion:[-0.2d,0.5d,-0.2d]}
execute as @e[type=sheep,tag=sheepwars.new] run function sheepwars:utils/new_sheep

# Remove the tag from the owner
tag @a[tag=sheepwars.owner] remove sheepwars.owner


