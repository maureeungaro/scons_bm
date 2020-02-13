from util import check_if_dir_exist
import os
from SCons.Builder import *


def loadcuda(env) :
	OSENV  = os.environ
	CUDA_HOME = OSENV['CUDA_HOME']
	CUDA_LIB  = OSENV['CUDA_LIB']
	check_if_dir_exist('CUDA_HOME')

	# Cuda compiler options
	env.Append(CUDA_FLAGS = env['INCPREFIX'] + CUDA_HOME + '/include ')
	env.Append(CUDA_FLAGS = env['INCPREFIX'] + CUDA_HOME + '/sdk/C/common/inc ')
	env.Append(CUDA_FLAGS = '--compiler-options ')
	if env['PLATFORM'] == 'posix':
		env.Append(CUDA_FLAGS='-DUNIX')
	if env['CUDA_EMU'] == "1":
		env.Append(CUDA_FLAGS=' -deviceemu ')
			
	if env['SHOWENV'] == "1":
		print ("Loading CUDA software from ", CUDA_HOME, CUDA_FLAGS)

	
	cuda_bld = Builder(action = '/usr/local/cuda/bin/nvcc  $CUDA_FLAGS -o $TARGETS -c $SOURCES',
										 suffix = '.cuo')
	env.Append(BUILDERS = {'CUDABuild' : cuda_bld})


	# Now normal source code options, libraries
	env.Append(CXXFLAGS = env['INCPREFIX'] + CUDA_HOME + '/include')
	env.Append(CXXFLAGS = env['INCPREFIX'] + CUDA_HOME + '/sdk/C/common/inc')
	
	libs = [
					'cudart', 'paramgl', 'rendercheckgl',  'GLEW_x86_64', 'cutil'
	       ]
	if env['CUDA_EMU'] == "1":
		libs.append('cudpp64_emu')
	else:
		libs.append('cudpp64')
		
	
	cudalibs = []
	for lib in libs:
		cudalibs.append(lib)


	env.Append(LIBPATH = [CUDA_LIB])
	env.Append(LIBPATH = [CUDA_HOME + '/sdk/C/lib'])
	env.Append(LIBS = cudalibs)

	if env['PLATFORM'] == 'posix':
		env.Append(LIBPATH = [CUDA_HOME + '/sdk/C/common/lib/linux'])
		env.Append(CXXFLAGS='-DUNIX')
		cudalibs.append('GL')
		cudalibs.append('GLU')
		cudalibs.append('Xmu')
		cudalibs.append('X11')
		cudalibs.append('Xi')
		cudalibs.append('Xmu')
		cudalibs.append('glut')
		env.Append(LIBS = cudalibs)
		if env['CUDA_EMU'] == "1":
			env.Append(CXXFLAGS='-D__DEVICE_EMULATION__')
			



