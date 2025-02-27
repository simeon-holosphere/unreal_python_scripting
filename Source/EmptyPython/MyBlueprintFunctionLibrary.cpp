// Fill out your copyright notice in the Description page of Project Settings.


#include "MyBlueprintFunctionLibrary.h"

#include "Json.h"
#include "JsonUtilities.h"
#include "Math/Vector2D.h"
#include "Containers/Array.h"

TArray<FVector2D> UMyBlueprintFunctionLibrary::ExtractGeometryPoints()
{
	FString JsonString;
	FString JsonPath = FPaths::ProjectPluginsDir().Append(TEXT("test_python_plugin/Content/Python	/ExternalJson/test_api_output.json"));
	if (!FFileHelper::LoadFileToString(JsonString, *JsonPath))
	{
		UE_LOG(LogTemp, Error, TEXT("%s"), *JsonPath);
		return TArray<FVector2D>();
	}
	
	TArray<FVector2D> Points;
    
	TSharedPtr<FJsonObject> JsonObject;
	TSharedRef<TJsonReader<>> Reader = TJsonReaderFactory<>::Create(JsonString);
    
	if (FJsonSerializer::Deserialize(Reader, JsonObject) && JsonObject.IsValid())
	{
		// Get the features array from the JSON
		TArray<TSharedPtr<FJsonValue>> FeaturesArray = JsonObject->GetArrayField("features");
        
		// Loop through each feature
		for (const auto& FeatureValue : FeaturesArray)
		{
			TSharedPtr<FJsonObject> FeatureObject = FeatureValue->AsObject();
            
			// Get the geometry object for this feature
			TSharedPtr<FJsonObject> GeometryObject = FeatureObject->GetObjectField("geometry");
			if (GeometryObject.IsValid())
			{
				// Extract x and y coordinates
				double X = GeometryObject->GetNumberField("x");
				double Y = GeometryObject->GetNumberField("y");
                
				// Add the point to our array
				Points.Add(FVector2D(X, Y));
			}
		}
	}
    
	return Points;
}

