# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 10:07:25 2020

@author: Young May

"""
'''
这一段主要负责文本规范化
'''
import nltk
import re
import string
from pprint import pprint

corpus = ["The brown fox wasn't that quick and he couldn't win the race",
          " Hey that's a great deal! I just bought a phone for $199",
          "@@ You'll (learn) a ***lot*** in the book, Python is an amazing language!@@"
          ]

'''
以下做的是把文本切成单词。
'''
def tokensize_text(text):
    sentences = nltk.sent_tokenize(text)
    word_tokens = [nltk.word_tokenize(sentence) for sentence in sentences]
    return word_tokens


token_list = [tokensize_text(text) for text in corpus]
# pprint (token_list)


'''
以下是删除特殊字符
'''
'''
在文本切分之后删除
'''
def remove_characters_after_tokenization(tokens):
    pattern = re.compile('[{}]'.format(re.escape(string.punctuation)))
    filtered_tokens = filter(None, [pattern.sub('', token) for token in tokens])
    return filtered_tokens


filtered_list_1 = [filter(None, [remove_characters_after_tokenization(tokens)for tokens in sentence_tokens]) for sentence_tokens in token_list]
'''
注意: Pyhton2.7 返回列表，Python3.x 返回迭代器对象
newlist = list(tmplist) 
改完了，但是改的还是有点莫名其妙
'''
#print(filtered_list_1)
newlist = list(filtered_list_1)
for n in newlist:
    res = list(list(n)[0])
    print(res)


'''
在文本切分之前删除
好像下面也有错
后面的就没抄了


def remove_characters_before_tokenization(sentence,keep_apostrophes=False):
    sentence=sentence.strip
    if keep_apostrophes:
        PATTERN=r'[?|$|&|*|@|(|)|~]' #add other characters here to remove them
        filtered_sentence=re.sub(PATTERN,r'',sentence)
    else:
        PATTERN=r'[^a-zA-Z0-9]' #only extract alpha-numeric characters
        filtered_sentence=re.sub(PATTERN,r'',sentence)
    return filtered_sentence
filtered_list_2=[remove_characters_before_tokenization(sentence) for sentence in corpus]

print(filtered_list_2)
'''

