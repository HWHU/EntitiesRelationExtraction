# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 12:54:03 2016

@author: chyam
"""

import csv

with open("./Data/pubmedAbstractsWithID_mini.csv", newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quote="\"")
    for row in reader:
        pmid, abstract = row        
        print(pmid, abstract)