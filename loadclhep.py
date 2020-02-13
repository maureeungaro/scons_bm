import os
from util import scanFiles, check_if_dir_exist

def loadclhep(env) :
	OSENV = os.environ
	CLHEP_BASE_DIR = OSENV['CLHEP_BASE_DIR']
	check_if_dir_exist('CLHEP_BASE_DIR')

	## includes
	clhepincs = [CLHEP_BASE_DIR + '/include']
	[env.Append(CXXFLAGS=[env['INCPREFIX']+d+env['INCSUFFIX']]) for d in clhepincs]

	## library paths
	clhldir = [CLHEP_BASE_DIR + '/lib']
	env.Append(LIBPATH = clhldir)

	## libraries
	# Only the main CLHEP library is needed
	libs = scanFiles(CLHEP_BASE_DIR + '/lib', accept=[ "*CLHEP.a", "*CLHEP.lib"])
	clhlibs = [] 
	for dir in libs:
		basename = os.path.basename(dir)
		wout_lib = basename.strip("lib")
		lib      = wout_lib.strip(".a")
		clhlibs.append(lib)
	env.Append(LIBS = clhlibs)


	# print environment if requested
	if env['SHOWENV'] == "1":
		print ("\n > Loading CLHEP software from ", CLHEP_BASE_DIR)
		print ("   CLHEP include flags: ",  clhepincs)
		print ("   CLHEP libraries path: ", clhldir)
		print ("   CLHEP libraries: ",      clhlibs)
