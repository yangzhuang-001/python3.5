#!/usr/bin/env python3
import sys

#命令行参数（接收工资数额）
#salary 工资
#qiZheng 起征点
#taxIncome 应纳税所得额
#rate 税率
#taxPayable 应纳税额
taxIncome = 0
try :
    salaryList = sys.argv[1:]
    for salary in salaryList :
        if int(salary) <= 3500:
            taxPayable = int(salary)
        if int(salary) > 3500:
            taxIncome = int(salary) - 3500

except ValueError :
    print("Parameter Error")
    exit()

#应纳税额所得额 taxIncome
if taxIncome <= 1500 :
    taxPayable = taxIncome * 0.03
elif taxIncome > 1500 and taxIncome <= 4500 :
    taxPayable = taxIncome * 0.1 - 105
elif taxIncome > 4500 and taxIncome <= 9000 :
    taxPayable = taxIncome * 0.2 - 555
elif taxIncome > 9000 and taxIncome <= 35000 :
    taxPayable = taxIncome * 0.25 - 1005
elif taxIncome > 35000 and taxIncome <= 55000 :
    taxPayable = taxIncome * 0.3 - 2755
elif taxIncome > 55000 and taxIncome <= 80000 :
    taxPayable = taxIncome * 0.35 - 5505
else:
    taxPayable = taxIncome * 0.45 - 13505


print(format(int(taxPayable),'.2f'))


#if __name__=='__main__':

#实现个税计算器
#计算应纳税所得额


#判断应纳税所得额所在应纳税额区间，并计算，打印显示计算结果

