# # print("helloworld!")
# # from urllib.request import urlretrieve
# # from urllib.request import urlopen
# # from bs4 import BeautifulSoup
# # html = urlopen("http://www.pythonscraping.com")
# # bsObj = BeautifulSoup(html,features='lxml')
# # imageLocation = bsObj.find("a", {"id": "logo"}).find("img")["src"]
# # urlretrieve (imageLocation, "logo.jpg")
# #
# # print("end")
#
# # import smtplib
# # from email.mime.text import MIMEText
# # msg = MIMEText("The body of the email is here")
# # msg['Subject'] = "An Email Alert"
# # msg['From'] = "ryan@pythonscraping.com"
# # msg['To'] = "webmaster@pythonscraping.com"
# # s = smtplib.SMTP('localhost')
# # s.send_message(msg)
# # s.quit()
# #
# # from urllib.request import urlopen
# # textPage = urlopen(
# #     "http://www.pythonscraping.com/pages/warandpeace/chapter1.txt")
# # print(textPage.read())
#
# # from urllib.request import urlopen
# # from bs4 import BeautifulSoup
# # def ngrams(input, n):
# #     input = input.split(' ')
# #     output = []
# #     for i in range(len(input)-n+1):
# #         output.append(input[i:i+n])
# #     return output
# #
# # html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
# # bsObj = BeautifulSoup(html)
# # content = bsObj.find("div", {"id":"mw-content-text"}).get_text()
# # ngrams = ngrams(content, 2)
# # print(ngrams)
# # print("2-grams count is: "+str(len(ngrams)))
#
# import sys
#
# def getPos(m):
#     for i in range(len(m)):
#         if m[i] == 9 :
#             return i
#
# def result(state,cache,l,r):
#     for i in range(l,r):
#         if state == cache[i]:
#             return i
#     return -1
#
# step = 0
#
# def print_after(cache,far,num):#print 后序
#     if num==-1:
#         return
#     print_after(cache,far,far[num])
#     print(cache[num])
#     global step
#     step+=1
#
#
# def printf_before(cache2,far2,num):#print 前序
#     if num == -1:
#         return
#     print(cache2[num])
#     printf_before(cache2,far2,far2[num])
#     global step
#     step += 1
#
# def do_with(cache,cache2,far,l,r,l2,r2):
#     flag = 0
#     t = cache[l]
#
#     #得到9所在的行列数x，y
#     pos = getPos(t)
#     x,y = divmod(pos,3)
#
#     #四个方向，四种新状态
#     newpos = []
#     if y < 2:newpos.append(pos+1)
#     if y > 0:newpos.append(pos-1)
#     if x < 2:newpos.append(pos+3)
#     if x > 0:newpos.append(pos-3)
#     for ipos in newpos:
#         tt = cache[l][:]
#         tt[ipos]=cache[l][pos]
#         tt[pos]=cache[l][ipos]
#
#         #如果新状态没在cache中就加入cache，队列尾巴r+1
#         if tt not in cache:
#             cache.append(tt)
#             far.append(l)
#             r += 1
#             #如果新状态在逆向的cache2中找到，那么新状态就是接口状态
#             #找到接口状态就可以直接打印了，返回接口状态的下标res，赋值给flag
#             res = result(tt,cache2,l2,r2)
#             if res != -1:
#                 flag = res
#     l += 1
#     return cache,cache2,far,l,r,l2,r2,flag
#
# def do_with_print(before,after):
#     print_after(cache,far,before)
#     printf_before(cache2,far2,far2[after])#如果这里不用far2[flag]而用flag就重复计算中间的接口状态
#     print ("step-1") #减去一开始的状态不计算步数
#     sys.exit(0)
#
# start = [1,2,3,4,5,6,7,8,9]
# end   = [9,8,7,6,5,4,3,2,1]
#
# cache = [start] #保存正向状态
# cache2 = [end]  #保存逆向状态
# far = [-1]      #保存正向状态的left节点下标
# far2 = [-1]     #保存逆向状态的left节点下标
#
# l = l2 = 0
# r = r2 = 1
#
#
# while (l!=r)and(l2!=r2):      #BFS，left == right表示队列为空
#     flag = -1 #保存中间接口状态的下标
#     cache,cache2,far,l,r,l2,r2,flag = do_with(cache,cache2,far,l,r,l2,r2)
#     if flag:
#         do_with_print(r-1,flag)
#     cache2,cache,far2,l2,r2,l,r,flag = do_with(cache2,cache,far2,l2,r2,l,r)
#     if flag:
#         do_with_print(flag,r-1)

dllinks=['http://185.38.13.130//mp43/264345.mp4?st=Fx_oeP404bEevKWXCprYEg&e=1525581565',
'http://185.38.13.130//mp43/264347.mp4?st=8eLndQq9dSxdFdJgjZGbrg&e=1525581565',
'http://185.38.13.130//mp43/264316.mp4?st=qIhDwkLP1bzNlnAs50pHDA&e=1525581565',
'http://185.38.13.130//mp43/264341.mp4?st=Aq6vjKC2lo0-xMgXBWlgcQ&e=1525581566',
'http://185.38.13.130//mp43/264344.mp4?st=FqF1ms1kLeLkubnYzEGVaA&e=1525581566',
'http://185.38.13.130//mp43/264333.mp4?st=19jYr_fQNZO-IGH0AAXZPw&e=1525581566',
'http://185.38.13.130//mp43/264356.mp4?st=-34kbJ8PQhuRcj-Xe2nJ8w&e=1525581566',
'http://185.38.13.130//mp43/264207.mp4?st=3KSY63k4dTk6IDiAyGYuHA&e=1525581566',
'http://185.38.13.130//mp43/264200.mp4?st=_LaYga4AvkstTmkPsKqPEw&e=1525581567',
'http://185.38.13.130//mp43/264277.mp4?st=PmWo_oWIFyNK961kOhsTog&e=1525581567',
'http://185.38.13.130//mp43/264323.mp4?st=eqV1GLy4NjxfoTSPG_O9nQ&e=1525581567',
'http://185.38.13.130//mp43/264208.mp4?st=CqRNea-sv_fNUXgiWLBvFw&e=1525581567',
'http://185.38.13.130//mp43/264205.mp4?st=xGCD2Ns_OlfL_HE17uxFsA&e=1525581568',
'http://185.38.13.130//mp43/264336.mp4?st=frAeLzPTgP96I_ZKKqoBxA&e=1525581568',
'http://185.38.13.130//mp43/264222.mp4?st=Yvqvh2EXFOWKTHscuwclIw&e=1525581568',
'http://185.38.13.130//mp43/264189.mp4?st=1z4zPemla7LrTFbCxy8q7w&e=1525581568',
'http://185.38.13.130//mp43/264188.mp4?st=-nsxlnM8k73hK0UREnnTHQ&e=1525581569',
'http://185.38.13.130//mp43/264184.mp4?st=Mlqoy36X24iSlvHddsU7RQ&e=1525581569',
'http://185.38.13.130//mp43/264196.mp4?st=Y1ZjmJSOrfI3l7HUABol0w&e=1525581569',
'http://185.38.13.130//mp43/264199.mp4?st=b1TUBVXNasd_jipG7D__-g&e=1525581569']

for index in range(len(dllinks)):
    print(dllinks[index])
    name =dllinks[index]
    name = name[name.index('//mp43') + 7:name.index('.mp4') + 4]
    print(name)

import time
print(time.asctime(time.localtime(time.time())))
print(time.strftime("%m-%d-%Y %H:%M:%S", time.localtime()))