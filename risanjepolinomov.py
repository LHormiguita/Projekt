import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter.ttk import *
from tkinter.simpledialog import askstring

def vnosi():#funkcija, ki se pokliče, ko se odpre glavno okno
    polinom=askstring("Risanje polinoma", "Napiši koeficiente polinoma, ločene s presledki", parent=okno,initialvalue='1 -2 1 0' )
    polinom=[int(i) for i in polinom.split()]
    pol=np.poly1d(polinom,False)#naredi polinom v splošni obliki
    print('Polinom:')
    print(pol)
    nicle=np.roots(polinom)#najde vse ničle
    nicle = nicle[nicle.imag == 0]#odstrani kompleksne ničle
    print('Realne ničle:',nicle)
    print('Začetna vrednost:',np.polyval(polinom,0))
    x=np.linspace(min(nicle)-5,max(nicle)+5,100)
    plt.plot(x,np.polyval(polinom,x))#nariše graf
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim(-10,10)
    plt.scatter(nicle, np.zeros_like(nicle), color='red', label='ničle',s=5)#označi ničle
    plt.axhline(0, color='black', linewidth=0.4)
    plt.axvline(0, color='black', linewidth=0.2)
    plt.show()
    
okno = Tk()#ustvari okno
okno.title('Graf polinoma')
okno.geometry("600x600")
okno.after(1,vnosi())
mainloop()
