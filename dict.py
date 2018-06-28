#!/usr/bin/env python3
#字典： 集合。 每一个元素都是一个key和一个value 的组合
# key 值在字典中必须是唯一的，因此可以很方便的从字典中使用key 获得其对应的value值
# {} 会创建一个空字典，如果非空 每个元素都是 key:value 这样的写法。

coursesdict = {1:'Linux',2:'Vim'}
print(coursesdict[1])

#注意 字典的key 不一定只有数字，可以使用各种不同类型
testdict = {1:2,'testr':'shiyanlou.com',9:[123]}
print(testdict[9])

#在字典中这些混合在一起使用，是可以的。
#如果key  不存在dict[key] 则会抛出KeyError，为了避免这种错误出现
#会使用get()函数获取key对应的value ,如果此时key不存在则默认返回None
#亦可在get（）函数中给定一个默认值，如果key不存在则会返回默认值

print(coursesdict[2])

#print(coursesdict[3])

print(coursesdict.get(4)) #None

print(coursesdict.get(4,'default'))#如果key不存在则会返回默认值

#同集合 set 函数一样，字典也可以使用dict 函数进行创建
#参数是一个 包含若干个 二元组的元组

dict_from_tuple = dict(((1,'Linux'),(2,'Vim')))

print(dict_from_tuple)

#注意，字典也是通过[] 的方式获取值，但与列表不同的是[]中的内容是key,
#可以为数字或其他类型，并不是列表的索引。
#字典是无序的，不能够通过索引进行访问。
#注意：字典的key 必须为不可变的类型，列表是不能够当作key 的

#向字典中增加元素的方法只需要为字典中的某一个key进行赋值，
#如果key已经存在则是更新该key对应的value值，
#如果不存在则表向字典中增加该key ： value:

coursesdict[3] = 'Bash'
coursesdict[4] = 'Java'

print(coursesdict)

#字典中删除一个元素，只需要使用del 删除，如果Key 不存在则抛出keyError
del coursesdict[1]
print(coursesdict)

#del coursesdict[1]
#print(coursesdict)
# del coursesdict[1]
# KeyError: 1

#字典中可以使用items()函数获取所有的字典元素，返回得到的是dict_items 类型
#的对象，这个对象可以使用for 进行遍历，遍历的每个元素都是一个二元组
for key,value in coursesdict.items():
    print(key,value)

print(type(coursesdict.items())) #dict_items 类型

#可以使用keys() 和 values() 分别只获取字典中的所有key 和 value 的列表
#这个两个方法返回的类型都可以使用for进行遍历

print(coursesdict)

print(coursesdict.keys())
print(coursesdict.values())

#pop（key）函数，可以返回key 对应的value,并将该key：value键值对删除
print(coursesdict.pop(2))
print(coursesdict)

#字典总结：dict 是无序的键值对集合。字典中的每一个元素都是一个key和一个value的组合
       #key值在字典中是必须唯一的，从字典中使用key获得对应的value的值
       #{} 会创建一个空字典，如果非空字典，大括号中的每个元素都是key:value
       #coursesdict = {1:'Liux',2:'Vim'}
       #coursesdict[1]
       #Linux
       #couesesdict[2]
       #Vim

       #字典key并不一定只有数字，可以使用各种不同的类型
       #testdict = {1:2,'testr':'shiyanlou.com',9:[1,2,3]}

       #如果key 不存在dict[key] 则会抛出KeyError，有点时候为了避免这种错误出现，
       #会使用get() 函数获取key对应的value ，如果此时key 不存在则默认返回None
       #也可以在get 函数中给定一个默认值，如果key不存在则返回默认值

       #coursesdict[2]
       #vim

       #coursesdict.get(4)
       #None

       #coursesdict.get(4,'default')
       #'default'

       #同set 一样字典也可以使用dict函数进行创建
       #参数是一个包含若干个二元组的元组
       #dict_from_tuple = dict((1,'Linux'),(2,'Vim'))
       #{1:'Linux',2:'Vim'}

       #字典是无序的，不能够通过索引进行访问。

       #向字典中增加元素的方法只需要为字典中的某个key 进行赋值，这个时候如果key存在
       #则是更新该key对应的value值
       #如果不存在则表示向字典中增加该key：value

       #从字典中删除一个元素，只要使用del 删除，如果key不存在则抛出keyError
       #del coursesdict[1]

       #KeyError:1

       #items() 函数获取所有的字典元素，返回得到的是dict_items 类型的对象
       #dict items 这个类型对象可以使用for进行遍历，遍历每个元素都是一个二元组
       # for key,value in coursesdict.items():
       #      print(key,value)

       #可以使用keys() 和 values() 分别只获取字典中的所有key或value的列表
       #coursesdict.keys()
       #dict_keys([2,5,6])

       #coursesdict.values()
       #dict_values(['Vim','Bash','Python'])

       #如上两个返回的类型都可以使用for 进行遍历。

       #pop（key） 函数，可以返回key 对应的value ，并将key:value 键值对删除
       #{2：'Vim',3：'Bash',4:'Python'}
       #coursesdict.pop(2)
       #Bash

       #列表：可修改有序的数据集合
       #元组：不可修改的有序数据集合
       #集合：无序的不重复的数据集合
       #字典：无序的存储key:value 键值对的数据集合


