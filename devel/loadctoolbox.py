from util import check_if_dir_exist
import os

def loadctoolbox(env) :
	OSENV = os.environ
	CTOOLBOX = OSENV['CTOOLBOX']
	check_if_dir_exist('CTOOLBOX')
	if env['SHOWENV'] == "1":
		print "Loading CToolBox software from ", CTOOLBOX

	env.Append(CCFLAGS = '-std=c++0x')

	ctoolincs = [ CTOOLBOX ]
	ctoolincs.append(CTOOLBOX)
	[env.Append(CXXFLAGS=[env['INCPREFIX']+d+env['INCSUFFIX']]) for d in ctoolincs]

	ctoolldir = []
	ctoolldir.append(CTOOLBOX)
	env.Append(LIBPATH = ctoolldir)

	ctoollibs = []
	ctoollibs.append('ctools')
	env.Append(LIBS = ctoollibs)
