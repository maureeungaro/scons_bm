from util import scanFiles, check_if_dir_exist
import os


# MLIBRARY already has the version in it

def loadmlibrary(env) :
	OSENV = os.environ
	MLIBRARY = OSENV['MLIBRARY']
	check_if_dir_exist('MLIBRARY')
	env.Append(LIBPATH = [MLIBRARY + '/lib'])
	env.Append(CPPPATH = [MLIBRARY + '/options'])

	libs = scanFiles(MLIBRARY + '/lib', accept=[ "*.a", "*.lib"])

	# only load library if it exists
	c12libs = []
	for dir in libs:
		basename = os.path.basename(dir)
		wout_lib = basename.strip("lib")
		lib      = wout_lib.strip(".a")
		print "mlibrary: ", lib
		c12libs.append(lib)

	env.Append(LIBS = c12libs)

	if env['SHOWENV'] == "1":
		print "Loading MLIBRARY software from ", MLIBRARY

