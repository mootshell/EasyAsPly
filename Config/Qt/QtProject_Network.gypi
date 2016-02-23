# A Specific QT Module
{
	'defines' : ['QT_NETWORK_LIB' ],
	'include_dirs': ['<(QT_INC_DIR)/QtNetwork'],

	'conditions': [
		['TARGET_PLATFORM=="Linux64"', {
			'link_settings': {'libraries': ['-lQt5Network']},
			'variables': { 'QT_DLLS': [], 'QT_DLLS_DEBUG': [], },
		}],

		['TARGET_PLATFORM=="OSX64"', {
			'link_settings': {'libraries': ['<(QT_LIB_DIR)/QtNetwork.framework']},
			'variables': { 'QT_DLLS': ['QtNetwork'], 'QT_DLLS_DEBUG': [], },
		}],

		['TARGET_PLATFORM=="Win64"', {
			'msvs_settings': {'VCLinkerTool': {'AdditionalDependencies': ['Qt5Network.lib']}},
			'configurations': {
				'Debug': {'msvs_settings': {'VCLinkerTool': {'AdditionalDependencies!': ['Qt5Network.lib'], 'AdditionalDependencies': ['Qt5Networkd.lib']}}},
			},
			'variables': { 
				'QT_DLLS': ['<(QT_BIN_DIR)/Qt5Network.dll',], 
				'QT_DLLS_DEBUG': ['<(QT_BIN_DIR)/Qt5Networkd.dll',],
			},
		}],
	],
}