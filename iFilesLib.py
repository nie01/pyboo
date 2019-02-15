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
import urllib2
import random
import socket
import winsound
import ssl
import json
import struct
# custom HTTPS opener, banner's oracle 10g server supports SSLv3 only
import httplib, ssl, socket
import StringIO, gzip
from cnLib import iPath
from cnLib import iFile

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
    return None  # 返回说明
    return True  # 返回说明
# ----------------------------------------------------------------------
'''
文件结构：
    00 00 fileslib  # 定长 标识符 2 + 8 字节
    00 00 # 定长 版本 2 字节
    [起点8，长度4] 备注
    [起点8，长度4] 索引数据 索引列表可以看成二维数组 [ [起点8，长度4], [[起点8，长度4]] ]  ，(8+4)* n
    
    8+4=12    *1万 = 
    
    
32=16B
MD5: 76C781F4CA1EF54F7BDD66B8A3345E28
40=20B
SHA1: 2F1CFA7FA65A385DEEDADADCEC7AC22E408E5A8E

'''
# ------------------------------------------------------------------

'''
# 功能： 文件库类
# 时间： 2018-2-17 21:30:44
# 返回： 
# 参数：
# 实例：
    # fl = iFilesLib.CLfilesLib()
    # fl.setPath('ff.fsl')
    # print fl.createLib()

# 说明：
'''
class CLfilesLib:
    def __init__(self, path=None):
        self.setPath(path)
        class_name = self.__class__.__name__
        print '构造函数=CLfilesLib' +class_name

    '''
    # 功能： 设置数据文件库路径
    # 时间：
    # 返回： =0失败，=1成功
    # 参数：
    # 实例： 
    # 说明：
    '''
    def setPath(self, path):
        if path == None:
            return 0  # 失败！ 传入参数异常

        self.path = path
        # return 1  # 返回说明
        # return None  # 返回说明
        return 1  # 返回说明

    # ----------------------------------------------------------------------

    '''
    # 功能： 创建数据库
    # 时间： 2018-2-17 21:58:10
    # 返回：
         1 # 文件保存成功
        -1 # 当前路径是 目录无法保存文件
        -2 # 创建父级目录 失败
        -3 # 父级目录路径是文件 无法保存文件
        -4 # 文件已经存在 但不允许覆盖
        -5 # 文件无法写入
    # 参数：
        path 路径
        cacheSize 缓存文件的大小
    # 参数： 
    # 实例： 
    # 说明： 
    '''
    def createLib(self, cacheSize=1024):
        if self.path == None:
            return 0  # 失败！ 传入参数异常

        re = iFile.createEmptyFile(self.path, cacheSize, 1)  # 创建空文件
        if re != 1:
            return re

        '''
        文件结构：
            00 00 fileslib  # 定长 标识符 2 + 8 字节
            00 00 # 定长 版本 2 字节
            [起点8，长度4] 备注
            [起点8，长度4] 索引数据 索引列表可以看成二维数组 [ [起点8，长度4], [[起点8，长度4]] ]  ，(8+4)* n
        '''
        iFile.saveFile_seek(self.path, '\x00\x00fileslib', 0)  # 00 00 fileslib  # 定长 标识符 2 + 8 字节
        iFile.saveFile_seek(self.path, '\x01\x00', 2+8)  # 00 00 # 定长 版本 2 字节
        b = pack("i", 12345, 67.89, 15)
        iFile.saveFile_seek(self.path, '\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x01', 10+8+4)  # [起点8，长度4] 备注位置
        iFile.saveFile_seek(self.path, '\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x02', 22+8+4)  # [起点8，长度4] 索引数据位置

        # return 1  # 返回说明
        # return None  # 返回说明
        return 1  # 返回说明

    # ----------------------------------------------------------------------


    def __del__(self):
        class_name = self.__class__.__name__
        print '析构函数=' + class_name



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
