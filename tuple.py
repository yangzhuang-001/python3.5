#!/usr/bin/env python3
#元组（tuple):一种特殊的列表，不同点是元组一旦创建就不能修改。
#如果是只读的数据，尽可能使用元组。
courses = ('C++','Cloud','Linux','PHP')
print(courses)
print(courses[1])

#元组中如果包含可变的数据元素，这些数据元素是可以修改是，例如元组中包含一个列表
#这个列表的内容是可以修改的

new_courses = ('Linux',['BigData1','BigData2','BigData3'],'Vim')
print(new_courses[1])

new_courses[1].append('Java')
print(new_courses[1])

#元组不可以直接使用括号中的一个元素的，需要在元素后面跟一个逗号
new_courses = ('Linux')
print(new_courses)
print(type(new_courses))

new_courses = ('vim',)
print(new_courses)
print(type(new_courses))

#元组总结：一种特殊的列表，不同点是一旦创建成功就不能进行修改；
         #如果是只读的数据，尽可能只用元组；
         #元组中包含可变的的数据类型，是可以进行修改的，比如元组内
         #包含了列表数据类型；
         #元组进行打印不可以直接使用括号中的一个元素，需要在元素后面加个逗号。

