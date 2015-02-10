import os

def loadclas(env) :
	OSENV  = os.environ
	CLAS6INC = OSENV['CLAS6INC']
	CLAS6LIB = OSENV['CLAS6LIB']
	CERNLIB  = OSENV['CERNLIB']
	if env['SHOWENV'] == "1":
		print "Loading CLAS software from ", CLAS_PACK

	env.Append(CXXFLAGS = env['INCPREFIX'] + CLAS6INC)
#	env.Append(CXXFLAGS = env['INCPREFIX'] + CLAS_PACK + '/inc_derived')
#	env.Append(CXXFLAGS = env['INCPREFIX'] + CLAS_PACK + '/caldb/Map')

	libs = [
	           'pid', 'sc', 'tag', 'cc', 'st', 'ec', 'dc', 'trk', 'clasutil', 'c_bos_io',  'recutl', 'bosio',
                'vertex', 'trk', 'dc', 'st', 'pid', 'sc', 'tag', 'c_bos_io', 'caldbMap', 'clasutil', 'bankdefs', 'c_cern',
                'tcl', 'recutl', 'packlib', 'mathlib'
	       ]

	claslibs = []
	for lib in libs:
		claslibs.append(lib)


	env.Append(LIBPATH = [CLAS6LIB])
	env.Append(LIBPATH = [CERNLIB])
	env.Append(LIBS = claslibs)

  if env['ARCHI'] == 'x86':
    env.Append(LINKFLAGS = '-L/usr/lib -l:libgfortran.so.1')
  else:
    env.Append(LINKFLAGS = '-L/usr/lib64 -l:libgfortran.so.1')
    


	if env['PLATFORM'] == 'darwin':
		#env.Append(CPPPATH = '/sw/include')
		#env.Append(CPPPATH = '/Developer/SDKs/MacOSX10.5.sdk/usr/include')

		#env.Append(LIBPATH = '/usr/X11/lib')
		env.Append(LIBPATH = '/sw/lib/gcc4.4/lib')

		#env.Append(LIBS = ['Xm', 'Xt'])
