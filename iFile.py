#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
#  相关的文件操作
创建： 2018-1-8 08:51:50
'''

import os
import re
import time
import datetime
import sys
import urllib
# import urllib2
import random
import socket
import winsound
import win32file
import json
import struct
# custom HTTPS opener, banner's oracle 10g server supports SSLv3 only
# import httplib
import io
import gzip
import hashlib
import math
import binascii

from cnLib import iPath

from cnLib import boo
# import traceback
from struct import *


# print "cnLib"
# ------------------------------------------------------------------
# print __name__

# 当前函数名
# fn_name = (lambda: sys._getframe(1).f_code.co_name)()
# print fn_name

'''
前缀说明：
FP //Function parameter, parameter [pəˈræmɪtɚ] n.  参数
IN //使用 在函数参数名称前 如md5Date(inDate)  目的： 特别提示
OUT //使用 在函数参数名称前 如getDate(&outDate)  目的： 特别提示 用于获取 返回的数据

'''

# ---------------------------------------------------------------------------
'''
# 功能：
# 时间：
# 返回： =0失败，=1成功
# 参数：
# 实例： re = demo(u'传入参数')
# 说明：IN特别说明传入,FP,OUT
'''
def model(IN,FP,OUT):
    return 1  # 返回说明
    # return None  # 返回说明
    # return True  # 返回说明
# ----------------------------------------------------------------------

'''
# 功能：文件部分内容的md5值 
# 目的：  便于初步快速对比可能相同的文件内容，因为只是截取文件部分内容所有碰撞的概率很大

# import binascii  #  二进制 转 16进制
# # print(binascii.b2a_hex(byte))
'''
def getFile_partMD5_1(filePath):
    try:
        quan = 10 # 截取的块数
        block = 1024*10  # 块大小
        dataLen = block*quan
        if not os.path.exists(filePath):
            return ''  # 无效路径

        if not os.path.isfile(filePath):
            return ''  # 不是文件路径

        fileSize = os.path.getsize(filePath)  # 文件大小
        # print(fileSize)
        h = hex(fileSize)[2:]
        data = h.encode("utf-8")

        # data = bytes('', "ascii")  # 定义一个空字节变量
        # step = math.floor(fileSize/dataLen)
        step = math.floor(fileSize/quan)
        # print(step)
        fh = open(filePath, "rb+")  # 文件句柄

        if fileSize < dataLen:
            data = fh.read()  # 读取一个字节
            # print('一口气！')
        else:
            for i in range(0, quan):
                fh.seek(step*i)  # 指针
                d = fh.read(block)  # 读取
                if not data:
                    break
                data += d

        # print(binascii.b2a_hex(data))  以十六进制方式显示二进制
        return hashlib.md5(data).hexdigest()
    except:
        return ''  # 异常

# ----------------------------------------------------------------------

# 读取文本
def getFileMD5(filePath):
    if not os.path.exists(filePath):
        return ''  # 无效路径

    if not os.path.isfile(filePath):
        return ''  # 不是文件路径

    fh = open(filePath, "rb+")  # 文件句柄
    md5_obj = hashlib.md5()

    while True:
        data = fh.read(1024*512)  # 读取一个字节
        if not data:
            break
        md5_obj.update(data)

    return md5_obj.hexdigest()
# ----------------------------------------------------------------------

# 读取文本
def readFile(path):
    # print u'F>readTxtFile'
    try:
        f = open(path, "rb")
        data = f.read()
        f.close() #关闭文件
        return data
    except Exception as e:
        boo.logError()
        # boo.show(path + '位置错误@文件无法写入')
        return -5


# ----------------------------------------------------------------------
'''
#
# 功能： 创建空文件，指定大小 默认 isCover=0
# 时间： 2018-2-17 21:57:57
# 返回：
     1 # 文件保存成功
    -1 # 当前路径是 目录无法保存文件
    -2 # 创建父级目录 失败
    -3 # 父级目录路径是文件 无法保存文件
    -4 # 文件已经存在 但不允许覆盖
    -5 # 文件无法写入
# 参数：
    path 路径
    INsize 空文件 的大小
    isCover =1 如果文件已经存在 则覆盖，=0 如果如果文件已经存在则跳过 返回 -4
