
#> sheepwars:sheeps/summon/soutien
#
# @executed	as the player & at current position
#
# @within	sheepwars:right_click/all
#
# @description		Summons a sheep with tag "soutien" and apply NBT changes to it
#

# Summon the sheep
summon sheep ^ ^1 ^1 {Tags:["sheepwars.sheep","sheepwars.soutien","sheepwars.new"],Color:6,DeathLootTable:"minecraft:empty"}

# Store player's rotation
data modify storage sheepwars:main Rotation set from entity @s Rotation

# Execute as the sheep the function that will apply NBT changes
execute as @e[tag=sheepwars.new] at @s run function sheepwars:utils/new_sheep

# Success
scoreboard players set #success sheepwars.data 1

