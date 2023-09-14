from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

website = 'https://www.thesun.co.uk/sport/football/'

# Add headless mode
options = Options()
options.headless = True

# Use webdriver_manager to automatically download and manage the ChromeDriver executable
driver_service = Service(ChromeDriverManager().install())

# Create a ChromeDriver instance
driver = webdriver.Chrome(service=driver_service, options=options)

# Open the URL
driver.get(website)

# Find the containers that hold the headlines
containers = driver.find_elements(by='xpath', value='//div[@class="teaser__copy-container"]')

titles = []
subtitles = []
links = []
for container in containers:
    title = container.find_element(by='xpath', value='./a/span').text
    subtitle = container.find_element(by='xpath', value='./a/h3').text
    link = container.find_element(by='xpath', value='./a').get_attribute('href')
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

my_dict = {'title': titles, 'subtitle': subtitles, 'link': links}
df_headlines = pd.DataFrame(my_dict)
df_headlines.to_csv('csv/headline-headless.csv')

driver.quit()