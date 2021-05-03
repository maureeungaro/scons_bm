import os
import glob
import sys

def recursiveDirs(root) :
	return filter( (lambda a : a.rfind( "CVS")==-1 ),  [ a[0] for a in os.walk(root)]  )

def check_if_dir_exist(system, SYSTEM) :
	if os.path.exists(SYSTEM) == False :
		print ("  !! Error: " , SYSTEM , " does not exist. Maybe ", system, " is not installed?")
		sys.exit(1)

def get_subdirectories(dir, reject=''):
	return [name for name in os.listdir(dir)
					if os.path.isdir(os.path.join(dir, name))
					if name != reject]
					
def unique(list) :
	return dict.fromkeys(list).keys()


# In Python 3, dict.keys() returns a dict_keys object (a view of the dictionary);
# unlike Python 2, where dict.keys() returns a list object.
# To return the list here, we add list(object)
def scanFiles(dir, accept=["include"], reject=[]) :
	sources = []
	paths = recursiveDirs(dir)
	for path in paths :
		for pattern in accept :
			sources+=glob.glob(path+"/"+pattern)
	for pattern in reject :
		sources = filter( (lambda a : a.rfind(pattern)==-1 ),  sources )
	return list(unique(sources))

#def subdirsContaining(root, patterns):
#	print("subdirsContaining")
#	dirs = unique(map(os.path.dirname, scanFiles(root, patterns)))
#	dirs.sort()
#	return dirs

# s is the original command line
# target and src are lists of target source nodes respectively
def print_cmd_line(s, target, src, env):
	c=s.split()
	sys.stdout.write("Building (%s) %s\n" %
	(c[0],
	', '.join([str(x) for x in target]) )  )


def loadoptions(env) :
	# EHsc and MD only for win32 envs
	if  env['PLATFORM'] == 'win32':
		env.Append(CXXFLAGS='-MD')     # for multithread, dynamic link. Causes compiler to place msvcrt in object file
		env.Append(CXXFLAGS='-EHsc')     
		env.Append(ENV = {'PATH': os.environ['PATH']})
		env.Append(ENV = {'INCLUDE': os.environ['INCLUDE']})
		env.AppendUnique(LIBPATH = [os.environ['MSLIBS']])
		env.AppendUnique(LIBPATH = [os.environ['SDKLIBS']])

	elif env['PLATFORM'] == 'posix':
		env.Append(ENV = {'PATH': os.environ['PATH']})
		env.Append(CXXFLAGS = '-fexceptions')
		env.Append(CXXFLAGS = '-fstack-protector')
		env.Append(CXXFLAGS = '-Wall')
		env.Append(LIBS = 'dl')
		if env['LIBRARY'] == 'shared':
			env.Append(CPPFLAGS = ' -fPIC')

	elif env['PLATFORM'] == 'darwin':
		env.Append(CXXFLAGS = '-fexceptions')
		env.Append(CXXFLAGS = '-fstack-protector')
		env.Append(CXXFLAGS = '-Wall')
		env.Append(CCFLAGS  = '-Wno-unused-private-field')

			
	if env['SHOWBUILD'] != "1":
		env['PRINT_CMD_LINE_FUNC'] = print_cmd_line
		env['CXXCOM']   = "${TEMPFILE('%s')}" % env['CXXCOM'] 
	
	if env['SHOWENV'] == "1":
		print ("  ")
		print ("Compiler: ", env['CC'])
		print ("Linker: ",   env.subst('$LINK'))
		print ("Platform: ", env['PLATFORM'])
		print ("  ")
	
	if env['OPT'] == "1":
		if env['PLATFORM'] == 'posix':
			env.Append(CXXFLAGS = '-O2')
			print ("Compiling with -O2 optimization.")
		elif env['PLATFORM'] == 'darwin':
			env.Append(CXXFLAGS = '-O2')
			print ("Compiling with -O2 optimization.")
		elif env['PLATFORM'] == 'win32':
			env.Append(CXXFLAGS = '/O2 /Gs')
			print ("Compiling with /O2 /Gs optimization.")
	
#	if env['XERCES3'] == "1":
#		OSENV  = os.environ
#		XERCESCROOT = OSENV['XERCESCROOT']
#		env.Append(CXXFLAGS='-DHAVE_XERCES=1 -DXERCES3=1 -I' + XERCESCROOT + '/include')
#

	if env['DEBUG'] == "1":
		if env['PLATFORM'] == 'posix':
			env.Append(CXXFLAGS = '-g')
			print ("Compiling with -g debug.")
		elif env['PLATFORM'] == 'darwin':
			env.Append(CXXFLAGS = '-g')
			print ("Compiling with -g debug.")
		elif env['PLATFORM'] == 'win32':
			env.Append(CXXFLAGS = '/DEBUG')	
			print ("Compiling with -/DEBUG debug.")
	
	if env['ARCHI'] == 'x86':
		env.Append(CXXFLAGS  = '-m32 ')
		env.Append(CPPFLAGS  = '-m32 ')
		env.Append(LINKFLAGS = '-m32 ')
		

	if env['PROFILE'] == "1":
		if env['PLATFORM'] == 'posix':
			env.Append(CXXFLAGS = '-pg')
			env.Append(LINKFLAGS = '-pg')
			print ("Compiling with -pg profiling.")

	# using c++17 standards
	#env.Append(CXXFLAGS = ' -std=c++11 ')
	env.Append(CXXFLAGS = ' -std=c++17 ')


def cmloptions(opts) :
	opts.Add('ARCHI',     'Set to x86 to force 32 bit environment', 0)
	opts.Add('SHOWENV',   'Set to 1 to show environment used', 0)
	opts.Add('SHOWBUILD', 'Set to 1 to show build commands executed', 0)
	opts.Add('OPT',       'Set to 1 to optimize code', 0)
	opts.Add('DEBUG',     'Set to 1 to compile in debug mode', 0)
	opts.Add('PROFILE',   'Set to 1 to compile in profiling mode', 0)
	opts.Add('CUDA_EMU',  'Set to 1 to compile in video-card emulation mode', 0)
	opts.Add('XERCES3',   'Set to 1 to compile with option -DXERCES3=1', 0)
	opts.Add('LIBRARY',   'Set at run time to compile shared or static library', 0)
	opts.Add('SDEBUG',    'Set to 1 to profile scons calls', 0)
	print(" - Command Line Options")

