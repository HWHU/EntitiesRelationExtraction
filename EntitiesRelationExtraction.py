# -*- coding: utf-8 -*-
#import urllib.request
import xml.dom.minidom
import xml.etree.cElementTree as ET
import csv

def parseXML(filename):
    DOMTree= xml.dom.minidom.parse(filename)
    PubmedArticleSet = DOMTree.documentElement
    return PubmedArticleSet
#url = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&query_key=1&WebEnv=NCID_1_2878613_165.112.9.28_9001_1460133461_281781643_0MetA0_S_MegaStore_F_1&rettype=xml"
#local_filename, headers = urllib.request.urlretrieve(url)

#filename = "C:/PythonProjects/git_EntityRelationExtraction/OpenData/EfetchResult_mini.xml"
filename = "C:/PythonProjects/git_EntityRelationExtraction/OpenData/EfetchResult.xml"
#filename = "C:/PythonProjects/git_EntityRelationExtraction/OpenData/test.xml"

#xmlData = parseXML(filename)
#pmids = xmlData.getElementsByTagName("PMID")  
#for pmid in pmids:
 #   print(pmid.getAttribute("Version"))
 #  print(pmid.getAttribute("Version=\"1\""))  

tree = ET.parse(filename)
root = tree.getroot()
#for node in root.iter():
#    print(node.tag, node.attrib)

#for node in root.findall(".//PMID[@Version='1']"):
#    print(node.tag, node.attrib)
    
#for pmid in root.iter('PMID'):
#    print(pmid.text)
try:    
    with open('./pubmedAbstractsWithID.csv', 'w', newline='') as csvfile:
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