#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
#  相关的文件操作
创建： 2018-1-8 08:51:50
'''

import os
import re
import win32file
# import time
# import sys
# import urllib
# import random
# import socket
# import winsound
# import ssl
# import json
# # custom HTTPS opener, banner's oracle 10g server supports SSLv3 only
# import ssl, socket
# import io, gzip



# ---------------------------------------------------------------------------
'''
# 功能：
# 时间：
# 返回： =0失败，=1成功
# 参数：
# 实例： re = demo(u'传入参数')
'''
def model(IN):
    return 1  # 返回说明
    return None  # 返回说明
    return True  # 返回说明


# ---------------------------------------------------------------------------
'''
# 功能： 获取文件类型
# 时间：
# 返回： =0无效的路径，=1是文件路径，=2是目录路径
# 参数：
# 实例：
'''
def pathType(path):
    if os.path.isfile(path):
        return 1  # 1是文件路径

    if os.path.isdir(path):
        return 2  # 2是目录路径

    return 0  # 0无效的路径


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
    if type(path) == str:
        path = unicode(path, 'utf8')

    return win32file.GetFileAttributesW(path)

# ---------------------------------------------------------------------------
# 功能： 获取父级目录
# 时间：
# 返回： 父级路径
# 实例：
def parentDirPath(path):
    parentDir = os.path.split(path)[0]  # 获得目录名
    return parentDir  # 父级目录

# ---------------------------------------------------------------------------

# 获取文件名 ** 不含扩展名
def name(path):
    return os.path.splitext(path)[0]  # 扩展名

# 获取扩展名
def name2(path):
    return os.path.splitext(path)[1]  # 扩展名

# 获取完整的 文件名/目录名  （文件名+扩展名）
def fullName(path):
    return os.path.basename(path)
    # return os.path.split(path)[1]

# ---------------------------------------------------------------------------
# 功能：删除 文件名/目录名 不能包含的字符
# 时间：
# 返回： 符合要求的 文件名/目录名
# 实例：
def clearName_illegalStr(name):
    okName = re.sub(r'[\\/:\*\?"<>\|]', "", name)
    return okName  # 返回说明

# 功能：删除 路径中 不能包含的字符
# 时间：
# 返回： =符合要求的 路径
# 实例：
def clearPath_illegalStr(path):
    okPath = re.sub(r'[:\*\?"<>\|]', "", path)
    return okPath  # 返回说明


# ------------------------------------------------------------------
# 功能： 一次创建多级目录（文件夹）
# 时间：
# 返回： =0创建失败，=1 当前路径是文件路径，=2创建成功/目录已经存在
# 实例： re = makeDir(u'a/b/c')
def makeDir(dirPath):
    if os.path.isfile(dirPath):
        return 1  #当前路径是文件路径

    if os.path.isdir(dirPath):
        return 2  #目录已经存在

    # print os.path.exists(dirPath),'=',dirPath
    if not os.path.exists(dirPath):  # 判断目录是否存在
        try:
            os.makedirs(dirPath)  # 创建目录
        except OSError as exc:
            # print exc.args
            return 0
        except :
            return 0

    # 判断创建 结果

    if os.path.isfile(dirPath):
        return 1  # 当前路径是文件路径

    if os.path.isdir(dirPath):
        return 2  # 创建成功

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
