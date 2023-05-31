import numpy as np
import matplotlib.pyplot as plt
#vnos polinomov, ki tvorita racionalno funkcijo
polinom1=[2,2,0]#polinom v števcu 
polinom2=[1,0,-5]#polinom v imenovalcu
nicle=np.roots(polinom1)#poišče ničle in pole
poli=np.roots(polinom2)
nicle=nicle[nicle.imag == 0]#odstrani kompleksne ničle in pole
poli=poli[poli.imag == 0]
print('Realne ničle:',nicle)
print('Realni poli:',poli)
stopnja1=len(polinom1)-1 #najde stopnjo polinoma
stopnja2=len(polinom2)-1
tocke=np.concatenate((nicle,poli))
if len(tocke)==1:
    t=int(tocke[0])
    x=np.linspace(t-10,t+10,100)
else:
    x=np.linspace(-10,10,100)
plt.plot(x,np.polyval(polinom1,x)/np.polyval(polinom2,x),'blue')
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(-10,10)
plt.scatter(nicle, np.zeros_like(nicle), color='red', label='ničle',s=5)#risanje ničel
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

