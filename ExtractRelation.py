# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 12:54:03 2016

@author: chyam
"""

import csv
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
import re

# A dictionary abstract_dict, where key=pmid, value=abstract
def AbstractsToDict(filename):
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            
            abstract_dict = {}
            for row in reader:
                pmid, abstract = row
                abstract_dict[pmid] = abstract
                #print(pmid, abstract_dict[pmid])
    except Exception as e:
        print(e)
    return abstract_dict

# Tokenize abstract into seperate sentences
# A dictionary sent_dict, where key=pmid, value=sentence_list
def TokeniseSentence(abstract_dict):
    sentence_dict = {}
    for a in abstract_dict:
        sentence_list = sent_tokenize(abstract_dict[a])
       # print(a)
       # print(abstract_dict[a])
        sentence_dict[a] = sentence_list
        #print(len(sentence_list))
    return sentence_dict

# Find the pair of miRNA and gene with known relationship
# TODO: find specific pair, now only finding anyword containint 'mir'
def findmiRNA(sentence_dict): #TODO
    for a in sentence_dict: # pubmed id = a 
       for s in sentence_dict[a]: # for each sentence in the abstract with pubmed id = a
           word_list = word_tokenize(s)
           for word in word_list:
               position = word.lower().find('mir') # may need to do the same for let-, lin-
               if position >= 0: # if found
                   print(word)

    
if __name__ == '__main__':
    
    filename = "./Data/pubmedAbstractsWithID_mini.csv"
    abs_dict = AbstractsToDict(filename)
    sent_dict = TokeniseSentence(abs_dict)
    findmiRNA(sent_dict) # TODO
#==============================================================================
# Description	Alias	Regular Expression Pattern
# ----------------------------------------------------------------------
# Digit sequences	D	(\d?\d*)
# Admissible hypens with a trailing space	Z	([\-]?[\-]*)
# Admissible hypens with a leading space	S	([\-]?[\-]*)
# 3-letter prefix for human followed by a 
# hyphen	Pref	([hH][sS][aA][\-])
# Non-specific miRNA mentions	miRNA	([mM][iI]([cC][rR][oO])+[rR]([nN][aA]s+)+)
# Let-7 miRNA mention	Let	([lL][eE][tT] S*[7]?\l+)
# Lin-4 miRNA mention	Lin	([lL][iI][nN] S*[4]?\l+)
# Oncomir miRNA mention	Onco	([oO][nN][cC][oO][mM][iI][rR])
# Admissible tilde and word boundaries	Cluster	(∼[\b]-[\b]-*)
# Admissible hyphen and separator and and 
# comma	Sep	( S*((and?, S,\/,)? S*)+)
# Admissible combination of upper and lower 
# case alphabets	UL	(?\l?\l+,?\u?\u+)
# Admissible alpha-numerical identifiers in
# specific miRNA mentions	AN	( UL((/, *and*, D+)? UL)+)
# Admissible alpha-numerical identifiers in
# oncomir mentions	Tail	( D( AN Cluster+,\- D AN+)+)
#==============================================================================
#==============================================================================
# Regular expression patterns	Description	Example of identified text
# --------------------------------------------------------------------------
# (Pref+(Lin,Let))	Detection of Lin and Let 
# variations of miRNAs	lin-4; hsa-let-7a-1
# (Pref+(miRNA, Onco)(S*Tail)(Sep Tail)*)	MiRNAs mentions for different 
# separators	hsa-mir-21/22; Oncomir-17∼92
# (Pref+(miRNA, Onco) S*(D(Z([/]Z)*)+) ([\,] 
# S*? (Pref+(miRNA, Onco) S*(D(Z([/]Z)*)+)*)))	Multiple miRNA mentions 
# occurring progressively	miR-17b, -1a; hsa-miR-21,22, 
# and hsa-miR-17
#==============================================================================
