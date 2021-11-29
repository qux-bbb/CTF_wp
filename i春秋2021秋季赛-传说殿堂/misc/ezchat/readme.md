# ezchat

题目描述：  
```r
Alice and Bob are chatting online, can you get the content of the encrypted file?
附件下载: https://pan.baidu.com/s/1jG5cCYR2whsUMzKzl7r_ow 提取码（GAME）
备用下载: https://share.weiyun.com/OUlrKx2B
```
题目附件: ezchat_7136a25ca1ec19ceecc49790fc69cb7e.zip  

附件解压得到ezchat.pcapng  

tcp流1和2是Alice和Bob的irc聊天记录  
```r
PRIVMSG bob :Hello, Bob! Do you have the flag?
PRIVMSG alice :Hello, Alice! I have a flag, but how can I send it to you securely?
PRIVMSG bob :Don't worry, I will send you a archive file, just unzip it and follow the steps in the file inside. I will use the password we argeed on before.
PRIVMSG alice :Thanks. Let me try.
PRIVMSG alice :.DCC SEND flag.txt.gpg
PRIVMSG bob :Good job, see you next time~
PRIVMSG alice :Bye.
```

tcp流3是zip压缩包，保存为hello.zip, 有密码，爆破不出来  

tcp流3除了zip，还有其它数据  
这样过滤显示zip数据: `tcp.stream eq 3 and ipv6.dst == fd47:67ac:60f9::67a and tcp.len!=0`，保存pcap包为 about_zip.pcapng, 提取文件为the_zip.zip  
这样过滤显示其它数据: `tcp.stream eq 3 and ipv6.src == fd47:67ac:60f9::67a and tcp.len!=0`，保存pcap包为 about_another.pcapng, 提取文件为another(没用)  

the_zip.zip压缩包里一共有4个文件：  
```r
└─$ unzip -v the_zip.zip
Archive:  the_zip.zip
 Length   Method    Size  Cmpr    Date    Time   CRC-32   Name
--------  ------  ------- ---- ---------- ----- --------  ----
    2444  Defl:N     1854  24% 2021-10-25 11:07 2a66edce  alice_public_key.asc
    5070  Defl:N     3830  25% 2021-10-25 10:45 05a3997a  bob_secret_key.asc
30136688  Defl:N 30010467   0% 2021-10-25 10:38 e03055f4  gpg4win-3.1.16.exe
     285  Defl:N      206  28% 2021-10-25 17:11 cc25f1a0  instruction.txt
```
推测gpg4win-3.1.16.exe 明文攻击, 在这里下载: https://www.gpg4win.org/, 确认crc32相同  
使用压缩软件将gpg4win-3.1.16.exe以相同算法压缩(不设密码)作为gpg4win-3.1.16.zip(压缩包名字随意)，使用ARCHPR4.54明文攻击成功，zip密钥保存在zip密钥.txt，没有密码的压缩包保存为the_zip_decrypted.zip  
按instruction.txt步骤安装gpg4win进行操作，可以自己选一个文件加密测试看看效果  

经测试，tcp流6包含加密文件  
这里注意另存为文件后，最后4个字节是响应需要去掉  
重命名为flag.txt.gpg，解密即可  

flag{a2449a02-975b-4b25-ad44-3157c3fcb571}  
