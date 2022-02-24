import os
import subprocess

list_files = subprocess.run("ls", "-l", capture_output=True)
print ("the files were: %s", list_files)