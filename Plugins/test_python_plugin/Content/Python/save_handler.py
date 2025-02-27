import unreal

class SaveHandler:
    def __init__(self):
        self.level_editor = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)
        self.level_editor.on_post_save_world.add_callable(self.on_level_saved)
    
    def on_level_saved(self, save_flags, world, success):
        print(f"Save detected with flags: {save_flags}, success: {success}")

handler = SaveHandler()