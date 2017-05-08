from util import check_if_dir_exist
import os

def loadclas12(env) :
	OSENV = os.environ
	BANKS = OSENV['BANKS']
	GEMC  = OSENV['GEMC']
	check_if_dir_exist('BANKS')
	check_if_dir_exist('GEMC')

	env.Append(CPPPATH = [BANKS + '/src'])
	env.Append(CPPPATH = [GEMC + '/src'])
	env.Append(CPPPATH = [GEMC + '/output'])
	env.Append(CPPPATH = [GEMC + '/utilities'])

	# Notice: The order counts here
	libs = [
			  'banks',
			  'goutput',
			  'gutilities'
			  ]

	c12libs = []
	for lib in libs:
		c12libs.append(lib)

	env.Append(LIBPATH = [BANKS + '/lib'])
	env.Append(LIBPATH = [GEMC +  '/lib'])
	env.Append(LIBS = c12libs)

	if env['SHOWENV'] == "1":
		print "\n > Loading BANKS software from ", BANKS
		print "   > Loading GEMC software from ", GEMC
		print "\n > BANKS, GEMC  libraries: ",  c12libs
