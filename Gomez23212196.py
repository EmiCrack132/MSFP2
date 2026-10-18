"""
Práctica 2: Modelado y control del sistema cardiovascular mediante
el modelo Windkessel.

Departamento de Ingeniería Eléctrica y Electrónica, Ingeniería Biomédica
Tecnológico Nacional de México [TecNM - Tijuana]
Blvd. Alberto Limón Padilla s/n, C.P. 22454, Tijuana, B.C., México

Nombre del alumno: Emiliano Gómez Quiroa
Número de control: 23212196
Correo institucional: l23212196@tectijuana.edu.mx

Asignatura: Modelado de Sistemas Fisiológicos
Docente: Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx
"""

# Librerías para cálculo numérico y generación de gráficas
import numpy as np
import math as m
import matplotlib.pyplot as plt
from scipy import signal
import control as ctrl
import pandas as pd

# Datos de la simulación
x0,t0,tend,dt,w,h=0,0,15,1E-3,7,3.5
#N=round(tend/dt)+1 #numero de iteraciones para la funcion de tranferencia
N=round((tend-t0)/dt)+1
t=np.linspace(t0,tend,N) #arreglo del tiempo
signals=['Individual','Hipotenso','Hipertenso']
u=np.array(pd.read_excel('signal.xlsx',header=None))
#u=np.reshape(signal.resample(u,len(t)),-1)
u=np.reshape(u,-1)

# Componentes del circuito RLC y función de transferencia
#Normotenso
Z,L,R,C=0.010,0.001,1.000,1.500
numN=[L*R,R*Z]
denN=[C*L*R*Z,L*(Z+R),R*Z]
sysN=ctrl.tf(numN,denN)

#Hipotenso
Z,L,R,C=0.010,0.001,1.000,3.500
numL=[L*R,R*Z]
denL=[C*L*R*Z,L*(Z+R),R*Z]
sysL=ctrl.tf(numL,denL)

#Hipertenso
Z,L,R,C=0.010,0.001,1.000,1.000
numH=[L*R,R*Z]
denH=[C*L*R*Z,L*(Z+R),R*Z]
sysH=ctrl.tf(numH,denH)

print(f"Función de tranferencia (Normotenso): {sysN}\n")
print(f"Función de tranferencia (Hipotenso): {sysL}\n")
print(f"Función de tranferencia (Hipertenso): {sysH}\n")

# Polos del sistema
LN=np.roots(denN)
LL=np.roots(denL)
LH=np.roots(denH)

print(f"Normotenso: Polos del sistema: L1={LN[0]:.3e}, L2={LN[1]:.3e}\n")
print(f"Hipotenso: Polos del sistema: L1={LL[0]:.3e}, L2={LL[1]:.3e}\n")
print(f"Hipertenso: Polos del sistema: L1={LH[0]:.3e}, L2={LH[1]:.3e}\n")

# Componentes del controlador
#Hipotenso
kP=174.4048
kI=15212.346
Cr=1E-6
Re=1/(Cr*kI)
Rr=kP*Re

numPIDL=[Rr*Cr,1]
denPIDL=[Re*Cr,0]
PIDL=ctrl.tf(numPIDL,denPIDL)
print(f"Hipotenso:\n")
print(f"El valor de la capacitancia Cr es de {Cr} Faradios.\n")
print(f"El valor de la capacitancia Re es de {Re} Ohms.\n")
print(f"El valor de la capacitancia Rr es de {Rr} Ohms.\n")
print(f"Funcion de transferencia del controlador PI: {PIDL}.\n")

#Hipertenso
kP=205.8701
kI=74187.5742
Cr=1E-6
Re=1/(Cr*kI)
Rr=kP*Re

numPIDH=[Rr*Cr,1]
denPIDH=[Re*Cr,0]
PIDH=ctrl.tf(numPIDH,denPIDH)
print(f"Hipertenso:\n")
print(f"El valor de la capacitancia Cr es de {Cr} Faradios.\n")
print(f"El valor de la capacitancia Re es de {Re} Ohms.\n")
print(f"Funcion de transferencia del controlador PI: {PIDH}.\n")

