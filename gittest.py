import os
message = "Auto Commit Attempts..."

os.system("git add .")
os.system("git commit -a -m \"{}\"".format(message))
os.system("git push")
