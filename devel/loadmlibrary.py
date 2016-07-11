from util import scanFiles, check_if_dir_exist
import os


# MLIBRARY already has the version in it

def loadmlibrary(env) :
	OSENV = os.environ
	MLIBRARY = OSENV['MLIBRARY']
	check_if_dir_exist('MLIBRARY')


	## includes
	mlibraryincs1 = [MLIBRARY + '/options']
	mlibraryincs2 = [MLIBRARY + '/translationTable']
	env.Append(CPPPATH = mlibraryincs1)
	env.Append(CPPPATH = mlibraryincs2)


	## library paths
	mlibrarydir = [MLIBRARY + '/lib']
	env.Append(LIBPATH = mlibrarydir)

	## libraries
	libs = scanFiles(MLIBRARY + '/lib', accept=[ "*.a", "*.lib"])

	# only load library if it exists
	mlibs = []
	for dir in libs:
		basename = os.path.basename(dir)
		wout_lib = basename.strip("lib")
		lib      = wout_lib.strip(".a")
		mlibs.append(lib)

	env.Append(LIBS = mlibs)

	if env['SHOWENV'] == "1":
		print "\n > Loading MLIBRARY software from ", MLIBRARY
		print "   MLIBRARY include flags: ",  mlibraryincs1, mlibraryincs1
		print "   MLIBRARY libraries path: ", mlibrarydir
		print "   MLIBRARY libraries: ",      mlibs

