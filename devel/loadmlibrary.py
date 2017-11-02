from util import scanFiles, check_if_dir_exist
import os
import re


# MLIBRARY already has the version in it

def loadmlibrary(env) :
	OSENV = os.environ
	MLIBRARY = OSENV['MLIBRARY']
	check_if_dir_exist('MLIBRARY')

	## includes
	mincs = ['options', 'translationTable', 'splash', 'gruns', 'textProgressBar', 'gstring', 'frequencySyncSignal', 'qtButtonsWidget', 'gfactory', 'gdynamic', 'gtouchable', 'gvolume', 'g4volume', 'g4display', 'ghit', 'gdata']
	mincludes = []
	for minc in mincs:
		thisInc =  MLIBRARY + '/' + minc
		env.Append(CXXFLAGS=[env['INCPREFIX'] + thisInc + env['INCSUFFIX']])
		mincludes += [thisInc]

	## library paths
	mlibrarydir = [MLIBRARY + '/lib']
	env.Append(LIBPATH = mlibrarydir)

	## libraries - this will include cadmesh
	libs = scanFiles(MLIBRARY + '/lib', accept=[ "*.a", "*.lib"])

	# only load library if it exists
	mlibs = []
	for dir in libs:
		basename = os.path.basename(dir)
		wout_lib = basename.strip('lib')
		lib      = re.sub("\.a", "", wout_lib)
		mlibs.append(lib)


	env.Append(LIBS = mlibs)

	if env['SHOWENV'] == "1":
		print "\n > Loading MLIBRARY software from ", MLIBRARY
		print "   MLIBRARY include flags: ",  mincludes
		print "   MLIBRARY libraries path: ", mlibrarydir
		print "   MLIBRARY libraries: ",      mlibs

