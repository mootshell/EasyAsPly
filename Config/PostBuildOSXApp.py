#!/usr/bin/env python

import sys
import os
import shutil
from subprocess import call

def Run(args):
	#print args
	call(args)

appFile = sys.argv[1]
qtPath = sys.argv[2]
libs = sys.argv[3:-1]
binaryName = os.path.splitext(os.path.basename(appFile))[0]

# Update DLL/Binary stoof
frameworkFolder = appFile + "/Contents/Frameworks"
Run(["mkdir", "-p", frameworkFolder])
for lib in libs:
	Run(["cp", "-R", qtPath+"/"+lib+".framework", frameworkFolder])
	
for lib in libs:
	Run(["install_name_tool", "-id", 
		"@executable_path/../Frameworks/"+lib+".framework/"+lib, 
		appFile+"/Contents/Frameworks/"+lib+".framework/"+lib])
	Run(["install_name_tool", "-id", 
		"@executable_path/../Frameworks/"+lib+".framework/"+lib+"_debug", 
		appFile+"/Contents/Frameworks/"+lib+".framework/"+lib+"_debug"])

for lib in libs:
	Run(["install_name_tool", "-change", 
		qtPath+"/"+lib+".framework/"+lib,
		"@executable_path/../Frameworks/"+lib+".framework/"+lib, 
		appFile+"/Contents/MacOS/"+binaryName])
	Run(["install_name_tool", "-change", 
		qtPath+"/"+lib+".framework/"+lib,
		"@executable_path/../Frameworks/"+lib+".framework/"+lib+"_debug", 
		appFile+"/Contents/MacOS/"+binaryName])

for lib in libs:
	for libB in libs:
		Run(["install_name_tool", "-change", 
			qtPath+"/"+lib+".framework/"+lib,
			"@executable_path/../Frameworks/"+lib+".framework/"+lib, 
			appFile+"/Contents/Frameworks/"+libB+".framework/"+libB])
		Run(["install_name_tool", "-change", 
			qtPath+"/"+lib+".framework/"+lib+"_debug",
			"@executable_path/../Frameworks/"+lib+".framework/"+lib+"_debug", 
			appFile+"/Contents/Frameworks/"+libB+".framework/"+libB+"_debug"])

# Copy The pain... So much pain
platformsFolder = appFile+"/Contents/Frameworks/platforms/"
Run(["mkdir", "-p", platformsFolder])
Run(["cp", "-R", qtPath+"/"+"../plugins/platforms/libqcocoa.dylib", platformsFolder])
for lib in libs:
	Run(["install_name_tool", "-change", 
		qtPath+"/"+lib+".framework/"+lib,
		"@executable_path/../Frameworks/"+lib+".framework/"+lib, 
		appFile+"/Contents/Frameworks/platforms/libqcocoa.dylib"])
	Run(["install_name_tool", "-change", 
		qtPath+"/"+lib+".framework/"+lib+"_debug",
		"@executable_path/../Frameworks/"+lib+".framework/"+lib+"_debug", 
		appFile+"/Contents/Frameworks/platforms/libqcocoa.dylib"])
