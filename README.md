# Cross-Domain Topic Classification for Political Texts

This repository includes scripts and models used in the paper:

Osnabrügge, Moritz, Ash, Elliott and Morelli, Massimo. 2021. "Cross-Domain Topic Classification for Political Texts". Political Analysis, 1-22, doi: https://doi.org/10.1017/pan.2021.37.

The material can be used to predict the topics of texts. 

The folder "models" includes the models trained using the 44-topic and the 8-topic specifications as well as the files on the vocabulary:
- "logistic_model_44.pkl"
- "logistic_model_8.pkl"
- "tfidf_44.pkl"
- "tfidf_8.pkl"

The folder "code" includes scripts to predict the topics of a text based on these models. In the paper, we use the trained models to predict the topics of parliamentary speeches. However, the trained models can also be applied to other texts:
- "0-extract": a python script to extract the files from the zip folders
- "1-make-predictions-44topics": a python script to predict the topics of the text, 44 topics
- "2-make-predictions-8topics": a python script to predict the topics of the text, 8 topics

The folder "data" includes a dataset with parliamentary speeches:
- "target_corpus_example.csv": This file includes a corpus with parliamentary speeches

The full replication materials can be found here:
https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/CHTWUB
