from util import check_if_dir_exist
import os

def loadclara(env) :
	OSENV = os.environ
	CLARA = OSENV['CLARA']
	check_if_dir_exist('CLARA')
	if env['SHOWENV'] == "1":
		print "Loading CLARA software from ", CLARA

	env.Append(CCFLAGS = '-std=c++0x')

	claraincs = [ CLARA ]
	claraincs.append(CLARA)
	[env.Append(CXXFLAGS=[env['INCPREFIX']+d+env['INCSUFFIX']]) for d in claraincs]

	claraldir = []
	claraldir.append(CLARA)
	env.Append(LIBPATH = claraldir)

	claralibs = []
	claralibs.append('clara')
	env.Append(LIBS = claralibs)
