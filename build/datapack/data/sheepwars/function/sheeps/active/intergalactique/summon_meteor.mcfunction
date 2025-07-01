
#> sheepwars:sheeps/active/intergalactique/summon_meteor
#
# @within	sheepwars:sheeps/active/intergalactique/main
#
# @executed			as the new marker & at the sheep
# 
# @description		Summons meteors on the sheep with random offsets
#

# Remember player UUID
data modify entity @s data.UUID set from storage sheepwars:main UUID

# Add a tag to remember the meteor
tag @s add sheepwars.intergalactique_marker

# Get positions
scoreboard players set #10 sheepwars.data 10
scoreboard players set #20 sheepwars.data 20
execute store result score #x sheepwars.data run data get entity @s Pos[0]
execute store result score #y sheepwars.data run data get entity @s Pos[1]
execute store result score #z sheepwars.data run data get entity @s Pos[2]

# Get random number between 0 and 10 for x and z
execute store result score #x_rand sheepwars.data run data get entity @s UUID[0]
execute store result score #z_rand sheepwars.data run data get entity @s UUID[1]
scoreboard players operation #x_rand sheepwars.data %= #10 sheepwars.data
scoreboard players operation #z_rand sheepwars.data %= #10 sheepwars.data

# Get random number between 0 and 20 for y
execute store result score #y_rand sheepwars.data run data get entity @s UUID[2]
scoreboard players operation #y_rand sheepwars.data %= #20 sheepwars.data

# Apply new positions
scoreboard players add #y sheepwars.data 20
scoreboard players remove #x sheepwars.data 10
scoreboard players remove #z sheepwars.data 10
scoreboard players operation #x sheepwars.data += #x_rand sheepwars.data
scoreboard players operation #z sheepwars.data += #z_rand sheepwars.data
scoreboard players operation #y sheepwars.data += #y_rand sheepwars.data
execute store result entity @s Pos[0] double 1 run scoreboard players get #x sheepwars.data
execute store result entity @s Pos[1] double 1 run scoreboard players get #y sheepwars.data
execute store result entity @s Pos[2] double 1 run scoreboard players get #z sheepwars.data

# Rotation to look at the sheep
execute at @s run tp @s ~ ~ ~ facing entity @e[type=sheep,tag=sheepwars.aim_for_meteor,limit=1,sort=nearest] feet

# Teleport the marker a bit offset
execute at @s run tp @s ~-16 ~ ~-8
execute if predicate sheepwars:random/0.5 at @s run tp @s ~1 ~ ~
execute if predicate sheepwars:random/0.5 at @s run tp @s ~2 ~ ~
execute if predicate sheepwars:random/0.5 at @s run tp @s ~4 ~ ~
execute if predicate sheepwars:random/0.5 at @s run tp @s ~8 ~ ~
execute if predicate sheepwars:random/0.5 at @s run tp @s ~16 ~ ~
execute if predicate sheepwars:random/0.5 at @s run tp @s ~ ~ ~1
execute if predicate sheepwars:random/0.5 at @s run tp @s ~ ~ ~2
execute if predicate sheepwars:random/0.5 at @s run tp @s ~ ~ ~4
execute if predicate sheepwars:random/0.5 at @s run tp @s ~ ~ ~8

