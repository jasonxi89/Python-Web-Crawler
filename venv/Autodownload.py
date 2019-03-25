from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
from PIL import Image
import os
import requests
import re
import sys
import time




class ProgressBar(object):

    def __init__(self, title,
                 count=0.0,
                 run_status=None,
                 fin_status=None,
                 total=100.0,
                 unit='', sep='/',
                 chunk_size=1.0):
        super(ProgressBar, self).__init__()
        self.info = "【%s】%s %.2f %s %s %.2f %s"
        self.title = title
        self.total = total
        self.count = count
        self.chunk_size = chunk_size
        self.status = run_status or ""
        self.fin_status = fin_status or " " * len(self.statue)
        self.unit = unit
        self.seq = sep

    def __get_info(self):
        # 【名称】状态 进度 单位 分割线 总数 单位
        _info = self.info % (self.title, self.status,
                             self.count/self.chunk_size, self.unit, self.seq, self.total/self.chunk_size, self.unit)
        return _info

    def refresh(self, count=1, status=None):
        self.count += count
        # if status is not None:
        self.status = status or self.status
        end_str = "\r"
        if self.count >= self.total:
            end_str = '\n'
            self.status = status or self.fin_status
        print(self.__get_info(), end=end_str)

def mkdir(path):
    # 判断目录是否存在，不存在制造个
    #去除开头空格
    path = path.strip()
    #去除结尾\
    path = path.rstrip("\\")

    #判断路径是不是存在
    isExists=os.path.exists(path)
    if not + isExists:
        print ('创建目录' + path + '中....')

        os.makedirs(path)

        return True

    else:

        print('目录' + path + '已存在')

        return False


def report(count, blockSize, totalSize):
        percent = int(count * blockSize * 100 / totalSize)
        sys.stdout.write("\r%d%%" % percent + ' complete')
        sys.stdout.flush()

#获取下载链接的方法
def downLoadLink(session,url):
    index1 = session.get(url).text
    soup = BeautifulSoup(index1,features='lxml')

    dllinks= soup.find('a',{
        'href':re.compile('.*?\.mp4.*?'),
        'target':'blank'
    })

    # print(index1)
    # for dllink in dllinks:
    #     print(dllink)
    return dllinks

t=time.time()


# 程序实现目标：
# 1.自动登录
# 2.自动爬视频
# 3.自动下载

#1.实现验证码登录

##1.1 获取验证码



s=requests.session()

codeUrl = 'http://XXX.com/captcha.php'
valcode = requests.get('http://XXX.com/captcha.php')

f = open('valcode.png', 'wb')
# 将response的二进制内容写入到文件中
f.write(valcode.content)
# 关闭文件流对象
f.close()

#打开图片
img = Image.open('valcode.png')
img.show()
#输入验证码
code = input('请输入验证码:')
codeInfo = str(code)

#准备好登录用的信息
data={'username': 'sach1130', 'password': '7758521abc', 'captcha_input': codeInfo,'fingerprint':'3628342716','fingerprint2':'149a571a56fac10c8f2b7b5ac6c6f7b8','action_login':'Log+In','x':'39','y':16}
# 构造Header
checkHeader = {
    'Host': 'XXX.com',
    'Connection': 'keep-alive',
    'Content-Length': '155',
    'Cache-Control': 'max-age=0',
    'Origin': 'XXXX',
    'Referer': 'http://XXX.com/login.php',
    'Upgrade-Insecure-Requests': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'

}

#登录
print('logging...'+'\n')
r = s.post('http://XXX.com/login.php',
                  headers=checkHeader,
                  # cookies=requests.utils.dict_from_cookiejar(valcode.cookies),
                  data=data)
# r = s.get('http://XXX.com/my_profile.php')
#
# print(r.text)
#2 开始爬视频
#2.1 带着cookie打开新页面
#打开最近加精
dllinks=[]
vlink=[]

#r是登录路径
r = s.get('http://XXX.com/v.php?category=rf&viewtype=basic')
print('finish logging'+'\n')

#开始读第1页-n页
i = 1
while i < 3 :
    #用Get得到的是cookie乱七八糟的，所以为了用beautiful必须把他变成.text
    html = r.text
    #使用bs来获取连接
    soup = BeautifulSoup(html,features='lxml')
    #获取连接后，写入Vlinks
    print('analysing page '+ str(i) + ' links...'+'\n')
    vlinks = soup.find_all('a',{
        'target':'blank',
        'href':re.compile('http://XXX.com/view_video.php\?viewkey=.*?')
    })
    #新建List，获取只含有href的list

    for links in vlinks:
        vlink.append(links['href'])
    i = i + 1
    r=s.get('http://XXX.com/v.php?category=rf&viewtype=basic&page='+str(i))

#获取到的新list,并且去重
vlink = list(set(vlink))

#打开网页，获取到下载地址的links
for link in vlink:
    dllinks.append(downLoadLink(s,link))

# for pintlk in dllinks:
#     print(pintlk)
#
# print('bye')

print('finish analysting...'+'\n')
print('begin downloading...'+'\n')


newDllinks=[]
for links in dllinks:
    newDllinks.append(links['href'])

# for links in newDllinks:
#     print(links)

for link in newDllinks:
    print('downloading')
    name = link[link.index('//mp43') + 7:link.index('.mp4') + 4]
    sys.stdout.write('\rdownloading ' + name + '...\n')
    if os.path.exists('./video/'+name):
        print(name+' already exists. Begin next one.' + '\n')
        continue
    urlretrieve(link, './video/'+name, reporthook=report)
    sys.stdout.write("\rdownload complete, saved as %s" % (name) + '\n\n')
    sys.stdout.flush()


t=time.time()-t
print('Finished. Time Used: '+ str(t) + 'seconds.'+'\n')

print('Total Download #:' + str(len(newDllinks)))
# name=[]

#注释掉测试
# for index in range(len(dllinks)-1):
#     name = dllinks[index][0]['href']
#     name = name[name.index('//mp43') + 7:name.index('.mp4') + 4]
#     sys.stdout.write('\rFetching ' + name + '...\n')
#     urlretrieve(dllinks[index][0]['href'], './video/'+name, reporthook=report)
#     sys.stdout.write("\rDownload complete, saved as %s" % (name) + '\n\n')
#     sys.stdout.flush()
#
# print('done')




#目标下载图片

# r = requests.get(IMAGE_URL, stream=True)    # stream
#
# with open('./img/', 'wb') as f:
#     for chunk in r.iter_content(chunk_size=32):
#         f.write(chunk)



