# -*- coding: utf-8 -*-
# @Time : 2019-09-03 11:47
# @Author : cxa
# @File : sourcetest.py
# @Software: PyCharm
import ast

a = """
[
{
"Ip": "113.12.202.50",
"Port": 50327,
"Country": "广西南宁市",
"FullAddres": "电信",
"ProxyType": 1,
"Sec": 0,
"AnonymousType": 3
},
{
"Ip": "116.62.204.186",
"Port": 3128,
"Country": "浙江省杭州市",
"FullAddres": "阿里云",
"ProxyType": 0,
"Sec": 0,
"AnonymousType": 2
}]
"""
print(ast.literal_eval(a))
