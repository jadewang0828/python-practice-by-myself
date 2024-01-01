# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 04:32:49 2024

@author: User
"""

import random

list_1=list()
list_2=list()
list_3=list()
for i in range(10):
    a=random.randint(1, 100)
    list_1.append(a)
    list_2=list_1.copy()
    while a in list_2:
        for j in range(10):
            a=random.randint(1, 100)
        list_3.append(a)
        
print(list_1)
print(list_3)
set_1=set(list_1)
set_2=set(list_3)
print("交集為:",set_1&set_2)
print("聯集為:",set_1.union(set_2))
print("差集為:",set_2-set_1)
print("對稱差集為:",set_1^set_2)
