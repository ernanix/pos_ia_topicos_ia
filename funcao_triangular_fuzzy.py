import matplotlib.pyplot as plt

def funcao_triangular(d):
  grau_pertinencia = []
  a = 0
  b = d
  c = d * 2

  for x in range((2*d)+1):
    if x >= a and x <b:
      grau_pertinencia.append((x-a) / (b-a))
    elif x >= b and  x < c:
      grau_pertinencia.append((c-x) / (c-b))
    else:
      grau_pertinencia.append(0)

  return grau_pertinencia

d = 10
coordenada_x = list(range((2*d)+1))
coordenada_y = funcao_triangular(d)

plt.plot(coordenada_x,coordenada_y)
plt.axvline(x = d,color = 'red')
plt.show()