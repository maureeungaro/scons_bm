import os

def loadqt(env) :

	OSENV = os.environ
	QTDIR = OSENV['QTDIR']

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
	else:
		env['ENV']['PKG_CONFIG_PATH'] = os.environ['PKG_CONFIG_PATH']
		env.EnableQt5Modules(qtModules)
		env.Append(CPPFLAGS = ' -fPIC')

	# Qt existance is already checked
	if env['SHOWENV'] == "1":
		print "Loading QT5 software from ", QTDIR , "for ", env['PLATFORM']
		print "Qt Modules to be loaded: ", qtModules
