#!/usr/bin/env python

from subprocess import call
import os
import argparse

if __name__ == '__main__':
	parser = argparse.ArgumentParser('Generate platform specific build projects')
	parser.add_argument('-q', '--quite', action='store_true', default=False, help='Run without user interaction')

	opt = parser.parse_args()

	basePath = os.getcwd()
	gypScript = os.path.realpath(basePath + "/ThirdParty/gyp/gyp_main.py")
	projFile = "EasyAsPLY.gyp"
	outputDir = "Build/Projects"
	configPath = "Config"

	os.environ['GYP_DEFINES'] = 'ROOT_DIR=\"' + basePath +'\"'

	print "Generating %s into %s" % (projFile, outputDir)
	callArgs = ["python",
	    gypScript,
	    "--no-duplicate-basename-check",
	    "--config-dir=" + configPath,
	    #"--debug=general",
	    "--depth=" + basePath,
	    "--generator-output=" + outputDir,
	    projFile
	    ]
	#print callArgs
	call(callArgs);
	if not opt.quite:
		raw_input("Press Enter to continue...")