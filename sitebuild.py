# Tyler Rajotte
# Script to take content from a csv and convert it to HTML to copy paste into my site
import datetime
import os
import git


class SiteBuild(object):
    def __init__(self):
        self.MainExport = []
        self.data = []

        self.__import()
        self.__createdata()
        self.__export()
        # self.__deploy()

        print("Site Built!")

    @staticmethod
    def __deploy():
        repo = git.Repo(os.getcwd())
        repo.git.add(".")
        repo.git.commit(m="SiteAutoBuild-{}".format(datetime.datetime.now().date()))
        repo.git.push()

    @staticmethod
    def __convertdate(inputdate):
        monthdata = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                     "November", "December"]
        splited = inputdate.split("-")
        year = splited[0]
        date = splited[2]
        month = monthdata[int(splited[1]) - 1]
        return "{} {}, {}".format(month, date, year)

    def __import(self):
        database = open("TotalyANewDatabase.csv", "r")
        self.data = database.read().split("\n")
        database.close()
        del self.data[0]

    def __export(self):
        output = open("SiteBuild_{}.txt".format(datetime.datetime.now().date()), "w")
        for entry in self.MainExport:
            for xline in entry:
                output.write(xline)
        output.close()

    def __createdata(self):
        for line in self.data:
            if line == "":
                continue

            line = line.split(",")

            print("Created: " + str(line))

            Title = line[0]
            FontSize = line[1]
            Date = self.__convertdate(line[2])
            TitleImage = "./images/icon" + line[3]
            PageName = "./pages/" + line[4] + ".html"

            Template = []
            Template.append("      <div class=\"flexboxchild\" style=\"background-image: url(\'{}\')\">\n".format(TitleImage))
            Template.append("        <a class=\"hiddenlink\" href=\"{}\">\n".format(PageName))
            Template.append("          <div class=\"childcontainer\">\n")
            Template.append("            <div class=\"childtitle\" style=\"font-size: {}vw\">{}</div>\n".format(FontSize, Title))
            Template.append("            <div class=\"childdate\">{}</div>\n".format(Date))
            Template.append("          </div>\n")
            Template.append("        </a>\n")
            Template.append("      </div>\n")

            self.MainExport.append(Template)
