import requests
from bs4 import BeautifulSoup
import pandas

# Create a csv file 'ProductBasicData.csv' to store the data
# The file will be created in the same folder as the python file
# The columns of the csv file are: 'Name', 'Category', Pledgegoal', 'Pledged', 'DaysToGo'


# Empty List of urls
url = []

# URL of the page to be scraped
#url_example = 'https://www.kickstarter.com/projects/336477435/mini-pupper-2-open-source-ros2-robot-kit-for-dreamers?ref=section-homepage-view-more-discovery-p1'
url_example = 'https://www.indiegogo.com/projects/ayaneo-2-completely-different-amd-6800u-handheld#/updates/all'
url.append(url_example)


# Empty Function that scrapes the data from the page
def scrape_data_and_write_in_csv(url):
        soup = getSoup(url)
        print(getNameKickstarter(soup))



# Function that gets an url and returns the soup object
def getSoup(url):
        page = requests.get(url).content
        print(page)
        soup = BeautifulSoup(page, 'html.parser')
        return soup

def getNameKickstarter(soup):
    # # Return the text in the h2 tag with the class "type-28 type-24-md soft-black mb1 project-name"
    # name = soup.body.find('h2', {'class': 'type-28 type-24-md soft-black mb1 project-name'}).contents[0].get_text()
    # return name

    # Return the text in the div 'data-v-16a8e71a' with the class 'basicsSection-title fullhd t-h3--sansSerif'
    name = soup.body.find('div', {'class': 'basicsSection-title fullhd t-h3--sansSerif'}).contents[0].get_text()
    return name

def getCategoryKickstarter(soup):
    ()

def getPledgeGoalKickstarter(soup):
    ()

def getPledgedKickstarter(soup):
    ()

def getDaysToGoKickstarter(soup):
    ()


print('Start')
scrape_data_and_write_in_csv(url_example)
print('End')

