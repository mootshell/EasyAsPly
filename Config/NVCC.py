
from subprocess import call
import sys

if __name__ == '__main__':

	callArgs = [sys.argv[1]]

	os_label = 'win'
	params_start_index = 2
	if sys.argv[params_start_index].startswith('OS='):
		os_label = sys.argv[params_start_index].split('=')[-1]
		params_start_index += 1


	callArgs += [
		'-gencode=arch=compute_30,code=\"sm_30,compute_30\"', 
		'-gencode=arch=compute_35,code=\"sm_35,compute_35\"',
		'-gencode=arch=compute_37,code=\"sm_37,compute_37\"',
		'-gencode=arch=compute_50,code=\"sm_50,compute_50\"',
		'-cudart', 'static',
        ]
        windowsSpecific = [
		'-Xcompiler', '\"/wd 4819\"',
		'-Xcompiler', '\"/EHsc /W3 /nologo /O2 /Zi  /MD  \"',
		'--compile',
		'--use-local-env',
		'--cl-version', '2010',
		#'-ccbin', '\"C:\\Program Files (x86)\\Microsoft Visual Studio 10.0\\VC\\bin\\x86_amd64\"',
		'--machine', '64',		
		'--keep-dir', 'x64/Release',
		'-maxrregcount=0',
        ]
        linuxSpecific = [
		'--compile',
		'--machine', '64',		
		'--keep-dir', 'x64/Release',
		'-maxrregcount=0',
        ]
	if os_label == 'linux':
	    callArgs += linuxSpecific
	else:
	    callArgs += windowsSpecific

	callArgs += sys.argv[params_start_index:]
	
	call(callArgs);

