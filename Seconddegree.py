# Resolution sur console de l"equation du second degree
# import math
# a = float(input("Entrer indice a"))
# b = float(input("Entrer indice b"))
# c = float(input ("Entrer indice c"))

# print("a =",a ,"b =",b,"c = ",c)


# delta = b * b - 4 * a * c

# print("delta =", delta)

# if delta==0:
#     x = -b / 2 * a
#     print("Solution Double racine x1 = x2 =",x)
# elif delta > 0:
#     racinedelta = math.sqrt(delta)
#     print("racine de delta = ",math.sqrt(delta))  
#     x1= -b - (racinedelta / 2 * a)
#     x2= -b + (racinedelta/ 2 * a)
#     print("Deux racines distincts : x1 = ",x1,", x2 = ",x2)
# else:
#     print("Impossible, Donc, solution vide")


# Interface Resolution de l"equation du second degree 
from tkinter import * 
import math  
 
 
def Second_Degree (): 
    
    a=float(A.get()) 
    b=float(B.get()) 
    c=float(C.get()) 
 
    #Calcul de la solution
    delta = b * b - 4*(a * c)
    deltalabel.configure(text = "delta = {}".format(delta))
 
    if delta == 0:
        x = -b / 2 * a
        racinedelta = math.sqrt(delta)
        labelpositif.configure(text="Une double racine x1 = x2 = {}".format(x))

    elif delta>0:
        racinedelta = math.sqrt(delta)
        x1 = (-b - racinedelta) / 2 * a
        x2 = (-b + racinedelta) / 2 * a
        labelpositif.configure(text="Deux racines distincts: x1 = {}".format(x1)+" et  x2 = {}".format(x2))
    else:
        labelpositif.configure(text="Solution impossible")
   
   
 
fenetre = Tk() 
fenetre.title("Calcul de l\"equation du Second degree") 
 
txt1=Label(fenetre, text="Entrer l'indice a:").grid(row=1, column=1) 
txt2=Label(fenetre, text="Entrer l'indice b:").grid(row=2, column=1) 
txt3=Label(fenetre, text="Entrer l'indice c:").grid(row=3, column=1)
Button(fenetre,text='Resoudre',command=Second_Degree).grid(row=4 , column=1) 
 
A=Entry(fenetre) 
B=Entry(fenetre) 
C=Entry(fenetre)
deltalabel = Label(fenetre) 
labelpositif = Label(fenetre)
 
A.grid(row=1, column=2) 
B.grid(row=2, column=2) 
C.grid(row=3, column=2)
deltalabel.grid(row=5, column=1) 
labelpositif.grid(row=6, column=2)
 
fenetre.mainloop()