import nltk 
import ssl
from nltk.tokenize import sent_tokenize,word_tokenize
import re
from unidecode import unidecode 
import numpy as np

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('punkt') 
nltk.download('stopwords')


sentences = ["Paulo gosta de batata doce",
             "Maria adora doces",
             "Paulo é vegetariano"]
sw = nltk.corpus.stopwords.words('portuguese')

def text_clean(raw_text): 
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

# Apresentar frases 
print(sentences) 
# Aplicar função no texto 
clean_sentences = [] 
for frase in sentences: 
  clean_sentences.append(text_clean(frase))

# Apresentar frases preprocessadas 
print(clean_sentences)


# cria os vetores 
def criaVetores(sentencas, words):
    res = list(sentencas)
    for i in range(0,len(sentencas)):
        s = nltk.word_tokenize(sentencas[i])
        nova = []
        for w in s:
            if w in words:
                nova.append( words.index(w) )
        res[i] = nova
    return res

def criaVocabulario(listaSentencas):
  listaPalavras = []
  for sentenca in listaSentencas:
     tokens = nltk.word_tokenize(sentenca)
     listaPalavras = listaPalavras + tokens
  listaPalavras = set(listaPalavras)    
  return sorted(listaPalavras)

palavras = criaVocabulario(clean_sentences)
print(palavras)
vetor = criaVetores(clean_sentences,palavras)
print(vetor)

matriz = np.array(vetor)
print(matriz)