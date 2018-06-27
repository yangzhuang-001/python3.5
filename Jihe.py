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

