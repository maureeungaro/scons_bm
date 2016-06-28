from util import check_if_dir_exist
import os

def loadclas12(env) :
	OSENV = os.environ
	MLIBRARY = OSENV['MLIBRARY']
	check_if_dir_exist('MLIBRARY')

	OPTIONSV = OSENV['OPTIONS_VERSION']

	env.Append(CPPPATH = [MLIBRARY + '/options' + OPTIONS_VERSION])

	libs = [
			  'options',
			  ]

	c12libs = []
	for lib in libs:
		c12libs.append(lib)

	env.Append(LIBPATH = [MLIBRARY + '/lib'])
	env.Append(LIBS = c12libs)

	if env['SHOWENV'] == "1":
		print "Loading MLIBRARY software from ", MLIBRARY

