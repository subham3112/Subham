# -*- coding: utf-8 -*-
"""ques1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WfDz4b5yj7EImUCKSpuv44a9P2jjdQRn
"""

def outerfunction(a,b):
    a = int(input("enter 1st number"))
    b = int(input("enter 2nd number"))
    def innerfunction(a,b):
        return a+b
    add = innerfunction(a,b)
    return add+5
result = outerfunction(5,6)
print(result)

