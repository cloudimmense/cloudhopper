import sys
import os , inspect
path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) 
sys.path.insert(0, path)

