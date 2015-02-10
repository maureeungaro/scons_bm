from util import check_if_dir_exist
import os

def loadcmsg(env) :
	OSENV = os.environ
	CMSG = OSENV['CMSG']
	check_if_dir_exist('CMSG')
	if env['SHOWENV'] == "1":
		print "Loading cmsg software from ", CMSG

	cmsgincs = []
	cmsgincs.append(CMSG + '/include')
	[env.Append(CXXFLAGS=[env['INCPREFIX']+d+env['INCSUFFIX']]) for d in cmsgincs]

	cmsgldir = []
	cmsgldir.append(CMSG + '/lib')
	env.Append(LIBPATH = cmsgldir)

	cmsglibs = []
	cmsglibs.append('cmsgxx')
	cmsglibs.append('cmsg')
	cmsglibs.append('cmsgRegex')
	cmsglibs.append('pthread')
	cmsglibs.append('rt')
	cmsglibs.append('dl')
        cmsglibs.append('et')
        cmsglibs.append('codaObject')

	env.Append(LIBS = cmsglibs)
