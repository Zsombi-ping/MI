import os
import sys

if len(sys.argv) == 2:
    if sys.argv[1] == '1':
        os.system('python backtrack.py')
    elif sys.argv[1] == '2':
        os.system('python MI.py')
else:
    print('usage: {} option'.format(sys.argv[0]))
    print('options 1: backtracking \n 2: backtracking + MVR + forward checking: \n 3: backtracking + MVR + AC-3')