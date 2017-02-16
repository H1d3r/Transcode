# Transcode
python2.x---transcode ，解决python2.x编码报错问题，适用于网页编码、文件编码、系统编码、python编码的转换；适用于windows以及linux，对于windows下编码问题有良好的解决。

### Install
```bash
git clone https://github.com/subscription/Transcode

python setup.py install 
```
依赖：
chardet
安装：pip install chardet

### Usage

#### python内部<Str>格式转化为<Unicode>编码。
```bash
#! -*- coding:utf-8 -*-
from transcode import convert
a="中文"
b=convert(a)
print type(b)
print b
```

#### 转换网页编码
```bash
#! -*- coding:utf-8 -*-
import urllib2
from transcode import convert
body=urllib2.urlopen('http://thief.one').read()
body=convert(body)
print type(body)
print body
```
#### 转换文件编码
```bash
#! -*- coding:utf-8 -*-
from transcode import convert
#内容写入文件
f=open("test.txt","w")
a=u"中文"   #或者 a="中文"
f.write(a)
f.close()
#读取文件内容
body=open("test.txt","r").read()
body=convert(body)
print type(body)
print body
```

### Instructions
　　经过convert函数的内容，都会转为unicode格式，这与python2.x解决编码问题的思路是一致的。此模块应该在一切外部内容传递到python程序时进行使用，将外部字符串转化为统一的unicode编码，而在输出结果时，python内部已经有良好的机制，可以将unicode转化为相应操作系统类型的编码格式（linux为utf-8，windows为gbk)。对于中文unicode写入文件问题，transcode模块也给予了解决，只要导入此模块，便可以正常将unicode中文字符串转为相应操作系统类型的编码格式并写入文件。
