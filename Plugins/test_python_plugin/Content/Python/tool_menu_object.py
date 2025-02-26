import unreal
import os

@unreal.uclass()
class MyScriptObject(unreal.ToolMenuEntryScript):
    callback = None

    def set_callback(self, callback_function):
        MyScriptObject.callback = staticmethod(callback_function)

    @unreal.ufunction(override=True)
    def execute(self, context):
        if self.callback:
            self.callback()
        else:
            print("SCRIPT EXECUTED")
