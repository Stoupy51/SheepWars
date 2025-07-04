
# Import database helper
from stewbeet import Context, Mem, add_item_name_and_lore_if_missing, add_private_custom_data_for_namespace, add_smithed_ignore_vanilla_behaviours_convention


# Main function should return a database
def beet_default(ctx: Context):
	if Mem.ctx is None:
		Mem.ctx = ctx
	Mem.definitions = {
		"explosif":			{"id":"minecraft:red_wool",			"item_name":{"text":"Mouton Explosif","color":"red"}},
		"tenebreux":		{"id":"minecraft:black_wool",		"item_name":{"text":"Mouton Ténébreux","color":"dark_gray"}},
		"glouton":			{"id":"minecraft:green_wool",		"item_name":{"text":"Mouton Glouton","color":"green"}},
		"sismique":			{"id":"minecraft:brown_wool",		"item_name":{"text":"Mouton Sismique","color":"#B37520"}},
		"foudroyant":		{"id":"minecraft:yellow_wool",		"item_name":{"text":"Mouton Foudroyant","color":"yellow"}},
		"incendiaire":		{"id":"minecraft:orange_wool",		"item_name":{"text":"Mouton Incendiaire","color":"gold"}},
		"glace":			{"id":"minecraft:light_blue_wool",	"item_name":{"text":"Mouton Glacé","color":"aqua"}},
		"fragmentation":	{"id":"minecraft:light_gray_wool",	"item_name":{"text":"Mouton Fragmentation","color":"gray"}},
		"chercheur":		{"id":"minecraft:lime_wool",		"item_name":{"text":"Mouton Chercheur","color":"green"}},
		"distorsion":		{"id":"minecraft:purple_wool",		"item_name":{"text":"Mouton Distorsion","color":"dark_purple"}},
		"soutien":			{"id":"minecraft:pink_wool",		"item_name":{"text":"Mouton de Soutien","color":"#FF69B4"}},
		"abordage":			{"id":"minecraft:white_wool",		"item_name":{"text":"Mouton d'Abordage","color":"white"}},
		"intergalactique":	{"id":"minecraft:blue_wool",		"item_name":{"text":"Mouton Intergalactique","color":"blue"}},
	}
	for data in Mem.definitions.values():
		data["consumable"] = {"consume_seconds":1024}

	# Final adjustments
	add_item_name_and_lore_if_missing()
	add_private_custom_data_for_namespace()
	add_smithed_ignore_vanilla_behaviours_convention()

