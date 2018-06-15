#!/usr/bin/python
# -*- coding:UTF-8 -*-

def cal(n):
    sum = 0
    for i in range(n):
        for j in range(i+1):
            sum += n * (10 ** j)
    return sum

n = int(raw_input("input a number between 1 to 9:\n"))

print cal(n)
