# A Specific QT Module
{
	'defines' : ['QT_WEBSOCKETS_LIB' ],
	'include_dirs': ['<(QT_INC_DIR)/QtWebSockets'],
	'conditions': [
		['TARGET_PLATFORM=="Linux64"', {
			'link_settings': {'libraries': ['-lQt5WebSockets']},
			'variables': { 'QT_DLLS': [], 'QT_DLLS_DEBUG': [], },
		}],

		['TARGET_PLATFORM=="OSX64"', {
			'link_settings': {'libraries': ['<(QT_LIB_DIR)/QtWebSockets.framework']},
			'variables': { 'QT_DLLS': ['QtWebSockets'], 'QT_DLLS_DEBUG': [], },
		}],

		['TARGET_PLATFORM=="Win64"', {
			'msvs_settings': {'VCLinkerTool': {'AdditionalDependencies': ['Qt5WebSockets.lib']}},
			'configurations': {
				'Debug': {'msvs_settings': {'VCLinkerTool': {'AdditionalDependencies!': ['Qt5WebSockets.lib'], 'AdditionalDependencies': ['Qt5WebSocketsd.lib']}}},
			},
			'variables': { 
				'QT_DLLS': ['<(QT_BIN_DIR)/Qt5WebSockets.dll',],
				'QT_DLLS_DEBUG': ['<(QT_BIN_DIR)/Qt5WebSocketsd.dll',],
			},
		}],
	],
}