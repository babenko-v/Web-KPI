from requests import *
from bs4 import BeautifulSoup

link = 'https://browser-info.ru/'
response = get(link).text
soup = BeautifulSoup(response, 'lxml')
# result_1 = soup.find('div', id='javascript_check').find_all('span')[1].text
# print(result_1)
#
# result_2 = soup.find('div', id='flash_version').find_all('span')[1].text
# print(result_2)
#
# result_3 = soup.find('div', id='browser_lang').find_all('span')
# print(result_3)

result = soup.find('body')

# result1 = result.find('div', id='root')
result2 = soup.find('div', id='user_agent').text
print(result2)