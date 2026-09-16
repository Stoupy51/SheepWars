
#> sheepwars:sheeps/abordage_mount
#
# @executed	as @e[type=sheep,tag=sheepwars.sheep] & at @s
#
# @within	sheepwars:sheeps/passive_action
#

# Protect the rider from a fall it did not choose, until it lands again
attribute @s safe_fall_distance modifier add sheepwars:abordage 1024 add_value
tag @s add sheepwars.abordage_rider

