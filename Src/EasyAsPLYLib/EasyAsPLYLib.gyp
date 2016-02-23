# Project Level build file
# Define only the targets to be built from here
{
	'targets': [
		{
			'target_name': 'EasyAsPLYLib',
			'type': 'static_library',
			'dependencies': [
			],
			'include_dirs' : ['src'],
			'all_dependent_settings' : {
				'include_dirs' : ['src'],
			},

			'sources': [
				'src/PlyReader.cpp',
				'src/PlyReader.h',
				'src/PlyWriter.cpp',
				'src/PlyWriter.h',
				'src/PlyFormat.h',
				'src/PlyData.cpp',
				'src/PlyData.h',
				'src/PlyElement.cpp',
				'src/PlyElement.h',
				'src/PlyProperty.cpp',
				'src/PlyProperty.h'
			],
		},
	],
}