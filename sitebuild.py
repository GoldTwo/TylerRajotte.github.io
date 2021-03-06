# Tyler Rajotte
# Script to take content from a csv and convert it to HTML to copy paste into my site
import datetime
import os
import git


class SiteBuild(object):
    def __init__(self):
        self.data = []
        self.bestofdata = []

        self.homebody = []
        self.homebodystring = ""

        self.bestofbody = []
        self.bestofstring = ""

        self.__import()
        print("Imported Data")
        self.__importbestof()
        print("Imported Bestof Data")

        self.__newpost()
        print("Created Posts")
        self.__compileposts()
        print("Compiled Posts")
        self.__export()
        print("Exported Code Block")

        self.__newbestofposts()
        print("Created Best of Posts")
        self.__compilebestofposts()
        print("Compiled best of Posts")
        self.__exportbestof()
        print("Exported Best of Code Block")

        self.__deploy()
        print("Site Deployed")

        print("Site Built!")

    def __importbestof(self):
        bestoffile = open("bestof/BestOf20182019.txt", "r")
        formatedbestof = bestoffile.read().split("\n")
        bestoffile.close()
        del formatedbestof[0]
        for i in formatedbestof:
            if i == "":
                continue
            else:
                self.bestofdata.append(i)

    def __newbestofposts(self):
        # New post on homepage
        for entry in self.bestofdata:
            for potentialpost in self.data:
                if potentialpost == "":
                    continue
                potentialpostformatted = potentialpost.split(",")
                if potentialpostformatted[4] == entry:
                    self.__createbestofpost(potentialpostformatted)

    def __createbestofpost(self, entry):
        # Generates the html and appends it to main body array
        # Each item in the homebody array is a post containing the html
        title = entry[0]
        fontsize = entry[1]
        date = self.__convertdate(entry[2])
        titleimage = "./images/icon/" + entry[3]
        pagename = "./pages/" + entry[4] + ".html"

        template = [
            "      <div class=\"flexboxchild\" style=\"background-image: url(\'{}\')\">\n".format(titleimage),
            "        <a class=\"hiddenlink\" href=\"{}\">\n".format(pagename),
            "          <div class=\"childcontainer\">\n",
            "            <div class=\"childtitle {}text\">{}</div>\n".format(fontsize, title),
            "            <div class=\"childdate\">{}</div>\n".format(date),
            "          </div>\n",
            "        </a>\n",
            "      </div>\n"]

        self.bestofbody.append(template)

    def __compilebestofposts(self):
        # Converts the array to a string
        compileposts = ""
        for post in self.bestofbody:
            for codeline in post:
                compileposts = compileposts + codeline
        self.bestofstring = compileposts

    def __exportbestof(self):
        # Takes compiled string and copy pastes it on to the template
        indextemplatefile = open("template/bestofTemplate.html", "r")
        indextemplate = indextemplatefile.read().split("\n")
        indextemplatefile.close()

        indexoutput = open("bestof20182019.html", "w")
        for line in indextemplate:
            if line == "|body|":
                indexoutput.write(self.bestofstring)
            else:
                indexoutput.write(line + "\n")

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

    @staticmethod
    def __flattenlist(inputlist):
        flatten = ""
        for item in inputlist:
            for line in item:
                flatten = flatten + line
        return flatten

    def __compileposts(self):
        compileposts = ""
        for post in self.homebody:
            for codeline in post:
                compileposts = compileposts + codeline
        self.homebodystring = compileposts

    def __import(self):
        # Imports the CSV file and splits it based on newlines and puts it into self.data
        database = open("PageData.csv", "r")
        self.data = database.read().split("\n")
        database.close()
        del self.data[0]
        self.data = self.data[::-1]

    def __export(self):
        indextemplatefile = open("template/indexTemplate.html", "r")
        indextemplate = indextemplatefile.read().split("\n")
        indextemplatefile.close()

        indexoutput = open("index.html", "w")
        for line in indextemplate:
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
            try:
                self.__createpage(entry)
            except FileNotFoundError:
                print("Missing Files to Build Page: {}".format(entry[0]))

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
            "            <div class=\"childtitle {}text\">{}</div>\n".format(fontsize, title),
            "            <div class=\"childdate\">{}</div>\n".format(date),
            "          </div>\n",
            "        </a>\n",
            "      </div>\n"]

        self.homebody.append(template)

    def __createpage(self, entry):
        pagebody = []

        pagebodydatafile = open("pagedata/{}.txt".format(entry[5]), "r")
        pagebodydata = pagebodydatafile.read().replace("\n", " ")
        pagebodydatafile.close()

        texttemplate = [
            "      <div id=\"textbody\" class=\"desktoppagetext\" style=\"font-size: {}vw;\">\n".format(entry[6]),
            "{}\n".format(pagebodydata),
            "      </div>\n",
            "      <div id=\"textbody\" class=\"mobilepagetext\" style=\"font-size: {}vw;\">\n".format(float(entry[6]) * 3),
            "{}\n".format(pagebodydata),
            "      </div>\n"
        ]

        images = entry[7].split("|")

        for image in images:
            image = image.replace("\"", "")
            if "$" in image:
                image = image.replace("$", "")
                videotemplate = [
                    "      <div id=\"pagevideo\">\n",
                    "        <iframe width=\"100%\" height=\"100%\" src=\"{}\" frameborder=\"0\" allowfullscreen></iframe>\n".format(image),
                    "      </div>\n"
                ]
                pagebody.append(videotemplate)
            else:
                image = "../images/pageimages/" + image
                imagetemplate = [
                    "      <div id=\"pageimage\">\n",
                    "        <img src=\"{}\" style=\"width:inherit;\">\n".format(image),
                    "      </div>\n"
                ]
                pagebody.append(imagetemplate)

        pagebody.insert(1, texttemplate)

        # Writing Data to a new page
        pagetemplatefile = open("template/bodyTemplate.html", "r")
        pagetemplate = pagetemplatefile.read().split("\n")
        pagetemplatefile.close()

        newpage = open("pages/{}.html".format(entry[4]), "w")
        for line in pagetemplate:
            if line == "|body|":
                newpage.write(self.__flattenlist(pagebody))
            else:
                newpage.write(line + "\n")
        newpage.close()


if __name__ == "__main__":
    SiteBuild()
