
#> sheepwars:magic_wool/particles
#
# @executed	as @e[type=marker,tag=sheepwars.magic_wool] & at @s
#
# @within	sheepwars:magic_wool/tick
#

execute if score @s sheepwars.data matches 1..20 run return run particle dust{color:[1.0,1.0,1.0],scale:1} ~.5 ~.5 ~.5 .5 .5 .5 0 10 force
execute if score @s sheepwars.data matches 21..40 run return run particle dust{color:[0.85,0.5,0.2],scale:1} ~.5 ~.5 ~.5 .5 .5 .5 0 10 force
execute if score @s sheepwars.data matches 41..60 run return run particle dust{color:[0.75,0.3,0.7],scale:1} ~.5 ~.5 ~.5 .5 .5 .5 0 10 force
execute if score @s sheepwars.data matches 61..80 run return run particle dust{color:[0.3,0.6,0.85],scale:1} ~.5 ~.5 ~.5 .5 .5 .5 0 10 force
execute if score @s sheepwars.data matches 81..100 run return run particle dust{color:[0.9,0.8,0.2],scale:1} ~.5 ~.5 ~.5 .5 .5 .5 0 10 force
execute if score @s sheepwars.data matches 101..120 run return run particle dust{color:[0.45,0.75,0.2],scale:1} ~.5 ~.5 ~.5 .5 .5 .5 0 10 force
execute if score @s sheepwars.data matches 121..140 run return run particle dust{color:[0.9,0.55,0.65],scale:1} ~.5 ~.5 ~.5 .5 .5 .5 0 10 force
execute if score @s sheepwars.data matches 141..160 run return run particle dust{color:[0.3,0.3,0.3],scale:1} ~.5 ~.5 ~.5 .5 .5 .5 0 10 force
execute if score @s sheepwars.data matches 161..180 run return run particle dust{color:[0.6,0.6,0.6],scale:1} ~.5 ~.5 ~.5 .5 .5 .5 0 10 force
execute if score @s sheepwars.data matches 181..200 run return run particle dust{color:[0.15,0.5,0.55],scale:1} ~.5 ~.5 ~.5 .5 .5 .5 0 10 force
execute if score @s sheepwars.data matches 201..220 run return run particle dust{color:[0.5,0.2,0.7],scale:1} ~.5 ~.5 ~.5 .5 .5 .5 0 10 force
execute if score @s sheepwars.data matches 221..240 run return run particle dust{color:[0.2,0.25,0.6],scale:1} ~.5 ~.5 ~.5 .5 .5 .5 0 10 force
execute if score @s sheepwars.data matches 241..260 run return run particle dust{color:[0.4,0.25,0.15],scale:1} ~.5 ~.5 ~.5 .5 .5 .5 0 10 force
execute if score @s sheepwars.data matches 261..280 run return run particle dust{color:[0.35,0.45,0.15],scale:1} ~.5 ~.5 ~.5 .5 .5 .5 0 10 force
execute if score @s sheepwars.data matches 281..300 run return run particle dust{color:[0.6,0.2,0.2],scale:1} ~.5 ~.5 ~.5 .5 .5 .5 0 10 force
execute if score @s sheepwars.data matches 301..320 run return run particle dust{color:[0.1,0.1,0.1],scale:1} ~.5 ~.5 ~.5 .5 .5 .5 0 10 force

