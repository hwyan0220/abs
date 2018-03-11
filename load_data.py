#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 16:34:01 2018

@author: norman
"""
import pandas as pd
import numpy as np
import os
from urllib.request import urlretrieve


path = '/Users/norman/Desktop/abs'
os.chdir(path)
        
# url = 'http://www.abs.gov.au/ausstats/subscriber.nsf/log?openagent&816503.xls&8165.0&Data%20Cubes&194320433C31F92ECA25823A000AE7F6&0&Jun%202013%20to%20Jun%202017&20.02.2018&Latest'
# urlretrieve(url, '816503.xls')

file = '816503.xls'
usecols = list(range(9)) + list(range(10, 16)) + list(range(17, 23)) + list(range(24, 30)) + list(range(31, 37))

list_names = ['state', 'anzsic', 'anzsic_desc'] \
+ list(map(lambda x: 'fys_' + x, ['less_than_50k', 'less_than_200k', 'less_than_2m', 'less_than_5m', 'less_than_10m', '10m_or_more'])) \
+ list(map(lambda x: 'ent_' + x, ['less_than_50k', 'less_than_200k', 'less_than_2m', 'less_than_5m', 'less_than_10m', '10m_or_more'])) \
+ list(map(lambda x: 'exi_' + x, ['less_than_50k', 'less_than_200k', 'less_than_2m', 'less_than_5m', 'less_than_10m', '10m_or_more'])) \
+ list(map(lambda x: 'bal_' + x, ['less_than_50k', 'less_than_200k', 'less_than_2m', 'less_than_5m', 'less_than_10m', '10m_or_more'])) \
+ list(map(lambda x: 'fye_' + x, ['less_than_50k', 'less_than_200k', 'less_than_2m', 'less_than_5m', 'less_than_10m', '10m_or_more']))

df1 = pd.read_excel(file, sheetname = 'June 2017', skiprows = 6, skip_footer = 5, names = list_names, usecols = usecols).dropna(axis = 0)
df2 = pd.melt(df1, id_vars = ['state', 'anzsic', 'anzsic_desc'])
df2['status'] = df2.variable.str[:3]
df2['size'] = df2.variable.str[4:]
df2 = df2.drop(['variable'], axis = 1)
df2.columns = ['state', 'anzsic', 'anzsic_desc', 'num_biz', 'status', 'size']



print(df2.head(20))
print(df1.loc[9, :])
print(df1.tail(1))
print(df1.shape)
print(df1.columns)
print(df1.info())