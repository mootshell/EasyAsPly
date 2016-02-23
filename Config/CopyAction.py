#!/usr/bin/env python


import sys
import os
import errno

import distutils.dir_util
import distutils.file_util
 
def copy(src, dest):
    try:
        if os.path.isfile(src):
            distutils.file_util.copy_file(src, dest)
        elif os.path.isdir(src):
            distutils.dir_util.copy_tree(src, dest)
        print('Copy %s --> %s' % (src, dest))
    except OSError as e:
        print('Copy Failed %s --> %s. Error: %s' % (src, dest, e))

basePath = os.getcwd()
copyList = sys.argv[1:-1]
for copyPath in copyList:
    if os.path.isabs(copyPath) != True:
	   copyPath = os.path.realpath(basePath + "/" + copyPath)

destPath = sys.argv[-1]
if destPath[-1:] == '"':
	destPath = destPath[:-1]
if os.path.isabs(destPath) != True:
	os.path.realpath(basePath + "/" + destPath)

for copyPath in copyList:
    copy(copyPath, destPath + "/" + os.path.basename(copyPath))