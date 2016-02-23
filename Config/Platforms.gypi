# Settings for the different Platform Configs
{
	'target_defaults': {
		'conditions': [

			['TARGET_PLATFORM=="Android"', {
				'msbuild_toolset': 'arm-linux-androideabi-4.9',
			}],

			['TARGET_PLATFORM=="iOS"', {
				'hard_dependency': 1,
			}],

			['TARGET_PLATFORM=="Win32"', {
				'variables': {'TOOLSET%' : 'v120'},
				'msbuild_toolset': '<(TOOLSET)',
				'msvs_cygwin_shell': 0,
			}],

			['TARGET_PLATFORM=="Win64"', {
				'variables': {'TOOLSET%' : 'v120'},
				'msbuild_toolset': '<(TOOLSET)',
				'msvs_cygwin_shell': 0,
			}],

			['TARGET_PLATFORM=="Web"', {
				'msbuild_toolset': 'emcc',
				'msvs_cygwin_shell': 0,
			}],

			['TARGET_PLATFORM=="Linux64"', {
				#'link_settings' : {
					#'libraries' : [
						#'-lpthread',
						#'-lc',
						#'-ldl',
					#],
				#},

			}],
		],

		'configurations': {

			'Platform_Android': {
				'abstract': 1,
				'defines': ['PLATFORM_ANDROID', 'RENDERER_OPENGLES2'],
				'msvs_configuration_platform': 'Android',
				'msvs_settings': {
					'VCCLCompilerTool': {'AdditionalOptions': [ '-fexceptions' ] }
				},
			},

			'Platform_iOS': {
				'abstract': 1,
				'defines': ['PLATFORM_IOS', 'RENDERER_OPENGLES2'],
				'xcode_settings':{
					'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
					'GCC_SYMBOLS_PRIVATE_EXTERN': 'YES',
					'IPHONEOS_DEPLOYMENT_TARGET': '6.1',
					'SDKROOT': 'iphoneos',
				},
			},

			'Platform_Linux32': {
				'abstract': 1,
				'defines': ['PLATFORM_LINUX'],
				'cflags': [
					'-march=i386',
					'-fPIC', # For dylibs to work
					'-msse4.2',
					'-I/usr/local/include',
				],
				'cflags_cc': [
					'-Wno-unknown-pragmas',
					'-Wno-reorder',
					'-Wno-sign-compare',
					'-Wno-unused-variable',
					'-Wno-unused-but-set-variable',
					'-Wno-unused-value',
					'-Wno-unused-result',
				],
				'ldflags': [
					'-L/usr/local/lib',
				],
			},

			'Platform_Linux64': {
				'abstract': 1,
				'defines': ['PLATFORM_LINUX'],
				'cflags': [
					'-march=x86-64',
					'-fPIC', # For dylibs to work
					'-msse4.2',
					'-I/usr/local/include',
				],
				'cflags_cc': [
					'-Wno-unknown-pragmas',
					'-Wno-reorder',
					'-Wno-sign-compare',
					'-Wno-unused-variable',
					'-Wno-unused-but-set-variable',
					'-Wno-unused-value',
					'-Wno-unused-result',
				],
				'ldflags': [
					'-L/usr/local/lib',
				],
			},

			'Platform_OSX32': {
				'abstract': 1,
				'defines' : ['__MACOSX__', 'PLATFORM_OSX'],
				'xcode_settings': {
					'ARCHS': [ '$(ARCHS_STANDARD_32_BIT)' ],
					'CLANG_X86_VECTOR_INSTRUCTIONS' : 'sse4.2',
					'GCC_DYNAMIC_NO_PIC': 'NO', #For dylibs
					'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
					'GCC_SYMBOLS_PRIVATE_EXTERN': 'YES',
					'SDKROOT': 'macosx',
					'MACOSX_DEPLOYMENT_TARGET': '10.9',
				},
			},

			'Platform_OSX64': {
				'abstract': 1,
				'defines' : ['__MACOSX__', 'PLATFORM_OSX', 'RENDERER_OPENGL'],
				'xcode_settings': {
					'ARCHS': [ '$(ARCHS_STANDARD_64_BIT)' ],
					'CLANG_X86_VECTOR_INSTRUCTIONS' : 'sse4.2',
					'GCC_DYNAMIC_NO_PIC': 'NO', #For dylibs
					'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
					'GCC_SYMBOLS_PRIVATE_EXTERN': 'YES',
					'SDKROOT': 'macosx',
					'MACOSX_DEPLOYMENT_TARGET': '10.9',
				},
			},

			'Platform_Win32': {
				'abstract': 1,
				'defines': ['WIN32', 'PLATFORM_WINDOWS', 'RENDERER_D3D11', 'RENDERER_OPENGL', '_WIN32_WINNT=0x0601'],
				'msvs_configuration_platform': 'Win32',
				'msvs_settings': {
					'VCLibrarianTool': { 'TargetMachine': '1' }, # MachineX86
					'VCCLCompilerTool': {
						'CallingConvention': 0, #cdecl
					},
				},
			},

			'Platform_Win64': {
				'abstract': 1,
				'defines': ['WIN64', 'PLATFORM_WINDOWS', 'RENDERER_D3D11', 'RENDERER_OPENGL', '_WIN32_WINNT=0x0601'],
				'msvs_configuration_platform': 'x64',
				'msvs_settings': {
					'VCLibrarianTool': { 'TargetMachine': '17' }, # MachineX64
					'VCCLCompilerTool': {
						'CallingConvention': 0, #cdecl
					},
				},
			},

			'Platform_Web': {
				'abstract': 1,
				'defines' : ['PLATFORM_WEB', 'RENDERER_OPENGLES2'],
				'msvs_configuration_platform': 'Emscripten',
			},
		},
	},
}
