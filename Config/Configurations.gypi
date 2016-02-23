# Settings for the different Build Configurations.
{
	'target_defaults': {
		'default_configuration' : '<(USER_DEFAULT_CONFIG)',

		'configurations': {
			
			###################################################################
			# Base Configuration
			###################################################################
			'Base': {
				'abstract': 1,
				'defines' : ['<@(USER_DEFINES)'],
			},

			# No Opt is a special case that cannot have NDEBUG defined.
			'NoOpt': {
				'abstract': 1,
				'defines!' : ['NDEBUG', '_NDEBUG'],
			},

			###################################################################
			# Final Used Configurations
			###################################################################

			'Debug': 		{ 'inherit_from': ['Base', 'Platform_<(TARGET_PLATFORM)', 'Optimisation_None', 'Config_Debug'] },
			'ReleaseNoOpt': { 'inherit_from': ['Base', 'Platform_<(TARGET_PLATFORM)', 'Optimisation_None', 'Config_Release', 'NoOpt'] },
			'Release': 		{ 'inherit_from': ['Base', 'Platform_<(TARGET_PLATFORM)', 'Optimisation_Full', 'Config_Release'] },
			'Master':		{ 'inherit_from': ['Base', 'Platform_<(TARGET_PLATFORM)', 'Optimisation_Full', 'Config_Master'] },
		},
	},
}