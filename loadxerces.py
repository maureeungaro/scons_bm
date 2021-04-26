from util import check_if_dir_exist

def loadxerces(env, OSENV) :
	XERCESCROOT = OSENV['XERCESCROOT']
	check_if_dir_exist('XERCESCROOT', XERCESCROOT)

	## includes
	xercesincs = [XERCESCROOT + '/include']
	env.Append(CPPPATH = xercesincs)

	## library paths
	xercesldir1 = [XERCESCROOT + '/lib']
	env.Append(LIBPATH = xercesldir1)

	## some OS need lib64
	if env['PLATFORM'] == 'posix':
		xercesldir2 = [XERCESCROOT + '/lib64']
		env.Append(LIBPATH = xercesldir2)

	## libraries
	xerceslibs = ['xerces-c']
	env.Append(LIBS = xerceslibs)

	# forgot why we needed /usr/local?
	#env.Append(LIBPATH = ['/usr/local/lib'])

	# print environment if requested
	if env['SHOWENV'] == "1":
		print ("\n > Loading XERCESC software from ", XERCESCROOT)
		print ("   XERCESC include flags: ",  xercesincs)
		print ("   XERCESC libraries path: ", xercesldir1)
		print ("   XERCESC libraries: ",      xerceslibs)
