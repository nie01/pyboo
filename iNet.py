#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
#  相关的文件操作
创建： 2018-1-8 08:51:50
'''

# import os
# import re
# import time
# import sys
# import urllib
#
# import random
# import socket
# import winsound
# import ssl
# import json
# # custom HTTPS opener, banner's oracle 10g server supports SSLv3 only
import urllib.request
import urllib
import socket
import io
import gzip
import chardet

from cnLib import boo
from cnLib import iFile
# print "cnLib"
# ------------------------------------------------------------------
# print __name__

# '''
# # 功能：
# # 时间：
# # 返回： =0失败，=1成功
# # 参数：
# # 实例： re = demo(u'传入参数')
# '''
# def model(IN):
#     return 1  # 返回说明
#     return None  # 返回说明
#     return True  # 返回说明
# ----------------------------------------------------------------------

#---------------------------------------------------------------------------
# 请求头信息
request_heads = {
    'Chrome-win10': {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Upgrade-Insecure-Requests': '1',
        # 'Referer': '',
    },
    'Firefox-win10': {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        # 'Referer': '',
    },
}
class iNet():

    def __init__(self):
        self.request_heads = request_heads['Chrome-win10']  # 请求头
        self.response_info = {'code': 0, 'msg': 'ready'}  # 响应相关信息
        self.response_heads = None  # 响应头
        self.Referer = None  # 请求头
        self.response_data = None  # 响应数据
        self.response_txt = None  # 响应文本数据
    def gzdecode(self, data):
        '''
        # 解压gzip
        :param data:
        :return: 返回解压后的数据 如果 失败则 返回 原数据
        '''
        # print u'F>gzdecode'
        # data2 = gzip.decompress(data)
        # compressedstream = io.StringIO(data)
        # gziper = gzip.GzipFile(fileobj=compressedstream)
        # data2 = gziper.read()  # 读取解压缩后数据
        # return data2
        try:
            return gzip.decompress(data)
        except:
            return data

    # ----------------------------------------------------------------------

    '''
        # 修改/添加 请求请求头
        heads 必须是字典
        返回：修改后的请求头
        注意**
            {'Referer': ''} 表示删除 Referer
            注意 区分大小写
                {'Referer': http://'www.abc.com'}  正确格式
                {'referer': http://'www.abc.com'}  错误格式
    '''
    def setHeads(self, heads):
        if dict!=type(heads):
            return
        self.request_heads = dict(self.request_heads)
        self.request_heads.update(heads)  # 合并请求头
        for key in list(self.request_heads):
            # 清除无效的请求头
            if '' == self.request_heads[key] or None == self.request_heads[key]:
                self.request_heads.pop(key)

        return self.request_heads

    # ----------------------------------------------------------------------

    # 保存原始响应数据
    def saveData(self, path):
        if self.response_data:
            iFile.saveFile(path, data=self.response_data, isAdd=0)

    # ----------------------------------------------------------------------

    # 保存原始响应 文本数据
    def saveTxt(self, path):
        iFile.saveFile(path, data=self.response_txt, isAdd=0)

    # ----------------------------------------------------------------------

    # 下载文本文件
    # 返回文本文件  失败则返回 None
    # charType = utf8,gbk
    def download_txt(self, url, charType):
        if None == self.download_file(url):
            return

        if 'Content-Encoding' in self.response_heads and self.response_heads['Content-Encoding']:
            # print '是gzip'
            self.response_txt = self.gzdecode(self.response_data)  # 解码gzip
        else:
            self.response_txt = self.response_data

        try:
            if '' == charType: #自动判断
                # 判断文本编码
                if 'Content-Type' in self.response_heads:
                    encoding = self.response_heads['Content-Type'].lower() # 获取值并统一转为小写字母
                    if encoding.find('charset=gbk')>-1:
                        self.response_txt = self.response_txt.decode('gb2312')
                    elif encoding.find('charset=utf')>-1:
                        self.response_txt = self.response_txt.decode('utf-8')
            elif 'utf8' == charType:
                self.response_txt = self.response_txt.decode('utf-8')
            elif 'gbk' == charType:
                self.response_txt = self.response_txt.decode('gb2312')
        except:
            pass

        # print(type(self.response_txt))
        return self.response_txt

    # ----------------------------------------------------------------------

    # 下载文件
    # 返回二进制数据  失败则返回FALSE
    def download_file(self, url):
        try:
            self.response_info = {'code': 0, 'msg': 'waiting'}  # 响应相关信息- 等待中
            # url = 'http://www.zmt656568.com'
            # url = 'http://www.nie01.com/6466'
            # if len(url) < 5:
            #     return  # URL异常
            # 发送请求头
            send_headers = self.request_heads
            req = urllib.request.Request(url, headers=send_headers)  # 生成请求信息

            # f = urllib2.urlopen(req, data=None, timeout=60)
            self.response_info = {'code': 2, 'msg': 'loading'}  # 响应相关信息- 下载中
            re = urllib.request.urlopen(req, data=None, timeout=30)
            self.response_heads = re.info()  # 返回的 头部
            self.response_data = re.read()
            # print reHeaders
            self.response_info = {'code': re.code, 'msg': re.msg}  # 响应相关信息- 错误， 如：404
            return self.response_data
        except socket.timeout as e:
            # print(e)
            self.response_info = {'code': 9, 'msg': 'timeout下载超时'}  # 响应相关信息- 下载超时
            boo.show('下载超时！')
        except urllib.request.URLError as e:
            # urllib.error.URLError: <urlopen error [WinError 10054] 远程主机强迫关闭了一个现有的连接。>
            # <urlopen error [WinError 10054] 远程主机强迫关闭了一个现有的连接。>
            print(e)
            if hasattr(e, 'code'):
                pass
                # self.response_info = {'code': e.code, 'msg': e.msg}  # 响应相关信息- 错误， 如：404
                self.response_info = {'code': e.code, 'msg': e.reason}  # 响应相关信息- 错误， 如：404
                errorStr = "下载失败！错误代码：%d ， 错误描述：%s" % (e.code, e.reason)
            elif hasattr(e, 'reason'):
                pass
                # self.response_info = {'code': e.reason.errno, 'msg': e.reason.strerror}  # 响应相关信息- 错误， 如：404
                # errorStr = "下载失败！错误代码：%d ， 错误描述：%s" % (e.reason.errno, e.reason.strerror)
            else:
                self.response_info = {'code': -1, 'msg': e}  # 响应相关信息- 错误， 如：404
                errorStr = "错误描述：%s" % (e)
            # boo.show(errorStr)
        except Exception as e:
            print(e)
            errorStr = ''
            self.response_info = {'code': 7, 'msg': '下载失败 未知错误->1！！:'}  # 响应相关信息- 错误， 如：404
            # print(type(e))
            if ValueError == type(e):
                self.response_info = {'code': 4, 'msg': 'ValueError,参数错误'}  # 响应相关信息- 错误， 如：404
                errorStr = 'ValueError,参数错误'
            # errorStr = "下载失败！\n    错误代码：%d ，\n    错误描述：%s\n" % (e.reason.errno, e.reason.strerror)
            # boo.show(errorStr)
            # print('下载失败 未知错误1！！:')
        except:
            self.response_info = {'code': 6, 'msg': '下载失败 未知错误！！:'}  # 响应相关信息- 错误， 如：404
            print('下载失败 未知错误！！:')
        return
