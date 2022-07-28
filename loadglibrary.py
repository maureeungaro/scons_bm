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


	# appending glibraries in proper order
	glibs = []
	glibs.append('pthread')
	glibs.append('eventDispenser')
	glibs.append('textProgressBar')
	glibs.append('gdata')
	glibs.append('gtranslationTable')
	glibs.append('gdynamic')
	glibs.append('gtranslationTable')
	glibs.append('gtouchable')
	glibs.append('gparticle')
	glibs.append('goptions')
	glibs.append('g4system')
	glibs.append('gsystem')
	glibs.append('gQtButtonsWidget')
	glibs.append('gsplash')
	glibs.append('gdynamic')
	glibs.append('g4display')
	glibs.append('gstreamer')
	glibs.append('guts')
	glibs.append('ghit')
	glibs.append('gdata')
	env.Append(LIBS = glibs)

	if env['SHOWENV'] == "1":
		print ("\n > Loading GLIBRARY software from ", GLIBRARY)
		print ("   GLIBRARY include flags: ",  gincludes)
		print ("   GLIBRARY libraries path: ", glibrarydir)
		print ("   GLIBRARY libraries: ",      glibs)

