import bs4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

USERNAME = "Your username"
PASSWORD = "Your password"

driver = webdriver.Chrome()
driver.get("https://studentnet.cs.manchester.ac.uk/ugt/year3/project/projectbooktitles.php?year=2024")

username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
username.send_keys(USERNAME)
password.send_keys(PASSWORD)
driver.find_element(By.NAME,"submit").click()

file = driver.page_source
driver.quit()
soup = bs4.BeautifulSoup(file, "html.parser")

categories = soup.select(f"#content > div > section > article > div > div")

outputFile = open("./output.csv", "w")

header = "Title,Category,Project Link,Proposer,Student Availability,CM COMP30030 Difficulty,CS COMP30040 Difficulty,PhD Potential\n"
outputFile.write(header)

for category in categories[2:]:
    projectCategory = category.a.attrs['name']
    for project in category.find_all("div", recursive=False):
        print(project)
        projectCMDifficulty = project.select("div:nth-child(1) > table > tbody > tr:nth-child(3) > td:nth-child(1)")[0].getText()
        projectCSDifficulty = project.select("div:nth-child(1) > table > tbody > tr:nth-child(3) > td:nth-child(2)")[0].getText()
        projectLink = project.select("div:nth-child(2) > p:nth-child(1) > a")[0].attrs["href"]
        projectTitle = project.select("div:nth-child(2) > p:nth-child(1) > a")[0].getText().replace('"', "")
        projectProposer = project.select("div:nth-child(2) > p:nth-child(2)")[0].getText().replace("Proposer: ", "")
        projectAvailability = project.select("div:nth-child(2) > p:nth-child(3)")[0].getText().replace("Available for ", "")
        temp = project.select("div:nth-child(2)")[0]
        print(len(temp.findChildren()))
        if len(temp.findChildren()) == 5:
            projectPHD = False
        else:
            projectPHD = True
        line = f"\"{projectTitle}\",\"{projectCategory}\",\"{projectLink}\",\"{projectProposer}\",\"{projectAvailability}\",\"{projectCMDifficulty}\",\"{projectCSDifficulty}\",\"{projectPHD}\"\n"
        print(line)
        outputFile.write(line)

outputFile.close()