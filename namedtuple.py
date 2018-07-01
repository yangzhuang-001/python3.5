#!/usr/bin/env python3
from collections import namedtuple
#测试学习namedtuple
fruit = namedtuple('fruit',['fruitName','fruitNum','fruitSalary'])

buy_fruit = [
    fruit('apple',0.45,13.5),
    fruit('banana',0.55,23),
    fruit('orange',0.56,25)
    ]

for item in buy_fruit:
    result = item._make(item)
    print(result)