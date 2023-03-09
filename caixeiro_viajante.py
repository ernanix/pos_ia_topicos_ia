
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

def populacaoInicial(qtdCidades,tamPopulacao,tamEspaco):
    #Cria as cidades
    cidades = criacaoCidades(qtdCidades,tamEspaco)
    populacaoInicial = []
    for x in range(tamPopulacao):
        pop = random.sample(cidades,len(cidades))
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


def preservaMelhor(geracao,nova):
  ava = avaliacao(geracao)
  maior = 0;
  for i in range(1,len(ava)):
    #print(f'comparando {maior} ({geracao[maior]} : {ava[maior]}) com {i} ({geracao[i]} :{ava[i]}) ')
    if ava[maior] < ava[i]:
      maior = i
  nova.append( geracao[maior] )
  #print('melhor: ', nova, geracao[maior])
  return geracao[maior]

def cruzamento(listaCidades, populacao, qdade, nova):
  qdeSaida = len(nova) + qdade
  while len(nova)<qdeSaida:
    indA = random.randrange(0,len(populacao));
    indB = indA;
    while indA==indB:
      indB = random.randrange(0,len(populacao));
    

    corte = random.randrange(len(indA)-10,len(indA)-1);
    filho1 =  indA[:corte] + indB[corte:];
    filho2 =  indB[:corte] + indA[corte:];

    filho1 = corrigeCruzamento(listaCidades,filho1,corte)
    filho2 = corrigeCruzamento(listaCidades,filho2,corte)

    nova.append(filho1)
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

def mutacao(populacao, qdade, nova):
  qdeSaida = len(nova) + qdade
  while len(nova)<qdeSaida:
    individuo = random.randrange(0,len(populacao))
    posicao1 = random.randrange(0,len(posicao1))
    posicao2 = random.randrange(0,len(posicao1))
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
    
qtdCidades = 6
tamEspaco = 10
tamPopInicial = 2
numGeracoes = 10

random.seed(10)

populacao0 = populacaoInicial(qtdCidades,tamPopInicial,tamEspaco)
avaliacao0 = avaliacao(populacao0)

geracao = populacao0

while numGeracoes > 0:
   nova = []
   preservaMelhor(geracao,nova)
   cruzamento(geracao, 3, nova);
   mutacao(geracao, 1, nova);
   numGeracoes=numGeracoes-1;  
   avaliacao = avaliacao(nova)    
   nova2 = sorted(zip(avaliacao,nova),reverse=True)
   geracao = [x for _,x in nova2]
   print( f'Geracao {numGeracoes} pop= {geracao}')

print(f'A melhor solucao encontrada: {geracao[0]}')
