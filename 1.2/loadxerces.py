import os
from util import subdirsContaining, check_if_dir_exist

def loadxerces(env) :
	OSENV  = os.environ
	XERCESCROOT = OSENV['XERCESCROOT']
	check_if_dir_exist('XERCESCROOT')

	## includes
	xercesincs = [XERCESCROOT + '/include']
	env.Append(CPPPATH = xercesincs)

	## library paths
	xercesldir = [XERCESCROOT + '/lib']
	env.Append(LIBPATH = xercesldir)

	## libraries
	xerceslibs = ['xerces-c']
	env.Append(LIBS = xerceslibs)

	# forgot why we needed /usr/local?
	#env.Append(LIBPATH = ['/usr/local/lib'])

	# print environment if requested
	if env['SHOWENV'] == "1":
		print "\n > Loading XERCESC software from ", XERCESCROOT
		print "   XERCESC include flags: ",  xercesincs
		print "   XERCESC libraries path: ", xercesldir
		print "   XERCESC libraries: ",      xerceslibs
