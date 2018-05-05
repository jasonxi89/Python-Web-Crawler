#过验证码
#MAC使用命令brew install tesseract安装GOOGLE的库文件
from PIL import Image
# import tesseract
import pytesseract
from PIL import ImageOps
import time
import requests
print(time.time())

# def binarizing(img,threshold):
#     """传入image对象进行灰度、二值处理"""
#     img = img.convert("L") # 转灰度
#     pixdata = img.load()
#     w, h = img.size
#     # 遍历所有像素，大于阈值的为黑色
#     for y in range(h):
#         for x in range(w):
#             if pixdata[x, y] < threshold:
#                 pixdata[x, y] = 0
#             else:
#                 pixdata[x, y] = 255
#     return img
#
# def depoint(img):
#     """传入二值化后的图片进行降噪"""
#     pixdata = img.load()
#     w,h = img.size
#     for y in range(1,h-1):
#         for x in range(1,w-1):
#             count = 0
#             if pixdata[x,y-1] > 245:#上
#                 count = count + 1
#             if pixdata[x,y+1] > 245:#下
#                 count = count + 1
#             if pixdata[x-1,y] > 245:#左
#                 count = count + 1
#             if pixdata[x+1,y] > 245:#右
#                 count = count + 1
#             if pixdata[x-1,y-1] > 245:#左上
#                 count = count + 1
#             if pixdata[x-1,y+1] > 245:#左下
#                 count = count + 1
#             if pixdata[x+1,y-1] > 245:#右上
#                 count = count + 1
#             if pixdata[x+1,y+1] > 245:#右下
#                 count = count + 1
#             if count > 4:
#                 pixdata[x,y] = 255
#     return img
#
#
# def get_bin_table(threshold=140):
#     """
#     获取灰度转二值的映射table
#     :param threshold:
#     :return:
#     """
#     table = []
#     for i in range(256):
#         if i < threshold:
#             table.append(0)
#         else:
#             table.append(1)
#
#     return table
#
# def clear_border(img,img_name):
#   filename = './out_img/' + img_name.split('.')[0] + '-clearBorder.jpg'
#   h, w = img.shape[:2]
#   for y in range(0, w):
#     for x in range(0, h):
#       if y  w - 2:
#         img[x, y] = 255
#       if x  h -2:
#         img[x, y] = 255
#   cv2.imwrite(filename,img)
#   return img



# img_path = 'valcode.png'
#
# im=Image.open(img_path)
#
# imgry=im.convert('L')
#
# imgry=ImageOps.invert(im)
#
# imgry=imgry.convert('1')
#
# imgry.show()

# im = im.convert('L')
# im = ImageOps.invert(im)
# im = im.convert('1')



# image = Image.open(img_path)
# imgry = image.convert('L')  # 转化为灰度图
#
# table = get_bin_table()
# out = imgry.point(table, '1')
# print(out)
# p1=depoint(p1)


#
# print(pytesseract.Output.BYTES(p1))
# print(pytesseract.image_to_data(p1))
# print(pytesseract.image_to_boxes(p1))
# print(pytesseract.image_to_data(imgry))

codeUrl = 'http://91porn.com/captcha.php'
valcode = requests.get('http://91porn.com/captcha.php')

f = open('valcode1.png', 'wb')
# 将response的二进制内容写入到文件中
f.write(valcode.content)
# 关闭文件流对象
f.close()

#打开图片
img = Image.open('valcode1.png')
img.show()