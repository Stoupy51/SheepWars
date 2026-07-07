
# ruff: noqa: E501
# Imports
from beet import Context
from stewbeet import write_function


# Setup magic wool functions
def setup_magic_wool_functions(ctx: Context) -> None:
	ns: str = ctx.project_id

	write_function(f"{ns}:magic_wool/arrow", f"""
#> {ns}:magic_wool/arrow
#
# @executed			as the arrow & at the colored wool marker
#
# @description		Launches a signal (function tag) on the arrow owner (origin) and kill the arrow
#

# Launch a signal on the arrow owner
execute on origin run function #{ns}:signals/magic_wool_shot

# Kill the arrow
scoreboard players set #success {ns}.data 1
kill @s

""")

	write_function(f"{ns}:magic_wool/summon", f"""
#> {ns}:magic_wool/summon
#
# @executed			at the middle position of the requested area
#
# @input score		#dx {ns}.data : The x offset
# @input score		#dy {ns}.data : The y offset
# @input score		#dz {ns}.data : The z offset
#
# @description		Summons a colored wool block at the given coordinates with random offsets.
#

# Summon a marker
execute summon marker run function {ns}:magic_wool/summon_on_marker

""")

	write_function(f"{ns}:magic_wool/summon_on_marker", f"""
#> {ns}:magic_wool/summon_on_marker
#
# @executed			at the middle position of the requested area
#
# @input score		#dx {ns}.data : The x offset
# @input score		#dy {ns}.data : The y offset
# @input score		#dz {ns}.data : The z offset
#
# @description		Get random offsets
#

# Get random offsets by using UUID
execute store result score #rand_x {ns}.data run data get entity @s UUID[0]
execute store result score #rand_y {ns}.data run data get entity @s UUID[1]
execute store result score #rand_z {ns}.data run data get entity @s UUID[2]
scoreboard players operation #rand_x {ns}.data %= #dx {ns}.data
scoreboard players operation #rand_y {ns}.data %= #dy {ns}.data
scoreboard players operation #rand_z {ns}.data %= #dz {ns}.data

# Get current position of the marker
execute store result score #x {ns}.data run data get entity @s Pos[0]
execute store result score #y {ns}.data run data get entity @s Pos[1]
execute store result score #z {ns}.data run data get entity @s Pos[2]

# 50% chance to invert the offsets
scoreboard players set #-1 {ns}.data -1
execute if predicate {ns}:random/0.5 run scoreboard players operation #rand_x {ns}.data *= #-1 {ns}.data
execute if predicate {ns}:random/0.5 run scoreboard players operation #rand_y {ns}.data *= #-1 {ns}.data
execute if predicate {ns}:random/0.5 run scoreboard players operation #rand_z {ns}.data *= #-1 {ns}.data

# Add the offsets to the current position
scoreboard players operation #x {ns}.data += #rand_x {ns}.data
scoreboard players operation #y {ns}.data += #rand_y {ns}.data
scoreboard players operation #z {ns}.data += #rand_z {ns}.data

# Apply the new position to the marker
execute store result entity @s Pos[0] double 1 run scoreboard players get #x {ns}.data
execute store result entity @s Pos[1] double 1 run scoreboard players get #y {ns}.data
execute store result entity @s Pos[2] double 1 run scoreboard players get #z {ns}.data

# Place the colored wool and a tag to the marker
execute at @s run setblock ~ ~ ~ white_wool
tag @s add {ns}.magic_wool

""")

	write_function(f"{ns}:magic_wool/tick", f"""
#> {ns}:magic_wool/tick
#
# @executed			as & at the colored wool marker
#
# @description		Updates the colored wool depending on the time, and launches a signal if there is an arrow on it.
#

# Particles
particle dust{{color:[255,255,255],scale:1}} ~.5 ~.5 ~.5 .5 .5 .5 0 10 force

# Update the colored wool every second
scoreboard players add @s {ns}.data 1
execute if score @s {ns}.data matches 1 run setblock ~ ~ ~ white_wool
execute if score @s {ns}.data matches 21 run setblock ~ ~ ~ orange_wool
execute if score @s {ns}.data matches 41 run setblock ~ ~ ~ magenta_wool
execute if score @s {ns}.data matches 61 run setblock ~ ~ ~ light_blue_wool
execute if score @s {ns}.data matches 81 run setblock ~ ~ ~ yellow_wool
execute if score @s {ns}.data matches 101 run setblock ~ ~ ~ lime_wool
execute if score @s {ns}.data matches 121 run setblock ~ ~ ~ pink_wool
execute if score @s {ns}.data matches 141 run setblock ~ ~ ~ gray_wool
execute if score @s {ns}.data matches 161 run setblock ~ ~ ~ light_gray_wool
execute if score @s {ns}.data matches 181 run setblock ~ ~ ~ cyan_wool
execute if score @s {ns}.data matches 201 run setblock ~ ~ ~ purple_wool
execute if score @s {ns}.data matches 221 run setblock ~ ~ ~ blue_wool
execute if score @s {ns}.data matches 241 run setblock ~ ~ ~ brown_wool
execute if score @s {ns}.data matches 261 run setblock ~ ~ ~ green_wool
execute if score @s {ns}.data matches 281 run setblock ~ ~ ~ red_wool
execute if score @s {ns}.data matches 301 run setblock ~ ~ ~ black_wool
execute if score @s {ns}.data matches 320 run scoreboard players set @s {ns}.data 0

# If there is an arrow on the colored wool, remove the wool and launch a signal
scoreboard players set #success {ns}.data 0
execute as @n[type=arrow,nbt={{inBlockState:{{}}}},distance=..1.69] run function {ns}:magic_wool/arrow
execute if score #success {ns}.data matches 1 run setblock ~ ~ ~ air
execute if score #success {ns}.data matches 1 run kill @s

""")

