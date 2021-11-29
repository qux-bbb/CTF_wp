# secret_chart

题目描述：  
```r
NO one know chart better than me!
附件下载: https://pan.baidu.com/s/1fyHWJHzN_HvC4uWMlQNGqQ 提取码（GAME）
备用下载: https://share.weiyun.com/WxWhZvVb
```
附件为: secret_chart_b3811511bcfb857054512f2768d3cb24.zip  

解压得到He11o.png  
图片后面拼了一个压缩包，保存为tail.zip  
tail.zip有密码，但其中的文件fl49.xlsx是以Store形式保存的，所以可以尝试 归档明文攻击: https://github.com/kimci86/bkcrack  

选一个xlsx文件的前48字节，保存为xlsx_header，执行命令：  
```r
./bkcrack -C tail.zip -c fl49.xlsx -p xlsx_header
    bkcrack 1.3.3 - 2021-11-08
    [00:16:03] Z reduction using 40 bytes of known plaintext
    100.0 % (40 / 40)
    [00:16:03] Attack on 192926 Z values at index 7
    Keys: 746739e0 9a3a46a3 1cb7a7b1
    83.9 % (161862 / 192926)
    [00:24:54] Keys
    746739e0 9a3a46a3 1cb7a7b1

./bkcrack -C tail.zip -k 746739e0 9a3a46a3 1cb7a7b1 -U tail_with_new_password.zip easy
```
用"easy"做密码解压tail_with_new_password.zip，可以得到fl49.xlsx  

把数据合并成24*24的矩阵，转成01的形式，保存为01.txt, 然后脚本转图片[test.py](files/test.py)，1对应黑色像素  

确认是DataMatrix，在这里解码: https://online-barcode-reader.inliteresearch.com/  
解码得到: zfua{B3s1o9in1Nw0halUnofuNc0HM1}  
然后是6位的凯撒: flag{H3y1u9ot1Tc0ngrAtulaTi0NS1}  