# 实例：
'''
def createEmptyFile(path,INsize,isCover = 0):
    pathType = iPath.pathType(path)
    if pathType == 2:
        return -1  # 当前路径是 目录无法保存文件

    if pathType == 1 and isCover == 0:
        return -4  # 1是文件路径 文件已经存在 但不允许覆盖

    parentDir = iPath.parentDirPath(path)
    if parentDir:
        # 有父级目录
        pathDirType = iPath.pathType(parentDir)
        if pathDirType == 0:
            # 父级目录 不存在 则创建
            re = iPath.makeDir(parentDir)  # 创建父级目录
            if re != 2:
                return -2  # 创建父级目录 失败
        elif pathDirType == 1:
            return -3  # 父级目录路径是文件 无法保存文件

    try:
        # print u'F>saveFile'
        b = pack("i", 0)
        l = len(b)
        # print l
        # size.write(b)
        f = open(path, "wb")
        f.seek(INsize - l)
        f.write(b)
        f.close()  # 关闭文件
        return 1 #文件保存成功
    except Exception as e:
        boo.logError()
        # boo.show(path + '位置错误@文件无法写入')
        return -5

# ----------------------------------------------------------------------
'''
#
# 功能： 保存 二进制文件
# 时间：
# 返回：
    True #文件保存成功
    -1 #当前路径是 目录无法保存文件
    -2 #创建父级目录 失败
    -3 #父级目录路径是文件 无法保存文件
    -5 #文件无法写入
# 参数：
    path
    data 如果 data是unicode字符串则会自动转为UTF-8保存
    isAdd =1追加到文件尾部
# 实例：
'''
def saveFile(path,data,isAdd):
    pathType = iPath.pathType(path)
    if pathType == 2:
        return -1 #当前路径是 目录无法保存文件

    parentDir = iPath.parentDirPath(path)
    if parentDir:
        # 有父级目录
        pathDirType = iPath.pathType(parentDir)
        if pathDirType == 0:
            # 父级目录 不存在 则创建
            re = iPath.makeDir(parentDir) #创建父级目录
            if re != 2:
                return -2 #创建父级目录 失败
        elif pathDirType == 1:
            return -3 #父级目录路径是文件 无法保存文件

    # print u'F>saveFile'
    # try:
    if 1:
        f = 0
        if isAdd==True:
            f = open(path, u"ab+")
        else:
            f = open(path, u"wb+")

        # print type(data)
        # data = struct.pack('unicode', data)
        # print type(data)

        dataType = type(data)
        # print(dataType)
        if bytes != dataType:
            if str == dataType:
                data = data.encode('UTF-8')
            # if unicode == dataType:
            #     data = data.encode('UTF-8')

        f.write(data)

        f.close() #关闭文件
        return True #文件保存成功
    # except Exception as e:
    #     print(e)
    #     boo.logError('ee.log')
    #     # boo.show(path + '位置错误@文件无法写入')
    #     return -5


# ----------------------------------------------------------------------
'''
#
# 功能： 指定位置 保存 二进制文件
# 时间：
# 返回：
    True # 文件保存成功
    -1 #当前路径是 目录无法保存文件
    -2 #创建父级目录 失败
    -3 #父级目录路径是文件 无法保存文件
    -5 #文件无法写入
# 参数：
    path
    data 如果 data是unicode字符串则会自动转为UTF-8保存
    start = 写入数据起点
# 实例：
'''
def saveFile_seek(path,data,start):
    pathType = iPath.pathType(path)
    if pathType == 2:
        return -1 #当前路径是 目录无法保存文件

    #
    # if pathType == 1 and isCover == 0:
    #     return -4  # 1是文件路径 文件已经存在 但不允许覆盖

    parentDir = iPath.parentDirPath(path)
    if parentDir:
        # 有父级目录
        pathDirType = iPath.pathType(parentDir)
        if pathDirType == 0:
            # 父级目录 不存在 则创建
            re = iPath.makeDir(parentDir) #创建父级目录
            if re != 2:
                return -2 #创建父级目录 失败
        elif pathDirType == 1:
            return -3 #父级目录路径是文件 无法保存文件

    # print u'F>saveFile'
    try:
        openType = 'rb+'
        if pathType == 0:
            openType = 'wb'  # 文件不存在则创建

        f = open(path, openType)
        f.seek(start)
        # print type(data)
        # data = struct.pack('unicode', data)
        # print type(data)

        tellA = f.tell()  # 保存前 文件指针位置。
        dataType = type(data)
        # print dataType
        if unicode == dataType:
            data = data.encode('UTF-8')

        f.write(data)
        tellZ = f.tell()  # 保存后 文件指针位置。
        f.close() #关闭文件
        dataLen = len(data)

        # 验证数据保持是否完整
        if dataLen == (tellZ - tellA):
            return True #文件保存成功
        else:
            return -6  # 数据未保存完整

    except Exception as e:
        boo.logError()
        # boo.show(path + '位置错误@文件无法写入')
        return -5


# ----------------------------------------------------------------------

'''
#
# 功能： 截取文件，使文件的大小为 size
# 时间： 2018-2-17 17:05:38
# 返回：
    True # 文件保存成功
    -1 #当前路径是 目录无法保存文件
    -2 #创建父级目录 失败
    -3 #父级目录路径是文件 无法保存文件
    -5 #文件无法写入
