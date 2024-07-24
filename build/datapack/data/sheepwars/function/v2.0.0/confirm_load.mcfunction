
#> sheepwars:v2.0.0/confirm_load
#
# @within	???
#

## Scoreboards
# Delete all scoreboards
scoreboard objectives remove sheepwars.data
scoreboard objectives remove sheepwars.right_click

# Data scoreboard for math and stuff
scoreboard objectives add sheepwars.data dummy

# Rightclick detection (You should use an invisible warped_fungus_on_a_stick in offhand)
scoreboard objectives add sheepwars.right_click minecraft.used:minecraft.warped_fungus_on_a_stick

# Previous color reminder
scoreboard objectives add sheepwars.previous_color dummy

# Additional
scoreboard objectives add sheepwars.launched_count dummy

# Team with no collision
team add sheepwars.sheeps
team modify sheepwars.sheeps collisionRule never

