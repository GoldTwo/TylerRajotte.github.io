import git
import os
import datetime

print(os.getcwd())
repo = git.Repo(os.getcwd())
repo.git.add(".")
repo.git.commit(m="SiteAutoBuild-{}".format(datetime.datetime.now().date()))
repo.git.push()
