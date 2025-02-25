# ContentBrowser.AssetContextMenu.Material
import unreal
from tool_menu_object import MyScriptObject

menus = unreal.ToolMenus.get()
material_context_menu = menus.find_menu("ContentBrowser.AssetContextMenu.Material")
script_object = MyScriptObject()
script_object.init_entry(
    owner_name=material_context_menu.menu_name,
    menu=material_context_menu.menu_name,
    section="GetAssetActions",
    name="CreateRandomInstancedMaterial",
    label="Create Random Instanced Material",
    tool_tip="This will set a random value for each parameter in your material and create an instanced version of it in a folder in this directory."
)
script_object.register_menu_entry()