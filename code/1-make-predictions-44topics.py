# -*- coding: utf-8 -*-
"""
"Cross-Domain Topic Classification for Political Texts"
Moritz Osnabruegge, Elliott Ash, Massimo Morelli

This script predicts the topics of the annotated speeches (44 topics).
"""


import os
import pandas as pd
import numpy as np


#Specify working directory
os.chdir("")

data = pd.read_csv('.\\data\\target_corpus_example.csv', encoding='utf-8')
X = data['text']

vectorizer1 = pd.read_pickle('.\\models\\tfidf_44.pkl')

policy_prob = pd.read_pickle('.\\models\\logistic_model_44.pkl')

Xtfidf = vectorizer1.transform(X)

data['top_topic'] = policy_prob.predict(Xtfidf)
policy_probs = policy_prob.predict_proba(Xtfidf)

for i, topic in enumerate(policy_prob.classes_):
    data[topic] = policy_probs[:,i]
    
data.to_csv('.\\data\\target_corpus_44.csv', encoding="utf-8")
