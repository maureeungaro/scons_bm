from util import scanFiles, check_if_dir_exist
import os
import re


# GLIBRARY already has the version in it

def loadglibrary(env, OSENV) :
	GLIBRARY = OSENV['GLIBRARY']
	check_if_dir_exist('GLIBRARY', GLIBRARY)

	## includes
	gincs1 = ['guts', 'goptions', 'gsplash', 'gdata', 'gfactory', 'gtouchable', 'gdynamicDigitization', 'ghit', 'gsystem', 'g4system']
	gincs2 = ['gstreamer', 'eventDispenser', 'textProgressBar', 'gQtButtonsWidget', 'g4display', 'gtranslationTable', 'gparticle']

	gincs = gincs1 + gincs2

	gincludes = []
	for ginc in gincs:
		thisInc =  GLIBRARY + '/' + ginc
		env.Append(CXXFLAGS=[env['INCPREFIX'] + thisInc + env['INCSUFFIX']])
		gincludes += [thisInc]

	## library paths
	glibrarydir = [GLIBRARY + '/lib']
	env.Append(LIBPATH = glibrarydir)

	## libraries - this will include cadmesh
	libs = scanFiles(GLIBRARY + '/lib', accept=[ "*.a", "*.lib"])

	# only load library if it exists
	glibs = []
	for dir in libs:
		basename = os.path.basename(dir)
		wout_lib = basename.strip('lib')
		lib      = re.sub("\.a", "", wout_lib)
		glibs.append(lib)

	# c++ MT
	glibs.append('pthread')

	# appending glibraries
	# to address Linux problems in -l order
	glibs.append('pthread')
	glibs.append('ghit')
	glibs.append('textProgressBar')
	glibs.append('gdata')
	glibs.append('gtranslationTable')
	glibs.append('gtouchable')

	env.Append(LIBS = glibs)

	if env['SHOWENV'] == "1":
		print ("\n > Loading GLIBRARY software from ", GLIBRARY)
		print ("   GLIBRARY include flags: ",  gincludes)
		print ("   GLIBRARY libraries path: ", glibrarydir)
		print ("   GLIBRARY libraries: ",      glibs)

