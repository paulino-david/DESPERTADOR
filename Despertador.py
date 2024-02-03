import win32com.client as wnclient
from tkinter import *
import time as time

parred= Tk()
parred.geometry("550x500")
parred.resizable(False,False)
parred.title("DEPERTADORA")
parred.config(bg="grey")

hovar=IntVar()
minvar=IntVar()
motext=StringVar()
menuvar1=StringVar()
menuvar2=StringVar()
rep=StringVar()

cantidad=None
def repeticiones(veces):
    global cantidad
    cantidad=veces

tipos=None
def despertar(tipo):
    global tipos
    tipos=tipo

def listo():
    hora_s=hovar.get()*3600
    minuto_s=minvar.get()*60
    calculo=sum([hora_s,minuto_s])
    motget=motext.get()
    parred.destroy()
    #time.sleep(calculo)
    numero=0
    config=wnclient.Dispatch("SAPI.spvoice")
    while numero!= cantidad:
        hablar=config.Speak(tipos)
        numero+=1
    
    
frame=Frame(parred,width=500,borderwidth=5,height=200,relief="raised",bg="lightgrey").place(x=20,y=20)
hora=Spinbox(frame,from_=00,to=23,width=5,borderwidth=1,textvar=hovar).place(x=180,y=100)
separador=Label(frame,text=":",font=16,bg="lightgrey").place(x=240,y=100)
minutos=Spinbox(frame,from_=00,to=59,width=5,borderwidth=1,textvar=minvar).place(x=260,y=100)

motivo=Entry(parred,width=70,borderwidth=1,bg="lightgrey",textvar=motext).place(x=20,y=250)

dias=Label(parred,text="Dias: ",font=12,bg="grey",fg="lightblue").place(x=20,y=300)
dia1=Checkbutton(parred,text="Lunes",bg="grey",fg="lightblue").place(x=60,y=300)
dia2=Checkbutton(parred,text="Martes",bg="grey",fg="lightblue").place(x=120,y=300)
dia3=Checkbutton(parred,text="Miercoles",bg="grey",fg="lightblue").place(x=190,y=300)
dia4=Checkbutton(parred,text="Jueves",bg="grey",fg="lightblue").place(x=270,y=300)
dia5=Checkbutton(parred,text="Viernes",bg="grey",fg="lightblue").place(x=335,y=300)
dia6=Checkbutton(parred,text="Sábado",bg="grey",fg="lightblue").place(x=400,y=300)
dia7=Checkbutton(parred,text="Domingo",bg="grey",fg="lightblue").place(x=470,y=300)

repeticion=Label(parred,text="Repeticiones: ",font=12,bg="grey",fg="lightblue").place(x=20,y=350)
veces=Menubutton(parred,text="Haga click aquí para seleccionar las veces que quiera",bg="grey",fg="lightblue")
veces.place(x=130,y=350)
veces.repeticiones=Menu(veces,tearoff=0)
veces["menu"]=veces.repeticiones

veces.repeticiones.add_command(label="Sin falta",command=lambda:repeticiones(1))
veces.repeticiones.add_command(label="5 veces",command=lambda:repeticiones(5))
veces.repeticiones.add_command(label="10 veces",command=lambda:repeticiones(10))
veces.repeticiones.add_command(label="20 veces",command=lambda:repeticiones(20))

despertadora=Label(parred,text="Depertadora: ",font=12,bg="grey",fg="lightblue").place(x=20,y=400)

modo=Menubutton(parred,text="Haga click aquí para los modos de Despertar",bg="grey",fg="lightblue")
modo.place(x=120,y=400)
modo.modos=Menu(modo,tearoff=0)
modo["menu"]=modo.modos

comando1=modo.modos.add_command(label="Despierta (nombre), que son la (hora y minutos), es la hora de (accion)",command=lambda: despertar(f"Despierta Paulino, que son las {hovar.get()} y {minvar.get()} minutos, es la hora de {motext.get()}"))
comando2=modo.modos.add_command(label="Levantate Campeon/a, que son las (hora y minutos)",command=lambda: despertar(f"Levantate Campeón, que son las {hovar.get()} y {minvar.get()} minutos"))
comando3=modo.modos.add_command(label="Silencio y Vibración solamente")

Listo=Button(parred,text="Listo",bg="grey",fg="lightblue",relief="flat",font=25,command=listo).place(x=150,y=470)
cancelar=Button(parred,text="Cancelar",bg="grey",fg="lightblue",relief="flat",font=25,command=exit).place(x=250,y=470)


mainloop()