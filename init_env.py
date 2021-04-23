from util import cmloptions, loadoptions, check_if_dir_exist
import os

from SCons.Environment import *
from SCons.Variables import *
from SCons.Script import *


def init_environment(reqlist) :
	print("Initializing Environment:")
	opts = Variables()
	print(" - Variables")
	cmloptions(opts)
	OSENV = os.environ
	print(" - os.environ")

	# first check if there's qt5 in the requirement
	print("Loading environment...")
	need_qt5 = 0
	list = reqlist.split()
	for l in list:
		if l == "qt5":
			QTDIR = OSENV['QTDIR']
			check_if_dir_exist('QTDIR', QTDIR)
			env = Environment(tools=['default', 'qt5'], options = opts)
			print("QT5 environment is loaded")
			need_qt5 = 1
			break

	# if not, build default
	if need_qt5 == 0:
		env = Environment(tools=['default'], options = opts)
		print("Default environment is loaded")

	sdebug = 0;
	if env['SDEBUG'] == "1":
		sdebug = 1
		print("SDEBUG is set")

	# Now scanning the dependencies
	for l in list:
		if l == "cadmesh":
			from loadcadmesh import loadcadmesh
			loadcadmesh(env)
		elif l == "ccdb":
			from loadccdb import loadccdb
			loadccdb(env)
		elif l == "clas":
			from loadclas import loadclas
			loadclas(env)
		elif l == "clas12":
			from loadclas12 import loadclas12
			loadclas12(env)
		elif l == "clhep":
			from loadclhep import loadclhep
			loadclhep(env, OSENV)
		elif l == "cuda":
			from loadcuda import loadcuda
			loadcuda(env)
		elif l == "evio":
			from loadevio import loadevio
			loadevio(env)
		elif l == "geant4":
			from loadgeant4 import loadgeant4
			loadgeant4(env, OSENV)
		elif l == "hipo":
			from loadhipo import loadhipo
			loadhipo(env)
		elif l == "jana":
			from loadjana import loadjana
			loadjana(env)
		elif l == "mu":
			from loadmu import loadmu
			loadmu(env)
		elif l == "mlibrary":
			from loadmlibrary import loadmlibrary
			loadmlibrary(env)
		elif l == "glibrary":
			from loadglibrary import loadglibrary
			loadglibrary(env, OSENV)
		elif l == "mysql":
			from loadmysql import loadmysql
			loadmysql(env)
		elif l == "qt5":
			QTDIR = OSENV['QTDIR']
			from loadqt import loadqt
			loadqt(env, QTDIR)
		elif l == "root":
			from loadroot import loadroot
			loadroot(env)
		elif l == "xercesc":
			from loadxerces import loadxerces
			loadxerces(env)

	# generating help list
	Help(opts.GenerateHelpText(env))
	if sdebug == 1:
		print("Help List Generated")
	# loading options
	loadoptions(env)
	if sdebug == 1:
		print("Options Loaded")
	return env
	
