#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
# boo 是basic or other的缩写 意思是： 基础 或 其他未分类
创建： 2018-1-8 08:51:50
'''
import traceback  # 获取错误信息
import sys
import os
import re
import time
import datetime
import urllib
import random
import socket
import winsound
import ssl
import json
# custom HTTPS opener, banner's oracle 10g server supports SSLv3 only
import socket
import io, gzip
import hashlib
import sqlite3
import threading

sys.path.append("..") # 跳到上级目录下面
# sys.path的作用是：当使用import语句导入模块时，解释器会搜索当前模块所在目录以及sys.path指定的路径去找需要import的模块
from cnLib import boo

# print "cnLib"
# os.system('pause') #按任意键继续。

# while 1:
#    pass

# print __name__


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
# ------------------------------------------------------------------


'''
实例：
# sqlite3数据库操作
class db_sqlite3:

rt = boo.runtime()
dbPath = "D:/tempD/img.db"
sql = "INSERT INTO img (`name2`,`url`,`md5`,`size` ) VALUES (?,'u',?,4);\n"

db = iDatabase.db_sqlite3("D:/tempD/img.db")
db.open()
db.runSQL_noReturn('DELETE FROM img WHERE size=4 ;')
db.fast_ready()
rt.start()
# ----------------------------------------------------------
one = {}
i=1
nCount = 100
for i in range(0,nCount):
    one['txt'] = "要计算的has值%d" % (i)
    one['md5'] = md5(one['txt'])
    one['sql'] = ''
    db.fast_into("INSERT INTO img (`name2`,`url`,`md5`,`size` ) VALUES (?, '', ?, 4 )", (i, one['md5']))
# ----------------------------------------------------------
db.fast_end()

rt.end()
# print rt.getRuntime()
su = -1
if rt.getRuntime()> 0:
    su = nCount/rt.getRuntime()

txt = "【共%d秒，循环%d次】速度= %f循环/秒"%(rt.getRuntime(), nCount, su)
print(txt)

