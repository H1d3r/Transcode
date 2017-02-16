#! -*- coding:utf-8 -*-

__author__="nMask"
__Date__="20170216"
__Blog__="http://thief.one"

'''
为彻底解决python2.x编码问题.
'''
import sys
import platform
import chardet

system_type=platform.system()   ##操作系统类型
bianma_list=["utf-8","gbk","gb2312"] ##编码类型列表

'''
设置系统默认编码为gbk
'''
if system_type=="Windows":
	reload(sys)
	sys.setdefaultencoding('gbk')
else:
	reload(sys)
	sys.setdefaultencoding("utf-8")


def convert(content):
	'''
	将<Str>编码转化为<Unicode>编码
	'''
	try:
		bianma=chardet.detect(content)["encoding"]  ##如若内容为网页，则获取网页编码。
	except:
		pass
	else:
		bianma_list.append(bianma)

	if isinstance(content,(str)):  ##判断编码是否为<str>格式。
		for i in bianma_list:
			try:
				content=content.decode(i)
				break
			except:
				pass

	return content  ##返回unicode格式编码。
	








