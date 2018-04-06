#Trying to print the name and the price
from urllib.request import urlopen
from bs4 import BeautifulSoup
html= urlopen("https://sfbay.craigslist.org/search/hhh?query=rent&sort=rel").read().decode('utf-8')
soup=BeautifulSoup(html,features='lxml')
res=soup.find_all("a",
                  {"class":"result-title hdrlink",
                   })
print(res)


