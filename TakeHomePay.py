#!/usr/bin/env python3
import sys
from  collections import namedtuple
#税后工资计算器
#16.5% 保险比例

Taxable_income_item = namedtuple(
     'Taxable_income_itrm',
     ['start_point','tax_rete','quick_subtractor']
)

QZ_start_point = 3500

QYtax_payable_Table = [
     Taxable_income_item(80000,0.45,13505),
     Taxable_income_item(55000,0.35,5505),
     Taxable_income_item(35000,0.30,2755),
     Taxable_income_item(9000,0.25,1005),
     Taxable_income_item(4500,0.2,555),
     Taxable_income_item(1500,0.1,105),
     Taxable_income_item(0,0.03,0)
]

#社保、公积金
Social_security = {
     'YL':0.08,
     'Yl':0.02,
     'SY':0.005,
     'GS':0.0,
     'Sy':0.0,
     'GJJ':0.06
}

#税后工资
def income_Bx_Gjj(income):
     #保险
     bX_money = income * sum(Social_security.values())
     #只交保险的工资
     real_incom = income - bX_money
     #应纳税所得额
     taxable_part = real_incom - QZ_start_point
     if taxable_part <= 0:
          return '0.00','{:.2f}'.format(real_incom)
     for item in QYtax_payable_Table:
          if taxable_part > item.start_point:
               tax = taxable_part * item.tax_rete - item.quick_subtractor
               return '{:.2f}'.format(tax),'{:.2f}'.format(real_incom - tax)



def main():
     for item in sys.argv[1:]:
         workNum_id,salary_String = item.split(':')
         try:
              salary = int(salary_String)
         except ValueError:
              print('Parameter Error')
         tax_home_pay = income_Bx_Gjj(salary)
         print('{}:{}'.format(workNum_id,tax_home_pay[1]))


if __name__ == '__main__':
     main()


#将计算好的税后工资列表与工号列表合并为字典输出（打印输出函数）


