import os
from os import listdir
from os.path import isfile, join

current_dir = os.path.dirname(os.path.realpath(__file__))

task_folder = os.path.join(current_dir, "task")

count_files = 0  # [f for f in listdir(current_dir) if isfile(join(current_dir, f))]
count_mastered = 0
count_dp = 0

for f in listdir(current_dir):
    if f in ["_leet_code_summary.py", "__init__.py"]:
        continue
    f_path = join(current_dir, f)
    if isfile(f_path):
        count_files += 1
        with open(f_path, 'r') as file:
            content = file.read()
            if content.find("[mastered]") > 0:
                count_mastered += 1
            if content.find("[dp]") > 0:
                count_dp += 1

print "============================================"
print "# {0} problems were solved".format(count_files)
print "# {0:3} problems were mastered".format(count_mastered)
print "# {0:3} dp problems".format(count_dp)
print "============================================"
