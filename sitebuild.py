# Tyler Rajotte
# Script to take content from a csv and convert it to HTML to copy paste into my site
import datetime
import os

def ConvertDate(Input):
    MonthData = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    Splited = Input.split("-")
    Year = Splited[0]
    Date = Splited[2]
    Month = MonthData[int(Splited[1]) - 1]
    return "{} {}, {}".format(Month, Date, Year)

MainExport = []

DataBase = open("TotalyANewDatabase.csv", "r")
Data = DataBase.read().split("\n")
DataBase.close()
del Data[0]

for line in Data:
    if line == "":
        continue

    line = line.split(",")

    print("Created: " + str(line))

    Title = line[0]
    FontSize = line[1]
    Date = ConvertDate(line[2])
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

    MainExport.append(Template)

output = open("SiteBuild_{}.txt".format(datetime.datetime.now().date()), "w")
for entry in MainExport:
    for line in entry:
        output.write(line)
output.close()
