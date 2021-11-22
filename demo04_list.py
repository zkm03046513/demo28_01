last =[]
last1 =['red','orange','old']
last2 =[1,2]
last3 =['a','b','a','a']

print(last)
print(last1)
print(last2)

#列表获取/查找
"""
index(obj)   查找列表中某个元素的位置
count(obj)   查找当前元素在列表中出现的次数

"""

print (last3.index('b'))
print (last3.count('a'))
"""
获取last1 中的所有元素

"""
for x in last1:
    print(x)

#列表的修改
"""
append(obj)            :向列表中添加一个元素
insert(index,obj)             ：向某个位置添加一个元素
expend(last1)      :向last1中的所有元素添加到当前列表中    
"""

last2.append(3)
print(last2)

last2.insert(1,'abc')
print(last2)

last2.extend(last1)
print(last2)
#列表删除
"""
pop()            删除列表最后一个元素
remove（obj）   删除列表中某一个元素
clear（）         清除所有元素
"""
last2.pop()
print(last2)
last2.remove(3)
print(last2)
last2.clear()
print(last2)

#列表的排序和翻转
"""
sort()      对当前列表进行排序
reverse（）   对当前列表进行翻转
"""

last1.sort()
print(last1)
last1.reverse()
print(last1)