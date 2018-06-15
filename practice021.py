#!/usr/bin/python

def cal(x):
    if (x - (x / 2 + 1)) == 1:
        print x
    else:
        cal(x - (x / 2 + 1))
total = 1
for i in range(10):
    total = total