# 参数：
    path
    size = 文件的大小
# 实例：
'''
def resizeFile(path,size):
    pathType = iPath.pathType(path)
    if pathType == 2:
        return -1 #当前路径是 目录无法保存文件

    parentDir = iPath.parentDirPath(path)
    if parentDir:
        # 有父级目录
        pathDirType = iPath.pathType(parentDir)
        if pathDirType == 0:
            # 父级目录 不存在 则创建
            re = iPath.makeDir(parentDir) #创建父级目录
            if re != 2:
                return -2 #创建父级目录 失败
        elif pathDirType == 1:
            return -3 #父级目录路径是文件 无法保存文件

    # print u'F>saveFile'
    try:
        openType = 'rb+'
        if pathType == 0:
            openType = 'wb'  # 文件不存在则创建

        f = open(path, openType)
        f.truncate(size)  # 截取文件，使文件的大小为size。
        f.close() #关闭文件
        return True  # 文件保存成功
    except Exception as e:
        boo.logError()
        # boo.show(path + '位置错误@文件无法写入')
        return -5


# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
'''
#
# 功能： 保存文本
# 时间：
# 返回：
    True #文件保存成功
    -1 #当前路径是 目录无法保存文件
    -2 #创建父级目录 失败
    -3 #父级目录路径是文件 无法保存文件
    -5 #文件无法写入
# 参数：
    path
    txt 如果 txt是unicode字符串则会自动转为UTF-8保存
    isAdd =1追加到文件尾部
# 实例：
'''
def saveTxtFile(path,txt,isAdd):
    dataType = type(txt)
    # print dataType
    try:
        if bytes == dataType:
            txt = txt.encode('UTF-8')
            # dataType = type(txt)
            # print dataType
    except:
        print('saveTxtFile-error')

    return saveFile(path, txt, isAdd)

# ----------------------------------------------------------------------

# 读取文本
def readTxtFile(path):
    # print u'F>readTxtFile'
    try:
        f = open(path, "r+")
        txt = f.read()
        f.close()  # 关闭文件
        return txt
        f.close() #关闭文件
    except Exception as e:
        boo.logError()
        # boo.show(path + '位置错误@文件无法写入')
        return -5


# ----------------------------------------------------------------------

# 获取扩展名
def getName2(path):
  return os.path.splitext(path)[1]

#---------------------------------------------------------------------------

# 解压gzip
# 返回解压后的数据 如果 失败则 返回 原数据
def gzdecode(data):
    try:
        # print u'F>gzdecode'
        compressedstream = io.StringIO(data)
        gziper = gzip.GzipFile(fileobj=compressedstream)
        data2 = gziper.read()  # 读取解压缩后数据
        return data2
    except:
        return data
# ----------------------------------------------------------------------

# 下载now_ts文件
# 返回ts二进制数据  失败则返回FALSE
def download_file(URL):
    # print u'F>download_now'
    req = urllib.Request(URL)
    req.add_header('User-Agent', 'Mozilla/5.0 (Linux; Android 7.0; PRA-AL00X Build/HONORPRA-AL00X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/56.0.2924.87 Mobile Safari/537.36')
    # req.add_header('allow-cross-domain-redirect', 'false')
    # req.add_header('Connection', 'Keep-Alive')
    # req.add_header('Accept-Encoding', 'gzip')
    # allLen=0
    try:

        # print 'urllib2.urlopen前'
        res = urllib.urlopen(req, data=None, timeout=60)
        # print 'urllib2.urlopen后'
        # print res.read()
        # print len(res)
        return res.read()
        # data = res.read()
    except urllib.URLError as e:
        print('下载失败1！！错误类型:')
        print(e.reason)  # 错误类型
    except:
        print( '下载失败 超时！！:')
        return False
        # return ''

# ------------------------------------------------------------------

'''把时间戳转化为时间: 1479264792 to 2016-11-16 10:53:12'''
def TimeStampToTime(timestamp):
    try:
        timeStruct = time.localtime(timestamp)
        return time.strftime('%Y-%m-%d %H:%M:%S', timeStruct)
        pass
    except:
        return
# ---------------------------------------------------------------------------
'''
# 功能： 获取文件属性
# 时间：
# 返回： =-1无效的路径，=16是目录路径....具体：
    FILE_ATTRIBUTE_READONLY = 1 (0x1)
    FILE_ATTRIBUTE_HIDDEN = 2 (0x2)
    FILE_ATTRIBUTE_SYSTEM = 4 (0x4)
    FILE_ATTRIBUTE_DIRECTORY = 16 (0x10)
    FILE_ATTRIBUTE_ARCHIVE = 32 (0x20)
    FILE_ATTRIBUTE_NORMAL = 128 (0x80)
    FILE_ATTRIBUTE_TEMPORARY = 256 (0x100)
    FILE_ATTRIBUTE_SPARSE_FILE = 512 (0x200)
    FILE_ATTRIBUTE_REPARSE_POINT = 1024 (0x400)
    FILE_ATTRIBUTE_COMPRESSED = 2048 (0x800)
    FILE_ATTRIBUTE_OFFLINE = 4096 (0x1000)
    FILE_ATTRIBUTE_NOT_CONTENT_INDEXED = 8192 (0x2000)
    FILE_ATTRIBUTE_ENCRYPTED = 16384 (0x4000)
