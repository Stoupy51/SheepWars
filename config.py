
# Imports
import os
ROOT: str = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")
IGNORE_UNSET: bool = True							# If True, the program will ignore unset optionnal values in the configuration dictionnary


# Folders
MERGE_FOLDER: str = f"{ROOT}/merge"					# If a file exists in both merge and build folder, they will be merged. Otherwise, it's just copied.
BUILD_FOLDER: str = f"{ROOT}/build"					# Folder where the final datapack and resource pack are built
LIBS_FOLDER: str = f"{ROOT}/libs"					# The libraries are copied to the build destination, and merged with the datapack using Weld
BUILD_COPY_DESTINATIONS: tuple[list, list] = (["D:/latest_snapshot/world/datapacks"], None)	# Can be empty lists if you don't want to copy the generated files


# Dev constants
DATABASE_DEBUG: str = f"{ROOT}/database_debug.json"	# Dump of the database for debugging purposes
MERGE_LIBS: bool = True								# Make new zip of merged libraries with the datapack and resource pack using Smithed Weld


# Datapack related constants
AUTHOR: str = "Stoupy51"				# Author(s) name(s) displayed in pack.mcmeta, also used to add convention.debug tag to the players of the same name(s) <-- showing additionnal displays like datapack loading
DATAPACK_NAME: str = "SheepWars"		# Name of the datapack, used for messages and items lore
MINECRAFT_VERSION: str = "1.21"			# Text used when loading the datapack to warn the user when the data version is not right
DATA_VERSION: int = 3947				# Depending on MC version, given by /data get entity @p DataVersion to check if the datapack is not running in an older version of MC
VERSION: str = "2.0.0"					# Datapack version in the following mandatory format: major.minor.patch, ex: 1.0.0 or 1.21.615
NAMESPACE: str = "sheepwars"			# Should be the same you use in the merge folder. Used to namespace functions, tags, etc.
DATAPACK_FORMAT: int = 48				# Pack format version, see https://minecraft.wiki/w/Pack_format#List_of_data_pack_formats
DESCRIPTION = f"{DATAPACK_NAME} [{VERSION}] by {AUTHOR}"	# Pack description displayed in pack.mcmeta

# Technical constants
SOURCE_LORE: list[dict] = [{"text": DATAPACK_NAME,"italic":True,"color":"blue"}]	# Appended lore to any custom item, can be an empty string

# Configuration dictionnary
configuration = {
	"ignore_unset": IGNORE_UNSET,

	"merge_folder": MERGE_FOLDER,
	"build_folder": BUILD_FOLDER,
	"libs_folder": LIBS_FOLDER,
	"build_copy_destinations": BUILD_COPY_DESTINATIONS,
	"database_debug": DATABASE_DEBUG,
	"merge_libs": MERGE_LIBS,
	"author": AUTHOR,
	"datapack_name": DATAPACK_NAME,
	"minecraft_version": MINECRAFT_VERSION,
	"data_version": DATA_VERSION,
	"version": VERSION,
	"namespace": NAMESPACE,
	"datapack_format": DATAPACK_FORMAT,
	"description": DESCRIPTION,
	"source_lore": SOURCE_LORE,
}

