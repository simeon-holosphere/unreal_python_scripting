import unreal

menus = unreal.ToolMenus.get()
main_menu = menus.find_menu("LevelEditor.MainMenu")
tool_menu = main_menu.add_sub_menu("Custom menu", "PythonAutomation", "Menu name", "Menu Label")
if tool_menu:
    menus.refresh_all_widgets()
    print(f"Successfully added menu {tool_menu}")