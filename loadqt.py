import os

def loadqt(env, QTDIR) :

	# QtCore, QtGui, QtWidgets, QtOpenGL, QtPrintSupport are enabled in geant4
	# However when compiling non-geant4 apps they need to be included
	qtincs = [];
	qtlibs = [];
	qtModules = ["QtCore", "QtGui", "QtWidgets", "QtOpenGL", "QtXml", "QtSql"]

	for mod in qtModules:
		qtincs.append(" -I" + QTDIR + "/lib/" + mod + ".framework/Headers")
		qtlibs.append(' -framework ' + mod )
	# joining all together
	qtcppf  = ''.join(qtincs)
	qtlinkf = ''.join(qtlibs)

	# The location of the headers is different in Linux and Darwin (oh why oh why)
	if env['PLATFORM'] == 'darwin':
		env.Append(CPPFLAGS  = "-F" + QTDIR + "/lib" )
		env.Append(CPPFLAGS = qtcppf )
		env.Append(LINKFLAGS = "-F" + QTDIR + "/lib" )
		env.Append(LINKFLAGS = qtlinkf)
		# added because starting with qt 5.5: the prebuilt 5.5.0 binaries from Qt
		# use @rpath for mac instead @excutable_path or an absolute path.
		# For Linux this is not necessary
		env.Append(LINKFLAGS  = "-rpath " + QTDIR + "/lib" )

	else:
		if os.environ.get('PKG_CONFIG_PATH') is not None:
			env['ENV']['PKG_CONFIG_PATH'] = os.environ['PKG_CONFIG_PATH']

		env.EnableQt5Modules(qtModules)
		env.Append(CPPFLAGS = ' -fPIC')

	# Qt existance is already checked
	if env['SHOWENV'] == "1":
		print ("\n > Loading QT5 software from ",  QTDIR , "for ", env['PLATFORM'])
		print ("   Qt Modules: ",  qtModules)
