# Tyler Rajotte
# Script to take content from a csv and convert it to HTML to copy paste into my site
import datetime
import os
import git


class SiteBuild(object):
    def __init__(self):
        self.homebody = []
        self.data = []

        self.__import()
        print("Imported Data")
        self.__newpost()
        print("Created Posts")
        self.__export()
        print("Exported Code Block")
        # self.__deploy()

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

    def __import(self):
        # Imports the CSV file and splits it based on newlines and puts it into self.data
        database = open("TotalyANewDatabase.csv", "r")
        self.data = database.read().split("\n")
        database.close()
        del self.data[0]

    def __export(self):
        output = open("SiteBuild_{}.txt".format(datetime.datetime.now().date()), "w")
        for entry in self.homebody:
            for xline in entry:
                output.write(xline)
        output.close()

    def __newpost(self):
        # New post on homepage
        for line in self.data:
            if line == "":
                continue

            line = line.split(",")

            print("Creating: " + str(line))

            title = line[0]
            fontsize = line[1]
            date = self.__convertdate(line[2])
            titleimage = "./images/icon" + line[3]
            pagename = "./pages/" + line[4] + ".html"

    def __createhomepost(self, title, fontsize, date, titleimage, pagename):
        date = self.__convertdate(date)
        titleimage = "./images/icon" + titleimage
        pagename = "./pages/" + pagename + ".html"

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


if __name__ == "__main__":
    SiteBuild()
