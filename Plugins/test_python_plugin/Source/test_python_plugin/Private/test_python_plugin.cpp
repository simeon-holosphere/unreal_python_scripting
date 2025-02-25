// Copyright Epic Games, Inc. All Rights Reserved.

#include "test_python_plugin.h"

#define LOCTEXT_NAMESPACE "Ftest_python_pluginModule"

void Ftest_python_pluginModule::StartupModule()
{
	// This code will execute after your module is loaded into memory; the exact timing is specified in the .uplugin file per-module
}

void Ftest_python_pluginModule::ShutdownModule()
{
	// This function may be called during shutdown to clean up your module.  For modules that support dynamic reloading,
	// we call this function before unloading the module.
}

#undef LOCTEXT_NAMESPACE
	
IMPLEMENT_MODULE(Ftest_python_pluginModule, test_python_plugin)