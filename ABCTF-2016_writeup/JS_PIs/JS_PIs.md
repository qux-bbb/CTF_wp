#JS Pls (Reverse Engineering)
##Problem
**Can you figure out the flag from [this](http://pastebin.com/raw/9Y55hxbw?) Have fun ;)**  

##Solution

I am very sorry,but i am so tired to convert it to English,maybe you can study Chinese?  

这题比较坑的是不能直接用工具来做，要手工……..
首先把那串字符串base64解密之后，发现是jsfuck编码，还以为可以直接用浏览器控制台运行js代码了，没想到报错，那就没办法了，只能一段一段解了，用alert函数把那些jsfuck编码替换掉，大概就是这个样子（可能某些地方稍微做了改正）

```
process.stdin.resume();
process.stdin.setEncoding('utf8');
console.log('Give me a flag');
process.stdin.on('data', (t) = > {
  t = t.trim();
  if (t.length === 19) {
    if (t.substr( 0, 5) === "ABCTF") {
      if (t[5].charCodeAt( 0) === t[18].charCodeAt( 0)  && t[5].charCodeAt( 0) === 123) {
        if (t.substr(6,4) === Object.keys(process.versions) [0]) {
          if (t[10] === t[13] && t[10].charCodeAt( 0) === 95) {
            if (t.substr(11, 2) === ((typeof x) [5] + (typeof t) [0])) {
              if (t.substr(14, 4) === "w4Ck"){
              	console.log('nice job!');
                process.exit();
              }
            }
          }
        }
      }
    }
  }
  console.log('nope!');
  process.exit();
});

```

接下来就是分析了  
先说几个函数的作用  
Trim  去掉字符串两侧的空白，不改变类型  
charCodeAt 返回Ascii码值（查的是返回Unicode值，我看的是ascii码）  
process.versions  node和node依赖库的版本  
{ node: '0.4.12',    
   v8: '3.1.8.26',    
   ares: '1.7.4',    
   ev: '4.4',    
   openssl: '1.0.0e-fips' }  

Object.keys（obj） 返回一个数组，数组里是该obj可被枚举的所有属性  
String1.substr(6,4)  返回String1从第7位开始的连续4位字符串  

也就这些函数吧，然后分析过程  
第1个if判断flag长度，应为19位  
第2个if判断前5位，应为 ABCTF  
第3个if 判断第6位和第19位，应为左右大括号  
第4个if判断7-10位 ，根据两个函数的作用，知道返回值为node  
第5个if判断11，,14位，应为 _ 下划线  
第6个if判断12,13位，这里比较复杂: x没有声明，所以返回 undefined,t是字符串型，返回 string，所以12,13位应为 is  
第7个if判断15-18位，应为 w4Ck  

好了，这样flag就出来了：**ABCTF{node_is_w4Ck}**
