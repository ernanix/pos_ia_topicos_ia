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

d = int(input("Digite o valor de d:"))
coordenada_x = list(range((2*d)+1))
coordenada_y = funcao_triangular(d)

fig, ax = plt.subplots(figsize=(6, 3))
ax.set(xlim=(-1, (2*d)+1), ylim=(0, 1))
ax.scatter(x=0,y=0)
ax.scatter(x=d,y=0,label="b")
ax.scatter(x=d*2,y=0,label="c")

ax.plot(coordenada_x,coordenada_y)

ax.axvline(x = d,color = 'red', ymin=0,ymax=1)
plt.show()
