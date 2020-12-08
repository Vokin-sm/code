import os
import os.path

os.chdir("C:\code")
print(os.getcwd())
print(os.path.exists("pyvenv.cfg"))

for current_dir, dirs, files in os.walk("."):
    print(current_dir, dirs, files)