# Sistema de control en lazo cerrado
#Hipotenso
sysPIDL=ctrl.feedback(ctrl.series(PIDL,sysL),1,sign=-1)
print(f"Hipotenso: Función de transferencia del sistema de control de lazo cerrado: {sysPIDL}")

#Hipertenso
sysPIDH=ctrl.feedback(ctrl.series(PIDH,sysH),1,sign=-1)
print(f"Hipertenso: Función de transferencia del sistema de control de lazo cerrado: {sysPIDH}")

# Colores
clr1=np.array([0, 148, 18])/255
clr2=np.array([8, 135, 255])/255
clr3=np.array([235, 9, 9])/255


# Funciones del sistema en lazo abierto y lazo cerrado
def openloop(t,sys,u):
    _,PAu=ctrl.forced_response(sys,t,u,x0)
    return PAu

def closedloop(t,sysPID,u):
    _,PIDu=ctrl.forced_response(sysPID,t,u,x0)
    return PIDu


# Respuesta del sistema en lazo abierto y en lazo cerrado
for i in range(0,3):
    
    
    
    if i==0:
        fg=plt.figure(i+1)
        fg.set_size_inches(w,h)
        plt.rcParams['font.size']=11
        plt.rcParams['font.family']='serif'
        plt.rcParams['font.serif']=['Times New Roman']

        
        
        Normotenso=openloop(t,sysN,u)
        Hipotenso=openloop(t,sysL,Normotenso)
        Hipertenso=openloop(t,sysH,Normotenso)
        
        #plt.plot(t,u[:,i],'-',color=clr1,label='Ve(t)')
        plt.plot(t,Normotenso,'-',color=clr1,linewidth=.8,label='Pp(t): Normotenso')
        plt.plot(t,Hipotenso,'--',color=clr2,linewidth=.8,label='Pp(t): Hipotenso')
        plt.plot(t,Hipertenso,':',color=clr3,linewidth=.8,label='Pp(t): Hipertenso')
        plt.xlim(0,15);plt.xticks(np.arange(0,16,1))

    elif i==1:
        fg=plt.figure(i+1)
        fg.set_size_inches(w,h)
        plt.rcParams['font.size']=11
        plt.rcParams['font.family']='serif'
        plt.rcParams['font.serif']=['Times New Roman']

        
        plt.xlim(0,15);plt.xticks(np.arange(0,16,1))
        Normotenso=openloop(t,sysN,u)
        Hipotenso=openloop(t,sysL,u)
        HipotensoPID=closedloop(t,sysPIDL,Normotenso)

        plt.plot(t,Normotenso,'-',color=clr1,linewidth=.8,label=['Pp(t): Normotenso'])
        plt.plot(t,Hipotenso,'--',color=clr2,linewidth=.8,label=['Pp(t): Hipotenso (LA)'])
        plt.plot(t,HipotensoPID,':',color=clr3,linewidth=.8,label=['Pp(t): Hipotenso (LC)'])
        
    elif i==2:
        fg=plt.figure(i+1)
        fg.set_size_inches(w,h)
        plt.rcParams['font.size']=11
        plt.rcParams['font.family']='serif'
        plt.rcParams['font.serif']=['Times New Roman']

        
        plt.xlim(0,15);plt.xticks(np.arange(0,16,1))
        Normotenso=openloop(t,sysN,u)
        Hipertenso=openloop(t,sysH,u)
        HipertensoPID=closedloop(t,sysPIDH,Normotenso)

        plt.plot(t,Normotenso,'-',color=clr1,linewidth=.8,label=['Pp(t): Normotenso'])
        plt.plot(t,Hipertenso,'--',color=clr2,linewidth=.8,label=['Pp(t): Hipertenso (LA)'])
        plt.plot(t,HipertensoPID,':',color=clr3,linewidth=.8,label=['Pp(t): Hipertenso (LC)'])
        
    plt.ylim(-0.4,1.2); plt.yticks(np.arange(-0.4,1.3,0.2))
    plt.xlabel('t [S]')
    plt.ylabel('Vi(t) [V]')
    plt.legend(bbox_to_anchor=(0.5,1.15),loc='center',ncol=3,frameon=False)
    plt.show()
    fg.savefig(signals[i]+'_python.pdf',bbox_inches='tight')