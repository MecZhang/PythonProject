# _*_ coding:utf-8 _*_ 
#文件I/O与文件操作

import os
f = open("./Blowing in the wind.txt", "a+")
# 创建并打开文件
f.write("How many roads must a man walk down\n\
Before they call him a man\n\
How many seas must a white dove sail\n\
Before she sleeps in the sand\n\
How many times must the cannon balls fly\n\
Before they're forever banned\n\
The answer my friend is blowing in the wind\n\
The answer is blowing in the wind\n")

f.seek(0,0)
#f.insert("Blowing in the wind")
#print(f.tell())
f.write("Blowing in the wind")
f.seek(0,1)
f.write("\tBob Dylan\n")
f.seek(0,2)
f.write("1962 by Warner Bros.Inc.")
a = f.readline()
print(a)
f.close()

a = input("do you want to clean the file? y or n\n")
if a == 'y':
    os.remove("./Blowing in the wind.txt")
