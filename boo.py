#!/usr/bin/python3
# -*- coding: UTF-8 -*-
'''
# boo 是basic or other的缩写 意思是： 基础 或 其他未分类
创建： 2018-1-8 08:51:50
'''
import traceback  # 获取错误信息
import os
import time
import random
import hashlib
import binascii  # 二进制 转 16进制

# print "cnLib"
# os.system('pause') #按任意键继续。

# while 1:
#    pass

# print __name__

# os.system('pause') # 按回车继续执行

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
    print(binascii.b2a_hex(byte))   # 二进制转16进制
    return True  # 返回说明
# ------------------------------------------------------------------

'''
# 功能： 记录错误信息
# 时间：2018-2-17 13:55:28
# 返回： 
# 参数：
# 实例： 
    try:
        return
    except Exception, e:
        boo.logError()
        return
        
        
        
import datetime
nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')#现在
pastTime = (datetime.datetime.now()-datetime.timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')#过去一小时时间
afterTomorrowTime = (datetime.datetime.now()+datetime.timedelta(days=2)).strftime('%Y-%m-%d %H:%M:%S')#后天
tomorrowTime = (datetime.datetime.now()+datetime.timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')#明天
print('\n',nowTime,'\n',pastTime,'\n',afterTomorrowTime,'\n',tomorrowTime)
        
'''

'''
# /*
# * 运行时间
# */
# class runtime:
# 	__t_start = 0 #  开始时间
# 	__t_end = 0 #  结束时间
# 	__t_duration = 0 #  持续时间
#     def start(self):
#     # 开始
# 	t_start = clock()
# 	return t_start
#
#     def end(self):
#     #// 结束
#         t_end = clock()
#         return t_end
'''
class runtime:
    __t_start = 0  # 开始时间
    __t_end = 0  # 结束时间
    __t_duration = 0  # 消耗的时间长度

    # 中间段
    __t_AB_amount = 0  # 计数器
    __t_AB_start = 0  # 开始时间
    __t_AB_end = 0  # 结束时间
    __t_AB_duration = 0  # 消耗的时间长度

    # 开始
    def start(self):
        self.__t_AB_start = time.clock()
        self.__t_start = time.clock()

        return self.__t_start

    # 结束
    def end(self):
        self.__t_AB_end = time.clock()
        self.__t_end = time.clock()
        return self.__t_end

    # 计算持续时间
    def getRuntime(self):
        self.__t_duration = self.__t_end - self.__t_start
        return self.__t_duration

    # 显示当前速度
    def showSpeek(self,amountALL):
        self.__t_AB_end = time.clock()
        self.__t_end = time.clock()
        self.__t_duration = self.__t_end - self.__t_start

        amountAB = amountALL - self.__t_AB_amount  # 重新计数
        self.__t_AB_amount = amountALL  # 重新计数
        self.__t_AB_end = time.clock()
        self.__t_AB_duration = self.__t_AB_end - self.__t_AB_start
        self.__t_AB_start = time.clock()  # 重新开始

        # 整体速度
        suALL = -1
        if self.__t_duration > 0:
            suALL = amountALL / self.__t_duration

        txtALL = "ALL【共%d秒，循环%d次】速度= %f循环/秒" % (self.__t_duration, amountALL, suALL)
        print(txtALL)

        # 间区速度
        suAB = -1
        if self.__t_AB_duration > 0:
            suAB = amountAB / self.__t_AB_duration

        txtAB = "AB【共%d秒，循环%d次】速度= %f循环/秒" % (self.__t_AB_duration, amountAB, suAB)
        print(txtAB)


# 显示
def logError(filePath=None):
    '''
    traceback.print_exc()跟traceback.format_exc()有什么区别呢？
    format_exc()返回字符串，print_exc()则直接给打印出来。
    即traceback.print_exc()与print traceback.format_exc()效果是一样的。
    print_exc()还可以接受file参数直接写入到一个文件。比如
    traceback.print_exc(file=open('tb.txt','w+'))
    写入到tb.txt文件去。
    '''
    errorInfo = traceback.format_exc()

    if str == type(filePath):
        traceback.print_exc(file=open(filePath, 'a+'))

    # print(errorInfo)
    # traceback.print_exc()
    return

