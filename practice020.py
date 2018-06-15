#!/usr/bin/python
#-*- coding:UTF-8 -*-

h = 100.0
sum = 0
for i in range(1,11):
    h = h / 2
    sum += h * 2
    if i == 10:
        print h
print sum