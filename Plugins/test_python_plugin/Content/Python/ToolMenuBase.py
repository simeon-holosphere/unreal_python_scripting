import unreal

@unreal.uclass()
class ToolMenuBaseObject(unreal.ToolMenuEntryScript):
    menus = None
    menu = None
    callback = None

    def init(self, 
                 parent_menu_name, 
                 parent_section_name, 
                 menu_name, 
                 menu_label, 
                 menu_tool_tip,
                 callback_function):

        self.menus = unreal.ToolMenus.get() 
        self.menu = self.menus.find_menu(parent_menu_name)

        self.init_entry(
            owner_name=self.menu.menu_name,
            menu=self.menu.menu_name,
            section=parent_section_name,
            name=menu_name,
            label=menu_label,
            tool_tip=menu_tool_tip
        )

        self.set_callback(callback_function)

        self.register_menu_entry()

    def set_callback(self, callback_function):
        ToolMenuBaseObject.callback = staticmethod(callback_function)

    @unreal.ufunction(override=True)
    def execute(self, context):
       if self.callback:
           self.callback() 
       else:
           print(f"Execute called {context}")