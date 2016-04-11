# EntitiesRelationExtraction
Extract relationship of two named entities, namely miRNA and gene from bio-medical journal articles. 

#### This is work in progress ...

This is example on how to:

1. Extract and process bio-medical freely available journal articles from PubMed.
2. Extract PubMed ID and associated Abstracts into a csvfile, which will serve as the database.
3. Extract named entities, namely miRNA and gene/protein from a sentence.
4. Entract word-based features for machine learning.
5. Train a model for predicting existance of a relationship between a pair of miRNA and gene/protein with new un-seen sentences from bio-medical journal articles. 

### 1. Extract journal articles from PubMed

The NCBI provides an E-Utilities API to allow for databases and articles searches and donwloads. See this [NCBI's video] (https://www.youtube.com/watch?v=iCFVVexp30o&feature=youtu.be) for introduction.

In this example, the search criteria is:

`((miRNA[Title/Abstract] OR microRNA[Title/Abstract] OR micro RNA[Title/Abstract]) AND "english"[Language]) AND "journal article"[Publication Type] AND "loattrfree full text"[sb]`

If you would like an example on how to use the E-Utilities API, I have a simple Jupyter exmple [Retreiving Abstracts from PubMed.ipynb] (https://github.com/ryubidragonfire/EntitiesRelationExtraction/).  Details on how to use E-Utilities can be found [here](http://www.ncbi.nlm.nih.gov/books/NBK25499/).

By using the search criteria above togheter with the E-Utilities API using `esearch` , an xml file [ResultFromESearch.xml] (https://github.com/ryubidragonfire/EntitiesRelationExtraction/tree/master/NCBI/) containing `WebEnv` is returned. Then use `efetch` to downlown all the journal articles where their PubMed IDs are stored in `WebEnv` :

`http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&query_key=1&WebEnv=NCID_1_2878613_165.112.9.28_9001_1460133461_281781643_0MetA0_S_MegaStore_F_1&retmode=xml`

The result is our raw data in [EfetchResult.zip] (https://github.com/ryubidragonfire/EntitiesRelationExtraction/tree/master/Data/). For convenience, [EfetchResult_mini.xml] (https://github.com/ryubidragonfire/EntitiesRelationExtraction/tree/master/Data/) is a subset of that .zip file which contains only 2 records, should you need to have a peek without unzipping the larger file.

### 2. Extract PubMed ID and Abstracts from data downloaded from NCBI

The only elements from raw data that we are interested in for this example are: PubMed ID and the associated Abstract. The text in abstracts will be served as the data for the machine learning task of entities relation recognition. This can be done using [ExtractPubMedIDAbstract.py] (https://github.com/ryubidragonfire/EntitiesRelationExtraction/). Don't forget to unzip the raw data [EfetchResult.zip] (https://github.com/ryubidragonfire/EntitiesRelationExtraction/tree/master/Data/).

