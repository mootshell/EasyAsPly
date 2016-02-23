# A Specific QT Module
{
	'defines' : ['QT_PRINTSUPPORT_LIB' ],
	'include_dirs': ['<(QT_INC_DIR)/QtPrintSupport'],
	'conditions': [
		['TARGET_PLATFORM=="Linux64"', {
			'link_settings': {'libraries': ['-lQt5PrintSupport']},
			'variables': { 'QT_DLLS': [], 'QT_DLLS_DEBUG': [], },
		}],

		['TARGET_PLATFORM=="OSX64"', {
			'link_settings': {'libraries': ['<(QT_LIB_DIR)/QtPrintSupport.framework']},
			'variables': { 'QT_DLLS': ['QtPrintSupport'], 'QT_DLLS_DEBUG': [], },
		}],

		['TARGET_PLATFORM=="Win64"', {
			'msvs_settings': {'VCLinkerTool': {'AdditionalDependencies': ['Qt5PrintSupport.lib']}},
			'configurations': {
				'Debug': {'msvs_settings': {'VCLinkerTool': {'AdditionalDependencies!': ['Qt5PrintSupport.lib'], 'AdditionalDependencies': ['Qt5PrintSupportd.lib']}}},
			},
			'variables': { 
				'QT_DLLS': ['<(QT_BIN_DIR)/Qt5PrintSupport.dll',],
				'QT_DLLS_DEBUG': ['<(QT_BIN_DIR)/Qt5PrintSupportd.dll',],
			},
		}],
	],
}