'''
# 功能： 记录日志
# 时间：
# 返回： =0失败，=1成功
# 参数：
# 实例： 
    try:
        return
    except Exception, e:
        boo.log()
        return
'''
# 显示
def log(logInfo):
    '''
    traceback.print_exc()跟traceback.format_exc()有什么区别呢？
    format_exc()返回字符串，print_exc()则直接给打印出来。
    即traceback.print_exc()与print traceback.format_exc()效果是一样的。
    print_exc()还可以接受file参数直接写入到一个文件。比如
    traceback.print_exc(file=open('tb.txt','w+'))
    写入到tb.txt文件去。
    '''
    # errorInfo = traceback.format_exc()
    # print errorInfo
    #  self.__class__.__name__ 获取当前函数
    try:
        if type(logInfo) == str:
            logInfo = logInfo.decode('utf-8')
        elif type(logInfo) == int:
            print(logInfo)
            return

        if type(logInfo) == unicode:
            # 先转为 unicode转gbk 再转unicode 谜底是去掉 特殊字符，因为特殊字符，在命令提示符运行时，显示会出错闪退
            logInfo = logInfo.encode('gbk', 'ignore').decode('gbk')

        # print type(logInfo)
        print(logInfo)
    except:
        print(logInfo)

# ------------------------------------------------------------------

# def md5(data):
#     try:
#         m2 = hashlib.md5()
#         m2.update(data)
#         return m2.hexdigest()
#     except:
#         return ''
def md5(data):
    try:
        # typyV = type(data)
        # if bytes != typyV:
        #     data = data.encode("utf-8")
        #
        return hashlib.md5(data).hexdigest()
    except:
        return ''

# ------------------------------------------------------------------

# 获取扩展名
def getName2(path):
  return os.path.splitext(path)[1]

# ------------------------------------------------------------------

# 显示
def show(showTxt):

    # print type(showTxt)
    try:
        if type(showTxt) == str:
            showTxt = showTxt.decode('utf-8')
        elif type(showTxt) == int:
            # print showTxt
            return

        if type(showTxt) == unicode:
            # 先转为 unicode转gbk 再转unicode 谜底是去掉 特殊字符，因为特殊字符，在命令提示符运行时，显示会出错闪退
            showTxt = showTxt.encode('gbk', 'ignore').decode('gbk')

        # print type(showTxt)
        print(showTxt)
    except:
        print(showTxt)

# ------------------------------------------------------------------


'''
获取日期时间
'''
def getDateTime():
    timeNum = time.time()
    time_local = time.localtime(timeNum)  # 转换成localtime
    dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)  # 转换成新的时间格式(2016-05-05 20:28:54)
    return dt
# # ------------------------------------------------------------------
'''
获取日期时间
'''
def getDateTime(timeNum = -1):
    if timeNum<0:
        timeNum = time.time()
    # print type(timeNum)
    if timeNum < 0:
        return ''
    time_local = time.localtime(timeNum)  # 转换成localtime
    dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)  # 转换成新的时间格式(2016-05-05 20:28:54)
    return dt

# ------------------------------------------------------------------
# A起点 Z终点 且是整型数值
# 返回的值 包含 A 和 Z
def getRandom(A,Z):
    # lenAZ=abs(Z-A) #绝对值

    if A == Z: #  没有区间
        return A
    elif A > Z: # 保证 A<= Z
        temp = A
        A = Z
        Z = temp
    Z += 1
    lenAZ = Z - A  # 绝对值
    return int(random.random() * lenAZ) + A
# ------------------------------------------------------------------
# 返回 随机数字字符串
# outLen 返回字符串的长度（数字个数）
# isFirs 第一个数字是否允许=0  =1可以0，=0不能为0
def getRandom_NumStr(outLen,isFirs0 = False):
    NumStr = random.choice('0123456789')
    if isFirs0 == False:
        NumStr = random.choice('123456789') #第一个数字 不会是0

    # NumStrArr = random.sample('0123456789', outLen-1)
    # NumStr = ''.join(NumStrArr)
    for i in range(1,outLen):
        NumStr += random.choice('0123456789')

    return NumStr

# ------------------------------------------------------------------

