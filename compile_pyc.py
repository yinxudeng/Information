import os
import sys
import shutil
from py_compile import compile

if len(sys.argv) == 3:
	comd = sys.argv[1]
	path = sys.argv[2]
	if os.path.exists(path) and os.path.isdir(path):
		for parent, dirname, filename in os.walk(path):
			for cfile in filename:
				fullname = os.path.join(parent, cfile)
				if comd == 'compile' and cfile[-3:] == '.py':
					try:
						compile(fullname)
						print("Successfully compile file:%s" % fullname)
					except:
						print("Can't compile file:%s" % fullname)
				if comd == 'copy' and cfile[-4:] == '.pyc':
					parent_list = parent.split('/')[:-1]
					parent_up_path= ''
					for i in range(len(parent_list)):
						parent_up_path += parent_list[i] + '/'
					shutil.copy(fullname, parent_up_path)
					print('Successfully update dir of file ')
				if comd == 'remove' and cfile[-3:] == '.py' and cfile != 'settings.py' and cfile != 'wsgi.py':
					try:
						os.remove(fullname)
						print("Successfully remove file:%s" % fullname)
					except:
						print("Can't remove file:%s" % fullname)
				if comd == 'delete' and cfile[-4:] == '.pyc':
					parent_list = parent.split('/')
					if parent_list[-1] == '__pycache__':
						try:
							shutil.rmtree(parent)
							print('Successfully delete:%s' % parent)
						except:
							print("Dir has been removed:%s" % parent)
				if comd == 'cpython' and cfile[-4:] == '.pyc':
					cfile_name = ''
					cfile_list = cfile.split('.')
					for i in range(len(cfile_list)):
						if cfile_list[i] == 'cpython-37':
							continue
						cfile_name += cfile_list[i]
						if i == len(cfile_list)-1:
							continue
						cfile_name += '.'
					shutil.move(fullname, os.path.join(parent, cfile_name))
					print('Successfully update name of file ')
	else:
		print("Not an directory or Directory doesn't exist!")
else:
	print("Usage(in order):")
	print("\tpython compile_pyc.py compile PATH\t\t#To generate pyc files in __pycache__ dir")
	print("\tpython compile_pyc.py copy PATH\t\t\t#To move pyc files out of __pycache__ dir")
	print("\tpython compile_pyc.py remove PATH\t\t#To remove py files")
	print("\tpython compile_pyc.py delete PATH\t\t#To delete __pycache__ dir")
	print("\tpython compile_pyc.py cpython PATH \t\t#To remove .cpython-37 from pyc file names")

#reference: https://blog.csdn.net/u010565765/article/details/82180287






