#!/user/bin/env python3
from math import pi
# calculate
result = 5 * 5 *pi
print(result)

a = 10
b = 10.6
c = True
d = None
'''
print(a,b,c,d)
print(type(a),a)
print(type(b),b)
print(type(c),c)
print(type(d),d)'''

#运算
e = a + b
print(e)

f = b/a
print(f)

g = b - a
print(g)

h = b * a
print(h)

aa = True and False
bb = True or False
cc = c and False
dd = c or False

print(aa,bb,cc,dd)

str1 = 'hello'
str2 = 'shiyanlou'
str3 = 'hello,\'shiyanlou\''
str4 = 'hello'
str5 = 'hello,"shiyanlou"'

print(str1,str2)
print(str3,str4)
print(str5)

#多行字符串
str6 = '''hello,
shiyanlou,python'''
print(str6)

# + 号 连接字符串
str7 = str1 +''+str2
print(str7)

#字符串使用数字进行索引，数字0作为第一个字符，数字-1 为最后一个字符
print(str1[0])
print(str1[-1])

#python3内置函数len()可以获得字符串的字符数量
print(len(str1))
print(len(str5))

#字符串常用方法 strip() 默认情况下会删除字符串首尾空格及换行等空白符
#split() 默认情况下会用空格将字符串中进行切分得到一个列表，传入参数的时候会用传入的参数对字符串进行切分。

str9 = str2.strip()
print(str9)

stra = str5.split()
print(stra)

strb = 'hello:louPlus'
strc = strb.split(':')
print(strc)

#控制结构
#input 函数 获取用户输入，input 中的参数字符串将输出到屏幕
a = int(input("please Enter :"))

if a > 10:
    print('a > 10')
elif a < 10:
    print('a < 10')
else:
    print('a = 10')

#考试成绩及格就给糖吃，考试成绩不及格就不给糖吃，没有参加考试的视为自动退出
b = int(input("please enter number:"))
if b > 60:
    print('有糖吃')
elif b < 60:
    print('没糖吃')
else:
    print('弃考')

#循环控制
#两种循环方式 一种 for, 一种 while

#for循环 依次取出一个列表中的项目，对列表进行遍历处理。
strlist = ['hello','shiyanlou','com']
for s in strlist:
    print(s)


#迭代一组数字列表，列表要满足一定规律，使用内置函数range()
for a in range(10):
    print(a)

#while循环: 使用一个表达式作为判断的条件，如果条件不能达成则停止循环。
w = 100
while w > 10:
    print(w)
    w -= 10

#break 和 continue 两个关键字，break 表示停止当前循环，continue 跳过当前循环轮次中的代码，去执行下一循环轮次。

for c  in range(10):
    if c == 5:
        break
    print(c)

for d in range(20):
    if d == 2:
        continue
    print(d)


e = 100
while e > 10:
    e -= 10
    if e == 50:
        continue
    print(e)

#异常处理

filename = input("enter file path:")
f = open(filename)
print(f.read())
