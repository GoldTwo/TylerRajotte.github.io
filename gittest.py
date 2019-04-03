import subprocess
message = "Auto Commit Attempts..."

addlist = ["git", "add", "."]
addcmd = "git add ."
subprocess.call(addcmd, shell=True)

commitlist = ["git", "commit", "-a", "-m", "\"" + message + "\""]
commitcmd = "git commit -a -m \"" + message + "\""
subprocess.call(commitcmd, shell=True)

pushlist = ["git", "push"]
pushcmd = "git push"
push = subprocess.Popen(pushcmd, stdout=subprocess.PIPE).communicate()
print(push)
