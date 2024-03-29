from util import check_if_dir_exist

def loadjana(env, OSENV) :
	JANA_HOME = OSENV['JANA_HOME']
	check_if_dir_exist('JANA_HOME')
	if env['SHOWENV'] == "1":
		print ("Loading JANA software from ", JANA_HOME)

	## includes
	env.Append(CPPPATH = JANA_HOME + '/include')

	## flags
	env.Append(LINKFLAGS = '-rdynamic')

	## libraries
	janalibs = ['JANA']
	janalibs.append('pthread')
	janalibs.append('dl')	
	env.Append(LIBPATH = [JANA_HOME + '/lib'])
	env.Append(LIBS = janalibs)

