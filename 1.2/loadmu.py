from util import check_if_dir_exist
import os

def loadmu(env) :
	OSENV  = os.environ
	MU     = OSENV['MU']
	check_if_dir_exist('MU')
	if env['SHOWENV'] == "1":
		print "Loading MU software from ", MU

	env.Append(CXXFLAGS = env['INCPREFIX'] + MU + '/V4/src')
	env.Append(CXXFLAGS = env['INCPREFIX'] + MU + '/CLAS_Event/src')
	env.Append(CXXFLAGS = env['INCPREFIX'] + MU + '/analysis/binning')

	libs = [
	        'CLAS_Event', 'V4', 'bin'
	       ]

	mulibs = []
	for lib in libs:
		mulibs.append(lib)


	env.Append(LIBPATH = [MU + '/V4'])
	env.Append(LIBPATH = [MU + '/CLAS_Event'])
	env.Append(LIBPATH = [MU + '/analysis/binning'])
	env.Append(LIBS = mulibs)

