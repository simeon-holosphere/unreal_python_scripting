from ToolMenuBase import ToolMenuBaseObject

def some_work():
    print("Successfully did some work!")

my_tool_menu = ToolMenuBaseObject()
my_tool_menu.init(
    parent_menu_name="LevelEditor.MainMenu.Edit",
    parent_section_name="EditMain",
    menu_name="MyExampleOption",
    menu_label="My Example Options",
    menu_tool_tip="This is my example option button that calls execute when clicked.",
    callback_function=some_work
)

print(my_tool_menu.menus)
print(my_tool_menu.menu)