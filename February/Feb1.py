# -*- coding: utf-8 -*-
# @Time    : 2020/2/1 上午 11:34
# @Author  : Young May

'''
浅层分析
'''
sentence='the brown fox is quick and he is jumping over the lazy dog'

from pattern.en import parsetree

tree = parsetree(sentence)
print(tree)