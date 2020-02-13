from util import check_if_dir_exist
import os

def loadccdb(env) :
	OSENV  = os.environ
	CCDB_HOME = OSENV['CCDB_HOME']
	check_if_dir_exist('CCDB_HOME')

	## includes
	ccdbincs = [CCDB_HOME + '/include']
	env.Append(CPPPATH = ccdbincs)

	## library paths
	ccdblibp = [CCDB_HOME + '/lib']
	env.Append(LIBPATH = ccdblibp)

	## libraries
	ccdblibs = ['ccdb']
	env.Append(LIBS = ccdblibs)

	# print environment if requested
	if env['SHOWENV'] == "1":
		print ("\n > Loading CCDB software from ", CCDB_HOME)
		print ("   CCDB include flags: ",  ccdbincs)
		print ("   CCDB libraries path: ", ccdblibp)
		print ("   CCDB libraries: ",      ccdblibs)
