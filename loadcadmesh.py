from util import scanFiles, check_if_dir_exist
import os
import re


# MLIBRARY already has the version in it

def loadcadmesh(env, OSENV) :
	MLIBRARY = OSENV['MLIBRARY']
	check_if_dir_exist('MLIBRARY', MLIBRARY)

	## includes
	# mincs = ['cadmesh/include', 'cadmesh/external/assimp/include', 'cadmesh/external/tetgen']
	# This is all that should be needed for the includes. The above can be actually removed from disk
	mincs = ['include']
	mincludes = []
	for minc in mincs:
		thisInc =  MLIBRARY + '/' + minc
		env.Append(CXXFLAGS=[env['INCPREFIX'] + thisInc + env['INCSUFFIX']])
		mincludes += [thisInc]


	## library paths
	mlibrarydir = [MLIBRARY + '/lib']
	env.Append(LIBPATH = mlibrarydir)

	## addind cadmesh library names by hand
	libs = ['cadmesh', 'assimp', 'tet']

	# only load library if it exists
	mlibs = []
	for dir in libs:
		basename = os.path.basename(dir)
		wout_lib = basename.strip('lib')
		lib      = re.sub("\.a", "", wout_lib)
		mlibs.append(lib)


	env.Append(LIBS = mlibs)

	if env['SHOWENV'] == "1":
		print ("\n > Loading Cadmesh software from ", MLIBRARY)
		print ("   Cadmesh include flags: ",  mincludes)
		print ("   Cadmesh libraries path: ", mlibrarydir)
		print ("   Cadmesh libraries: ",      mlibs)

