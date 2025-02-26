import unreal
import random
import re

def create_material_inst(selected_material):
    def_name = selected_material.get_name()

    def_path_name = selected_material.get_path_name()
    def_removed_str = def_name + '.' + def_name
    def_package = def_path_name.replace(def_removed_str, '')
    def_package = def_package + "Instances/"

    def_name = def_name.replace('M_', '')
    def_name = "MI_" + def_name

    assets_in_package_dest = unreal.EditorAssetLibrary.list_assets(def_package, False)
    counter = 0
    assets_found_len = len(assets_in_package_dest)
    if assets_found_len > 0:
        print(f"found {assets_found_len} in {def_package}")
        for i in range(assets_found_len):
            asset_found_name_path = assets_in_package_dest[i]
            asset_found_name_path_split = asset_found_name_path.split('.')
            asset_found_name = asset_found_name_path_split[1]

            # matches mattern with _ then any number and replaces
            pattern = r'_\d+$'
            result_str = re.sub(pattern, '', asset_found_name)
            
            if def_name == result_str:
                counter = counter + 1
    
    if counter > 0:
        def_name = def_name + "_" + str(counter)

    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    material_factory = unreal.MaterialInstanceConstantFactoryNew()
    created_asset = unreal.AssetTools.create_asset(asset_tools, def_name, def_package, None, material_factory)
    
    unreal.MaterialEditingLibrary.set_material_instance_parent(created_asset, selected_material)
    return created_asset

def set_vector_params_rand(instance, vector_param_names):
    for vector_param_name in vector_param_names:
        rand_colour = unreal.LinearColor(random.random(), random.random(), random.random())
        unreal.MaterialEditingLibrary.set_material_instance_vector_parameter_value(instance, vector_param_name, rand_colour) 

def set_scalar_params_rand(instance, scalar_param_names):
    for scalar_param_name in scalar_param_names:
        unreal.MaterialEditingLibrary.set_material_instance_scalar_parameter_value(instance, scalar_param_name, random.random())

def set_static_switch_params_rand(instance, static_switch_param_names):
    for static_switch_param_name in static_switch_param_names:
        unreal.MaterialEditingLibrary.set_material_instance_static_switch_parameter_value(instance, static_switch_param_name, random.getrandbits(1))

def create_randomized_material_instance_selected():
    selected_materials = unreal.EditorUtilityLibrary.get_selected_assets_of_class(asset_class=unreal.Material)
    if len(selected_materials) < 1:
        unreal.EditorDialog.show_message("Asset Creation:", "Select a Material to create an instance of.", unreal.AppMsgType.OK)
    
    for selected_material in selected_materials:
        print(f"selected material: {selected_material}")

        vector_names = unreal.MaterialEditingLibrary.get_vector_parameter_names(selected_material)
        float_names = unreal.MaterialEditingLibrary.get_scalar_parameter_names(selected_material)    
        static_switch_names = unreal.MaterialEditingLibrary.get_static_switch_parameter_names(selected_material)    

        created_asset = create_material_inst(selected_material)

        set_vector_params_rand(created_asset, vector_names)
        set_scalar_params_rand(created_asset, float_names)
        set_static_switch_params_rand(created_asset, static_switch_names)

        if created_asset: 
            created_asset_path = created_asset.get_full_name()
            success_msg = "Created material instance at " + created_asset_path
            unreal.MaterialEditingLibrary.update_material_instance(created_asset)
            unreal.EditorDialog.show_message("Asset Creation:", success_msg, unreal.AppMsgType.OK)
        else:
            unreal.EditorDialog.show_message("Asset Creation:", "Failed to create", unreal.AppMsgType.OK)
