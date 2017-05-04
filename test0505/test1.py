# _*_ coding:utf-8 _*_
#统计字母出现的次数

str1 = "Hope is goog thing."
str1 = str1.lower()
list1 = [0] * 26
for i in range(len(str1)):
	if(str1[i] >= 'a' and str1[i] <= 'z'):
		list1[ord(str1[i]) - ord('a') += 1
print(list1)
