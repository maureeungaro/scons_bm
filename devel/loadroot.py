from util import check_if_dir_exist
import os
import re

def loadroot(env) :

	ROOTSYS = os.environ.get('ROOTSYS')
	check_if_dir_exist('ROOTSYS')
	if env['SHOWENV'] == "1":
		print "Loading ROOT software from ", ROOTSYS

	inc_path = []

	if env['PLATFORM'] == 'posix' or env['PLATFORM'] == 'darwin':
		inc_path = os.popen('$ROOTSYS/bin/root-config --incdir').readline()

	# on Windows there is no script
	# Have to do it by hand
	if env['PLATFORM'] == 'win32':
		inc_path = ROOTSYS + "\include"

	env.Append(CXXFLAGS = env['INCPREFIX'] + inc_path)

	rootlibs = []
	root_config_libs = []
	if env['PLATFORM'] == 'posix' or env['PLATFORM'] == 'darwin':
		root_config_libs = os.popen('$ROOTSYS/bin/root-config --glibs').readline().rstrip().split()

	# on Windows there is no script
	# Have to do it by hand
	# Do a showenv on Linux/Darwin and copy here
	if env['PLATFORM'] == 'win32':
		rootlibs = ['libCore', 'libCint', 'libRIO', 'libNet', 'libHist', 'libGraf', 'libGraf3d', 'libGpad', 'libTree', 'libRint', 'libPostscript', 'libMatrix', 'libPhysics', 'libMathCore', 'libThread', 'libGui']

	rootlibs += [ x for x in root_config_libs if re.match('-l',x) ]

	env.Append(LIBPATH = [ x for x in root_config_libs  if re.match('-L',x) ] )

	if env['SHOWENV'] == "1":
		print "ROOT include path: ", inc_path
		print "ROOT Libraries: ", rootlibs


	env.Append(LIBS = rootlibs)

