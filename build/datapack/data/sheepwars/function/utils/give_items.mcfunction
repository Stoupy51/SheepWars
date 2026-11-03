
#> sheepwars:utils/give_items
#
# @within	sheepwars:utils/random_give
#			sheepwars:utils/give_items
#

execute unless data storage sheepwars:main Items[0] run return 0
data remove storage sheepwars:main Items[0].Slot
execute summon item run data modify entity @s Item set from storage sheepwars:main Items[0]
data remove storage sheepwars:main Items[0]
function sheepwars:utils/give_items

