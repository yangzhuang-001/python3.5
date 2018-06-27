#!/usr/bin/env python3

#列表、元组、集合与字典

#列表：是一种有序的数据集合

course = ['Linux','python','vim','c++']
#添加元素php 到列表末尾
course.append('PHP')
print(course)
#最后一个索引可以使用-1 进行标识
print(course[-2])
#print(len(course))

#列表操作
#列表是有序的数据集合
#插入到列表任何位置方法 insert()

course.insert(0,'Java')
print(course)

course.insert(1,'Ruby')
print(course)

#count（s） 方法会返回列表元素中（s）的数量。
print(course.count('python'))

# 移除列表中的任意指定值，需要使用remove()方法
#如果任意指定值出现多次，则只有第一个出现的元素会被清除
course.remove('Java')
print(course)

#另外一种删除元素的方法是del 关键字，这个关键字可以删除列表中指定位置的元素，
# 需要使用列表中要删除元素的索引
del course[1]
print(course)
del course[-2]
print(course)

#列表是有顺序的
#一种方法是将其中的一个列表合并到另一个列表的末尾位置
#可以使用 extend()
new_courses = ['Java1','Cloud']
course.extend(new_courses)
print(course)

#列表排序
#sort() 方法，排序的前提是列表的元素是可比较的，例如数字是按照大小进行排序
#字符串则会选择按照字母表的顺序进行排序。
course.sort()
print(course)

#列表 pop()函数 返回最后的一个元素，pop() 在返回元素的同时也会删除这个元素
#传入一个参数i 即 pop(i) 会将第i个元素弹出，并删除

name = course.pop()
print(name,course)

courseName = course.pop(1)
print(courseName)
print(course)

#列表学习总结：列表添加（每个列表都是有序的数据列表）函数 append('元素')

            #列表查询 列表名称【列表索引】 进行查询

            #列表插入 insert（1,'php'） 可以将数据插入到列表的任何位置

            #count(s)函数 列表方法 返回在列表元素中出现多少次
            #remove()方法 remove('Java') 可以移除任意一个元素
            #如果该元素值在列表出现多次，则只有一个出现的元素被清除

            #del 删除元素方法关键字，这个关键字可以删除列表指定位置的元素
            #del course[1]
            #del course[-1]

            #列表是有顺序的，在执行列表操作的过程中有序列表可以进行反转
            #course.reverse()

            #两个列表，合并到一起，一种方法是可以将其中一个列表合并到另外一个列表
            #末尾位置，可以使用extend（）：
            #new_courses = ['BigData','Cloud']
            #courses.extend(new_courses)

            #给列表排序，使用列表的sort 方法，例如 数字是按照大小进行排序，而字符串
            #则会选择按照字母表的顺序进行排序的
            #course.sort()

            #pop函数返回最后一个元素，pop()返回元素的同时也会删除这个元素
            #传入一个参数i即 pop(i) 会将第i 个 元素弹出
            #courses.pop()
            #courses.pop(1)























