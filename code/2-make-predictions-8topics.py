# -*- coding: utf-8 -*-
"""
"Cross-Domain Topic Classification for Political Texts"
Moritz Osnabruegge, Elliott Ash, Massimo Morelli

This script predicts the topics of annotated speeches (8 topics).
"""


import os
import pandas as pd
import numpy as np
import sklearn
from sklearn.linear_model import LogisticRegression
import zipfile


#Specify working directory
os.chdir("")

directory = ".\\models\\"

for file in os.listdir(directory):
    if zipfile.is_zipfile(file): 
        with zipfile.ZipFile(file) as item: 
           item.extractall()  

data = pd.read_csv('.\\data\\target_corpus_example.csv', encoding='utf-8')
X = data['text']
 
vectorizer2 = pd.read_pickle('.\\models\\tfidf_8.pkl')

policy_prob = pd.read_pickle('.\\models\\logistic_model_8.pkl')

Xtfidf = vectorizer2.transform(X)

data['top_topic'] = policy_prob.predict(Xtfidf)
policy_probs = policy_prob.predict_proba(Xtfidf)

for i, topic in enumerate(policy_prob.classes_):
    data[topic] = policy_probs[:,i]

data.to_csv('.\\data\\target_corpus_8.csv', encoding="utf-8")