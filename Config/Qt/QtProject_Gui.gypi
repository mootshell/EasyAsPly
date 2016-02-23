# A Specific QT Module
{
	'defines' : ['QT_GUI_LIB' ],
	'include_dirs': ['<(QT_INC_DIR)/QtGui'],

	'conditions': [
		['TARGET_PLATFORM=="Linux64"', {
			'link_settings': {'libraries': ['-lQt5Gui']},
			'variables': { 'QT_DLLS': [], 'QT_DLLS_DEBUG': [], },
		}],

		['TARGET_PLATFORM=="OSX64"', {
			'link_settings': {'libraries': ['<(QT_LIB_DIR)/QtGui.framework']},
			'variables': { 'QT_DLLS': ['QtGui'], 'QT_DLLS_DEBUG': [], },
		}],

		['TARGET_PLATFORM=="Win64"', {
			'msvs_settings': {'VCLinkerTool': {'AdditionalDependencies': ['Qt5Gui.lib']}},
			'configurations': {
				'Debug': {'msvs_settings': {'VCLinkerTool': {'AdditionalDependencies!': ['Qt5Gui.lib'], 'AdditionalDependencies': ['Qt5Guid.lib']}}},
			},
			'variables': { 
				'QT_DLLS': ['<(QT_BIN_DIR)/Qt5Gui.dll',], 
				'QT_DLLS_DEBUG': ['<(QT_BIN_DIR)/Qt5Guid.dll',],
			},
		}],
	],
}