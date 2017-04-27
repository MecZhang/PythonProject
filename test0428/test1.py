#  _*_ coding:utf-8 _*_
#列表统计字符串中所有出现的字母的个数，不论大小写

strA = input("input string please\n")
strB = [0]*26

i = 0
n = len(strA)
for i in range(0,n):
    if strA[i]: 
        m = ord(strA[i])-97     
        strB[m] = strB[m]+1
        
print("the number of every character is ")        
print(strB)
