# while  循环
"""
需求打印1~5的数字

"""

x = 1
while x <=5:
    print(x)
    x += 1

"""
需求打印1~100的数字
"""
x = 1
while x <=100:
    print(x)
    x += 1

#range () 循环

"""
range(start=0,end,step=1)
"""
for x in range (0,10,1):
    print(x)
for x in range (0,25,1):
    print(x)


x = 1
while x <=20:
    print(x)
    x += 1


"""
range(start=0,end,step=1)
"""
for x in range (0,20,2):
    print(x)

#需求，循环1-100，当循环到5结束本次循环

for x in range(1,101):
    print(x)
    if x == 5:
        break
print("===================")
#需求 循环1-10 当循环到3跳过本次循环
for x in range(1,11):
    if x == 3:
        continue
    print(x)
print("===================")
# 需求 循环1-10 当循环到2跳过本次循环
for y in range(1,11):
    if y == 2:
        continue
    print(y)






