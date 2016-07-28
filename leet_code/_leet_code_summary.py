import os
from os import listdir
from os.path import isfile, join

current_dir = os.path.dirname(os.path.realpath(__file__))

task_folder = os.path.join(current_dir, "task")

all_file = [f for f in listdir(current_dir) if isfile(join(current_dir, f))]

print "============================================"
print "# {0} problems were solved".format(len(all_file) - 2)
print "============================================"