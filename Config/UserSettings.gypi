# All static variables are defined here.
{
	'variables': {
		'USER_BUILD_DIR%' 	: 'Build/Product',
		
		'USER_INTERMEDIATE_DIR%' : 'Build/Intermediate',

		'USER_DEFAULT_CONFIG' : 'Release',
		
		'USER_DEFINES' : [],
	},

	'conditions': [
		['OS=="linux"', {
			'variables':{
				'PYTHON_EXE' : 'python',
				'QT_BIN_DIR' : '/usr/lib/x86_64-linux-gnu/qt5/bin',
				'QT_INC_DIR' : '/usr/include/x86_64-linux-gnu/qt5',
				'QT_LIB_DIR' : '/usr/include/x86_64-linux-gnu/qt5',
				'FLYCAP2_INC_DIR' : '/usr/include/flycapture',
				'FLYCAP2_LIB_DIR' : '/usr/lib',
				#'NUKE_INC_DIR' : '',
				#'NUKE_LIB_DIR' : '',
				#'NUKE_BIN_DIR' : '',
				'EXTERNAL_LIB_DIR' : '',
				'BOOST_INC_DIR' : '/usr/include',
				'CUDA_BIN_DIR' : '/usr/local/cuda/bin',
				'CUDA_INC_DIR' : '/usr/local/cuda/include',
				'CUDA_LIB_DIR' : '/usr/local/cuda/lib64',
				'USER_DIR': '~',
			},
		}],
		['OS=="mac"', {
			'variables':{
				'PYTHON_EXE' : 'python',
				'QT_BIN_DIR' : '/Users/8i/Qt5.4.1/5.4/clang_64/bin',
				'QT_INC_DIR' : '/Users/8i/Qt5.4.1/5.4/clang_64/include',
				'QT_LIB_DIR' : '/Users/8i/Qt5.4.1/5.4/clang_64/lib',
				'FLYCAP2_INC_DIR' : '',
				'FLYCAP2_LIB_DIR' : '',
				'NUKE_INC_DIR' : '',
				'NUKE_LIB_DIR' : '',
				'NUKE_BIN_DIR' : '',
				'EXTERNAL_LIB_DIR' : '',
				'BOOST_INC_DIR' : '',
				'CUDA_BIN_DIR' : '',
				'CUDA_INC_DIR' : '',
				'CUDA_LIB_DIR' : '',
				'USER_DIR': '~',
			},
		}],

		['OS=="win"', {
			'variables':{
				'PYTHON_EXE' : 'C:/Python27/python.exe',
				'QT_BIN_DIR' : 'C:/Qt/Qt5.4.1/5.4/msvc2013_64_opengl/bin',
				'QT_INC_DIR' : 'C:/Qt/Qt5.4.1/5.4/msvc2013_64_opengl/include',
				'QT_LIB_DIR' : 'C:/Qt/Qt5.4.1/5.4/msvc2013_64_opengl/lib',
				'FLYCAP2_INC_DIR' : 'C:/Program Files/Point Grey Research/FlyCapture2/include',
				'FLYCAP2_LIB_DIR' : 'C:/Program Files/Point Grey Research/FlyCapture2/lib64',
				'NUKE_INC_DIR' : 'C:/Program Files/Nuke8.0v3/include',
				'NUKE_LIB_DIR' : 'C:/Program Files/Nuke8.0v3',
				'NUKE_BIN_DIR' : 'C:/Program Files/Nuke8.0v3',
				'EXTERNAL_LIB_DIR' : '<(ROOT_DIR)/Lib/External/x64/Release',
				'BOOST_INC_DIR' : 'C:/Program Files/Boost/include',
				'CUDA_BIN_DIR' : 'C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v6.5/bin',
				'CUDA_INC_DIR' : 'C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v6.5/include',
				'CUDA_LIB_DIR' : 'C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v6.5/lib/x64',
				'USER_DIR': '%USERPROFILE%',
			},
		}],
	],
}
