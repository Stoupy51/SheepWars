
# Import database helper
from stewbeet import Context, Mem, Item, add_item_name_and_lore_if_missing, add_private_custom_data_for_namespace, add_smithed_ignore_vanilla_behaviours_convention


# Main function should return a database
def beet_default(ctx: Context):
	if Mem.ctx is None:
		Mem.ctx = ctx

	# New syntax:
	Item(id="explosif", base_item="minecraft:red_wool", components={"item_name":{"text":"Mouton Explosif","color":"red"}})
	Item(id="tenebreux", base_item="minecraft:black_wool", components={"item_name":{"text":"Mouton Ténébreux","color":"dark_gray"}})
	Item(id="glouton", base_item="minecraft:green_wool", components={"item_name":{"text":"Mouton Glouton","color":"green"}})
	Item(id="sismique", base_item="minecraft:brown_wool", components={"item_name":{"text":"Mouton Sismique","color":"#B37520"}})
	Item(id="foudroyant", base_item="minecraft:yellow_wool", components={"item_name":{"text":"Mouton Foudroyant","color":"yellow"}})
	Item(id="incendiaire", base_item="minecraft:orange_wool", components={"item_name":{"text":"Mouton Incendiaire","color":"gold"}})
	Item(id="glace", base_item="minecraft:light_blue_wool", components={"item_name":{"text":"Mouton Glacé","color":"aqua"}})
	Item(id="fragmentation", base_item="minecraft:light_gray_wool", components={"item_name":{"text":"Mouton Fragmentation","color":"gray"}})
	Item(id="chercheur", base_item="minecraft:lime_wool", components={"item_name":{"text":"Mouton Chercheur","color":"green"}})
	Item(id="distorsion", base_item="minecraft:purple_wool", components={"item_name":{"text":"Mouton Distorsion","color":"dark_purple"}})
	Item(id="soutien", base_item="minecraft:pink_wool", components={"item_name":{"text":"Mouton de Soutien","color":"#FF69B4"}})
	Item(id="abordage", base_item="minecraft:white_wool", components={"item_name":{"text":"Mouton d'Abordage","color":"white"}})
	Item(id="intergalactique", base_item="minecraft:blue_wool", components={"item_name":{"text":"Mouton Intergalactique","color":"blue"}})
	for item in Mem.definitions.values():
		item.components["consumable"] = {"consume_seconds":1_000_000}
		item.components["use_effects"] = {"can_sprint": True, "speed_multiplier": 1.0}

	# Final adjustments
	add_item_name_and_lore_if_missing()
	add_private_custom_data_for_namespace()
	add_smithed_ignore_vanilla_behaviours_convention()

