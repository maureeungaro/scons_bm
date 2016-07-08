from util import check_if_dir_exist
import os

# MLIBRARY already has the version in it

def loadmlibrary(env) :
	OSENV = os.environ
	MLIBRARY = OSENV['MLIBRARY']
	check_if_dir_exist('MLIBRARY')

	env.Append(CPPPATH = [MLIBRARY + '/options'])

	libs = [
			  'options',
			  'translationTable'
			  ]

	c12libs = []
	for lib in libs:
		c12libs.append(lib)

	env.Append(LIBPATH = [MLIBRARY + '/lib'])
	env.Append(LIBS = c12libs)

	if env['SHOWENV'] == "1":
		print "Loading MLIBRARY software from ", MLIBRARY

