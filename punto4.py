import numpy as np 
from math import exp 
from mathplotlib import pyplot as plt 

# Definición de varaibles
e0= 8.854e-12 #constante epsilon 
u0= 1.256e-6 #constante mu-0
pi= 3.1416
px= 1001  #valores en x
#py= 1001  #valores en y
xm= 500  #centro en x
#ym= 500  #centro en y 
#Hx= np.zeros((px,py) , dtype= "float64") 
Hy= np.zeros((1, px) , dtype= "float64") 
Ez= np.zeros((1, px) , dtype= "float64") 
freq= 10.3e9 #frecuencia en Hz
dx= 0.03   # dt=dx/c para guardar la relación corecta 
dt= 1e-10
dy= dt
Ttot= 100
c= 3e8 # velocidad de la luz 
xmax= 0.0254 # el lmite del cuadrado de plastico en m 
ymax= xmax 
#E0= 1

#definimos medio 1 y medio 2
medio1= (px*(xmax-(xmax/2)))
medio2=  medio1+ (xmax*px)

lol[:,1]= miu0 
lol[0: medio1,0]= epsilon0 
lol[medio1:medio2,0]= 12*epsilon0 
lol[medio2:px,0]= epsilon0 
 
#FDTD 1D
for n in range(0, Ttot+1):
    for x in range(0,(px - 1)):
         Hy[0,x] = Hy[0, x]+(dt/(u0)*(dx))*((Ez[0, x + 1] -Ez[0, x])/dy)
    #for y in range(0,(py-1)):
    #para calcular ez 
    for k in range(1, px):
        Ez[0,k] = Ez[0,k]+(dt/(e0)*(dx))*(Hy[0, k]- Hy[0, k-1])
    
for j in range(0, Ttot-1):
    #para el medio absorvente
    Ez[j+1,xmax] = Ez[j,xmax + 1]+((c*(dt-dx))/(c*(dt+dx)))* (Ez[j-1,xmax + 1] - Ez[j,xmax + 1]
    
# ingresamos el pulso 
#Ez[0,px]= sin(2*pi*freq*Ttot*dt)


#Profe no logré terminar y tampoco sé programar esto, lo siento ;c  
    

#x0=(np.linspace(-500,500, num= 1001))*dx
#plt.plot(x0, Ez[:,0])
#plt.ylabel('campo electrico [V/m]')
#plt.xlabel('distancia [m]')
#plt.show() 

#Hx[x,y] = Hy[x,y]+(dt/(u0))*((Ez[x + 1, y] -Ez[x,y])/dy)           
#calculo de ez 
    #for x in range(1,px): 
       # for y in range(1,py): 
        #    Ez[x,y] = Ez[x,y]+(dt/(e0))*((Hy[x,y])-Hy[x - 1,y])/dy)- ((Hx[x,y])-Hx[x,y -1])/dy)
