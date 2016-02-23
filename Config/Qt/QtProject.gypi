# A file to be included inside Projects
{
	# Setup Qt Variables
	'variables': {
		'QT_GENERATED_FILE_DIR' : '<(INTERMEDIATE_DIR)/GeneratedFiles',
		'QT_DLLS': [], 
		'QT_DLLS_DEBUG': [],
		'QT_SUBSYSTEM%' : 'window',
	},

	'include_dirs': [
		'<(QT_INC_DIR)',
		'<(QT_GENERATED_FILE_DIR)',
	],

	'defines' : [
		'UNICODE',
		'QT_DLL',
		'QT_NO_DEBUG',
	],
	'configurations': {
		'Config_Debug': {
			'defines!' : ['QT_NO_DEBUG'], 
			'defines' : ['QT_DEBUG'],
		},
	},

	'conditions': [
		# Set the subsystem
		['QT_SUBSYSTEM=="window"', {'msvs_settings': {'VCLinkerTool': {'SubSystem': '2'}}}],
		['QT_SUBSYSTEM=="console"', {'msvs_settings': {'VCLinkerTool': {'SubSystem': '1'}}}],

		# Setup Linking
		['TARGET_PLATFORM=="OSX64"', {'mac_framework_dirs': ['<(QT_LIB_DIR)']}],
		['TARGET_PLATFORM=="Win64"', {'msvs_settings': {'VCLinkerTool': {'AdditionalLibraryDirectories': ['<(QT_LIB_DIR)']}}}],

		# Copy Qt DLLs for Debugging
		['TARGET_PLATFORM=="Win64"', {
			'actions': [
				{
					'inputs': [],
					'outputs': ['$(ProjectDir)/',],
					'action_name': 'Copy Qt DLLS For Debugging',
					'action': [
						'<(PYTHON_EXE)', 
						'<(ROOT_DIR)/Config/CopyAction.py',
						'>@(QT_DLLS)', '>@(QT_DLLS_DEBUG)',
						'$(ProjectDir)', 
					],
				},
			],
		}],
		['TARGET_PLATFORM=="OSX64"', {
			'xcode_settings': {
				'INFOPLIST_FILE': 'Info.plist',
			},
			'mac_bundle': 1,
			'mac_bundle_resources': [
			],
			'postbuilds': [
				{
					'postbuild_name': 'Copy dependent framework into app',
					'action': [
						'python', '<(ROOT_DIR)/Config/PostBuildOSXApp.py',
						'${BUILT_PRODUCTS_DIR}/Orthrus.app',
						'<(QT_LIB_DIR)',
						'>@(QT_DLLS)'
					],
				},
			],
		}],
	],

	# Copy Qt DLLs
	'actions': [
		{
			'inputs': [],
			'outputs': ['<(PRODUCT_DIR)/',],
			'action_name': 'Copy Qt DLLs For Product',
			'action': [
				'<(PYTHON_EXE)', 
				'<(ROOT_DIR)/Config/CopyAction.py',
				'>@(QT_DLLS)',
				'<(PRODUCT_DIR)', 
			],
		},
	],

	# Setup Qt specific rules
	'rules': [
		{
			'rule_name': 'generate_moc',
			'extension': 'h',
			'outputs': [ '<(QT_GENERATED_FILE_DIR)/MOC_<(RULE_INPUT_ROOT).h' ],
			'action': [ '<(QT_BIN_DIR)/moc', '<(RULE_INPUT_PATH)', '-o', '<(QT_GENERATED_FILE_DIR)/MOC_<(RULE_INPUT_ROOT).h' ],
			'message': 'Generating MOC_<(RULE_INPUT_ROOT).h',
		},
		{
			'rule_name': 'generate_qrc',
			'extension': 'qrc',
			'outputs': [ '<(QT_GENERATED_FILE_DIR)/QRC_<(RULE_INPUT_ROOT).h' ],
			'action': [ '<(QT_BIN_DIR)/rcc', '-name', '<(RULE_INPUT_ROOT)', '-no-compress', '<(RULE_INPUT_PATH)', '-o', '<(QT_GENERATED_FILE_DIR)/QRC_<(RULE_INPUT_ROOT).h' ],
			'message': 'Generating QRC_<(RULE_INPUT_ROOT).h',
		},
		{
			'rule_name': 'generate_ui',
			'extension': '.ui',
			'outputs': [ '<(QT_GENERATED_FILE_DIR)/ui_<(RULE_INPUT_ROOT).h' ],
			'action': [ '<(QT_BIN_DIR)/uic', '-o', '<(QT_GENERATED_FILE_DIR)/ui_<(RULE_INPUT_ROOT).h', '<(RULE_INPUT_PATH)'],
			'message': 'Generating <(RULE_INPUT_ROOT).h',
		},
	],
}