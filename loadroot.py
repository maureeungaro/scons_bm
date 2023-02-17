from util import check_if_dir_exist
import os
import re


def loadroot(env, OSENV):
	BINROOT = os.popen('root-config --bindir').readline().strip()

	inc_path = []

	# includes
	if env['PLATFORM'] == 'posix' or env['PLATFORM'] == 'darwin':
		inc_path = os.popen(BINROOT+ '/root-config --incdir').readline().rstrip()

	env.Append(CXXFLAGS=env['INCPREFIX'] + inc_path)

	# libraries and paths
	rootlibs = []
	root_config_libs = []
	if env['PLATFORM'] == 'posix' or env['PLATFORM'] == 'darwin':
		# manual root_config_libs
		# root_config_libs = ['-lCore', '-lRIO', '-lTree', '-lHist']
		root_config_libs = os.popen(BINROOT + '/root-config --glibs').readline().rstrip().split()
		root_libpath = os.popen(BINROOT + '/root-config --libdir').readline().rstrip().split()

	# This filters out all the "-lxxx" parts of the root_config_libs
	rootlibs += [x for x in root_config_libs if re.match('-l', x)]
	# This grabs the "-L" part of the root_config_libs
	env.Append(LIBPATH=root_libpath)

	if env['SHOWENV'] == "1":
		print("\n > Loading ROOT software from as directed by root-config in", BINROOT)
		print("   ROOT include flags: ", inc_path)
		print("   ROOT libraries path: ", root_libpath)
		print("   ROOT libraries: ", rootlibs)

	env.Append(LIBS=rootlibs)
