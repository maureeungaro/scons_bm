from util import check_if_dir_exist
import os

def loadevio(env) :
	OSENV = os.environ
	EVIO = OSENV['EVIO']
	check_if_dir_exist('EVIO')

	## includes
	evioincs1 = [EVIO + '/src/libsrc']
	evioincs2 = [EVIO + '/src/libsrc++']
	env.Append(CPPPATH = evioincs1)
	env.Append(CPPPATH = evioincs2)


	## library paths
	evioldir = [EVIO + '/lib']
	env.Append(LIBPATH = evioldir)
			
	## libraries
	eviolibs = ['evioxx', 'evio']
	if env['PLATFORM'] == 'posix':
		eviolibs.append('z')
		eviolibs.append('libexpat')
		eviolibs.append('pthread')

	if env['PLATFORM'] == 'darwin':
		eviolibs.append('z')
		eviolibs.append('libexpat')
    	
		# Assuming we have boost, installed with FINK
		eviolibs.append('pthread')
	
	env.Append(LIBS = eviolibs)

	if env['PLATFORM'] == 'win32':
		MSSDK   =  OSENV['MSSdk']
		EXPAT   =  OSENV['EXPAT']
		env.Append(CPPPATH = [EXPAT + '/Source/lib'])
		env.Append(CPPPATH = [MSSDK + '/Include'])
		env.Append(LIBPATH = [EXPAT + '/bin'])

	# print environment if requested
	if env['SHOWENV'] == "1":
		print "\n > Loading EVIO software from ", EVIO
		print "   EVIO include flags: ",  evioincs1, evioincs2
		print "   EVIO libraries path: ", evioldir
		print "   EVIO libraries: ",      eviolibs
