from util import check_if_dir_exist

def loadmysql(env, OSENV) :
	MYSQL   = OSENV['MYSQL']
	MYSQINC = OSENV['MYSQINC']
	check_if_dir_exist('MYSQL', MYSQL)
	if env['SHOWENV'] == "1":
		print ("Loading Mysql software from ", MYSQL)

	mysqincs = []
	mysqincs.append(MYSQINC)
	[env.Append(CXXFLAGS=[env['INCPREFIX']+d+env['INCSUFFIX']]) for d in mysqincs]

	mysqldir = []

	if env['PLATFORM'] == 'posix':
		mysqldir.append(OSENV['MYSQLIB'])

	if env['PLATFORM'] == 'darwin':
		mysqldir.append(OSENV['MYSQLIB'])

	if env['PLATFORM'] == 'win32':
		mysqldir.append(OSENV['MYSQL'] + '/lib/opt')


	env.Append(LIBPATH = mysqldir)

	mysqlibs = []
	if env['PLATFORM'] == 'posix':
		mysqlibs.append('libmysqlclient')

	if env['PLATFORM'] == 'darwin':
		mysqlibs.append('libmysqlclient')

	if env['PLATFORM'] == 'win32':
		mysqlibs.append('libmysql')
  
	env.Append(LIBS = mysqlibs)
