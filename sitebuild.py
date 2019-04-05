# Tyler Rajotte
# Script to take content from a csv and convert it to HTML to copy paste into my site
import datetime
import os
import git


class SiteBuild(object):
    def __init__(self):
        self.homebody = []
        self.homebodystring = ""
        self.data = []

        self.__import()
        print("Imported Data")
        self.__newpost()
        print("Created Posts")
        self.__compileposts()
        print("Compiled Posts")
        self.__export()
        print("Exported Code Block")
        self.__deploy()
        print("Site Deployed")

        print("Site Built!")

    @staticmethod
    def __deploy():
        # Deploys current directory to github
        repo = git.Repo(os.getcwd())
        repo.git.add(".")
        repo.git.commit(m="SiteAutoBuild-{}".format(datetime.datetime.now().date()))
        repo.git.push()

    @staticmethod
    def __convertdate(inputdate):
        # Converts Dates from numbers to a nicely formated version 
        monthdata = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                     "November", "December"]
        splited = inputdate.split("-")
        year = splited[0]
        date = splited[2]
        month = monthdata[int(splited[1]) - 1]
        return "{} {}, {}".format(month, date, year)

    def __compileposts(self):
        compileposts = ""
        for post in self.homebody:
            for codeline in post:
                compileposts = compileposts + codeline
        self.homebodystring = compileposts

    def __import(self):
        # Imports the CSV file and splits it based on newlines and puts it into self.data
        database = open("TotalyANewDatabase.csv", "r")
        self.data = database.read().split("\n")
        database.close()
        del self.data[0]

    def __export(self):
        templateindexfile = open("UFindex.html", "r")
        templateindex = templateindexfile.read().split("\n")
        templateindexfile.close()

        indexoutput = open("index.html", "w")
        for line in templateindex:
            if line == "|body|":
                indexoutput.write(self.homebodystring)
            else:
                indexoutput.write(line + "\n")

    def __newpost(self):
        # New post on homepage
        for entry in self.data:
            if entry == "":
                continue

            entry = entry.split(",")

            print("Creating: " + str(entry))
            
            self.__createhomepost(entry)
            self.__createpage(entry)

    def __createhomepost(self, entry):
        title = entry[0]
        fontsize = entry[1]
        date = self.__convertdate(entry[2])
        titleimage = "./images/icon/" + entry[3]
        pagename = "./pages/" + entry[4] + ".html"

        template = [
            "      <div class=\"flexboxchild\" style=\"background-image: url(\'{}\')\">\n".format(titleimage),
            "        <a class=\"hiddenlink\" href=\"{}\">\n".format(pagename),
            "          <div class=\"childcontainer\">\n",
            "            <div class=\"childtitle\" style=\"font-size: {}vw\">{}</div>\n".format(fontsize, title),
            "            <div class=\"childdate\">{}</div>\n".format(date),
            "          </div>\n",
            "        </a>\n",
            "      </div>\n"]

        self.homebody.append(template)

    def __createpage(self, entry):
        print("Creating Page: {}".format(entry))


if __name__ == "__main__":
    SiteBuild()
