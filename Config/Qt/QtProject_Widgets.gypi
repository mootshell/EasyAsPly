# A Specific QT Module
{
	'defines' : ['QT_WIDGETS_LIB' ],
	'include_dirs': ['<(QT_INC_DIR)/QtWidgets'],
	'conditions': [
		['TARGET_PLATFORM=="Linux64"', {
			'link_settings': {'libraries': ['-lQt5Widgets']},
			'variables': { 'QT_DLLS': [], 'QT_DLLS_DEBUG': [], },
		}],

		['TARGET_PLATFORM=="OSX64"', {
			'link_settings': {'libraries': ['<(QT_LIB_DIR)/QtWidgets.framework']},
			'variables': { 'QT_DLLS': ['QtWidgets'], 'QT_DLLS_DEBUG': [], },
		}],

		['TARGET_PLATFORM=="Win64"', {
			'msvs_settings': {'VCLinkerTool': {'AdditionalDependencies': ['Qt5Widgets.lib']}},
			'configurations': {
				'Debug': {'msvs_settings': {'VCLinkerTool': {'AdditionalDependencies!': ['Qt5Widgets.lib'], 'AdditionalDependencies': ['Qt5Widgetsd.lib']}}},
			},
			'variables': {
				'QT_DLLS': ['<(QT_BIN_DIR)/Qt5Widgets.dll',],
				'QT_DLLS_DEBUG': ['<(QT_BIN_DIR)/Qt5Widgetsd.dll',],
			},
		}],
	]
}