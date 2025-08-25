
#> sheepwars:utils/launch_entity_in_direction
#
# @executed	as @e[tag=sheepwars.new] & at @s
#
# @within	sheepwars:sheeps/summon/abordage [ as @e[tag=sheepwars.new] & at @s ]
#			sheepwars:sheeps/summon/chercheur [ as @e[tag=sheepwars.new] & at @s ]
#			sheepwars:sheeps/summon/distorsion [ as @e[tag=sheepwars.new] & at @s ]
#			sheepwars:sheeps/summon/explosif [ as @e[tag=sheepwars.new] & at @s ]
#			sheepwars:sheeps/summon/foudroyant [ as @e[tag=sheepwars.new] & at @s ]
#			sheepwars:sheeps/summon/fragmentation [ as @e[tag=sheepwars.new] & at @s ]
#			sheepwars:sheeps/summon/glace [ as @e[tag=sheepwars.new] & at @s ]
#			sheepwars:sheeps/summon/glouton [ as @e[tag=sheepwars.new] & at @s ]
#			sheepwars:sheeps/summon/incendiaire [ as @e[tag=sheepwars.new] & at @s ]
#			sheepwars:sheeps/summon/intergalactique [ as @e[tag=sheepwars.new] & at @s ]
#			sheepwars:sheeps/summon/sismique [ as @e[tag=sheepwars.new] & at @s ]
#			sheepwars:sheeps/summon/tenebreux [ as @e[tag=sheepwars.new] & at @s ]
#
# @input storage	sheepwars:main Rotation : 2D rotation of the entity
# @input storage	sheepwars:main UUID : UUID of the player who launched the entity
# 
# @description		Handles the launch of an entity in a direction, remove "new" tag and store launcher's UUID.
#

# Remove the "new" tag and store the launcher's UUID
function sheepwars:utils/new_sheep

## Launch the entity
# Get the motion of the entity by summoning a temporary marker
execute at @s positioned 0 0 0 summon marker at @s run function sheepwars:utils/get_marker_motion

# Apply the motion to the entity
execute store result entity @s Motion[0] double 0.04 run data get storage sheepwars:main Motion[0]
execute store result entity @s Motion[1] double 0.04 run data get storage sheepwars:main Motion[1]
execute store result entity @s Motion[2] double 0.04 run data get storage sheepwars:main Motion[2]

