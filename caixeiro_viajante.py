
import random;
import matplotlib.pyplot as plt
import math

#
#  Passo 1 do AG, cria a populacao inicial
#

def criacaoCidades(qtdCidades,tamEspaco):
    cidades = [];
    for x in range(qtdCidades):
        cidadeEstaLista = False
        while not cidadeEstaLista:
          novaCidade = (random.randrange(tamEspaco),random.randrange(tamEspaco))
          cidadeEstaLista = novaCidade not in cidades
        cidades.append(novaCidade);
    return cidades;

def populacaoInicial(listaCidades,tamPopulacao):
    #Cria as cidades
    populacaoInicial = []
    for x in range(tamPopulacao):
        pop = random.sample(listaCidades,len(listaCidades))
        populacaoInicial.append(pop)
    return populacaoInicial

def calculoDistancia(cidadeA,cidadeB):
    distancia = math.sqrt(((cidadeB[0] - cidadeA[0])**2) + ((cidadeB[1] - cidadeA[1])**2))
    return distancia

def calculoPercurso(cidades):
    distancia = 0
    for c in range(len(cidades)):
        if c == len(cidades)-1:
            distancia = distancia + calculoDistancia(cidades[c],cidades[0])
        else:
            distancia = distancia + (calculoDistancia(cidades[c],cidades[c+1]))     
    return distancia

def avaliacao(populacao):
  fit = []
  for pop in populacao:
    fit.append(round(1/calculoPercurso(pop),6))
  return fit

def preservaMelhores(avaliacao,geracao,nova):
  qdeMelhores = round(len(geracao)/2)
  listaMelhores = sorted(range(len(avaliacao)), key=lambda i: avaliacao[i], reverse=True)[:qdeMelhores]
  for x in listaMelhores:
     nova.append(geracao[x])
   
 
def cruzamento(listaCidades, geracao, nova):
  qdeSaida = round(len(geracao)/2)-1
  tamMaxNova = len(nova) + qdeSaida
  while len(nova)<tamMaxNova:
    indexIndA = random.randrange(0,len(geracao));
    indexIndB = random.randrange(0,len(geracao));
    while indexIndA==indexIndB:
      indexIndB = random.randrange(0,len(geracao));
    
    indA = geracao[indexIndA]
    indB = geracao[indexIndB]

    corte = random.randrange(len(geracao)*0.6,len(geracao)-1);
    filho1 =  indA[:corte] + indB[corte:];
    filho2 =  indB[:corte] + indA[corte:];

    filho1 = corrigeCruzamento(listaCidades,filho1,corte)
    filho2 = corrigeCruzamento(listaCidades,filho2,corte)

    nova.append(filho1)
    if len(nova)<tamMaxNova:
      nova.append(filho2)
    
def corrigeCruzamento(listaCidades,individuo,corte):
    duplicados = [x for i, x in enumerate(individuo) if i != individuo.index(x)]
    faltantes = list(set(listaCidades)-set(individuo))
    indices = [individuo.index(x,corte) for x in duplicados]
    pos = 0
    for x in indices:
       individuo[x] = faltantes[pos]
       pos = pos+1
    return individuo

def mutacao(populacao, nova):
   individuo = random.choice(populacao)
   posicao1 = random.randrange(0,len(individuo))
   posicao2 = random.randrange(0,len(individuo))
   valorPos1 = individuo[posicao1]
   valorPos2 = individuo[posicao2]
   individuo[posicao1] = valorPos2
   individuo[posicao2] = valorPos1
   nova.append(individuo)
    

def plotaPercurso(cidades):
    x = [c[0] for c in cidades]
    y = [c[1] for c in cidades]
    
    plt.scatter(x,y, color="Red")
    plt.plot(x,y)

    plt.show()
    
qtdCidades = 100
tamEspaco = 100
tamPopInicial = 100
numGeracoes = 5000

random.seed(100)

listaCidades = criacaoCidades(qtdCidades,tamEspaco)
populacaoInicial = populacaoInicial(listaCidades,tamPopInicial)

geracao = populacaoInicial

for numGeracaoAtual in range(0,numGeracoes):
   nova = []
   avaliacaoGeracao = avaliacao(geracao)
   #Selecioná os 50% melhores
   preservaMelhores(avaliacaoGeracao,geracao,nova)
   #Cruzamento da população atual, gerando 50% - 1 novos indivíduos
   cruzamento(listaCidades, geracao, nova);
   #Mutação de 1 indivíduo aleatório da população atual
   mutacao(geracao, nova);
   
   ##Pegar o melhor valor da geração atual:
   indiceValorMax = avaliacaoGeracao.index(max(avaliacaoGeracao))
   valorMax = avaliacaoGeracao[indiceValorMax]
   individuoMax = geracao[indiceValorMax]  
   print(f'A melhor distância encontrada para a geração {numGeracaoAtual}: {valorMax}')
   print(f'O melhor percurso encontrado para a geração {numGeracaoAtual}: {individuoMax}')
   if (numGeracaoAtual == 0) or (numGeracaoAtual == numGeracoes-1):
      plotaPercurso(individuoMax)
   geracao = nova.copy()

   
