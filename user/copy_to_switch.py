
# Imports
from stewbeet import Context
import shutil


# Main function should return a database
def beet_default(ctx: Context):
    destination: str = "E:/my_folders/advanced_desktop/Switch/libs/datapack"
    source: str = f"{ctx.output_directory}/SheepWars_datapack_with_libs.zip"
    shutil.copy(source, destination)

