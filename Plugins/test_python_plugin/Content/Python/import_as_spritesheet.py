import unreal
import ImageBatch  
import os
import sys

def create_spritesheet(working_directory, spritesheet_file_name, x_row_count, y_row_count):
    try:
        print(f"Directory path: {working_directory}")
        print(f"Type of ImageBatch module: {type(ImageBatch)}")
        
        images = ImageBatch.ImageBatch(working_directory)  
        
        print(f"Created images object: {images}")
        
        border_list = images.batch_process(images.find_borders)
        print(f"Found borders: {border_list[:3] if len(border_list) >= 3 else border_list}")
        
        optimal_borders = images.minmax_borders(border_list)
        print(f"Optimal borders: {optimal_borders}")
        
        cropped_images = images.batch_process(images.crop_image, optimal_borders)
        print(f"Cropped {len(cropped_images)} images")
        
        stitched_img = images.stitch(cropped_images, x_row_count, y_row_count)
        print("Image stitched successfully")
        
        # Create output directory if it doesn't exist
        output_dir = working_directory 
        if not os.path.exists(output_dir):
            print(f"Creating output directory: {output_dir}")
            os.makedirs(output_dir)
        
        result_dir = output_dir + spritesheet_file_name
        images.save_image(stitched_img, result_dir)
        print("Spritesheet saved")
        
    except Exception as e:
        print(f"Error in create_spritesheet: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()

def import_spritesheet(working_directory, spritesheet_file_name, game_output_dir):
    try:
        # Check for the correct path to the saved spritesheet
        expected_path = working_directory + spritesheet_file_name
        print(f"Expected spritesheet path: {expected_path}")
        print(f"File exists: {os.path.exists(expected_path)}")
        
        # Update the path to use the output directory
        filenames = [
            expected_path 
        ]
        
        print(f"Using path for import: {filenames[0]}")
        print(f"File exists: {os.path.exists(filenames[0])}")

        asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
        print(f"Got asset tools: {asset_tools}")

        asset_import_data = unreal.AutomatedAssetImportData()
        asset_import_data.destination_path = game_output_dir 
        asset_import_data.filenames = filenames
        asset_import_data.replace_existing = True
        
        print("Importing spritesheet with settings:")
        print(f"  Destination: {asset_import_data.destination_path}")
        print(f"  Files: {asset_import_data.filenames}")
        
        result = asset_tools.import_assets_automated(asset_import_data)
        print(f"Import result: {result}")
        
    except Exception as e:
        print(f"Error in import_spritesheet: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()

try:
    working_directory = "C:\\Users\\Simeo\\GithubProjects\\unreal_python_scripting\\Plugins\\test_python_plugin\\Content\\Python\\ExternalArt\\"
    spritesheet_file_name = "new_spritesheet.png"
    game_output_dir = "/Game/Art/Textures/Spritesheet/"

    print("Starting spritesheet creation...")
    create_spritesheet(working_directory, spritesheet_file_name, 10, 10)
    print("Starting spritesheet import...")
    import_spritesheet(working_directory, spritesheet_file_name, game_output_dir)
    print("Process completed successfully")
except Exception as e:
    print(f"Fatal error: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()