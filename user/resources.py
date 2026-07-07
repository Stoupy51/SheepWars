
# ruff: noqa: E501
# Imports
from beet import Advancement, BlockTag, FunctionTag, ItemModifier, LootTable, Predicate
from stewbeet import Context, JsonDict, set_json_encoder


# Setup json resources (loot tables, predicates, tags, ...)
def setup_resources(ctx: Context) -> None:
	ns: str = ctx.project_id

	json_content: JsonDict

	json_content = {"type":"minecraft:block","pools":[{"rolls":1,"bonus_rolls":0,"entries":[{"type":"minecraft:item","name":"minecraft:yellow_shulker_box","functions":[{"function":"minecraft:copy_components","source":"block_entity","include":["minecraft:custom_name","minecraft:container","minecraft:lock","minecraft:container_loot"]}]}],"conditions":[{"condition":"minecraft:inverted","term":{"condition":"minecraft:match_tool","predicate":{"predicates":{"minecraft:custom_data":{"drop_contents":1}}}}}]},{"rolls":1,"bonus_rolls":0,"entries":[{"type":"minecraft:dynamic","name":"minecraft:contents"}],"conditions":[{"condition":"minecraft:match_tool","predicate":{"predicates":{"minecraft:custom_data":{"drop_contents":1}}}}]}],"random_sequence":"minecraft:blocks/yellow_shulker_box","__smithed__":{"priority":{"stage":"early"},"rules":[{"type":"append","target":"pools[0].conditions","source":{"type":"reference","path":"pools[0].conditions[0]"}},{"type":"append","target":"pools","source":{"type":"reference","path":"pools[1]"}}]}}
	ctx.data["minecraft"].loot_tables["blocks/yellow_shulker_box"] = set_json_encoder(LootTable(json_content), max_level=-1)

	json_content = {"criteria":{"requirement":{"trigger":"minecraft:using_item","conditions":{"item":{"predicates":{"minecraft:custom_data":f"{{{ns}:{{}}}}"}}}}},"rewards":{"function":f"{ns}:right_click/all"}}
	ctx.data[ns].advancements["using_item"] = set_json_encoder(Advancement(json_content), max_level=-1)

	json_content = {"function":"minecraft:set_count","count":-1,"add":True}
	ctx.data[ns].item_modifiers["remove_one"] = set_json_encoder(ItemModifier(json_content), max_level=-1)

	json_content = {"pools":[{"rolls":{"min":1,"max":{"min":1,"max":2}},"entries":[{"type":"minecraft:loot_table","weight":20,"value":f"{ns}:i/explosif"},{"type":"minecraft:loot_table","weight":12,"value":f"{ns}:i/tenebreux"},{"type":"minecraft:loot_table","weight":12,"value":f"{ns}:i/glouton"},{"type":"minecraft:loot_table","weight":12,"value":f"{ns}:i/sismique"},{"type":"minecraft:loot_table","weight":12,"value":f"{ns}:i/foudroyant"},{"type":"minecraft:loot_table","weight":12,"value":f"{ns}:i/incendiaire"},{"type":"minecraft:loot_table","weight":12,"value":f"{ns}:i/glace"},{"type":"minecraft:loot_table","weight":8,"value":f"{ns}:i/fragmentation"},{"type":"minecraft:loot_table","weight":8,"value":f"{ns}:i/chercheur"},{"type":"minecraft:loot_table","weight":8,"value":f"{ns}:i/distorsion"},{"type":"minecraft:loot_table","weight":8,"value":f"{ns}:i/soutien"},{"type":"minecraft:loot_table","weight":8,"value":f"{ns}:i/abordage"},{"type":"minecraft:loot_table","weight":2,"value":f"{ns}:i/intergalactique"}]}]}
	ctx.data[ns].loot_tables["basic_drop"] = set_json_encoder(LootTable(json_content), max_level=-1)

	json_content = {"condition":"minecraft:entity_properties","entity":"this","predicate":{"vehicle":{}}}
	ctx.data[ns].predicates["has_vehicle"] = set_json_encoder(Predicate(json_content), max_level=-1)

	json_content = {"condition":"minecraft:random_chance","chance":0.5}
	ctx.data[ns].predicates["random/0.5"] = set_json_encoder(Predicate(json_content), max_level=-1)

	json_content = {"replace":False,"values":["air","cave_air","void_air","structure_void","#wool_carpets","#saplings","#signs","#standing_signs","#wall_signs","moss_carpet","player_head","player_wall_head","short_grass","fern","dead_bush","tall_grass","large_fern","peony","rose_bush","lilac","sunflower","lily_pad","vine","red_mushroom","brown_mushroom","cobweb","water","kelp_plant","seagrass","ladder","tall_seagrass","snow","powder_snow","#leaves","moving_piston","oak_sapling","spruce_sapling","birch_sapling","jungle_sapling","acacia_sapling","dark_oak_sapling","mangrove_propagule","#flowers","mangrove_propagule","cobweb","torch","wall_torch","soul_torch","soul_wall_torch","redstone_torch","spore_blossom","brown_mushroom","red_mushroom","crimson_fungus","warped_fungus","crimson_roots","warped_roots","nether_sprouts","weeping_vines","twisting_vines","water","sugar_cane","kelp","hanging_roots","small_dripleaf","bamboo","end_rod","vine","#corals","dead_tube_coral","dead_brain_coral","dead_bubble_coral","dead_fire_coral","dead_horn_coral","dead_tube_coral_fan","dead_brain_coral_fan","dead_bubble_coral_fan","dead_fire_coral_fan","dead_horn_coral_fan","scaffolding","#flower_pots","#banners","lantern","soul_lantern","candle","small_amethyst_bud","medium_amethyst_bud","large_amethyst_bud","amethyst_cluster","redstone_wire","repeater","comparator","lever","tripwire_hook","#buttons","#pressure_plates","#rails","conduit"]}
	ctx.data[ns].block_tags["non_solid"] = set_json_encoder(BlockTag(json_content))

	json_content = {"replace":False,"values":[f"#{ns}:non_solid","#minecraft:trapdoors","#minecraft:slabs","#minecraft:stairs","#minecraft:walls","#minecraft:fences","#minecraft:signs"]}
	ctx.data[ns].block_tags["unplaceable_snow_on"] = set_json_encoder(BlockTag(json_content))

	json_content = {"values":[]}
	ctx.data[ns].function_tags["signals/magic_wool_shot"] = set_json_encoder(FunctionTag(json_content))

	json_content = {"values":[]}
	ctx.data[ns].function_tags["signals/player_killed"] = set_json_encoder(FunctionTag(json_content))

