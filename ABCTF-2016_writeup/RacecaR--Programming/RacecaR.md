#RacecaR (Programming)
##Problem
**Aren't Palindromes cool? I certainly think so, which is why I want you to find the longest palindrome in [this](https://gist.github.com/LiamRahav/5ac79c085a9a36e931d786c25c32dedc) file.**


---
##Solution
You need know the meaning of Palindromes,look like "abbc","abcdcba",you can look more at [Palindromes](https://en.wikipedia.org/wiki/Palindrome)

You need delete the "\n" in the file,then you can write a python script to print them.

The code :
```
#!/usr/bin/python
# -*-coding:utf-8 -*-

f = open("palindrome.txt","r")
a = f.read()

b = list(a)
leng = len(b)


def ispalindrome(i,j):
	for flag in range(0,i/2+1):
		if b[j+flag] != b[j+i-flag]:
			return 0
	return 1

for i in range(0,leng):   # i  the length of Palindromes
	for j in range(0,leng-1-i):
		if ispalindrome(i,j):
			print "".join(b[j:j+i+1])
	print i


print "Done!!!!!!!!!!!!!!!!!!!!!!!!!!!"
f.close()

```
When the length is 7,you can see three strings:

DbrMrbD

o4OmO4o

BZXTXZB

The first string is the flag.

**Flag:ABCTF{DbrMrbD}**


