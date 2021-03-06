from util import scanFiles, check_if_dir_exist
import os
import re


# GLIBRARY already has the version in it

def loadglibrary(env) :
	OSENV = os.environ
	GLIBRARY = OSENV['GLIBRARY']
	check_if_dir_exist('GLIBRARY')

	## includes
	gincs = ['goptions', 'gstring', 'gfactory', 'gtouchable', 'ghit', 'gdata']
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


	env.Append(LIBS = glibs)

	if env['SHOWENV'] == "1":
		print ("\n > Loading GLIBRARY software from ", GLIBRARY)
		print ("   GLIBRARY include flags: ",  gincludes)
		print ("   GLIBRARY libraries path: ", glibrarydir)
		print ("   GLIBRARY libraries: ",      glibs)

