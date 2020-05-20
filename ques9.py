# -*- coding: utf-8 -*-
"""ques9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UZYyMXLoF6eNirl0SOTETP3gldvlw6C7
"""

import pandas as pd
df = pd.read_csv("diamonds.csv")
print("total count in terms of cut")
print(pd.value_counts(df['cut']))
print("maximum rate per cut as follows")
print(df.groupby('cut').price.max())
print("minimum rate per cut as follows" )
print(df.groupby('cut').price.min())

