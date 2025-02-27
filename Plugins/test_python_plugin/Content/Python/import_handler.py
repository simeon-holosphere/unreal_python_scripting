import unreal
import traceback

# Global variable to prevent multiple instances
_import_handler_instance = None

class ImportHandler():
    def __init__(self):
        self.log_to_output("ImportHandler: Initializing...")
        try:
            editor_subsystem = unreal.get_editor_subsystem(unreal.ImportSubsystem)
            # Remove existing delegates before adding new one
            try:
                # Check if we already have an existing delegate
                delegates = editor_subsystem.on_asset_post_import.get_all_objects()
                if len(delegates) > 0:
                    self.log_to_output(f"ImportHandler: Clearing {len(delegates)} existing delegates")
                    editor_subsystem.on_asset_post_import.clear()
            except Exception as e:
                self.log_to_output(f"ImportHandler: Could not clear existing delegates - {str(e)}")
                
            # Add our callback
            editor_subsystem.on_asset_post_import.add_callable(self.on_asset_post_import)
            self.log_to_output("ImportHandler: Successfully registered on_asset_post_import callback")
        except Exception as e:
            self.log_to_output(f"ImportHandler: Failed to initialize - {str(e)}\n{traceback.format_exc()}")
        
    def log_to_output(self, message):
        """
        Logs messages to both the Unreal output log and Python's print for easier debugging
        """
        unreal.log(message)
        # Avoid duplicate logging by not using print, which also writes to LogPython
        
    def get_asset_prefix_by_type(self, type_string):
        """
        Returns the appropriate Unreal Engine prefix for the given asset type.

        Args:
            type_string: The type of asset (e.g., "Texture", "Material", "Blueprint")

        Returns:
            The appropriate prefix for the asset type
        """
        prefix_map = {
            # Textures
            "Texture": "T_",
            "Texture2D": "T_",
            "TextureCube": "TC_",
            "TextureRenderTarget": "RT_",
            "TextureRenderTarget2D": "RT_",
            "TextureRenderTargetCube": "RTC_",
            "TextureLightProfile": "TLP_",

            # Materials
            "Material": "M_",
            "MaterialInstanceConstant": "MI_",
            "MaterialFunction": "MF_",
            "MaterialParameterCollection": "MPC_",

            # Blueprints
            "Blueprint": "BP_",
            "WidgetBlueprint": "WBP_",
            "AnimBlueprint": "ABP_",

            # Static Meshes
            "StaticMesh": "SM_",
            "SkeletalMesh": "SK_",

            # Animations
            "Animation": "A_",
            "AnimationSequence": "A_",
            "AnimMontage": "AM_",
            "AnimComposite": "AC_",
            "BlendSpace": "BS_",
            "BlendSpace1D": "BS_",
            "AimOffset": "AO_",
            "AimOffset1D": "AO_",

            # Physics
            "PhysicsAsset": "PHYS_",
            "DestructibleMesh": "DM_",
            "PhysicalMaterial": "PM_",

            # Sounds
            "SoundWave": "S_",
            "SoundCue": "SC_",
            "SoundAttenuation": "SA_",
            "SoundMix": "Mix_",
            "ReverbEffect": "Reverb_",

            # Particle Systems
            "ParticleSystem": "P_",
            "CascadeParticleSystem": "P_",
            "NiagaraSystem": "NS_",
            "NiagaraEmitter": "NE_",

            # User Interfaces
            "WidgetBlueprint": "WBP_",
            "UserWidget": "W_",
            "Slate": "S_",
            "UMG": "UMG_",
            "Font": "Font_",

            # Data Assets
            "DataAsset": "DA_",
            "CurveTable": "Curve_",
            "DataTable": "DT_",
            "CurveFloat": "Curve_",
            "CurveVector": "Curve_",
            "CurveLinearColor": "Curve_",

            # Levels
            "World": "L_",
            "Level": "L_",
            "Map": "L_",

            # AI
            "BehaviorTree": "BT_",
            "BlackboardData": "BB_",
            "AIController": "AIC_",

            # Miscellaneous
            "LandscapeGrassType": "LG_",
            "LandscapeLayerInfoObject": "LL_",
            "MediaPlayer": "MP_",
            "MediaTexture": "MT_",
            "SubsurfaceProfile": "SP_",

            # Default (if no match is found)
            "Default": ""
        }

        # Return the prefix for the type, or the default if not found
        prefix = prefix_map.get(type_string, prefix_map["Default"])
        self.log_to_output(f"ImportHandler: Asset type '{type_string}' mapped to prefix '{prefix}'")
        return prefix

    def get_file_location_by_type(self, type_string):
        """
        Returns the appropriate folder path in the Art directory for the given asset type.

        Args:
            type_string: The type of asset (e.g., "Texture", "Material", "Blueprint")

        Returns:
            The appropriate folder path for the asset type
        """
        folder_map = {
            # Textures
            "Texture": "Art/Textures",
            "Texture2D": "Art/Textures",
            "TextureCube": "Art/Textures/Cubemaps",
            "TextureRenderTarget": "Art/Textures/RenderTargets",
            "TextureRenderTarget2D": "Art/Textures/RenderTargets",
            "TextureRenderTargetCube": "Art/Textures/RenderTargets",
            "TextureLightProfile": "Art/Textures/LightProfiles",

            # Materials
            "Material": "Art/Materials",
            "MaterialInstanceConstant": "Art/Materials/Instances",
            "MaterialFunction": "Art/Materials/Functions",
            "MaterialParameterCollection": "Art/Materials/ParameterCollections",

            # Blueprints
            "Blueprint": "Blueprints",
            "WidgetBlueprint": "UI",
            "AnimBlueprint": "Animation/Blueprints",

            # Static Meshes
            "StaticMesh": "Art/Meshes/StaticMeshes",
            "SkeletalMesh": "Art/Meshes/SkeletalMeshes",

            # Animations
            "Animation": "Animation",
            "AnimationSequence": "Animation/Sequences",
            "AnimMontage": "Animation/Montages",
            "AnimComposite": "Animation/Composites",
            "BlendSpace": "Animation/BlendSpaces",
            "BlendSpace1D": "Animation/BlendSpaces",
            "AimOffset": "Animation/AimOffsets",
            "AimOffset1D": "Animation/AimOffsets",

            # Physics
            "PhysicsAsset": "Physics",
            "DestructibleMesh": "Physics/Destructibles",
            "PhysicalMaterial": "Physics/Materials",

            # Sounds
            "SoundWave": "Audio/Waves",
            "SoundCue": "Audio/Cues",
            "SoundAttenuation": "Audio/Attenuation",
            "SoundMix": "Audio/Mixes",
            "ReverbEffect": "Audio/Reverb",

            # Particle Systems
            "ParticleSystem": "Art/Effects/Particles",
            "CascadeParticleSystem": "Art/Effects/Particles/Cascade",
            "NiagaraSystem": "Art/Effects/Particles/Niagara/Systems",
            "NiagaraEmitter": "Art/Effects/Particles/Niagara/Emitters",

            # User Interfaces
            "WidgetBlueprint": "UI/Widgets",
            "UserWidget": "UI/Widgets",
            "Slate": "UI/Slate",
            "UMG": "UI/UMG",
            "Font": "Art/UI/Fonts",

            # Data Assets
            "DataAsset": "DataAssets",
            "CurveTable": "DataAssets/Curves",
            "DataTable": "DataAssets/Tables",
            "CurveFloat": "DataAssets/Curves",
            "CurveVector": "DataAssets/Curves",
            "CurveLinearColor": "DataAssets/Curves",

            # Levels
            "World": "Levels",
            "Level": "Levels",
            "Map": "Levels",

            # AI
            "BehaviorTree": "AI/BehaviorTrees",
            "BlackboardData": "AI/Blackboards",
            "AIController": "AI/Controllers",

            # Miscellaneous
            "LandscapeGrassType": "Art/Landscape/Grass",
            "LandscapeLayerInfoObject": "Art/Landscape/Layers",
            "MediaPlayer": "Art/Media/Players",
            "MediaTexture": "Art/Media/Textures",
            "SubsurfaceProfile": "Art/Materials/SubsurfaceProfiles",

            # Default (if no match is found)
            "Default": "Art/Miscellaneous"
        }

        # Return the folder path for the type, or the default if not found
        location = folder_map.get(type_string, folder_map["Default"])
        self.log_to_output(f"ImportHandler: Asset type '{type_string}' mapped to folder path '{location}'")
        return location

    def on_asset_post_import(self, factory, created_object):
        self.log_to_output("ImportHandler: Asset post-import callback triggered")
        
        try:
            # Check if created_object is valid
            if not created_object:
                self.log_to_output("ImportHandler: ERROR - created_object is None or invalid")
                return
                
            self.log_to_output(f"ImportHandler: Processing imported asset: {created_object}")
            
            # Get asset type
            type_name = created_object.get_class().get_name()
            type_string = unreal.StringLibrary.conv_name_to_string(type_name)
            self.log_to_output(f"ImportHandler: Asset class type: {type_string}")
            
            # Get current asset name
            asset_name = created_object.get_name()
            self.log_to_output(f"ImportHandler: Current asset name: {asset_name}")
            
            # Get asset tools
            try:
                unreal_asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
                self.log_to_output("ImportHandler: Successfully obtained AssetTools")
            except Exception as e:
                self.log_to_output(f"ImportHandler: ERROR - Failed to get AssetTools - {str(e)}")
                return
            
            # Get asset prefix for renaming
            asset_prefix_string = self.get_asset_prefix_by_type(type_string)
            asset_current_name_string = unreal.StringLibrary.conv_name_to_string(asset_name)
            
            # Check if the asset already has the correct prefix
            if asset_current_name_string.startswith(asset_prefix_string):
                self.log_to_output(f"ImportHandler: Asset already has correct prefix '{asset_prefix_string}', skipping rename")
                asset_new_name_string = asset_current_name_string
            else:
                asset_new_name_string = asset_prefix_string + asset_current_name_string
                self.log_to_output(f"ImportHandler: New asset name will be: {asset_new_name_string}")
            
            asset_new_name = unreal.StringLibrary.conv_string_to_name(asset_new_name_string)
            
            # Get target path for asset
            type_package_path = self.get_file_location_by_type(type_string)
            new_package_path = "/Game/" + type_package_path
            
            self.log_to_output(f"ImportHandler: Target package path: {new_package_path}")
            
            # Get current path to compare
            current_path = created_object.get_path_name()
            self.log_to_output(f"ImportHandler: Current asset path: {current_path}")
            
            # First, let's check if target folder exists, create if not
            try:
                content_dir = unreal.Paths.project_content_dir()
                full_target_path = content_dir + type_package_path
                
                if not unreal.EditorAssetLibrary.does_directory_exist(new_package_path):
                    self.log_to_output(f"ImportHandler: Target directory does not exist, creating: {new_package_path}")
                    unreal.EditorAssetLibrary.make_directory(new_package_path)
            except Exception as e:
                self.log_to_output(f"ImportHandler: WARNING - Error checking/creating target directory - {str(e)}")
            
            # Create rename data
            try:
                asset_rename_data = unreal.AssetRenameData()
                asset_rename_data.asset = created_object
                asset_rename_data.new_name = asset_new_name
                asset_rename_data.new_package_path = new_package_path
                
                self.log_to_output(f"ImportHandler: Created AssetRenameData: asset={created_object}, new_name={asset_new_name_string}, new_path={new_package_path}")
                
                # Create array and add rename data
                asset_rename_data_arr = unreal.Array(unreal.AssetRenameData)
                asset_rename_data_arr.append(asset_rename_data)
                
                self.log_to_output(f"ImportHandler: Created array with {len(asset_rename_data_arr)} rename operations")
                
                # Perform the rename operation with the safer approach
                # Instead of directly calling rename, let's run it via a delayed task to not crash the engine
                # Try silent rename first
                rename_result = False
                try:
                    rename_result = unreal_asset_tools.rename_assets(asset_rename_data_arr)
                    self.log_to_output(f"ImportHandler: Silent rename result: {rename_result}")
                except Exception as e:
                    self.log_to_output(f"ImportHandler: ERROR during silent rename - {str(e)}")
                
                # Only try with dialog if silent rename failed
                if not rename_result:
                    try:
                        # We'll wrap this in a try/except since it might be causing the crash
                        self.log_to_output("ImportHandler: Silent rename failed, trying with dialog...")
                        
                        # Schedule the rename task to run on the next tick to avoid crashes
                        def run_rename_task():
                            try:
                                unreal_asset_tools.rename_assets_with_dialog(asset_rename_data_arr, True)
                                self.log_to_output("ImportHandler: rename_assets_with_dialog completed")
                            except Exception as e:
                                self.log_to_output(f"ImportHandler: ERROR during dialog rename - {str(e)}")
                        
                        unreal.call_latent_with_delay(None, 0.1, run_rename_task)
                        self.log_to_output("ImportHandler: Scheduled rename_assets_with_dialog for next tick")
                    except Exception as e:
                        self.log_to_output(f"ImportHandler: ERROR scheduling rename task - {str(e)}")
                        
            except Exception as e:
                self.log_to_output(f"ImportHandler: ERROR setting up rename operation - {str(e)}\n{traceback.format_exc()}")
                
        except Exception as e:
            self.log_to_output(f"ImportHandler: ERROR in on_asset_post_import - {str(e)}\n{traceback.format_exc()}")

def initialize_handler():
    """
    Safely initialize the import handler, ensuring only one instance exists
    """
    global _import_handler_instance
    
    # Clean up any existing instance
    if _import_handler_instance is not None:
        unreal.log("ImportHandler: An instance already exists, cleaning up")
        try:
            # Try to clean up the old delegate if possible
            editor_subsystem = unreal.get_editor_subsystem(unreal.ImportSubsystem)
            editor_subsystem.on_asset_post_import.clear()
            unreal.log("ImportHandler: Successfully cleared existing delegates")
        except Exception as e:
            unreal.log(f"ImportHandler: Could not clear existing delegates - {str(e)}")
    
    # Create a new instance
    try:
        _import_handler_instance = ImportHandler()
        unreal.log("ImportHandler: Successfully initialized")
        return _import_handler_instance
    except Exception as e:
        error_msg = f"ImportHandler: Failed to initialize - {str(e)}\n{traceback.format_exc()}"
        unreal.log(error_msg)
        return None

# Initialize the handler with our safe function
handler = initialize_handler()