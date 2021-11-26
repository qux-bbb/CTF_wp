# Baby_steg

题目提供文件: [Baby_steg.zip](files/Baby_steg.zip)  

根据wp复现，参考wp见文末。  

---
解压Baby_steg.zip得到flag1.txt和password.7z  

尝试用john爆破password.7z，提取hash出现错误：  
```r
└─$ python 7z2john.py password.7z > password.hash
password.7z : 7-Zip files without header encryption are *not* supported yet!
```

按照wp用hashcat爆破password.7z：  
```r
# 安装perl、7z2hashcat.pl、相关依赖
sudo apt update && sudo apt install perl liblzma-dev
sudo cpan install Compress::Raw::Lzma
wget https://raw.githubusercontent.com/philsmd/7z2hashcat/master/7z2hashcat.pl
chmod +x 7z2hashcat.pl
./7z2hashcat.pl password.7z > password.hash
hashcat -a 3 -m 11600 password.hash ?d?d?d?d?d?d
```
爆破成功后，查看结果: `hashcat -a 3 -m 11600 password.hash ?d?d?d?d?d?d --show`  
`result: $7z$2$19$0$$16$abc477f84f711f5530432e64418c8392$3167568243$16$12$40a31f0f88ac7b9a9acdc6cbb7d23f23$8$00:321456`  
passwrod.7z解压得到password.txt，内容为"7324623c"  

flag1.txt使用file识别: `flag1.txt: uuencoded or xxencoded, ASCII text`, 根据内容格式确定为uuencoded  
在ubuntu下解码：  
```r
sudo apt install sharutils
uudecode flag1.txt
```
得到flag.7z，使用"7324623c"作为密码解压，得到challenge.png和encode.py  

encode.py是加密脚本，原图像经过加密得到challenge.png  
encode.py的大概逻辑是将每行的像素乱序，保存为新图片，对使用的python库不太熟悉，这里给encode.py加些注释：  
```python
import numpy as np
import cv2
import sys
import random

def encode(image):
    i = random.randint(520,540)  # 从 [520, 540] 随机取一个整数
    np.random.seed(i)  # 设置随机数种子
    # image = 1298 * 695
    to_hide = cv2.imread(image)  # 读取原图
    to_hide_array = np.asarray(to_hide)  # 将像素数据转为数组，这里是3维数组 array[hight][width][pix_data]

    for i in range(to_hide_array.shape[0]):  # 以图片高度做for循环，即按行操作
        np.random.shuffle(to_hide_array[i])  # 随机排列一行的像素
    
    gray = cv2.cvtColor(to_hide_array, cv2.COLOR_BGR2GRAY)  # 转为灰度图片(颜色种类少了)
    cv2.imwrite('challenge.png', gray)  # 保存加密后的图片
    print("encode!")

def main():
    if len(sys.argv) != 2:
        print('error!')
        exit(1)
    encode(sys.argv[1])

if __name__ == '__main__':
    main()
```
如果想运行脚本测试，需要安装python模块：  
```r
pip install numpy
pip install opencv-python opencv-contrib-python
```

接下来就是对加密做逆操作，有随机种子，但范围很像，所以可以全部生成找正确的一个，解密脚本如下：  
```python
# coding:utf8

import numpy as np
import cv2
import sys

def unshuffle(arr, size, indexes):
    result = [0] * size  # 用于存排好序的像素
    for i, ind in enumerate(indexes):  # i, ind 分别是 下标,值  已经是乱序过的，所以下标表示现在的位置，值表示原来的位置
        result[ind] = arr[i]  # i表示现在的位置，ind表示原来的位置
    return np.array(result)

def decode(image):
    for j in range(520,541):  # [520,540]全部做一遍
        np.random.seed(j)
        to_show = cv2.imread(image)
        to_show_array = np.asarray(to_show)
        image_size = 1298

        for i in range(to_show_array.shape[0]):
            indexes = list(range(image_size))  # 如 [0, 1, 2, ...]
            np.random.shuffle(indexes)  # 对有序列表的元素随机排列
            to_show_array[i] = unshuffle(to_show_array[i], image_size, indexes)  # 最重要的逻辑

        gray = cv2.cvtColor(to_show_array, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('result{}.png'.format(j), gray)

def main():
    if len(sys.argv) != 2:
        print('error!')
        exit(1)
    decode(sys.argv[1])

if __name__ == '__main__':
    main()
```

使用解密脚本操作challenge.png，生成21张图片，最终发现随机数应该是540，result540.png显示了正确的flag  
`flag{931549887f0a1398807eb68a656180ef}`  


参考wp：  
1. https://mp.weixin.qq.com/s/OAEXZTJ1mp1ZyCSajKdL6w
2. https://miaotony.xyz/2021/05/31/CTF_2021chunqiu_Baby_steg
