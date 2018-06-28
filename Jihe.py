#!/usr/bin/env python3
#集合：是一个无序不重复元素的数据集，对比列表的区别是无序的。
#不可以使用索引进行顺序访问；不能够有重复的数据。

#项目开发中，集合主要用在数据元素的去重和测试是否存在。
#集合支持数学上的运算：
                #union （联合）
                #intersection (交)
                #difference (差)
                #symmetric difference (对称差集)

#注意空集合不能使用 {} 创建，只能使用set函数，因为 {} 创建的是一个空的字典

courses = set()
print(type(courses))

courses = {'Linux','C++','Vim','Linux'}
print(courses)
print(type(courses))

#集合可以直接由字符串与set函数进行创建。
#会将字符串拆散为不同的字符，并去除重复字段
new_courses = set('shiyanlou.com')
print(type(new_courses))
print(new_courses)

new_courses1 = set('shiyanlou')
print(new_courses1)

#集合操作
#not in 是一个判断python是否不在集合中的操作
# in 操作适用于列表和元组
#测试判断是否存在
print('Linux' in courses)
print('C++' not in courses)

#add 向集合中增加元素
#remove 从集合中删除元素
courses.add('python')
print('python' in courses)
print(courses)

courses.remove('Vim')
print(courses)

#尝试两个集合的运算
set1 = {1,2,3,4}
set2 = {3,4,5,6}

# | 操作 union操作
print(set1 | set2)
print(set1.union(set2))

# & 操作 找出相同的数值
print(set1 & set2)

# - 返回在set1 不在 set2 的元素
print(set1 - set2)

# ＾ 操作，返回只存在两个集合中的元素
print(set1 ^ set2)


#集合操作总结：集合set是一个无序不重复元素的数据集，对比列表的区别首先是无序的
#不可以使用索引进行顺序的访问
#不能够有重复的数据

#集合是能使用set 函数
#{} 创建的是一个空的字典

course = set()
print(type(course))

course = {'Linux','C++','Linux'}
print(course)
#多余的linux 字符串已被自动去除

#需要注意的是空的集合不能使用{} 创建
#只能使用set函数
#应为空的集合 {} 创建的是一个空字典

course2 = set()
print(type(course2))

course3 = {'linux','java'}
print(type(course3))

#集合可以直接由字符串与set函数进行创建，
#会将字符串拆散为不同的字符，并去除重复的字符

nameSet = set('shiyanlou.com')
print(nameSet)

#not in 是一个判断 python 是否不在集合中的操作。
#in 操作也适用与列表和元组

#向集合中增加元素的方法
course3.add('python')

#从集合中删除元素的方法
course3.remove('C++')

#两个集合的运算

# " | " 操作 set1 中或 set2 中的元素，等效于union 操作
set1 | set2
set1.union(set2)

#& 操作返回即在set1 又在set2 的元素
set1 & set2

# - 返回在set1 不在 set2 的元素
set1 - set2

# ^ 操作，返回只存在两个集合中的元素
set1 ^ set2




