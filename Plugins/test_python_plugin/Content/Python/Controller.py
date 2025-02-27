from Model import get_data
from ToolMenuBase import ToolMenuBaseObject

class ControllerObject():
    def __init__(self):
        # Initialize the tool_menus as an empty list
        self.tool_menus = []
        print("Controller has been initialized.")
        
        # Call the method to process data
        self.process_model_data()
    
    # Contacts model for data
    def process_model_data(self):
        model_data = get_data()
        for menu in model_data['menus']:
            # Append each menu to the tool_menus list
            self.tool_menus.append(menu)