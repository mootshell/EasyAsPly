# Sets the target build directory to USER_BUILD_DIR
{
	'target_defaults': {
		'msvs_configuration_attributes': {
			'OutputDirectory': '<(DEPTH)/<(USER_BUILD_DIR)/$(PlatformName)_$(ConfigurationName)_$(PlatformToolset)/$(TargetName)',
			'IntermediateDirectory' : '<(DEPTH)/<(USER_INTERMEDIATE_DIR)/$(PlatformName)_$(ConfigurationName)_$(PlatformToolset)/$(TargetName)',
		},
	},
}
