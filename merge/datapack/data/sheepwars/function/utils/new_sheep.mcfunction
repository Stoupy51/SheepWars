
#> sheepwars:utils/new_sheep
#
# @within			sheepwars:utils/launch_entity_in_direction
# @within			sheepwars:sheeps/summon/soutien
# @executed			as & at a non-player entity (sheep, etc.)
#
# @input storage	sheepwars:main Rotation : 2D rotation of the entity
# @input storage	sheepwars:main UUID : UUID of the player who launched the entity
#
# @description		Remove "new" tag and store launcher's UUID.
#

# Remove "new" tag
tag @s remove sheepwars.new

# Apply rotation to the entity
data modify entity @s Rotation set from storage sheepwars:main Rotation

# Store the launcher's UUID
data merge entity @s {ArmorItems:[{id:"minecraft:stone",count:1},{},{},{}],ArmorDropChances:[0.0f,0.0f,0.0f,0.0f]}
data modify entity @s ArmorItems[0].components."minecraft:custom_data".UUID set from storage sheepwars:main UUID

# Join the sheepwars.sheeps team (no collisions)
team join sheepwars.sheeps

# Give fire resistance
effect give @s fire_resistance infinite 0 true

# Remove fall damage
attribute @s generic.safe_fall_distance base set 1024

