import requests
from bs4 import BeautifulSoup
# scrap the html content
url="https://www.simplilearn.com/"
r=requests.get(url)
htmlContent =r.content
#print(htmlContent)
# parse the html content
soup= BeautifulSoup(r.content, 'html.parser')
#for i in soup.find_all("code"):
 #   print(i.text)
# get the titles of the website
titles =soup.title
#print(titles) 
# ----------get the first paragraph for the whole web page 
#print(soup.find('p'))
#-------get all paragraphs----------
#print(soup.find_all('p'))
# --------- get each paragraph ------
#a=soup.find_all('p')
#for i in a :
#    print(i)
#---------get the text of the first paragraph------
print(soup.find('p').get_text())
#------ print all the text from the webpage---
print(soup.get_text())