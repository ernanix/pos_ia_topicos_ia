
import random;
import matplotlib.pyplot as plt
import math

#
#  Passo 1 do AG, cria a populacao inicial
#

def criacaoCidades(tamanho):
    cidades = [];
    for x in range(tamanho):
        cidades.append( (random.randrange(10),random.randrange(10)) );
    return cidades;

def populacaoInicial(qtdCidades,tamPopulacao):
    #Cria as cidades
    cidades = criacaoCidades(qtdCidades)
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

def cruzamento(pop, qdade, nova):
  qdeSaida = len(nova) + qdade
  while len(nova)<qdeSaida:
    indA = random.randrange(0,len(pop));
    indB = indA;
    while indA==indB:
      indB = random.randrange(0,len(pop));
    # adapta a escala de valores de -10:10 para 0:20
    p1 = pop[indA]+10
    p2 =  pop[indB]+10
    v1 = bit2vet( p1 );
    v2 = bit2vet( p2 );
    corte = random.randrange(28,31);
    novoV1 =  v1[0:corte];
    novoV1.extend( v2[corte:] );
    novoV2 =  v2[0:corte];
    novoV2.extend( v1[corte:] );
    # print( 'saida 1 (v1,corte,v2) ',v1[0:corte], v2[corte:])
    # print( 'saida 2 (v2,corte,v1) ',v2[0:corte], v1[corte:])
    v1num = bin2num(novoV1)-10;
    if v1num >= -10 and v1num<= 10:
      nova.append( v1num );
    if len(nova)<qdeSaida:
      v2num = bin2num(novoV2)-10;
      if v2num >= -10 and v2num<= 10:
        nova.append( v2num );
    

def mutacao(pop, qdade, novo):
  qdeSaida = len(novo) + qdade
  while len(novo)<qdeSaida:
    indA = random.randrange(0,len(pop));
    p1 = pop[indA]+10
    v1 = bit2vet( p1 );
    pos = random.randrange(27,32);
    if v1[pos] == 0:
      v1[pos] = 1;
    else:
      v1[pos] = 0;
    v1num = bin2num(v1)-10;
    if v1num>=-10 and v1num<=10:
      novo.append( v1num );

def plotaPercurso(cidades):
    x = [c[0] for c in cidades]
    y = [c[1] for c in cidades]
    
    plt.scatter(x,y, color="Red")
    plt.plot(x,y)

    plt.show()
    
qtdCidades = 6
tamPopInicial = 2
numGeracoes = 10

random.seed(10)

populacao0 = populacaoInicial(qtdCidades,tamPopInicial)
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
