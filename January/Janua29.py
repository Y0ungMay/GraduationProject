# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 10:07:25 2020

@author: Young May

"""

import nltk
import re
import string
from pprint import pprint

corpus = [ "The brown fox wasn't that quick and he couldn't win the race",
          " Hey that's a great deal! I just bought a phone for $199",
          "@@ You'll (learn) a ***lot*** in the book, Python is an amazing language!@@"
        ]

def tokensize_text(text):
    sentences = nltk.sent_tokenize(text)
    word_tokens = [nltk.word_tokenize(sentence) for sentence in sentences]
    return word_tokens

token_list = [ tokensize_text(text) for text in corpus]
#pprint (token_list)
'''
以上，做的是把文本切成单词。
'''

def remove_characters_after_tokenization(tokens):
    pattern = re.compile('[{}]'.format(re.escape(string.punctuation)))
    filtered_tokens=filter(None,[pattern.sub('',token) for token in tokens])
    return filtered_tokens

filtered_list_1 = [filter(None,[remove_characters_after_tokenization(tokens) for tokens in sentence_tokens]) for sentence_tokens in token_list]
'''
注意: Pyhton2.7 返回列表，Python3.x 返回迭代器对象
newlist = list(tmplist)
'''
print(filtered_list_1)
newlist=list(filtered_list_1)
print(newlist)