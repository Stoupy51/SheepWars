
#> sheepwars:sheeps/summon/chercheur
#
# @within			sheepwars:right_click/all
# @executed			as & at the player
#
# @description		Summons a sheep with tag "chercheur" and launches it in the direction the player is looking at.
#

# Summon the sheep
summon sheep ^ ^1 ^1 {DeathLootTable:"sheepwars:i/chercheur",Color:5b,Tags:["sheepwars.sheep","sheepwars.explode","sheepwars.chercheur","sheepwars.new"],Passengers:[{id:"minecraft:husk",Silent:1b,Invulnerable:1b,NoAI:1b,DeathLootTable:"minecraft:empty",IsBaby:1b,Tags:["sheepwars.chercheur_rider"],active_effects:[{id:"minecraft:invisibility",amplifier:1,duration:20000000,show_particles:0b}],Attributes:[{Name:generic.attack_damage,Base:0}]}]}

# Store player's rotation and UUID
data modify storage sheepwars:main Rotation set from entity @s Rotation

# Execute as the sheep the function that will launch it
execute as @e[tag=sheepwars.new] at @s run function sheepwars:utils/launch_entity_in_direction

# Success
scoreboard players set #success sheepwars.data 1

