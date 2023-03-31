import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
from scipy.cluster.hierarchy import dendrogram,linkage,ClusterWarning 
from warnings import simplefilter 


def vectorDistance(v1,v2): 
    soma=0 
    for i in range(0,len(v1)): 
        d=v1[i]-v2[i] 
        soma=soma+d*d 
    return np.sqrt(soma)

def calcDistance(mat): 
    nrows=len(mat) 
    ncols=len(mat[0]) 
    res=np.zeros((nrows,nrows)) 
    for i in range(0,nrows): 
        m1=mat[i] 
        for j in range(0,nrows): 
            if i!=j: 
                m2=mat[j]
                res[i][j]=vectorDistance(m1,m2) 
            else: 
                res[i][j]=0 
    return res

aux=list([(1,0,0),(0,1,0),(0,0,1)]) 
aux.append(tuple(np.random.random_sample(3,))) 
aux.append(tuple(np.random.random_sample(3,))) 
aux.append(tuple(np.random.random_sample(3,))) 

vetores=np.array(aux) 
print(vetores) 
centro=vetores.mean(axis=0) 
v_centro=vetores-centro 
print('centro','\n',centro) 

print(np.allclose(vetores,v_centro+centro))

#obter o plano para projeção ortogonal 
U,s,Vh=np.linalg.svd(vetores)
print('Variancia:',np.square(s)/np.square(s).sum()) 
W2=Vh.T[:,:2] 
v1_plano=Vh.T[:,0] 
v2_plano=Vh.T[:,1] 
projetados2d=v_centro.dot(W2) 
print(projetados2d)

#calculando o plano de projeção 
menor=np.min(vetores,axis=0)-1 
maior=np.min(vetores,axis=0)+1 
x1s=np.linspace(menor[0],maior[0],10) 
y1s=np.linspace(menor[1],maior[1],10) 
z1s=np.linspace(menor[2],maior[2],10) 
C=Vh 
R=C.T.dot(C) 
x1,x2=np.meshgrid(x1s,y1s) 
z=(R[0,2]*x1+R[1,2]*x2)/(1-R[2,2])

#tentando visualizar as projeções no espaço3d 
fig=plt.figure(figsize=(6,3.8)) 
ax=fig.add_subplot(111,projection='3d') 
ax.plot_surface(x1,x2,z,alpha=0.2,color="k") 

#pontos originais 
for v in vetores: 
    xs=np.linspace(0,v[0],10) 
    ys=np.linspace(0,v[1],10) 
    zs=np.linspace(0,v[2],10) 
    plt.plot(xs,ys,zs=zs) 
plt.show()

fig=plt.figure(figsize=(6,3.8)) 
ax=fig.add_subplot(111,aspect='equal') 
#pontos projetados 
for v in projetados2d: 
    xs=np.linspace(0,v[0],10) 
    ys=np.linspace(0,v[1],10) 
    ax.plot(xs,ys) 
ax.arrow(0,0,0,1,head_width=0.05, length_includes_head=True,head_length=0.1,fc='k',ec='k') 
ax.arrow(0,0,1,0,head_width=0.05, length_includes_head=True,head_length=0.1,fc='k',ec='k')
ax.grid(True) 
plt.show()

d=calcDistance(vetores) 
d1=calcDistance(projetados2d) 
print('original') 
print(d) 
print('projetada') 
print(d1)


simplefilter("ignore",ClusterWarning) 
Z1=linkage(d,'single') 
fig=plt.figure() 
dn=dendrogram(Z1) 
plt.show() 

Z2=linkage(d1,'single') 
fig=plt.figure() 
dn=dendrogram(Z1) 
plt.show()