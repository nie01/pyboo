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
import ssl
import json
import struct
# custom HTTPS opener, banner's oracle 10g server supports SSLv3 only
# import httplib
import io
import gzip
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

import wmi
import win32api

# # 获取C盘卷序列号
# # 使用C盘卷序列号的优点是长度短，方便操作，比如1513085707，但是对C盘进行格式化或重装电脑等操作会影响C盘卷序列号。
# # win32api.GetVolumeInformation(Volume Name, Volume Serial Number, Maximum Component Length of a file name, Sys Flags, File System Name)
# # return(‘‘, 1513085707, 255, 65470719, ‘NTFS‘),volume serial number is  1513085707.
# def getCVolumeSerialNumber(driveRoot):
#     # CVolumeSerialNumber = win32api.GetVolumeInformation("C:\\")[1]
#     CVolumeSerialNumber = win32api.GetVolumeInformation(driveRoot)[1]
#     # print chardet.detect(str(CVolumeSerialNumber))
#     # print CVolumeSerialNumber
#     if CVolumeSerialNumber:
#         # return str(CVolumeSerialNumber)  # number is long type，has to be changed to str for comparing to content after.
#         return CVolumeSerialNumber
#     else:
#         return 0

# r = psutil.net_if_addrs()
# print(r)

# r = psutil.disk_partitions()  # 获取所有硬盘
# print(len(r),'】')
# for item in r:
#     # print(item[0])
#     print(item[0],getCVolumeSerialNumber(item[0]))
#     # print(psutil.disk_usage(item[0]))
#     # print(getCVolumeSerialNumber(item[0]))

# 获取所有硬盘名称
# 返回 名称数组
def getDisk():
    c = wmi.WMI()
    disk = []
    # 获取硬盘分区
    for physical_disk in c.Win32_DiskDrive():
        # uuid = physical_disk.qualifiers['UUID']
        for partition in physical_disk.associators("Win32_DiskDriveToDiskPartition"):
            disk.append(
                {
                    'name': physical_disk.Caption,  # 名称 不同操作系统下不一样
                    'index': physical_disk.Index,  # 磁盘序号
                    # 'description': physical_disk.Description,  # 描述
                    'size': physical_disk.Size,  # 大小
                    'serialnumber':  str(physical_disk.SerialNumber).strip(),  # 硬盘序列号 ， 部分硬盘盒链接的硬盘无法识别
                 })
            break

    return disk

# ------------------------------------------------------------------

def getDrives():
    c = wmi.WMI()
    drives = []
    # 获取硬盘分区
    for physical_disk in c.Win32_DiskDrive():
        for partition in physical_disk.associators("Win32_DiskDriveToDiskPartition"):
            for logical_disk in partition.associators("Win32_LogicalDiskToPartition"):

                # 盘符
                letter = logical_disk.Caption[0:-1]
                drives.append(
                    {
                        'letter': letter,  # 盘符
                        'name': logical_disk.VolumeName,  # 分区名称
                        'id': logical_disk.VolumeSerialNumber,  # 分区为唯一ID（16进制） ， 格式化后会被改变
                        'index': partition.Index,  # 分区序号
                        # 'description': logical_disk.Description,
                        # 'diskName': physical_disk.Caption,  # 磁盘名称
                        # 'diskIndex': physical_disk.Index,
                        'fileSystem': logical_disk.FileSystem,  # 文件系统
                        'freeSpace': logical_disk.FreeSpace,  # 可用空间
                        'size': logical_disk.Size,  # 分区空间
                     })
                # print(physical_disk.Caption, '】磁盘编号，分区编号=', partition.Caption, '】盘符=', logical_disk.Caption)
    return drives
# ------------------------------------------------------------------


# def getDrives():
#     l = getDrives()
# ------------------------------------------------------------------



# instance of Win32_LogicalDisk
# {
# 	Access = 0;
# 	Caption = "C:";
# 	Compressed = FALSE;
# 	CreationClassName = "Win32_LogicalDisk";
# 	Description = "本地固定磁盘";
# 	DeviceID = "C:";
# 	DriveType = 3;
# 	FileSystem = "NTFS";
# 	FreeSpace = "50332925952";
# 	MaximumComponentLength = 255;
# 	MediaType = 12;
# 	Name = "C:";
# 	Size = "106644488192";
# 	SupportsDiskQuotas = FALSE;
# 	SupportsFileBasedCompression = TRUE;
# 	SystemCreationClassName = "Win32_ComputerSystem";
# 	SystemName = "DESKTOP-9BIQU08";
# 	VolumeName = "sysC";
# 	VolumeSerialNumber = "14E44B2C";
# };

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
