#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
#  相关的文件操作
创建： 2018-1-8 08:51:50
'''

import os
import re
import time
import sys
import urllib
import urllib2
import random
import socket
import winsound
import ssl
import json
# custom HTTPS opener, banner's oracle 10g server supports SSLv3 only
import httplib, ssl, socket
import StringIO, gzip

import win32gui
import win32api
import win32con



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


# ---------------------------------------------------------------------------

'''
# 功能：GBK转UTF-8
# 时间：2018-2-12 18:30:36
# 返回： 
# 参数：
# 实例： 
'''
def GBKtoUTF8(INtxt):
    try:
        return INtxt.decode('gbk').encode('utf-8')  # gbk 转Unicode 再转 utf8
    except:
        return INtxt

# ---------------------------------------------------------------------------

'''
# 功能： 由父句柄，遍历所有子句柄句柄
# 时间： 2018-2-12 17:49:17
# 返回： =None失败，=有效句柄数组 句柄用long整数 表示
# 参数： parentHwnd父句柄，默认=0（就是顶级父层）
# 实例： hwndChildList
'''
def getChildList(parentHwnd=0):
    OUTwindows = []
    try:
        windows = []
        # EnumChildWindows如果父级句柄是0则只能获取1级深度 句柄，非0，则可以获取 父级子子孙孙 的句柄
        win32gui.EnumChildWindows(parentHwnd, lambda hwnd, param: param.append(hwnd), windows)
        OUTwindows += windows
        # print '父层=', parentHwnd, '=>', windows
        if parentHwnd == 0:  # 顶级句柄所以再次循环
            for hwnd in windows:
                list2 = getChildList(hwnd)  # 递归调用函数
                if list2:
                    OUTwindows += list2  # 合并子句柄
                    pass
        # end if

        return OUTwindows
    except:
        return None

# ---------------------------------------------------------------------------

'''
# 功能： 有窗口标题查找句柄
# 时间： 2018-2-12 18:32:39
# 返回：
        = none 没有一条符合条件
        =二维数据 符合条件的标题
            二维数据结构：
            row[0][0] = 句柄（long）
            row[0][1] = 标题
            row[0][2] = 类目
# 参数：
    FPtitle 全等 FPtitle
    FPinclude 包含FPinclude
    FPuninclude 不含FPuninclude
    FPstart 以FPstart开头
    FPend 以FPend结尾
# 实例： 
    findWindowByTitle(None,'包含字符串',None,None,None)
    findWindowByTitle(None,'包含字符串','','开头','')
'''
def findWindowByTitle(FPtitle, FPinclude,FPuninclude,FPstart,FPend, parentHwnd=0):
    if type(FPtitle) == unicode:
        FPtitle = FPtitle.encode('UTF-8')

    maxIf = 0 # 需要的条件个数
    maxIf += 1 if FPtitle else 0
    maxIf += 1 if FPinclude else 0
    maxIf += 1 if FPuninclude else 0
    maxIf += 1 if FPstart else 0
    maxIf += 1 if FPend else 0
    # print maxIf
    # if maxIf<1:
    #     return None

    windowsHwnds = getChildList(parentHwnd)
    outArray = []
    for hwnd in windowsHwnds:
        countOK = 0
        iTitle = win32gui.GetWindowText(hwnd)
        iTitle = GBKtoUTF8(iTitle)
        if len(iTitle) < 1:
            continue
        if maxIf > 0:
            # 判断是否 全等
            if FPtitle and iTitle == FPtitle > -1:
                countOK += 1

            # 判断是否 包含
            if FPinclude and iTitle.find(FPinclude) > -1:
                countOK += 1

            # 判断是否 不包含
            if FPuninclude and iTitle.find(FPuninclude) < 0:
                countOK += 1

            # 判断是否 以FPstart开头
            if FPstart and iTitle.startswith(FPstart):
                countOK += 1

            # 判断是否 以FPstart结尾
            if FPend and iTitle.endswith(FPend):
                countOK += 1
        # end >> if maxIf > 0:

        if maxIf == countOK:
            clsname = win32gui.GetClassName(hwnd)
            outArray.append((hwnd, iTitle, clsname))  # 满足所有条件返回句柄

    # end for---------------
    if len(outArray) > 0:
        return outArray
    else:
        return None

# ---------------------------------------------------------------------------

'''
# 功能： 由句柄，获取窗口标题
# 时间：2018-2-12 17:50:37
# 返回： 返回返回窗口标题，UTF-8
# 参数：
# 实例： 
'''
def getWindowTitleByHwnd(INhwnd):
    title = win32gui.GetWindowText(INhwnd)
    title = GBKtoUTF8(title)
    return title

# ------------------------------------------------------------------

'''
# 功能： 设置窗口置顶
# 时间： 2018-2-12 21:10:59
# 返回：  
# 参数：
# 实例： 
'''
def setWindowsTopMost(INhwnd):
    # 置顶
    win32gui.SetWindowPos(INhwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,
                          win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)  # //取消置顶  恢复正常
    return
# ------------------------------------------------------------------

'''
# 功能： 取消窗口置顶
# 时间： 2018-2-12 21:10:55
# 返回：  
# 参数：
# 实例： 
'''
def setWindowsNoTopMost(INhwnd):
    win32gui.SetWindowPos(INhwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0,
                          win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)  # //取消置顶  恢复正常
    return
# ------------------------------------------------------------------

'''
# 功能： 取消窗口置顶
# 时间： 2018-2-12 21:10:55
# 返回：  
# 参数：
# 实例： 
'''
def setWindows_show(INhwnd):
    # 置顶
    win32gui.SetWindowPos(INhwnd, None, 0, 0, 0, 0,
                          win32con.SWP_SHOWWINDOW | win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_NOACTIVATE | win32con.SWP_NOOWNERZORDER)
    return
# ------------------------------------------------------------------

'''
# 功能： 取消窗口置顶
# 时间： 2018-2-12 21:10:55
# 返回：  
# 参数：
# 实例： 
'''
def setWindows_hide(INhwnd):
    win32gui.SetWindowPos(INhwnd, None, 0, 0, 0, 0,
                          win32con.SWP_HIDEWINDOW | win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_NOACTIVATE | win32con.SWP_NOOWNERZORDER)
    return
# ------------------------------------------------------------------

'''
# 功能： 设置窗口大小
# 时间： 2018-2-12 21:10:51
# 返回：  
# 参数：
# 实例： setWindowsWidth_Height(hwnd,350,500)
'''
def setWindowsWidth_Height(INhwnd,width,height):
    win32gui.SetWindowPos(INhwnd, None, 0, 0, width, height,
                          win32con.SWP_NOMOVE)  # //取消置顶  恢复正常
    return
# ------------------------------------------------------------------

'''
# 功能： 设置窗口大小
# 时间： 2018-2-12 21:10:51
# 返回：  
# 参数： 
# 实例： setWindowsX_Y(hwnd, 50, 50)
'''
def setWindowsX_Y(INhwnd,X,Y):
    win32gui.SetWindowPos(INhwnd, None, X, Y, 0, 0, win32con.SWP_NOSIZE)  # //取消置顶  恢复正常
    return
# ------------------------------------------------------------------

'''
# 功能： 关闭窗口
# 时间： 2018-2-12 21:10:51
# 返回：  
# 参数： 
# 实例： setWindowsX_Y(hwnd, 50, 50)
'''
def closeWindow(INhwnd):
    win32gui.PostMessage(INhwnd, win32con.WM_CLOSE, 0, 0)
    return
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
