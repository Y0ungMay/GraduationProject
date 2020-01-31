# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 10:09:28 2020

@author: Young May
"""
'''
这是句子切分
'''
import nltk

from nltk.corpus import gutenberg

from pprint import pprint

alice = gutenberg.raw(fileids='carroll-alice.txt')

print (len(alice))

print(alice[0:100])

default_st = nltk.sent_tokenize
alice_sentences = default_st(text=alice)
print("Total sentences in alice:",len(alice_sentences))
print("first 5 sentences in alice:")
pprint(alice_sentences[0:5])