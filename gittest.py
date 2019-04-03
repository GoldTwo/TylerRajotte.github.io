import subprocess
message = "Auto Commit Attempts..."

addlist = ["git", "add", "."]
subprocess.call(addlist)

commitlist = ["git", "commit", "-a", "-m", "\"" + message + "\""]
subprocess.call(commitlist)

pushlist = ["git", "push"]
subprocess.call(pushlist)
