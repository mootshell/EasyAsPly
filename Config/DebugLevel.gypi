# Settings for the different Debug level Configurations
{
	'target_defaults': {
		'configurations': {

			###################################################################
			# Debug Configuration
			###################################################################
			'Config_Debug': {
				'abstract': 1,
				'defines' : [
					'DEBUG', '_DEBUG',
					'ENABLE_CORE_DEBUG',
					'ENABLE_LOGGING',
					'WEBSOCKET_PROFILING',

					'ENABLE_CORERENDER_ERROR_CHECKING',
					'ENABLE_CORERENDER_SHADER_ERROR_CHECKING',
					'ENABLE_DEBUGDRAW',
					'ENABLE_D3D11_DEBUG_DEVICE',
				],
				'conditions': [
					['TARGET_PLATFORM!="Web" and ENABLE_CPP11=="true"', {
						'defines': [
							'ENABLE_STATISTICS',
							'ENABLE_GPU_STATISTICS',
							'ENABLE_DIAGNOSTICS',
						]
					}],
				],
				'msvs_settings': {
					'VCCLCompilerTool': {'RuntimeLibrary' : '3'}, #/MDd
					'VCLinkerTool' : {'GenerateDebugInformation': 'true'},
				},
				'xcode_settings': {
					'GCC_GENERATE_DEBUGGING_SYMBOLS': 'YES',
				},
			},

			###################################################################
			# Release Configuration - For Dev & Profiling
			###################################################################
			'Config_Release': {
				'abstract': 1,
				'defines' : [
					'NDEBUG', '_NDEBUG',
					'ENABLE_CORE_DEBUG',
					'ENABLE_LOGGING',
					'WEBSOCKET_PROFILING',

					'ENABLE_CORERENDER_ERROR_CHECKING',
					'ENABLE_CORERENDER_SHADER_ERROR_CHECKING',
					'ENABLE_DEBUGDRAW',
				],
				'conditions': [
					['TARGET_PLATFORM!="Web" and ENABLE_CPP11=="true"', {
						'defines': [
							'ENABLE_STATISTICS',
							'ENABLE_GPU_STATISTICS',
							'ENABLE_DIAGNOSTICS',
						]
					}],
				],
				'msvs_settings': {
					'VCCLCompilerTool': {'RuntimeLibrary' : '2'}, #/MD
					'VCLinkerTool' : {'GenerateDebugInformation': 'true'},
				},
				'xcode_settings': {
					'GCC_GENERATE_DEBUGGING_SYMBOLS': 'YES',
				},
			},

			###################################################################
			# Master Configuration - For release to clients
			###################################################################
			'Config_Master': {
				'abstract': 1,
				'defines' : [
					'NDEBUG', '_NDEBUG',
				],
				'conditions': [
					['TARGET_PLATFORM!="Web"', {
						'defines': [
							'ENABLE_STATISTICS',
						]
					}],
				],
				'msvs_settings': {
					'VCCLCompilerTool': {'RuntimeLibrary' : '2'}, #/MD
					'VCLinkerTool' : {'GenerateDebugInformation': 'false'},
				},
				'xcode_settings': {
					'GCC_GENERATE_DEBUGGING_SYMBOLS': 'NO',
				},
			},
		},
	},
}