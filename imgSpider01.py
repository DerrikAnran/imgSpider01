#Filename:imgSpider01.py
#-*- coding:utf-8 -*-

'''
imgSpider01.py
------------

这是一个用来爬取贴吧中的图片至本地的python爬虫，需要你手动输入网址哦
作者：曾安然
版本：V0.1
制作时间：2017年6月6日

------------

'''
import re
import urllib


def getHtml(url):
    
    #提取网页源代码
    
    page = urllib.urlopen(url)
    html = page.read()
    return html


def downloadImg(html):

    #利用正则表达式提取出html中的图片位置

    reg = r'src="(http://.*?\.jpg)"'
    imgre = re.compile(reg)
    imgList = re.findall(imgre, html)
    i = 0
    for imgUrl in imgList:
        urllib.urlretrieve(imgUrl,r'C:\Users\apple\Documents\pyspiders\img\%s.jpg' %i)
        i += 1


if __name__ == '__main__':  #输入要爬取图片的贴吧帖子
    url = raw_input("请输入百度贴吧帖子地址：")
    html = getHtml(url)
    downloadImg(html)
