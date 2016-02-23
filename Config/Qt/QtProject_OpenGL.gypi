# A Specific QT Module
{
	'defines' : ['QT_OPENGL_LIB' ],
	'include_dirs': ['<(QT_INC_DIR)/QtOpenGL'],

	'conditions': [
		['TARGET_PLATFORM=="Linux64"', {
			'link_settings': {'libraries': ['-lQt5OpenGL']},
			'variables': { 'QT_DLLS': [], 'QT_DLLS_DEBUG': [], },
		}],

		['TARGET_PLATFORM=="OSX64"', {
			'link_settings': {'libraries': ['<(QT_LIB_DIR)/QtOpenGL.framework']},
			'variables': { 'QT_DLLS': ['QtOpenGL'], 'QT_DLLS_DEBUG': [], },
		}],

		['TARGET_PLATFORM=="Win64"', {
			'msvs_settings': {'VCLinkerTool': {'AdditionalDependencies': ['Qt5OpenGL.lib','opengl32.lib','glu32.lib']}},
			'configurations': {
				'Debug': {'msvs_settings': {'VCLinkerTool': {'AdditionalDependencies!': ['Qt5OpenGL.lib'], 'AdditionalDependencies': ['Qt5OpenGLd.lib']}}},
			},
			'variables': { 
				'QT_DLLS': ['<(QT_BIN_DIR)/Qt5OpenGL.dll',],
				'QT_DLLS_DEBUG': ['<(QT_BIN_DIR)/Qt5OpenGLd.dll',],
			},
		}],
	],
}