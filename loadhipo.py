from util import check_if_dir_exist

def loadhipo(env, OSENV) :
	HIPO = OSENV['HIPO']
	check_if_dir_exist('HIPO', HIPO)

	if env['SHOWENV'] == "1":
		print ("\n > Loading HIPO software from ", HIPO)
	
	## includes
	env.Append(CPPPATH = HIPO)

	## flags
	env.Append(LINKFLAGS = '-rdynamic')

	## libraries
	hipolibs = ['hipo4']
	hipolibs.append('lz4')
	if env['LIBRARY'] == 'shared':
		env.Append(LIBPATH = [HIPO + '/slib'])

	env.Append(LIBPATH = [HIPO + '/lib'])

	env.Append(LIBS = hipolibs)

