import numpy as np
import matplotlib.pyplot as plt
polinom1=[1,0,1]
polinom2=[1,-3]
nicle=np.roots(polinom1)#poišče ničle
nicle=nicle[nicle.imag == 0]#odstrani kompleksne ničle
poli=np.roots(polinom2)
poli=poli[poli.imag == 0]
print('Realne ničle:',nicle)
print('Realni poli:',poli)
stopnja1=len(polinom1)-1 #najde stopnjo polinoma
stopnja2=len(polinom2)-1
tocke=np.concatenate((nicle,poli))
print(tocke)
if len(tocke)==1:
    t=int(tocke[0])
    x=np.linspace(t-10,t+10,100)
else:
    x=np.linspace(min(tocke)-1,max(tocke)+1,100)
plt.plot(x,np.polyval(polinom1,x)/np.polyval(polinom2,x),'blue')
for x in range(-2,3):
    print(np.polyval(polinom1,x)/np.polyval(polinom2,x))
plt.xlabel('x')
plt.ylabel('y')
#plt.xlim(min(tocke)-0.5, max(tocke)+0.5)
plt.ylim(-10,10)
#plt.ylim(-100,100)
#plt.axis('equal')
plt.scatter(nicle, np.zeros_like(nicle), color='red', label='ničle',s=5)#risanje ničel
poli=poli.astype(int)
for i in poli:
    plt.axvline(x=i, linestyle='--', color='green', label='pol')
if stopnja1<stopnja2:#risanje vodoravnih asimptot
    plt.axhline(y=0, linestyle='--', color='green', label='asimptota')
elif stopnja1==stopnja2:
    plt.axhline(y=polinom1[0]/polinom2[0], linestyle='--', color='green', label='asimptota')
elif stopnja1-stopnja2==1:
    posevna=(np.polydiv(polinom1,polinom2))[0]
    print(posevna)
    plt.plot(x,posevna[0]*x+posevna[1],'red',linestyle='--')#nariše poševno asimptoto

plt.axvline(0, color='black', linewidth=0.2)
plt.axhline(0, color='black', linewidth=0.2)
plt.show()
