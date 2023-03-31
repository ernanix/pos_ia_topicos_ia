# -*- coding: utf-8 -*-
"""Topicos_IA_atividade3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aV3pusTzC0q0SSM_nFLdhQHRZGY0w6C6
"""

#Imports
from gensim.models import Word2Vec
import pandas as pd
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import sent_tokenize,word_tokenize
import numpy as np
import re
from unidecode import unidecode 
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

#Função de pré-processamento das sentenças 
def limpar_texto(raw_text): 
  # Remover acentos e padronizar em lower 
  clean_text = unidecode(raw_text.lower()) 
  # Substituir quebras e tabulações por espaços 
  clean_text = re.sub('[\n\t]', " ", clean_text) 
  # Manter somente caraceteres alfanumericos 
  clean_text = re.sub('[^ a-zA-Z]+', "", clean_text) 
  # Remover stopwords e juntar palavras 
  resultwords = [word for word in clean_text.split() if word not in sw] 
  clean_sw_text = ' '.join(resultwords) 
  return(clean_sw_text)

#Texto usado para a atividade
leminski = "O sentido, acho, é a entidade mais misteriosa do universo.\
            Relação, não coisa, entre a consciência, a vivência e as coisas e os eventos.\
            O sentido dos gestos. O sentido dos produtos. O sentido do ato de existir.\
            Me recuso a viver num mundo sem sentido.\
            Estes anseios/ensaios são incursões em busca do sentido.\
            Por isso o próprio da natureza do sentido: ele não existe nas coisas, tem que ser buscado, numa busca que é sua própria fundação.\
            Só buscar o sentido faz, realmente, sentido.\
            Tirando isso, não tem sentido."

#Tokeniza texto em sentenças
sentencas = sent_tokenize(leminski, language='portuguese')

#Lista de stopwrds da língua portuguesa
sw = nltk.corpus.stopwords.words('portuguese')

# Apresentar frases
print("----------------------------")
print("Sentenças do texto:") 
print(sentencas) 

# Aplicar função nas sentenças 
sentencas_limpas = [] 
for frase in sentencas: 
  sentencas_limpas.append(limpar_texto(frase))

# Apresentar frases preprocessadas
print("----------------------------")
print("Sentenças preprocessadas:")  
print(sentencas_limpas)

#Tokeniza senteças em palavras
tokens = [word_tokenize(palavras) for palavras in sentencas_limpas]

#Cria o modelo
modelo = Word2Vec(tokens,vector_size=50,min_count=1)

#Lista de palavras
palavras_vetor = sorted(list(modelo.wv.index_to_key))
print("----------------------------")
print("Lista de palavras:") 
print(palavras_vetor)

X=modelo.wv[palavras_vetor]
print("----------------------------")
print("Vetor:") 
print(X)

#Aplica o flatten no vetor através do PCA e apresenta graficamente o resultado
pca = PCA(n_components=2) 
resultado = pca.fit_transform(X) 
print("----------------------------")
print("PCA:") 
print(resultado)

plt.scatter(resultado[:, 0], resultado[:, 1])

for i, palavra in enumerate(palavras_vetor):
   plt.annotate(palavra, xy=(resultado[i, 0], resultado[i, 1]))

plt.show()