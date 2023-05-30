import numpy as np
import matplotlib.pyplot as plt
polinom=[2,4,0,-0]
nicle=np.roots(polinom)
nicle = nicle[nicle.imag == 0]
print('Realne ničle:',nicle)
print('Začetna vrednost:',np.polyval(polinom,0))
x=np.linspace(min(nicle)-5,max(nicle)+5,100)
plt.plot(x,np.polyval(polinom,x))
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(np.min(nicle), np.max(nicle))
#plt.ylim(np.min(np.polyval(polinom, x))+3, np.max(np.polyval(polinom, x))-3)
plt.ylim(-10,10)
plt.axis('equal')
plt.scatter(nicle, np.zeros_like(nicle), color='blue', label='ničle',s=5)
plt.axhline(0, color='black', linewidth=0.4)
plt.axhline(0, color='black', linewidth=0.2)




#razmak=(max(tocke)-min(tocke))
#print(razmak)




#plt.ylim(min (ra(polinom,x)) - y_margin,max (ra(polinom,x))  + y_margin)
#
plt.axis('equal')




plt.show()
