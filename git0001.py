#! /usr/bin/env python
# -*- coding:utf-8 -*-

from string import ascii_letters, digits
from random import choice

str = ascii_letters + digits


def generate(length):
    coupon_code = ""
    for j in range(length):
        coupon_code += choice(str)
    yield coupon_code


if __name__ == "__main__":
    for i in range(10):
        for code in generate(20):
            print (code)
