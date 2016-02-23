# Settings for Disabling RTTI
{
	'target_defaults': {
		'conditions': [
			['ENABLE_RTTI=="false"', {
				'msvs_settings': { 
					'VCCLCompilerTool': {
						'RuntimeTypeInfo': 'false',
					},
				},
				'xcode_settings': {
					'GCC_ENABLE_CPP_RTTI': 'NO',
				},
				'cflags_cc': ['-fno-rtti'],
				'conditions': [
					['TARGET_PLATFORM=="Android"', {
						'msvs_settings': {
							'VCCLCompilerTool': {'AdditionalOptions': [ '-fno-rtti' ] }
						},
					}],
					['TARGET_PLATFORM=="Web"', {
						'msvs_settings': {
							'VCCLCompilerTool': {'AdditionalOptions': [ '-fno-rtti' ] }
						},
					}],
				],
			}],
		],
	},
}