# 参数：
# 实例：
'''
def get_FileAttributes(path):
    return win32file.GetFileAttributesW(path)
# ---------------------------------------------------------------------------

'''获取文件的大小,结果保留两位小数，单位为MB'''
def get_FileSize(filePath):
    try:
        if type(filePath) == str:
            filePath = unicode(filePath, 'utf8')
        fsize = os.path.getsize(filePath)
        # fsize = fsize / float(1024 * 1024)
        # return round(fsize, 2)
        return fsize
        pass
    except:
        return
# ---------------------------------------------------------------------------

'''获取文件的访问时间'''
def get_FileAccessTime(filePath):
    try:
        if type(filePath) == str:
            filePath = unicode(filePath, 'utf8')
        t = os.path.getatime(filePath)
        return TimeStampToTime(t)
        pass
    except:
        return
# ---------------------------------------------------------------------------

'''获取文件的创建时间'''
def get_FileCreateTime(filePath):
    try:
        if type(filePath) == str:
            filePath = unicode(filePath, 'utf8')
        t = os.path.getctime(filePath)
        return TimeStampToTime(t)
        pass
    except:
        return
# ---------------------------------------------------------------------------

'''获取文件的修改时间'''
def get_FileModifyTime(filePath):
    try:
        if type(filePath) == str:
            filePath = unicode(filePath, 'utf8')
        t = os.path.getmtime(filePath)
        return TimeStampToTime(t)
        pass
    except:
        return


# ------------------------------------------------------------------
# def  fssize(dirpath):
#
#     size = 0
#             if os.path.exists(dirpath):
#                 if os.path.isdir(dirpath):
#                     for root, dirs, files in os.walk(dirpath):
#                         for name in files:
#                             try:
#                                 size += getsize(join(root, name))
#                             except:
#                                 continue
#                         #size += sum([getsize(join(root, name)) for name in files])
#                 elif os.path.isfile(dirpath):
#                     size = os.path.getsize(dirpath)
#                 else:
#                     continue
#     return size
# ------------------------------------------------------------------

# ------------------------------------------------------------------

# ------------------------------------------------------------------

# ------------------------------------------------------------------

# ------------------------------------------------------------------

# ------------------------------------------------------------------

# ------------------------------------------------------------------

# ------------------------------------------------------------------

# ------------------------------------------------------------------

# ------------------------------------------------------------------

# ------------------------------------------------------------------

# ------------------------------------------------------------------
