
#> your_namespace:v1.0.0/load/main
#
# @within	your_namespace:v1.0.0/load/resolve
#

# Avoiding multiple executions of the same load function
execute unless score #your_namespace.loaded load.status matches 1 run function your_namespace:v1.0.0/load/secondary

