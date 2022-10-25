# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import bs4 as bs
import urllib.request
import re
import nltk
nltk.download('punkt')
nltk.download('stopwords')
import bs4
import urllib.request
import requests
from bs4 import BeautifulSoup
from inscriptis import get_text
from googletrans import Translator

#Scrapea articulo de wikipedia
enlace = "https://en.wikipedia.org/wiki/Chatbot"
html = urllib.request.urlopen(enlace).read().decode('utf-8')
text = get_text(html)
article_text = text
article_text = article_text.replace("[ edit ]", "")
print("################")

from nltk import word_tokenize,sent_tokenize
#Removing Square Brackets and Extra spaces
article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
article_text = re.sub(r'\s+', ' ', article_text)

formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text)
formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)   

#EN ESTA PARTE SE HACE LA TOKENIZACION
sentence_list = nltk.sent_tokenize(article_text)    

#EN ESTA PARTE ENCUENTRA LA FRECUENCIA DE CADA PALABRA
stopwords = nltk.corpus.stopwords.words('english')   

word_frequencies = {}
for word in nltk.word_tokenize(formatted_article_text):
    if word not in stopwords:
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1

maximum_frequency = max(word_frequencies.values())

for word in word_frequencies.keys():
    word_frequencies[word] = (word_frequencies[word]/maximum_frequency)
    
#CALCULA LAS FRASES QUE MAS SE REPITEN
sentence_scores = {}
for sent in sentence_list:
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frequencies.keys():
            if len(sent.split(' ')) < 30:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]

#REALIZA EL RESUMEN CON LAS MEJORES FRASES
import heapq 
summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)

summary = ' '.join(summary_sentences)
print(summary)

#TRADUCIR RESUMEN
from googletrans import Translator

translator = Translator()
translated = translator.translate(summary)

print(translated.text)