# All static variables are defined here.
{
	'variables': {
		'TARGET_PLATFORM%' : 'None',
		'RENDER_API' : 'OpenGL4',
		'ENABLE_RTTI%' : 'false',
		'ENABLE_CPP11%' : 'true',
		'ENABLE_CUDA%' : 'false',
	},

	'conditions': [
		#######################################################################
		# OS Variables
		#######################################################################
		['OS=="linux"', {
			'variables':{
				'TARGET_PLATFORM%' : 'Linux64',
			},
		}],
		['OS=="mac"', {
			'variables':{
				'TARGET_PLATFORM%' : 'OSX64',
			},
		}],

		['OS=="win"', {
			'variables':{
				'TARGET_PLATFORM%' : 'Win64',
			},
		}],


		#######################################################################
		# Target Platform Variables
		#######################################################################
		['TARGET_PLATFORM=="Android"', {
			'variables': {
				'RENDER_API' : 'OpenGLES2',
			},
		}],

		['TARGET_PLATFORM=="iOS"', {
			'variables': {
				'RENDER_API' : 'OpenGLES2',
			},
		}],

		['TARGET_PLATFORM=="Web"', {
			'variables': {
				'RENDER_API' : 'OpenGLES2',
			},
		}],

	],
}