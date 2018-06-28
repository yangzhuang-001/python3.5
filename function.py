#!/usr/bin/env python3
#函数：在一个程序里多次复用相同的代码
#在任何需要的时候调用它
#函数有参数和返回值，在函数内部对参数进行处理，并把处理结果返回给调用者

#内置函数

#函数的定义和调用
#使用关键字def 来定义一个函数，定义函数后需要在函数名的括号中写入参数，最后加：
#在换行输入函数内部的代码
#注意函数内部代码的缩进
#def functionname(params):
#    staticmethod
#    staticmethod

#写一个函数接受一个字符串和一个字母作为参数，并将字符串中出现的字母的数量作为返回值
#第二行的return 关键字，把str中包含char的次数返回给调用者
#def char_count(str,char):
 #   return str.count(char)

#使用函数
#result变量用来保存函数的返回值，传入的两个参数分别是用来检测字符串和字母
#result = char_count('shiyanlou','o')
#print(result)

#改变这个函数 char_count()函数，接受一个参数，并将所有的字母及出现的频次
#打印出来
'''def char_count(str):
    char_list = set(str)
    for char in char_list:
        print(char,str.count(char))
'''

#变量作用域：
'''def change():
    a = 90
    print(a)
a = 9
print(a)
change()
print(a)
'''
#global 关键字 ，对函数中的a标志为全局变量，让函数内部使用全局变量的a

a = 90
def change():
    global a
    print(a)


change()

#end='' 参数表示，print打印后的结尾不用换行，而用空格。
#（默认情况下print打印后会在结尾处换行）

#通过关键字global来告诉a 的定义是全局的。


#函数的参数
#常用的参数有两种：必选参数、默认参数、可变参数和关键字参数。
#以上四种参数可符合使用
#复合使用时各类参数的定义顺序必须同上。

#必选参数
#使用函数时必选参数可以不写参数名，但必须对其赋值，参数赋值顺序是定义的时候指定的
#所以必选参数又称为 位置参数。

#注意：如果不按照定义顺序传参，就要使用参数名进行传参。

#举例
def connect(ipaddress,port):
    print("IP:",ipaddress)
    print("port",port)

result = connect('192.168.1.1',22)
print(result)

result1 = connect(22,'192.168.1.1')
print(result1)

result2 = connect(port=22,ipaddress='192.168.1.1')
print(result2)

#上面例子中尝试了三次传参：第一次使用必选参数默认的顺序，结果正确。
#第二次使用错误的顺序，结果错误
#第三次虽然顺序错误但是使用了参数名传参，结果正确

#默认参数
#函数的参数可以设定默认值，这种参数称为默认参数。
#调用函数时，如果对默认参数没有赋值，则会自动赋值其默认值。

def connect1(ipaddress,port=22):
    print("IP:",ipaddress)
    print("Port",port)

result3 = connect1('192.168.1.12')
print(result3)

#注意：1.各类参数的顺序问题，默认参数后面不能再有必选参数
#例如 f(a,b=99,c) 就是错误的；

#2.默认参数的默认值必须设为不可变的数据类型（如 字符串、元组、数字、布尔值、None等）
#是错误的。

#错误的：
'''def f (a,data=[]):
  data.append(a)
  return data
'''

#避免默认参数的默认值必须设为不可变数据类型
def f (a,data=None):
    if data == None:
        data = []
    data.append(a)
    return data
#默认参数的默认值是不可变对象，所以无论执行多少次，默认值都不会变。


#可变参数:
#如果一个函数需要传入的参数数量是不固定的，可能是 0 个，也可能是N个，这种情况
#可以为函数设置一个可变参数。

#可变参数意味着参数的数量是可变的，调用函数时，在可变参数的位置传入一个元组或者
#任意数量的参数。

#可变参数的定义格式是在参数名前 加上 *，参数名可以自定义，通常写成 *args
#注意：在函数体内部使用该参数时，前面要加 *

#举例
def connect(ipaddress,*ports):
    print("IP:",ipaddress)
    for port in ports:
        print("Port:",port)

result4 = connect('192.168.1.16')
print(result4)

result5 = connect('192.168.18',22,23,24)
print(result5)

params = (22,23,24,25)
result6 = connect('192.168.120',params)
print(result6)

#调用含可变参数函数时，如果在可变参数的位置传入多个参数而不是元组，
#那么这些参数会自动生成一个元组传入函数。


#关键字函数



#if __name__ == '__main__':

