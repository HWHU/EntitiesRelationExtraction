# EntitiesRelationExtraction
Extract relationship of two named entities, namely miRNA and gene from bio-medical journal articles. 

#### This is work in progress ...

This is example on how to:

1. Extract and process bio-medical freely available journal articles from PubMed.
2. Extract PubMed ID and associated Abstracts into a csvfile, which will serve as the database.
3. Extract named entities, namely miRNA and gene/protein from a sentence.
4. Entract word-based features for machine learning.
5. Train a model for predicting existance of a relationship between a pair of miRNA and gene/protein with new un-seen sentences from bio-medical journal articles. 

### Extract journal articles from PubMed

The NCBI provides an E-Utilities API to allow for databases and articles searches and donwloads. See this [NCBI's video] (https://www.youtube.com/watch?v=iCFVVexp30o&feature=youtu.be) for introduction.

In this example, the search criteria is:

`((miRNA[Title/Abstract] OR microRNA[Title/Abstract] OR micro RNA[Title/Abstract]) AND "english"[Language]) AND "journal article"[Publication Type] AND "loattrfree full text"[sb]`

If you would like an example on how to use the E-Utilities API, I have a simple Jupyter exmple [here] ().  Details on how to use E-Utilities can be found [here](http://www.ncbi.nlm.nih.gov/books/NBK25499/).

