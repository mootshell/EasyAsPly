# Settings for warnings
{
	'target_defaults': {
		'msvs_settings': {
			'VCCLCompilerTool': {
				'WarningLevel': '3',
				'WarnAsError': 'false',
				'AdditionalOptions' : [
					#'/wd4100',	# Ignore 'unreferenced formal parameter'
				],
			},
			'VCLinkerTool' : {
				'TreatLinkerWarningAsErrors' : 'false',
			},
		},
		'xcode_settings': {
			'GCC_WARN_PEDANTIC' : 'YES',
			'GCC_TREAT_WARNINGS_AS_ERRORS': 'NO',
			'WARNING_CFLAGS': [
				'-Wall',
				'-Wno-gnu-anonymous-struct',
				'-Wno-nested-anon-types',
				'-Wno-unused-function',
			],
		},
		'cflags': [
			'-Wall',
			#'-Werror',
		],
	},
}