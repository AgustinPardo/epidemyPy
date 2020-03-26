import requests
import re
from bs4 import BeautifulSoup

# Argentina
page_argentina = requests.get("https://public.flourish.studio/visualisation/1605488/embed?auto=1")
content=page_argentina.text.replace("\n","").replace("\t","").split(";")[-5]
cases_per_day_argentina = re.findall("(?<=\"value\":\[\")[0-9]+",content)
print(cases_per_day_argentina)


# Otro pais
page = requests.get("https://www.worldometers.info/coronavirus/country/italy/")
soup = BeautifulSoup(page.content, 'html.parser')
images = soup.find_all('script', type='text/javascript')
print(images)