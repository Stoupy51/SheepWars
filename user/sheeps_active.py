
# ruff: noqa: E501
# Imports
from beet import Context
from stewbeet import write_function


# Setup sheeps active functions
def setup_sheeps_active_functions(ctx: Context) -> None:
	ns: str = ctx.project_id

	write_function(f"{ns}:sheeps/active/glace/1st_dimension", f"""
#> {ns}:sheeps/active/glace/1st_dimension
#
# @executed			as & at the sheep (position offset)
#
# @description		Look up a 11x11 area for air blocks and replace them with snow layers if possible (if the block under is not air)
#

# Execute for each possible z position
execute positioned ~ ~ ~5 run function {ns}:sheeps/active/glace/2nd_dimension
execute positioned ~ ~ ~4 run function {ns}:sheeps/active/glace/2nd_dimension
execute positioned ~ ~ ~3 run function {ns}:sheeps/active/glace/2nd_dimension
execute positioned ~ ~ ~2 run function {ns}:sheeps/active/glace/2nd_dimension
execute positioned ~ ~ ~1 run function {ns}:sheeps/active/glace/2nd_dimension
execute positioned ~ ~ ~0 run function {ns}:sheeps/active/glace/2nd_dimension
execute positioned ~ ~ ~-1 run function {ns}:sheeps/active/glace/2nd_dimension
execute positioned ~ ~ ~-2 run function {ns}:sheeps/active/glace/2nd_dimension
execute positioned ~ ~ ~-3 run function {ns}:sheeps/active/glace/2nd_dimension
execute positioned ~ ~ ~-4 run function {ns}:sheeps/active/glace/2nd_dimension
execute positioned ~ ~ ~-5 run function {ns}:sheeps/active/glace/2nd_dimension

""")

	write_function(f"{ns}:sheeps/active/glace/2nd_dimension", f"""
#> {ns}:sheeps/active/glace/2nd_dimension
#
# @executed			as & at the sheep (position offset)
#
# @description		Look up a 1x11 area for air blocks and replace them with snow layers if possible (if the block under is not air)
#

# Execute for each possible y position
execute positioned ~ ~5 ~ run function {ns}:sheeps/active/glace/3rd_dimension
execute positioned ~ ~4 ~ run function {ns}:sheeps/active/glace/3rd_dimension
execute positioned ~ ~3 ~ run function {ns}:sheeps/active/glace/3rd_dimension
execute positioned ~ ~2 ~ run function {ns}:sheeps/active/glace/3rd_dimension
execute positioned ~ ~1 ~ run function {ns}:sheeps/active/glace/3rd_dimension
execute positioned ~ ~0 ~ run function {ns}:sheeps/active/glace/3rd_dimension
execute positioned ~ ~-1 ~ run function {ns}:sheeps/active/glace/3rd_dimension
execute positioned ~ ~-2 ~ run function {ns}:sheeps/active/glace/3rd_dimension
execute positioned ~ ~-3 ~ run function {ns}:sheeps/active/glace/3rd_dimension
execute positioned ~ ~-4 ~ run function {ns}:sheeps/active/glace/3rd_dimension
execute positioned ~ ~-5 ~ run function {ns}:sheeps/active/glace/3rd_dimension

""")

	write_function(f"{ns}:sheeps/active/glace/3rd_dimension", f"""
#> {ns}:sheeps/active/glace/3rd_dimension
#
# @executed			as & at the sheep (position offset)
#
# @description		Place snow layers if possible (if the block under is not air) and if the block is already a snow layer, add one layer
#

# Add one layer to the snow layer
execute if block ~ ~ ~ snow[layers=7] run setblock ~ ~ ~ snow[layers=8] replace
execute if block ~ ~ ~ snow[layers=6] run setblock ~ ~ ~ snow[layers=7] replace
execute if block ~ ~ ~ snow[layers=5] run setblock ~ ~ ~ snow[layers=6] replace
execute if block ~ ~ ~ snow[layers=4] run setblock ~ ~ ~ snow[layers=5] replace
execute if block ~ ~ ~ snow[layers=3] run setblock ~ ~ ~ snow[layers=4] replace
execute if block ~ ~ ~ snow[layers=2] run setblock ~ ~ ~ snow[layers=3] replace
execute if block ~ ~ ~ snow[layers=1] run setblock ~ ~ ~ snow[layers=2] replace

# If block is air and placeable, place a snow layer
execute if block ~ ~ ~ #{ns}:non_solid unless block ~ ~-1 ~ #{ns}:unplaceable_snow_on unless block ~ ~ ~ snow run setblock ~ ~ ~ snow[layers=1] replace

""")

	write_function(f"{ns}:sheeps/active/glace/main", f"""
#> {ns}:sheeps/active/glace/main
#
# @executed			as & at the sheep (position offset)
#
# @description		Look up a 11x11x11 area for air blocks and replace them with snow layers if possible (if the block under is air)
#

# Execute for each possible x position
execute positioned ~5 ~ ~ run function {ns}:sheeps/active/glace/1st_dimension
execute positioned ~4 ~ ~ run function {ns}:sheeps/active/glace/1st_dimension
execute positioned ~3 ~ ~ run function {ns}:sheeps/active/glace/1st_dimension
execute positioned ~2 ~ ~ run function {ns}:sheeps/active/glace/1st_dimension
execute positioned ~1 ~ ~ run function {ns}:sheeps/active/glace/1st_dimension
execute positioned ~0 ~ ~ run function {ns}:sheeps/active/glace/1st_dimension
execute positioned ~-1 ~ ~ run function {ns}:sheeps/active/glace/1st_dimension
execute positioned ~-2 ~ ~ run function {ns}:sheeps/active/glace/1st_dimension
execute positioned ~-3 ~ ~ run function {ns}:sheeps/active/glace/1st_dimension
execute positioned ~-4 ~ ~ run function {ns}:sheeps/active/glace/1st_dimension
execute positioned ~-5 ~ ~ run function {ns}:sheeps/active/glace/1st_dimension

""")

	write_function(f"{ns}:sheeps/active/intergalactique/main", f"""
#> {ns}:sheeps/active/intergalactique/main
#
# @executed			as & at the sheep
#
# @description		Summons meteors on the sheep with random offsets
#

# Get player UUID
data modify storage {ns}:main UUID set from entity @s ArmorItems[0].components."minecraft:custom_data".UUID

# Add a temporary tag for markers to rotate on the sheep
tag @s add {ns}.aim_for_meteor

# Summon the meteors (x4)
execute summon marker run function {ns}:sheeps/active/intergalactique/summon_meteor
execute summon marker run function {ns}:sheeps/active/intergalactique/summon_meteor
execute summon marker run function {ns}:sheeps/active/intergalactique/summon_meteor
execute summon marker run function {ns}:sheeps/active/intergalactique/summon_meteor

# Remove the temporary tag
tag @s remove {ns}.aim_for_meteor

""")

	write_function(f"{ns}:sheeps/active/intergalactique/marker_tick", f"""
#> {ns}:sheeps/active/intergalactique/marker_tick
#
# @executed			as & at an intergalactique marker
#
# @description		Function executed every tick, it handles sheeps, wools, and right click detection.
#

# Teleport ahead
tp @s ^ ^ ^0.75

# Do particles
particle large_smoke ~ ~ ~ 1 1 1 0.01 5 force @a
particle flame ~ ~ ~ 1 1 1 0.01 10 force @a

# If block is not air, explode and disappear
scoreboard players set #is_air {ns}.data 0
execute at @s if block ~ ~ ~ air run scoreboard players set #is_air {ns}.data 1
execute at @s if score #is_air {ns}.data matches 0 run function {ns}:sheeps/final/normal_explosion
execute at @s if score #is_air {ns}.data matches 0 run function {ns}:sheeps/final/disappear


""")

	write_function(f"{ns}:sheeps/active/intergalactique/summon_meteor", f"""
#> {ns}:sheeps/active/intergalactique/summon_meteor
#
# @executed			as the new marker & at the sheep
#
# @description		Summons meteors on the sheep with random offsets
#

# Remember player UUID
data modify entity @s data.UUID set from storage {ns}:main UUID

# Add a tag to remember the meteor
tag @s add {ns}.intergalactique_marker

# Get positions
scoreboard players set #10 {ns}.data 10
scoreboard players set #20 {ns}.data 20
execute store result score #x {ns}.data run data get entity @s Pos[0]
execute store result score #y {ns}.data run data get entity @s Pos[1]
execute store result score #z {ns}.data run data get entity @s Pos[2]

# Get random number between 0 and 10 for x and z
execute store result score #x_rand {ns}.data run data get entity @s UUID[0]
execute store result score #z_rand {ns}.data run data get entity @s UUID[1]
scoreboard players operation #x_rand {ns}.data %= #10 {ns}.data
scoreboard players operation #z_rand {ns}.data %= #10 {ns}.data

# Get random number between 0 and 20 for y
execute store result score #y_rand {ns}.data run data get entity @s UUID[2]
scoreboard players operation #y_rand {ns}.data %= #20 {ns}.data

# Apply new positions
scoreboard players add #y {ns}.data 20
scoreboard players remove #x {ns}.data 10
scoreboard players remove #z {ns}.data 10
scoreboard players operation #x {ns}.data += #x_rand {ns}.data
scoreboard players operation #z {ns}.data += #z_rand {ns}.data
scoreboard players operation #y {ns}.data += #y_rand {ns}.data
execute store result entity @s Pos[0] double 1 run scoreboard players get #x {ns}.data
execute store result entity @s Pos[1] double 1 run scoreboard players get #y {ns}.data
execute store result entity @s Pos[2] double 1 run scoreboard players get #z {ns}.data

# Rotation to look at the sheep
execute at @s run tp @s ~ ~ ~ facing entity @n[type=sheep,tag={ns}.aim_for_meteor] feet

# Teleport the marker a bit offset
execute at @s run tp @s ~-16 ~ ~-8
execute if predicate {ns}:random/0.5 at @s run tp @s ~1 ~ ~
execute if predicate {ns}:random/0.5 at @s run tp @s ~2 ~ ~
execute if predicate {ns}:random/0.5 at @s run tp @s ~4 ~ ~
execute if predicate {ns}:random/0.5 at @s run tp @s ~8 ~ ~
execute if predicate {ns}:random/0.5 at @s run tp @s ~16 ~ ~
execute if predicate {ns}:random/0.5 at @s run tp @s ~ ~ ~1
execute if predicate {ns}:random/0.5 at @s run tp @s ~ ~ ~2
execute if predicate {ns}:random/0.5 at @s run tp @s ~ ~ ~4
execute if predicate {ns}:random/0.5 at @s run tp @s ~ ~ ~8

""")

