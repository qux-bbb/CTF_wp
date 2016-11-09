# Obfuscated 1
##Problem
**Get this to return true! The grader runs the same script as you got! [Here](http://pastebin.com/8JkW5E1m) it is. There is no need to submit abctf{} wrapping**

##Solution
Just a python program，but you need convert something.

the code:

```
from _md5 import MD5Type as z

def is_flag(s):
   a = int(s[pow(ord(s[0]), 2) - 7226:])   #①  
   b = list(filter(lambda q: q % 3 == 0, [a, a * 2, a * 3, a * 4, a * 5]))  #②
   if len(b) != 5:
       return False       
   c = s[1:-2]
   if (len([n for n in list(c) if lambda y: int(y) in b])) != 8:     # ③
       return False
   d = [(ord(x) - 48) for x in list(s)] # fill in the blanks     #④ d[0]=37 d[13]=9
   if s.count('U') != 3:   #⑤
       return False
   if c.index("_") != c[::-1].index("_"):  # ⑥
   if (s[d[3]]) != 'U':   # 
       return False
   return True

```

① guess only 1 to convert,just the last one,so you can get s[0]="U"

② from "if",you can know a=3*i (i=1,2,3) ,i set "a" as 9

③ from here you can get the length of the string,it is 11

④ combine the last "if" ,you can set s[3]="0"  s[10]="9"

⑤ You can know 3 "U" in the string

⑥ "_" is  symmetrical in the string

Finally ,i find a string  **s="UUU0__\-\-\-\-9"**

You can find many like that.
