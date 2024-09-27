
#> sheepwars:sheeps/final/normal_explosion
#
# @within			sheepwars:sheeps/final_action
# @executed			as & at the sheep
#
# @description		Explode the sheep with a normal explosion
#

# Particles and sound
particle explosion_emitter ~ ~ ~ 0.5 0.5 0.5 0.1 1
playsound entity.generic.explode block @a[distance=..42] ~ ~ ~ 1 1 0.3

## Tag the player that launched the sheep
# Get player UUID
data modify storage sheepwars:main UUID set from entity @s[type=sheep] ArmorItems[0].components."minecraft:custom_data".UUID
data modify storage sheepwars:main UUID set from entity @s[type=marker] data.UUID
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

# Remove the tag from the owner
tag @a[tag=sheepwars.owner] remove sheepwars.owner


