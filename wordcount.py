#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'rongfudi636'
__mtime__ = '26/06/2017'
"""

import time
# from pyspark import SparkContext
# from operator import add
#
# sc = SparkContext('local', 'pyspark')
#
# text = sc.textFile("Shakespeare.txt")
# print(text)
#
#
# def tokenize(text):
#     return text.split()
#
#
# words = text.flatMap(tokenize)
# print(words)
# wc = words.map(lambda x: (x, 1))
# print(wc.toDebugString())
# counts = wc.reduceByKey(add)
# counts.saveAsTextFile('wc')
