# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 14:55:58 2021

@author: TOYGARTANYEL
"""

import collections

# def get_corpus for unigram
# We are taking the text and counting the each word in corpus.
# Change it to dict which looks like: 
# defaultdict(<class 'int'>, {'<s>': 3, 'I': 3, 'am': 2, 'Sam': 2, '</s>': 3, 
#             'do': 1, 'not': 1, 'like': 1, 'green': 1, 'eggs': 1, 'and': 1, 'ham': 1})
def get_corpus(filename):
    vocab = collections.defaultdict(int)
    with open(filename, "r", encoding='utf-8') as fhand:
        for line in fhand:
            words = line.strip().split() ## delete left and right spaces and split everyword line by line
            for word in words:
                vocab[''.join(list(word))] += 1  ## we count the words and take in list
    return vocab
            

def unigram_calc(corpus, word1):
    c_num = 0
    c_total = 0
    for word in corpus:
        c_total += corpus[word]
        if word == word1:
            c_num = corpus[word]
        
    return c_num/c_total
    


def bigram_calc(word1, word2):
    ## I can't use the get_corpus func here because it changes the queue of words 
    ## We should keep the original text for n-gram
    ## It only makes easy unigram calculations
    c_num = 0 
    c_denom = 0
    with open("mini_corpus.txt", "r", encoding='utf-8') as f:
        for line in f:
            c = 0
            words = line.split()
            for word in words:
                c+=1
                if word1 == word:
                    c_denom += 1
                if word1 == word and word2 == words[c]:
                    c_num += 1
    return c_num/c_denom
    

#main
corpus = get_corpus("mini_corpus.txt")
res = unigram_calc(corpus, "am")
print("Unigram res: ",res)

res = bigram_calc("<s>", "Sam" )
print("Bigram res: ",res)
