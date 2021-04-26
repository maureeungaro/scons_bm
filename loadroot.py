from util import check_if_dir_exist
import os
import re

def loadroot(env, OSENV) :

	ROOTSYS = OSENV['ROOTSYS']
	check_if_dir_exist('ROOTSYS', ROOTSYS)

	inc_path = []

	if env['PLATFORM'] == 'posix' or env['PLATFORM'] == 'darwin':
		inc_path = os.popen('$ROOTSYS/bin/root-config --incdir').readline().rstrip()

	# on Windows there is no script
	# Have to do it by hand
	if env['PLATFORM'] == 'win32':
		inc_path = ROOTSYS + "\include"

	env.Append(CXXFLAGS = env['INCPREFIX'] + inc_path)

	rootlibs = []
	root_config_libs = []
	if env['PLATFORM'] == 'posix' or env['PLATFORM'] == 'darwin':
		root_config_libs = os.popen('$ROOTSYS/bin/root-config --glibs').readline().rstrip().split()
		root_libpath     = os.popen('$ROOTSYS/bin/root-config --libdir').readline().rstrip().split()

	# on Windows there is no script
	# Have to do it by hand
	# Do a showenv on Linux/Darwin and copy here
	if env['PLATFORM'] == 'win32':
		rootlibs = ['libCore', 'libCint', 'libRIO', 'libNet', 'libHist', 'libGraf', 'libGraf3d', 'libGpad', 'libTree', 'libRint', 'libPostscript', 'libMatrix', 'libPhysics', 'libMathCore', 'libThread', 'libGui']

	# This filters out all the "-lxxx" parts of the root_config_libs
	rootlibs += [ x for x in root_config_libs if re.match('-l',x) ]

	# This grabs the "-L" part of the root_config_libs
	env.Append(LIBPATH = root_libpath )

	if env['SHOWENV'] == "1":
		print ("\n > Loading ROOT software from ", ROOTSYS)
		print ("   ROOT include flags: ",  inc_path)
		print ("   ROOT libraries path: ", root_libpath)
		print ("   ROOT libraries: ",      rootlibs)

	env.Append(LIBS = rootlibs)

