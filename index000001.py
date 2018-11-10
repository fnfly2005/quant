#!/usr/bin/python
#coding:utf-8
##################################
'''
Path: 
Description: 
Date: 
Version: v1.0
'''
##################################
import tushare as ts

df = ts.get_hist_data('sh',start='2018-09-01',end='2018-11-10',ktype='60')
print df
