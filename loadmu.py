from util import check_if_dir_exist

def loadmu(env, OSENV) :
	MU = OSENV['MU']
	check_if_dir_exist('MU', MU)
	if env['SHOWENV'] == "1":
		print ("Loading MU software from ", MU)

	env.Append(CXXFLAGS = env['INCPREFIX'] + MU + '/v4')
	env.Append(CXXFLAGS = env['INCPREFIX'] + MU + '/src')
	env.Append(CXXFLAGS = env['INCPREFIX'] + MU + '/bos2mu')
	env.Append(CXXFLAGS = env['INCPREFIX'] + MU + '/binning')

	libs = [
	        'CLAS_Event', 'V4', 'utilities', 'CLAS_Event', 'bin'
	       ]

	mulibs = []
	for lib in libs:
		mulibs.append(lib)


	env.Append(LIBPATH = [MU + '/lib'])
	env.Append(LIBS = mulibs)

