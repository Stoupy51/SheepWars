
#> sheepwars:sheeps/active/glace/3rd_dimension
#
# @executed	positioned ~ ~5 ~
#
# @within	sheepwars:sheeps/active/glace/2nd_dimension [ positioned ~ ~5 ~ ]
#			sheepwars:sheeps/active/glace/2nd_dimension [ positioned ~ ~4 ~ ]
#			sheepwars:sheeps/active/glace/2nd_dimension [ positioned ~ ~3 ~ ]
#			sheepwars:sheeps/active/glace/2nd_dimension [ positioned ~ ~2 ~ ]
#			sheepwars:sheeps/active/glace/2nd_dimension [ positioned ~ ~1 ~ ]
#			sheepwars:sheeps/active/glace/2nd_dimension [ positioned ~ ~0 ~ ]
#			sheepwars:sheeps/active/glace/2nd_dimension [ positioned ~ ~-1 ~ ]
#			sheepwars:sheeps/active/glace/2nd_dimension [ positioned ~ ~-2 ~ ]
#			sheepwars:sheeps/active/glace/2nd_dimension [ positioned ~ ~-3 ~ ]
#			sheepwars:sheeps/active/glace/2nd_dimension [ positioned ~ ~-4 ~ ]
#			sheepwars:sheeps/active/glace/2nd_dimension [ positioned ~ ~-5 ~ ]
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
execute if block ~ ~ ~ #sheepwars:non_solid unless block ~ ~-1 ~ #sheepwars:unplaceable_snow_on unless block ~ ~ ~ snow run setblock ~ ~ ~ snow[layers=1] replace

