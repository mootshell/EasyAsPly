# Settings for PDB stuff
{
	'target_defaults': {
		'msvs_settings': {
			'VCCLCompilerTool': {
				'ProgramDataBaseFileName': '$(OutDir)/pdb/$(TargetName).pdb',
			},
			'VCLinkerTool' : {
				'ProgramDatabaseFile' : '$(OutDir)/pdb/$(TargetName).pdb',
			},
		},
	},
}