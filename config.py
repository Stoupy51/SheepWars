
# Imports
import os
ROOT: str = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")
IGNORE_UNSET: bool = True							# If True, the program will ignore unset optionnal values in the configuration dictionnary


# Folders
ASSETS_FOLDER: str = f"{ROOT}/assets"				# Folder where the assets are stored
MERGE_FOLDER: str = f"{ROOT}/merge"					# If a file exists in both merge and build folder, they will be merged. Otherwise, it's just copied.
BUILD_FOLDER: str = f"{ROOT}/build"					# Folder where the final datapack and resource pack are built
LIBS_FOLDER: str = f"{ROOT}/libs"					# The libraries are copied to the build destination, and merged with the datapack using Weld
BUILD_COPY_DESTINATIONS: tuple[list, list] = (["D:/latest_snapshot/world/datapacks"], ["D:/minecraft/snapshot/resourcepacks"])	# Can be empty lists if you don't want to copy the generated files to other folders.


# Dev constants
DATABASE_DEBUG: str = f"{ROOT}/database_debug.json"	# Dump of the database for debugging purposes
MERGE_LIBS: bool = True								# Make new zip of merged libraries with the datapack and resource pack using Smithed Weld


# Datapack related constants
AUTHOR: str = "Stoupy51"				# Author(s) name(s) displayed in pack.mcmeta, also used to add convention.debug tag to the players of the same name(s) <-- showing additionnal displays like datapack loading
PROJECT_NAME: str = "SheepWars"		# Name of the datapack, used for messages and items lore
VERSION: str = "2.3.2"					# Datapack version in the following mandatory format: major.minor.patch, ex: 1.0.0 or 1.21.615
NAMESPACE: str = "sheepwars"			# Used to namespace functions, tags, etc. Should be the same you use in the merge folder.
DESCRIPTION = f"{PROJECT_NAME} [{VERSION}] by {AUTHOR}"	# Pack description displayed in pack.mcmeta

# Technical constants
SOURCE_LORE: list[dict] = [{"text": PROJECT_NAME,"italic":True,"color":"blue"}]	# Appended lore to any custom item, can be an empty string

# Configuration dictionnary
configuration = {
	"ignore_unset": IGNORE_UNSET,

	"assets_folder": ASSETS_FOLDER,
	"merge_folder": MERGE_FOLDER,
	"build_folder": BUILD_FOLDER,
	"libs_folder": LIBS_FOLDER,
	"build_copy_destinations": BUILD_COPY_DESTINATIONS,
	"database_debug": DATABASE_DEBUG,
	"merge_libs": MERGE_LIBS,
	"author": AUTHOR,
	"project_name": PROJECT_NAME,
	"version": VERSION,
	"namespace": NAMESPACE,
	"description": DESCRIPTION,
	"source_lore": SOURCE_LORE,
}

