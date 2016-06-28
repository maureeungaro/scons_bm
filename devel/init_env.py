from util import cmloptions, loadoptions, check_if_dir_exist
import os

from SCons.Environment import *
from SCons.Variables import *
from SCons.Script import *

def init_environment(reqlist) :
	opts = Variables()
	cmloptions(opts)

	# first check if there's qt5 in the requirement
	need_qt5 = 0
	list = reqlist.split()
	for l in list:
		if l == "qt5":
			check_if_dir_exist('QTDIR')
			env = Environment(tools=['default', 'qt5'], options = opts, ENV = os.environ)
			need_qt5 = 1
			break

	# if not, build default
	if need_qt5 == 0:
		env = Environment(options = opts)


	# Now scanning the dependencies
	for l in list:
		if l == "ccdb":
			from loadccdb import loadccdb
			loadccdb(env)
		if l == "clas":
			from loadclas import loadclas
			loadclas(env)
		if l == "clas12":
			from loadclas12 import loadclas12
			loadclas12(env)
		if l == "clhep":
			from loadclhep import loadclhep
			loadclhep(env)
		if l == "cmsg":
			from loadcmsg import loadcmsg
			loadcmsg(env)
		if l == "clara":
			from loadclara import loadclara
			loadclara(env)
		if l == "ctoolbox":
			from loadctoolbox import loadctoolbox
			loadctoolbox(env)
		if l == "cuda":
			from loadcuda import loadcuda
			loadcuda(env)
		if l == "evio":
			from loadevio import loadevio
			loadevio(env)
		if l == "geant4":
			from loadgeant4 import loadgeant4
			loadgeant4(env)
		if l == "jana":
			from loadjana import loadjana
			loadjana(env)
		if l == "mu":
			from loadmu import loadmu
			loadmu(env)
		if l == "mysql":
			from loadmysql import loadmysql
			loadmysql(env)
		if l == "qt5":
			from loadqt import loadqt
			loadqt(env)
		if l == "root":
			from loadroot import loadroot
			loadroot(env)
		if l == "xercesc":
			from loadxerces import loadxerces
			loadxerces(env)
		if l == "mlibrary":
			from loadmlibrary import loadmlibrary
			loadmlibrary(env)

	# generating help list
	Help(opts.GenerateHelpText(env))
	# loading options
	loadoptions(env)
	return env
	