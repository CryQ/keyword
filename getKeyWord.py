#!/usr/bin/python
# -*- coding: utf-8 -*-

__doc__ = '''
使用jieba分词模块进行分词，统计各分词的出现频率，然后排序，
过滤一些介词（可在filterWord.py里面配置）
'''
import jieba
from filterWord import filerWordDict

def splitWord(word):
    seg_list = jieba.cut(word, cut_all=False)
    content = ",".join(seg_list)
    return content

#创建包含所有文档中出现的不重复词的列表
def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        #print document
        vocabSet = vocabSet | set(document)
        #print vocabSet

    return list(vocabSet)

def readData(filename):
    f = open(filename)
    content = ''.join(f.readlines())
    return content

if __name__ == '__main__':
    filterWordList = filerWordDict.values()
    text = readData('2.txt') #读取数据
    wordList = splitWord(text).split(',')
    a = {}

    for word in wordList:
        num = wordList.count(word)
        index = wordList.index(word)
        a[index] = num
    
    sortDict = sorted(a.iteritems(), key=lambda d:d[1], reverse = True )

    wordNum = 0
    for wlist in sortDict:
        if len(wordList[wlist[0]]) > 1:
            if wordList[wlist[0]] in filterWordList:
                continue
            wordNum = wordNum + 1
            print wordList[wlist[0]]
            if wordNum > 5:
                break
