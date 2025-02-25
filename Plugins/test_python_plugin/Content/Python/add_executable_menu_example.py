import unreal

@unreal.uclass()
class MyScriptObject(unreal.ToolMenuEntryScript):
    @unreal.ufunction(override=True)
    def execute(self, context):
        print("SCRIPT EXECUTED")

menus = unreal.ToolMenus.get()
edit_menu = menus.find_menu("LevelEditor.MainMenu.Edit")
script_object = MyScriptObject()
script_object.init_entry(
    owner_name=edit_menu.menu_name,
    menu=edit_menu.menu_name,
    section="EditMain",
    name="Custom Menu Option",
    label="Custom Menu Option",
    tool_tip="Custom Menu Option that runs Custom Script"
)
script_object.register_menu_entry()