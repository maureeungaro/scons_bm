from util import check_if_dir_exist

def loadbc12Map(env, OSENV) :
	C12BFIELDS = OSENV['C12BFIELDS']
	check_if_dir_exist('C12BFIELDS', C12BFIELDS)

	## includes
	incs = [C12BFIELDS + '/includes']
	env.Append(CPPPATH = incs)


	## library paths
	ldir = [C12BFIELDS + '/lib']
	env.Append(LIBPATH = ldir)
			
	## libraries
	libs = ['cMag']
	env.Append(LIBS = libs)

	# print environment if requested
	if env['SHOWENV'] == "1":
		print ("\n > Loading C12BFIELDS software from ", C12BFIELDS)
		print ("   C12BFIELDS include flags: ",  incs)
		print ("   C12BFIELDS libraries path: ", ldir)
		print ("   C12BFIELDS libraries: ",      libs)
