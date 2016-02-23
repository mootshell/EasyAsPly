# Project Level build file
# Define only the targets to be built from here
{
	'targets': [
		{
			'target_name': 'EasyAsPLYMain',
			'type': 'executable',
			'dependencies': [
				'../EasyAsPLYLib/EasyAsPLYLib.gyp:*',
			],

			'sources': [
				'src/Main.cpp'
			],
		},
	],
}