print('结束')
'''
# sqlite3数据库操作
class db_sqlite3:
    __isDebug = False
    __dataPath = None
    __conn = None
    __c = None
    __fast_count_i = 0
    __fast_count_max = 10000  # 用于控制长 执行SQL语句多少次 保存1次 数据到硬盘并重启快速模式

    # ------------------------------------------------------------------
    # 构造函数
    def __init__(self, path=None):
        # print "A"
        if path:
            self.setPath(path)

    # ------------------------------------------------------------------
    # 析构函数
    def __del__(self):
        # print "Z"
        self.close()

    # ------------------------------------------------------------------
    # 设置路径
    def isDebug(self, TF):
        self.__isDebug = TF

    # ------------------------------------------------------------------
    # 设置路径
    def setPath(self, path):
        self.__dataPath = path

    # ------------------------------------------------------------------
    # 打开
    def open(self):
        try:
            self.__conn = sqlite3.connect(self.__dataPath)
            self.__conn.text_factory = str  ## !!!
            self.__c = self.__conn.cursor()
        except:
            if self.__isDebug:
                strArr = []
                strArr.append("\033[1;31m")
                strArr.append("打开-发生错误!\n")
                strArr.append("被调用的上一层函数：%s\n"%(sys._getframe().f_back.f_code.co_name)) # 获取调用函数名
                strArr.append("当前位置：%s.%s\n"%(self.__class__,sys._getframe().f_code.co_name))
                strArr.append("详细错误信息：\n【\n%s】\n"%(traceback.format_exc()))
                strArr.append(" \033[0m!")
                boo.show(''.join(strArr))


    # ------------------------------------------------------------------
    # 关闭
    def close(self):
        try:
            self.__conn.commit()
            self.__conn.close()
        except:
            return
            # if self.__isDebug:
            #     showStr = "关闭-发生错误!\n"
            #     showStr += "当前位置：%s.%s\n"%(self.__class__,sys._getframe().f_code.co_name)
            #     errorInfo = traceback.format_exc()
            #     showStr += "详细错误信息：\n【\n"+errorInfo+"】\n"
            #     boo.show(showStr)

    # ------------------------------------------------------------------
    '''
    作用：
        用于控制长 执行SQL语句多少次 保存1次 数据到硬盘并重启快速模式 
    参数：
        maxNum # 默认 = 1000  用于控制长 执行SQL语句多少次 保存1次 数据到硬盘并重启快速模式 
    '''
    def fast_count_max(self,maxNum):
        if maxNum > 0:
            self.__fast_count_max = maxNum

    # ------------------------------------------------------------------
    '''
    作用：
        快速操作 - -准备/初始化
    参数：
        maxNum # 默认 = 1000  用于控制长 执行SQL语句多少次 保存1次 数据到硬盘并重启快速模式 
    '''
    def fast_ready(self, maxNum = 0):
        # boo.show('fast_ready')
        try:
            if maxNum > 0:
                self.__fast_count_max = maxNum

            self.__c.execute("begin;")
        except:
            if self.__isDebug:
                funcName = sys._getframe().f_back.f_code.co_name  # 获取调用函数名
                # lineNumber = sys._getframe().f_back.f_lineno  # 获取行号
                # from_funcation = sys._getframe().f_code.co_name  # 获取当前函数名
                showStr = "快速操作 - -准备/初始化-发生错误!\n"
                showStr += "被调用的上一层函数：" + funcName + "\n"
                showStr += "数据库：" + self.__dataPath + "\n"
                showStr += "当前位置：%s.%s\n"%(self.__class__,sys._getframe().f_code.co_name)
                errorInfo = traceback.format_exc()
                showStr += "详细错误信息：\n【\n"+errorInfo+"】\n"
                boo.show(showStr)

    # ------------------------------------------------------------------
    # 快速操作 - -重新-准备/初始化
    def fast_re_ready(self):
        # showStr = "被调用的上一层函数：" + sys._getframe().f_back.f_code.co_name + "\n"
        # boo.show('快速操作 - -重新-准备/初始化_fast_re_ready_' + showStr)
        try:
            self.__conn.commit()
            self.__c.execute("begin;")
        except:
            if self.__isDebug:
                showStr = "快速操作 - -重新-准备/初始化-发生错误!\n"
                showStr += "当前位置：%s.%s\n"%(self.__class__,sys._getframe().f_code.co_name)
                errorInfo = traceback.format_exc()
                showStr += "详细错误信息：\n【\n"+errorInfo+"】\n"
                boo.show(showStr)

    # ------------------------------------------------------------------
    # 快速操作 - - 执行中
    # 返回： 操作后 自动编号的ID
    def fast_into(self, sql, paramObj):
        # boo.show("【%d / %d 数据库：%s" % (self.__fast_count_i, self.__fast_count_max, self.__dataPath))
        # c.execute("INSERT INTO img (`name2`,`url`,`md5`,`size` ) VALUES (?, '', ?, 4 )", (i, one['md5']))
        try:
            if self.__fast_count_max < self.__fast_count_i:
                # boo.show('fast_re_ready_快速操作 - -重新-准备/初始化')
                self.fast_re_ready()  # 保存数据到硬盘并重启快速模式
                self.__fast_count_i = 0
            # else:
            #     self.__fast_count_i += 1
            self.__fast_count_i += 1
            self.__c.execute(sql, paramObj)
            return self.__c.lastrowid
        except:
            if self.__isDebug:
                funcName = sys._getframe().f_back.f_code.co_name  # 获取调用函数名
                # lineNumber = sys._getframe().f_back.f_lineno  # 获取行号
                # from_funcation = sys._getframe().f_code.co_name  # 获取当前函数名

                showStr = "快速操作 - - 执行中-发生错误!\n"
                showStr += "被调用的上一层函数：" + funcName + "\n"
                showStr += "数据库：" + self.__dataPath + "\n"
                showStr += "当前位置：%s.%s\n"%(self.__class__,sys._getframe().f_code.co_name)
                errorInfo = traceback.format_exc()
                showStr += "详细错误信息：\n【\n"+errorInfo+"】\n"
                boo.show(showStr)

    # ------------------------------------------------------------------
    # 快速操作 - - 结束/收尾
    def fast_end(self):
        try:
            self.__conn.commit()
        except:
            if self.__isDebug:
                showStr = "快速操作 - - 结束/收尾-发生错误!\n"
                showStr += "当前位置：%s.%s\n"%(self.__class__,sys._getframe().f_code.co_name)
                errorInfo = traceback.format_exc()
                showStr += "详细错误信息：\n【\n"+errorInfo+"】\n"
                boo.show(showStr)

    # ------------------------------------------------------------------
    #  获取数据库 操作符指针
    def get_c(self):
        return self.__c

    # ------------------------------------------------------------------

    # ------------------------------------------------------------------
    #  获取第一行数据
    def getData_firstRow(self, sql):
        try:
            # cursor = self.__conn.execute("SELECT *  from `buy5sell5`")
            cursor = self.__conn.execute(sql)
            for row in cursor:
                return row
        except:
            if self.__isDebug:
                strArr = []
                strArr.append("\033[1;31m")
                strArr.append("快速操作 - - 结束/收尾-发生错误!\n")
                strArr.append("当前位置：%s.%s\n"%(self.__class__,sys._getframe().f_code.co_name))
                strArr.append("详细错误信息：\n【\n%s】\n"%(traceback.format_exc()))
                strArr.append(" \033[0m!")
                boo.show(''.join(strArr))
            # print(row)

    #  获取第一行数据
    # maxRow 返回最大行数 =0表示无限制
    def getData_more(self, sql,maxRow=0):
        try:
            # cursor = self.__conn.execute("SELECT *  from `buy5sell5`")
            cursor = self.__conn.execute(sql)
            i = 0
            outArr = []  # 返回的数组
            for row in cursor:
                if 0 == maxRow or i < maxRow:
                    outArr.append(row)
                    i += 1
                else:
                    return outArr  # 达到上限提前返回

            return outArr

        except:
            if self.__isDebug:
                strArr = []
                strArr.append("\033[1;31m")
                strArr.append("快速操作 - - 结束/收尾-发生错误!\n")
                strArr.append("当前位置：%s.%s\n"%(self.__class__,sys._getframe().f_code.co_name))
                strArr.append("详细错误信息：\n【\n%s】\n"%(traceback.format_exc()))
                strArr.append(" \033[0m!")
                boo.show(''.join(strArr))
            # print(row)

    # ------------------------------------------------------------------

    #  没有返回的 - 执行多条sql语句
    def runSQL_many_noReturn(self,SQL):
        try:
            self.__c.executemany(SQL)  # 执行多条sql语句
            self.__conn.commit()
        except:
            if self.__isDebug:
                showStr = "执行SQL发生错误!\n"
                showStr += "当前位置：%s.%s\n"%(self.__class__,sys._getframe().f_code.co_name)
                errorInfo = traceback.format_exc()
                showStr += "详细错误信息：\n【\n"+errorInfo+"】\n"
                boo.show(showStr)

    #  没有返回的 - 执行一条sql语句
    def runSQL_noReturn(self,SQL):
        try:
            self.__c.execute(SQL)  # 执行一条sql语句
            self.__conn.commit()
        except:
            if self.__isDebug:
                showStr = "执行SQL发生错误!\n"
                showStr += "当前位置：%s.%s\n"%(self.__class__,sys._getframe().f_code.co_name)
                errorInfo = traceback.format_exc()
                showStr += "详细错误信息：\n【\n"+errorInfo+"】\n"
                boo.show(showStr)
    # ------------------------------------------------------------------

    #  统计数据
    # sql 格式必须是 COUNT "SELECT COUNT(*) FROM img_index WHERE  state=0 ;"
    def countItems(self,SQL):
        try:
            # self.__c.execute("SELECT COUNT(*) FROM img_index WHERE  state=0 ;")
            self.__c.execute(SQL)
            amount = self.__c.fetchone()[0]  # 获取统计总是
            return amount
        except:
            if self.__isDebug:
                showStr = "统计数据发生错误!\n"
                showStr += "当前位置：%s.%s\n"%(self.__class__,sys._getframe().f_code.co_name)
                errorInfo = traceback.format_exc()
                showStr += "详细错误信息：\n【\n"+errorInfo+"】\n"
                boo.show(showStr)

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
