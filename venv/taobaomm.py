#Time: 05/02/2018
#Author: Xi Chen
#淘宝模特
from urllib.request import Request, urlopen
from generalFunction import getHeaders


def getUrlList():
    req = Request('https://mm.taobao.com/tstar/search/tstar_model.do?_input_charset=utf-8')
    req.add_header('user-agent',getHeaders())


print(getHeaders())