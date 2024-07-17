from util import scanFiles, check_if_dir_exist
import os
import re


# GLIBRARY already has the version in it

def loadcadmesh(env, OSENV) :
	GLIBRARY = OSENV['GLIBRARY']
	check_if_dir_exist('GLIBRARY', GLIBRARY)

	gincs = ['include']
	gincludes = []
	for ginc in gincs:
		thisInc =  GLIBRARY + '/' + ginc
		env.Append(CXXFLAGS=[env['INCPREFIX'] + thisInc + env['INCSUFFIX']])
		gincludes += [thisInc]


	## library paths
	glibrarydir = [GLIBRARY + '/lib']
	env.Append(LIBPATH = glibrarydir)

	## addind cadmesh library names by hand
	libs = ['cadmesh', 'assimp', 'tet']

	# only load library if it exists
	glibs = []
	for dir in libs:
		basename = os.path.basename(dir)
		wout_lib = basename.strip('lib')
		lib      = re.sub(".a", "", wout_lib)
		glibs.append(lib)


	env.Append(LIBS = glibs)

	if env['SHOWENV'] == "1":
		print ("\n > Loading Cadmesh software from ", GLIBRARY)
		print ("   Cadmesh include flags: ",  gincludes)
		print ("   Cadmesh libraries path: ", glibrarydir)
		print ("   Cadmesh libraries: ",      glibs)

