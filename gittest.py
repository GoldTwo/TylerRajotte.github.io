import subprocess
message = "Auto Commit Attempts..."
username = input("Username: ")
password = input("Password: ")

addlist = ["git", "add", "."]
addcmd = "git add ."
subprocess.call(addcmd, shell=True)

commitlist = ["git", "commit", "-a", "-m", "\"" + message + "\""]
commitcmd = "git commit -a -m \"" + message + "\""
subprocess.call(commitcmd, shell=True)

pushlist = ["git", "push"]
pushcmd = "git push"
push = subprocess.Popen(pushlist, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
push.communicate(input=username)
push.communicate(input=password)

# It might be better to use communicate:
#
# from subprocess import Popen, PIPE, STDOUT
# p = Popen(['myapp'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
# stdout_data = p.communicate(input='data_to_write')[0]
#
# "Better", because of this warning:
#
#     Use communicate() rather than .stdin.write, .stdout.read or .stderr.read to avoid deadlocks due to any of the other OS pipe buffers filling up and blocking the child process.
#

