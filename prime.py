#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'rongfudi636'
__mtime__ = '26/06/2017'
"""
import time
from pyspark import SparkContext

sc = SparkContext('local', 'pyspark')


def isprime(n):
    """
    check if integer n is a prime
    """
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2:
        return True
    # all other even numbers are not primes
    if not n & 1:
        return False
    # range starts with 3 and only needs to go up the square root of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

start = time.time()
nums = sc.parallelize(xrange(1000000))
result = nums.filter(isprime).count()
end = time.time()
print("primes total:{}, cost: {}s".format(result, end-start))
total = 0
for i in xrange(1000000):
    if isprime(i):
        total += 1
print("primes total:{}, cost: {}s".format(total, time.time()-end))