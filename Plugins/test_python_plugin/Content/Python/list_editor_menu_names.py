import unreal
import sys

def list_menu(keyword, num=5000):
    menu_list = set()
    for i in range(num):
        obj = unreal.find_object(None, "/Engine/Transient.ToolMenus_0:RegisteredMenu_%s" % i)
        if not obj:
            obj = unreal.find_object(None,
                                     f"/Engine/Transient.ToolMenus_0:ToolMenu_{i}") # for backward compatibility
            
            if not obj:
                continue

        menu_name = str(obj.menu_name)
        if menu_name == "None" or keyword != "" and not menu_name.__contains__(keyword):
            continue

        menu_list.add(menu_name)
    return list(menu_list)

keyword = ""
if len(sys.argv) > 1:
    keyword = sys.argv[1]

list = list_menu(keyword, 5000)
for i in range(len(list)):
    print(list[i])
