# -*- coding: utf-8 -*-
# @Time    : 2020/1/31 下午 06:30
# @Author  : Young May

import nltk

'''
理解文本句法和结构
'''

'''
使用nltk获得POS标签
'''
sentence='the brown fox is quick and he is jumping over the lazy dog'
tokens=nltk.word_tokenize(sentence)


tagged_sent=nltk.pos_tag(tokens,tagset='universal')
print(tagged_sent)

'''
#使用pattern获得POS标签
'''
from pattern.en import tag
tagged_sent = tag(sentence)
print(tagged_sent)

'''
#建立自己的POS标签器
'''

from nltk.corpus import  treebank
data = treebank.tagged_sents()
train_data =data[:3500]
test_data=data[3500:]
print(train_data[0])

tokens=nltk.word_tokenize(sentence)
print(tokens)

from nltk.tag import  DefaultTagger
dt= DefaultTagger('NN')
print(dt.evaluate(test_data))
print(dt.tag(tokens))


from nltk.tag import  RegexpTagger
patterns = [
    (r'.*ing$','VBG'), #gerunds
    (r'.*ed$','VBD'),  #simple past
    (r'.es$','VBZ'),   #3rd singular present
    (r'.*ould$','MD'), #modals
    (r'.*s$','NN$'),   #possessive nouns
    (r'^-?[0-9]+(.[0-9]+)?$','CD'), #cardinal numbers
    (r'.*','NN')    #nouns default
]
rt=RegexpTagger(patterns)
print(rt.evaluate(test_data))

import nltk
from nltk.corpus import  treebank
from nltk.tag import UnigramTagger
from nltk.tag import  BigramTagger
from nltk.tag import  TrigramTagger

data = treebank.tagged_sents()
train_data =data[:3500]
test_data=data[3500:]
sentence='the brown fox is quick and he is jumping over the lazy dog'
tokens=nltk.word_tokenize(sentence)

ut=UnigramTagger(train_data)
bt=BigramTagger(train_data)
tt=TrigramTagger(train_data)

print(ut.evaluate(test_data))
print(ut.tag(tokens))

print(bt.evaluate(test_data))
print(bt.tag(tokens))

print(tt.evaluate(test_data))
print(tt.tag(tokens))



def combined_tagger(train_data,taggers,backoff=None):
    for tagger in taggers:
        backoff = tagger(train_data , backoff=backoff)
    return backoff

ct = combined_tagger(train_data,[UnigramTagger,BigramTagger,TrigramTagger],rt)

print(ct.evaluate(test_data))
print(ct.tag(tokens))


from nltk.classify import  NaiveBayesClassifier
from nltk.tag.sequential import  ClassifierBasedPOSTagger
nbt = ClassifierBasedPOSTagger(train=train_data,
                               classifier_builder=NaiveBayesClassifier.train)
print(nbt.evaluate(test_data))


