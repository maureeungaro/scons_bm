from util import check_if_dir_exist

def loadccdb(env, OSENV) :
	CCDB_HOME = OSENV['CCDB_HOME']
	check_if_dir_exist('CCDB_HOME', CCDB_HOME)

	## includes
	ccdbincs = [CCDB_HOME + '/include']
	env.Append(CPPPATH = ccdbincs)

	## library paths
	ccdblibp = [CCDB_HOME + '/lib']
	env.Append(LIBPATH = ccdblibp)

	if env['PLATFORM'] == 'darwin' and env['HOST_ARCH'] == 'arm64':
		print(" > Apple M1 or M2 chip detected, adding /opt/homebrew/lib to paths    ")
		env.Append(LIBPATH = '/opt/homebrew/lib')

	## libraries
	ccdblibs = ['ccdb', 'libmysqlclient', 'sqlite3']
	env.Append(LIBS = ccdblibs)

	# print environment if requested
	if env['SHOWENV'] == "1":
		print ("\n > Loading CCDB software from ", CCDB_HOME)
		print ("   CCDB include flags: ",  ccdbincs)
		print ("   CCDB libraries path: ", ccdblibp)
		print ("   CCDB libraries: ",      ccdblibs)
