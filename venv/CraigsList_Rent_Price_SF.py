from bs4 import BeautifulSoup
from urllib.request import urlopen
# Craigslist Renting Info
html= urlopen("https://sfbay.craigslist.org/search/hhh?query=rent&sort=rel").read().decode('utf-8')
print(html)
import re
res=re.findall(r"\$(\d*)</span>",html)
print(res)
sum=0
for i in res:
    sum=sum+int(i)
print(int(sum/len(res)))
# soup=BeautifulSoup(html,features='html.parser')
# print(soup.h1)
# print('\n', (soup))
