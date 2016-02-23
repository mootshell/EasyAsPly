# Settings for the different Optimisation Levels
{
	'target_defaults': {
		'configurations': {

			###################################################################
			# Optimisation level Configurations
			###################################################################
			'Optimisation_None': {
				'abstract': 1,
				'msvs_settings': {
					'VCCLCompilerTool': {
						'Optimization': '0',
						#'OmitFramePointers': 'false',
						#'EnableIntrinsicFunctions': 'false',
						#'InlineFunctionExpansion': '0',
						#'FavorSizeOrSpeed': '0', 	#1)Speed 2)Size
						#'WholeProgramOptimization': 'false',
						#'StringPooling': 'false',
						#'EnableFiberSafeOptimizations': 'false',
						#'EnableFunctionLevelLinking' : 'true',
					},
					'VCLinkerTool': {
						'LinkIncremental': '1',    # /LTCG
					},
				},
				'xcode_settings': {
					'DEAD_CODE_STRIPPING': 'NO',
					'GCC_INLINES_ARE_PRIVATE_EXTERN': 'NO',
					'GCC_OPTIMIZATION_LEVEL': '0',
					'GCC_THREADSAFE_STATICS': 'YES',
					'GCC_STRICT_ALIASING': 'NO',
					'GCC_UNROLL_LOOPS': 'NO',
					'LLVM_LTO': 'NO',
				},
				'cflags': [
					'-g',
					'-O0',
				],
			},

			###################################################################
			# Max Optimisation Configuration
			###################################################################
			'Optimisation_Full': {
				'abstract': 1,
				'msvs_settings': {
					'VCCLCompilerTool': {
						'Optimization': '2',
						#'OmitFramePointers': 'false',
						'EnableIntrinsicFunctions': 'true',
						'InlineFunctionExpansion': '1',
						'FavorSizeOrSpeed': '1', #1)Speed 2)Size
						'WholeProgramOptimization': 'true',
						'StringPooling': 'true',
						#'EnableFiberSafeOptimizations': 'false',
						'EnableFunctionLevelLinking' : 'true',
					},
					'VCLinkerTool': {
						'LinkTimeCodeGeneration': '1',    # /LTCG
					},
				},
				'xcode_settings': {
					'DEAD_CODE_STRIPPING': 'YES',
					'GCC_INLINES_ARE_PRIVATE_EXTERN': 'YES',
					'GCC_OPTIMIZATION_LEVEL': 's',
					'GCC_THREADSAFE_STATICS': 'YES',
					'GCC_STRICT_ALIASING': 'YES',
					'GCC_UNROLL_LOOPS': 'NO',
					#'LLVM_LTO': 'YES', # Makes filesize huge for some reason, so disabled
				},
				'cflags': [
					'-O2',
					'-pipe',
				],
			},
		},
	},
}