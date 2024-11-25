
# Import database helper
from python_datapack.utils.database_helper import *

# Main function should return a database
def main(config: dict) -> dict[str, dict]:
	database: dict[str,dict] = {
		"explosif":			{"id":"minecraft:red_wool",			"item_name":'{"text":"Mouton Explosif","color":"red"}'},
		"tenebreux":		{"id":"minecraft:black_wool",		"item_name":'{"text":"Mouton Ténébreux","color":"dark_gray"}'},
		"glouton":			{"id":"minecraft:green_wool",		"item_name":'{"text":"Mouton Glouton","color":"green"}'},
		"sismique":			{"id":"minecraft:brown_wool",		"item_name":'{"text":"Mouton Sismique","color":"#B37520"}'},
		"foudroyant":		{"id":"minecraft:yellow_wool",		"item_name":'{"text":"Mouton Foudroyant","color":"yellow"}'},
		"incendiaire":		{"id":"minecraft:orange_wool",		"item_name":'{"text":"Mouton Incendiaire","color":"gold"}'},
		"glace":			{"id":"minecraft:light_blue_wool",	"item_name":'{"text":"Mouton Glacé","color":"aqua"}'},
		"fragmentation":	{"id":"minecraft:light_gray_wool",	"item_name":'{"text":"Mouton Fragmentation","color":"gray"}'},
		"chercheur":		{"id":"minecraft:lime_wool",		"item_name":'{"text":"Mouton Chercheur","color":"green"}'},
		"distorsion":		{"id":"minecraft:purple_wool",		"item_name":'{"text":"Mouton Distorsion","color":"dark_purple"}'},
		"soutien":			{"id":"minecraft:pink_wool",		"item_name":'{"text":"Mouton de Soutien","color":"#FF69B4"}'},
		"abordage":			{"id":"minecraft:white_wool",		"item_name":'{"text":"Mouton d\'Abordage","color":"white"}'},
		"intergalactique":	{"id":"minecraft:blue_wool",		"item_name":'{"text":"Mouton Intergalactique","color":"blue"}'},
	}
	for data in database.values():
		data["food"] = {"saturation":0, "nutrition":0, "can_always_eat":True, "eat_seconds":1024}
		data["consumable"] = {}

	# Final adjustments
	add_item_name_and_lore_if_missing(config, database)
	add_private_custom_data_for_namespace(config, database)
	add_smithed_ignore_vanilla_behaviours_convention(database)
	print()

	# Return database
	return database