# ------------------------------------------------------------------

# # 返回二进制数据  失败则返回FALSE
# def download_file(URL,fromURL=False):
#
#     if URL.find('http')!=0:
#         boo.show('download_file,URL地址异常')
#         return False
#
#     # print u'F>download_now'
#     req = urllib2.Request(URL)
#     req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0')
#     req.add_header('Accept-Encoding', 'gzip, deflate')
#     req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
#     req.add_header('Accept-Language', 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3')
#     if fromURL!=False:
#         req.add_header('Referer', fromURL)
#
#     req.add_header('Connection', 'keep-alive')
#
#     # allLen=0
#     try:
#         f = urllib2.urlopen(req, data=None, timeout=60)
#
#         reHeaders = f.info() # 返回的 头部
#         reData = f.read()
#         # print reHeaders
#
#         if ('Content-Encoding' in reHeaders and reHeaders['Content-Encoding']) or \
#                 ('content-encoding' in reHeaders and reHeaders['content-encoding']):
#             # print '是gzip'
#             reData = gzdecode(reData)  # 解码gzip
#
#         # print reData
#         return reData
#     except urllib2.URLError, e:
#         # boo.show('download_file下载失败1！！错误类型:')
#         # print e.reason #错误类型
#         return False
#     except:
#         boo.show('download_file下载失败2 超时！！')
#         return False
#         # return ''

# ------------------------------------------------------------------

# # 下载文件
# # 返回二进制数据  失败则返回FALSE
# def download_txt(URL,fromURL=False):
#     # print u'F>download_now'
#     req = urllib2.Request(URL)
#     req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0')
#     req.add_header('Accept-Encoding', 'gzip, deflate')
#     req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
#     req.add_header('Accept-Language', 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3')
#     # req.add_header('Referer', 'http://www.11vvt.com/')
#     if fromURL!=False:
#         req.add_header('Referer', fromURL)
#
#     req.add_header('Connection', 'keep-alive')
#
#     # allLen=0
#     try:
#         f = urllib2.urlopen(req, data=None, timeout=60)
#
#         reHeaders = f.info() # 返回的 头部
#         reData = f.read()
#         # print reHeaders
#
#         if ('Content-Encoding' in reHeaders and reHeaders['Content-Encoding']) or \
#                 ('content-encoding' in reHeaders and reHeaders['content-encoding']):
#             # print '是gzip'
#             reData = gzdecode(reData)  # 解码gzip
#
#         # print reData
#         return reData
#     except urllib2.URLError, e:
#         boo.show('download_txt下载失败1！！错误类型:')
#         print e.reason #错误类型
#         return False
#     except:
#         boo.show('download_txt下载失败2 超时！！:')
#         return False
#         # return ''

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

# ------------------------------------------------------------------

# ------------------------------------------------------------------
