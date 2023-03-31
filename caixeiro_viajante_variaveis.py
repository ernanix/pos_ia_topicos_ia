
import random;
import matplotlib.pyplot as plt
import math

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

#Cálculo da distância entre duas cidades
def calculoDistancia(cidadeA,cidadeB):
    distancia = math.sqrt(((cidadeB[0] - cidadeA[0])**2) + ((cidadeB[1] - cidadeA[1])**2))
    return distancia

#Cálculo do percurso total (passa por todas as cidades e retorna para cidade inicial)
def calculoPercurso(cidades):
    distancia = 0
    for c in range(len(cidades)):
        if c == len(cidades)-1:
            distancia = distancia + calculoDistancia(cidades[c],cidades[0])
        else:
            distancia = distancia + (calculoDistancia(cidades[c],cidades[c+1]))     
    return distancia

#Avaliação de cada indivíduo da população (inverso da distância)
def avaliacao(populacao):
  fit = []
  for pop in populacao:
    fit.append(round(1/calculoPercurso(pop),8))
  return fit

#Seleciona os melhores de acordo com o rank baseado no cálculo da avaliação
def preservaMelhores(avaliacao,geracao,nova):
  qdeMelhores = round(len(geracao)*0.3)
  listaMelhores = sorted(range(len(avaliacao)), key=lambda i: avaliacao[i], reverse=True)[:qdeMelhores]
  for x in listaMelhores:
     nova.append(geracao[x])
   
#Cruza 2 indivíduos, gerando metade menos 1 novos indivíduos 
def cruzamento(listaCidades, geracao, nova):
  qdeSaida = round(len(geracao)*0.7)-2
  tamMaxNova = len(nova) + qdeSaida
  while len(nova)<tamMaxNova:
    indexIndA = random.randrange(0,len(geracao));
    indexIndB = random.randrange(0,len(geracao));
    while indexIndA==indexIndB:
      indexIndB = random.randrange(0,len(geracao));
    
    indA = geracao[indexIndA]
    indB = geracao[indexIndB]
    rangeIni = round(len(geracao)*0.5)
    rangeFim = len(geracao)-1
    corte = random.randrange(rangeIni,rangeFim);
    filho1 =  indA[:corte] + indB[corte:];
    filho2 =  indB[:corte] + indA[corte:];

    filho1 = corrigeCruzamento(listaCidades,filho1,corte)
    filho2 = corrigeCruzamento(listaCidades,filho2,corte)

    nova.append(filho1)
    if len(nova)<tamMaxNova:
      nova.append(filho2)

#Corrige os filhos gerados no cruzamento, para que não tenham cidades duplicadas    
def corrigeCruzamento(listaCidades,individuo,corte):
    duplicados = [x for i, x in enumerate(individuo) if i != individuo.index(x)]
    faltantes = list(set(listaCidades)-set(individuo))
    indices = [individuo.index(x,corte) for x in duplicados]
    pos = 0
    for x in indices:
       individuo[x] = faltantes[pos]
       pos = pos+1
    return individuo

#Mutação de um indivíduo da população trocando a posição de duas cidades
def mutacao(populacao, nova):
   while len(nova) < len(populacao):
      individuo = random.choice(populacao)
      posicao1 = random.randrange(0,len(individuo))
      posicao2 = random.randrange(0,len(individuo))
      valorPos1 = individuo[posicao1]
      valorPos2 = individuo[posicao2]
      individuo[posicao1] = valorPos2
      individuo[posicao2] = valorPos1
      nova.append(individuo)
    
#Representação gráfica do percurso
def plotaPercurso(cidades,numGeracao):
    x = [c[0] for c in cidades]
    y = [c[1] for c in cidades]
    
    distancia = calculoPercurso(cidades)

    x.append(x[0])
    y.append(y[0])

    plt.suptitle(f'Gráfico de representação do melhor percurso: Geração {numGeracao}')
    plt.title(f'Distância Percorrida:{round(distancia,5)}')
    plt.scatter(x,y, color="Red")
    plt.plot(x,y)

    plt.show()


######### Início ##############
#Parâmetro 1 - Quantidade de cidades
qtdCidades = 100
#Parâmetro 2 - Tamanho do espaço no plano cartesiano (x,y)
tamEspaco = 100
#Parâmetro 3 - Tamanho da população inicial
tamPopInicial = 1000
#Parâmetro 4 - Número de gerações
numGeracoes = 15000

random.seed(1400)

#Criação das cidades
listaCidades = criacaoCidades(qtdCidades,tamEspaco)
#Gera população inicial
populacaoInicial = populacaoInicial(listaCidades,tamPopInicial)

geracao = populacaoInicial

for numGeracaoAtual in range(0,numGeracoes):
   nova = []
   #Gera array com as avaliações de cada indivídul
   avaliacaoGeracao = avaliacao(geracao)
   #Seleciona os 50% melhores
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
   #print(f'O melhor percurso encontrado para a geração {numGeracaoAtual}: {individuoMax}')
   if (numGeracaoAtual == 0) or (numGeracaoAtual == numGeracoes-1):
      plotaPercurso(individuoMax,numGeracaoAtual)
   geracao = nova.copy()

   
