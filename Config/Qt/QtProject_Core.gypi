# A Specific QT Module
{
	'defines' : ['QT_CORE_LIB' ],
	'include_dirs': ['<(QT_INC_DIR)/QtCore'],

	'conditions': [
		['TARGET_PLATFORM=="Linux64"', {
			'link_settings': {'libraries': ['-lQt5Core']},
			'variables': { 'QT_DLLS': [], 'QT_DLLS_DEBUG': [], },
		}],

		['TARGET_PLATFORM=="OSX64"', {
			'link_settings': {'libraries': ['<(QT_LIB_DIR)/QtCore.framework']},
			'variables': { 'QT_DLLS': ['QtCore'], 'QT_DLLS_DEBUG': [], },
		}],

		['TARGET_PLATFORM=="Win64"', {
			'msvs_settings': {'VCLinkerTool': {'AdditionalDependencies': ['qtmain.lib','Qt5Core.lib','Shell32.lib']}},
			'configurations': {
				'Config_Debug': {'msvs_settings': {'VCLinkerTool': {'AdditionalDependencies!': ['qtmain.lib','Qt5Core.lib'], 'AdditionalDependencies': ['qtmaind.lib','Qt5Cored.lib']}}},
			},
			'variables': { 
				'QT_DLLS': [
					'<(QT_BIN_DIR)/Qt5Core.dll',
					'<(QT_BIN_DIR)/icudt53.dll',
					'<(QT_BIN_DIR)/icuin53.dll',
					'<(QT_BIN_DIR)/icuuc53.dll',
					'<(QT_BIN_DIR)/../plugins/platforms/qwindows.dll',
				], 
				'QT_DLLS_DEBUG': [
					'<(QT_BIN_DIR)/Qt5Cored.dll',
					'<(QT_BIN_DIR)/icudt53.dll',
					'<(QT_BIN_DIR)/icuin53.dll',
					'<(QT_BIN_DIR)/icuuc53.dll',
					'<(QT_BIN_DIR)/../plugins/platforms/qwindows.dll',
				],
			},
		}],
	],
}