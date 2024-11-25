
#> sheepwars:sheeps/tick_sheep
#
# @within	sheepwars:v2.3.1/tick
#

#> sheepwars:sheeps/tick_sheep
#
# @within			sheepwars:tick
# @executed			as & at the sheep
#
# @description		Manages the sheep actions
#

# Increment the sheep timer
scoreboard players add @s sheepwars.data 1

# Manages sheep blinking for sheeps that can explode
execute if score @s[tag=sheepwars.explode] sheepwars.data matches 90.. run function sheepwars:sheeps/blink

# Sheep passive actions
execute if score @s sheepwars.data matches 40.. run function sheepwars:sheeps/passive_action

# Fragmentation parts
execute if score @s sheepwars.data matches 20.. if entity @s[tag=sheepwars.fragmentation_part] run function sheepwars:sheeps/final_action

# Final action of the sheep (Explosion, fire, disappear, etc.)
execute if score @s sheepwars.data matches 190.. run function sheepwars:sheeps/final_action

