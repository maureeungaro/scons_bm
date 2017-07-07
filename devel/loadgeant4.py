import os
from util import subdirsContaining, scanFiles, check_if_dir_exist

def loadgeant4(env) :
	OSENV = os.environ
	G4INSTALL = OSENV['G4INSTALL']
	check_if_dir_exist('G4INSTALL')

	# Geant 4 additional compiler options
	env.Append(CXXFLAGS='-DG4OPTIMISE')
	env.Append(CXXFLAGS='-DG4_STORE_TRAJECTORY')
	env.Append(CXXFLAGS='-DG4VIS_USE_OPENGL')
	env.Append(CXXFLAGS='-DG4UI_USE_TCSH')
	env.Append(CXXFLAGS='-DG4INTY_USE_QT')
	env.Append(CXXFLAGS='-DG4UI_USE_QT')
	env.Append(CXXFLAGS='-DG4VIS_USE_OPENGLQT')
	env.Append(CXXFLAGS='-DG4USE_STD11')
	env.Append(CXXFLAGS='-DG4MULTITHREADED')

	## includes
	# Stripping all entries that are not geant4 related
	validg4incs = []
	g4incs =  os.popen('$G4INSTALL/bin/geant4-config --cflags').readline()
	splits  = g4incs.split('-D')
	for s in splits:
		# remove spaces
		spl = s.split()
		for ss in spl:
			# only add if it's a g4 library
			if ss.startswith('G4'):
				validg4incs.append('-D' + ss);

	splits  = g4incs.split('-I')
	for s in splits:
		# remove spaces
		spl = s.split()
		for ss in spl:
			# only add if it's a g4 library
			if 'geant4' in ss:
				validg4incs.append('-I'+ss);

	# geant4 had this additional flag.
	# validg4incs.append('-std=c++98');
	env.Append(CXXFLAGS  = validg4incs)

	## Libraries
	# We can't just add g4libs to LINKFLAGS because in
	# some systems the library order comes out not correct
	# and LINKFLAGS always come before LIBS
	# So we use the geant4-config and strip the path and the libs independently
	# Also, we strip out CLHEP from the libraries
	g4libs =  os.popen('$G4INSTALL/bin/geant4-config --libs').readline()

	# splits list based on -l
	splits  = g4libs.split('-l')

	validg4libs = []
	for s in splits:
		# remove spaces
		spl = s.split()
		for ss in spl:
			# only add if it's a g4 library
			if ss.startswith('G4'):
				validg4libs.append(ss);

	## Library paths
	libpath = []
	for s in splits:
		if s.startswith('-L'):
			libpath.append(s.strip())
	env.Append(LINKFLAGS = libpath)
			

	if env['PLATFORM'] == 'posix':
		env.Append(CXXFLAGS='-I/usr/include/GL')
		env.Append(CXXFLAGS='-DG4VIS_USE_OPENGLX')
		validg4libs.append('GL')
		# manually adding G4zlib
		# looks like geant4-config does not provide it?
		validg4libs.append('G4zlib')

	if env['PLATFORM'] == 'darwin':
		env.Append(CXXFLAGS='-I/System/Library/Frameworks/OpenGL.framework/Headers')
		env.Append(LINKFLAGS = '-L/System/Library/Frameworks/OpenGL.framework/Libraries/')
		validg4libs.append('GL')

	if env['PLATFORM'] == 'win32':
		validg4libs.append('glu32')
		validg4libs.append('opengl32')
		validg4libs.append('gdi32')
		validg4libs.append('user32')
		env.Append(CXXFLAGS='-D_CONSOLE')
		env.Append(CXXFLAGS='-DOS')
		env.Append(CXXFLAGS='-DWIN32')
		env.Append(CXXFLAGS='-D_WIN32')

	env.Append(LIBS  = validg4libs)

	# print environment if requested
	if env['SHOWENV'] == "1":
		print "Loading Geant4 software from ", G4INSTALL
		print "Geant4 include flags: ",  validg4incs
		print "Geant4 libraries path: ", libpath
		print "Geant4 libraries: ",      validg4libs