# ------------------------------------------------------------------
def makeDir(dirPath):
    '''
    功能： 一次创建多级目录（文件夹）
    :param string dirPath 路径
    :return string =False创建失败，=True创建成功/目录已经存在
    实例：
     re = makeDir(u'a/b/c')
    '''
    if os.path.isfile(dirPath):
        # return 1  #当前路径是文件路径
        return False  #当前路径是文件路径

    if os.path.isdir(dirPath):
        # return 2  #目录已经存在
        return True  #目录已经存在

    # print os.path.exists(dirPath),'=',dirPath
    if not os.path.exists(dirPath):  # 判断目录是否存在
        try:
            os.makedirs(dirPath)  # 创建目录
        except OSError as exc:
            # print exc.args
            # return 0
            return False
        except :
            # return 0
            return False

    # 判断创建 结果
    if os.path.isfile(dirPath):
        # return 1  # 当前路径是文件路径
        return False  # 当前路径是文件路径

    if os.path.isdir(dirPath):
        # return 2  # 创建成功
        return True  # 创建成功

# ------------------------------------------------------------------
def saveData(path, dataByte,methon='wb'):
    '''
    保存byte数据
    :param string path 文件路径
    :param byte dataByte 文件数据
    :param string methon 文件打开方式
    '''
    path = os.path.abspath(path)  # 转换为绝对路径
    dir = os.path.dirname(path)  # 获取父层目录
    re = makeDir(dir)  # 如果目录不存在则创建
    if re:
        f = open(path, methon)
        f.write(dataByte)
        f.close
        return True

    return False

# ------------------------------------------------------------------
def url2path(url, name2=None, parentDir=''):
    '''
    url转换为文件路径
    :param string url 必须，要转换的url
    :param string name2 可选，强加扩展名，默认无
    :param string parentDir 可选，转换路径的相对根目录
    :return string 转换后的路径
    '''
    try:
        path = url.split('//', 1)[1]
        # name2有效值 且 name2与path没有扩展名不一致
        if path.endswith('/'):
            path += 'index.html'  # 添加扩展名

        if name2 and False == path.endswith(name2):
            path = path + name2  # 添加扩展名

        if parentDir:
            path = parentDir + '/' + path  # 添加扩展名

        path = re.sub('[*?"<>|]', '-', path)  # 去掉文件名的非法字符
        path = path.replace('\\', '/')
        path = re.sub("/{2,}", '/', path)
        return path
    except:
        return None

# ------------------------------------------------------------------
def URLads2rela(targetAbsPath,nowAbsDir):
    '''
    URLads2rela URL绝对路径转相对路径
        abs absolutely 绝对
        rela relatively 相对
    :param string targetAbsPath 目标绝对路径
    :param string nowAbsDir 当前目录绝对路径
    :return string 相对路径
    '''
    try:
        pass
        targetAbsPath = targetAbsPath.replace('\\', '/')
        nowAbsDir = nowAbsDir.replace('\\', '/')
        targetAbsPath = re.sub("/{2,}", '/', targetAbsPath)
        nowAbsDir = re.sub("/{2,}", '/', nowAbsDir)
        if nowAbsDir.endswith('/'):
            nowAbsDir = nowAbsDir[:-1]  # 删除末尾的 "/"

        # prefix = os.path.commonprefix([targetAbsPath, nowAbsDir])  # 公共前缀 ** 不能用容易出错(如，d:/a/b/gtsfel.gif 与 d:/a/b/gt123,结果是d:/a/b/gt，而实际要的结果是d:/a/b/)
        prefix = os.path.commonpath([targetAbsPath, nowAbsDir]) + '/'  # 公共目录
        prefix_len = len(prefix)

        targetAbsPath = targetAbsPath[prefix_len:]
        if targetAbsPath.startswith('/'):
            targetAbsPath = targetAbsPath[1:]  # 删除开头的 "/"

        nowAbsDir = nowAbsDir[prefix_len:]
        dd_count = 0
        if nowAbsDir:
            nowSplit = nowAbsDir.split('/')
            dd_count = len(nowSplit)

        dd = ''
        for i in range(dd_count):
            dd += '../'

        out = dd + targetAbsPath
        return out
    except:
        pass
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
