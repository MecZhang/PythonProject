# _*_ coding:utf-8 _*_ 
# QQ与姓名

listA = ["xiaoyun","xiaohong","xiaoteng","xiaoyi","xiaoyang"]
listB = [88888,5555555,11111,1234321,1212121]
a = zip(listA,listB)
b = dict(a)

print(a)
print(b)

c = input("Please input the name:")
#如果姓名不在字典中则再次输入,未完成
print(b[c])

print("Who is th nice QQ number?")
m = len(b)
for k,v in b.items():
    if v < 1000000:
        print(k)
