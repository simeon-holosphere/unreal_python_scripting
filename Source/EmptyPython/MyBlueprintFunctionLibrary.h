// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"

#include "MyBlueprintFunctionLibrary.generated.h"

/**
 * 
 */
UCLASS()
class EMPTYPYTHON_API UMyBlueprintFunctionLibrary : public UBlueprintFunctionLibrary
{
	GENERATED_BODY()

public:
	UFUNCTION(BlueprintCallable)
	static TArray<FVector2D> ExtractGeometryPoints(); 

};
