# -*- coding: utf-8 -*-
#import urllib.request
import csv
import xml.etree.cElementTree as ET

#Below is the url used to download EfetchResult.xml
#url = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&query_key=1&WebEnv=NCID_1_2878613_165.112.9.28_9001_1460133461_281781643_0MetA0_S_MegaStore_F_1&rettype=xml"

filename = "./Data/EfetchResult.xml"

tree = ET.parse(filename)
root = tree.getroot()

try:    
    with open('./Data/PubmedAbstractsWithID.csv', 'w', newline='') as csvfile:
        pubmedWriter = csv.writer(csvfile, delimiter=',')
        
        try:
            for pubmed_article in root.findall('PubmedArticle'):
                pmid = pubmed_article.find('MedlineCitation').find('PMID').text
                try:
                    abstract = pubmed_article.find('MedlineCitation').find('Article').find('Abstract').find('AbstractText').text
                    print(pmid)
                    pubmedWriter.writerow([pmid, abstract.encode("utf-8")]) 
                except Exception as e:
                    print("Error with Abstract: ", e)
                    
        except Exception as e:
            print("Error with PubmedArticle: ", e)
            
except Exception as e:
    print("Error with opening csvfile for writing: ", e)