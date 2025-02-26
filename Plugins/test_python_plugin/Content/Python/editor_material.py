import unreal
from tool_menu_object import MyScriptObject
import create_random_material_inst
import time

def setup_create_random_material_instance():
    try:
        menus = unreal.ToolMenus.get()
        if menus.find_menu("ContentBrowser.AssetContextMenu.Material.CreateRandomInstancedMaterial"):
            return True
        material_context_menu = menus.find_menu("ContentBrowser.AssetContextMenu.Material")
        script_object = MyScriptObject()
        script_object.set_callback(create_random_material_inst.create_randomized_material_instance_selected)
        script_object.init_entry(
            owner_name=material_context_menu.menu_name,
            menu=material_context_menu.menu_name,
            section="GetAssetActions",
            name="CreateRandomInstancedMaterial",
            label="Create Random Instanced Material",
            tool_tip="This will set a random value for each parameter in your material and create an instanced version of it in a folder in this directory."
        )

        script_object.register_menu_entry()
        print("Successully registered create random material instance button")
        return True
    except Exception as error:
        print("Unsuccessfully registered create random material instance button: ", error)
        return False

def setup():
    if not setup_create_random_material_instance():
        return False

    return True
