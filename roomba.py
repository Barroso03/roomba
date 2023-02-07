from tkinter import *
# crea la ventana
ventana = Tk()
ventana.geometry("560x690")

ventana.title("Roomba")
canvas = Canvas(ventana, width=500, height=630, bg='white')
canvas.pack(anchor=CENTER, expand=True)
canvas.create_rectangle((131, 150), (221, 410), fill='brown', outline='orange',width=5)

canvas.create_line((0, 0), (500, 0), fill='orange', width=10)
canvas.create_line((0, 0), (0, 630), fill='orange', width=10)
canvas.create_line((500, 0), (500, 630), fill='orange', width=5)
canvas.create_line((0, 630), (500, 630), fill='orange', width=5)
canvas.create_line((0, 150), (500, 150), fill='orange', width=5)
canvas.create_line((131, 410), (131, 630), fill='orange', width=5)
canvas.create_line((221, 410), (221, 630), fill='orange', width=5)

canvas.create_text(250, 50, text="Zona 1", font=("Arial", 15), fill='blue')
canvas.create_text(70, 300, text="Zona 2", font=("Arial", 15), fill='blue')
canvas.create_text(350, 500, text="Zona 3", font=("Arial", 15), fill='blue')
canvas.create_text(177, 470, text="Zona 4", font=("Arial", 15), fill='blue')
canvas.create_text(281, 300, text="Habitación", font=("Arial", 10), fill='blue')
canvas.create_text(281, 320, text="31,5 m^2", font=("Arial", 15), fill='blue')

zona1=(500,150)
zona2=(480,101)
zona3=(309,480)
zona4=(90,220)
zonas=[]
zonas.append(zona1)
zonas.append(zona2)
zonas.append(zona3)
zonas.append(zona4)

def superficie_a_limpiar(zonas):
    superficie=0
    for zona in zonas:
        superficie+=zona[0]*zona[1]
    superficie=superficie/10000
    # poner el resultado en la ventana
    resultado = Label(ventana, text="La superficie a limpiar es de "+str(superficie)+" m^2", font=("Arial", 15), fg='black')
    resultado.pack(anchor=CENTER, expand=True)
    print("La superficie a limpiar es de ",superficie,"m2")
superficie_a_limpiar(zonas)
def tiempo_estimado(zonas):
    tiempo=0
    velocidad=2
    for zona in zonas:
        tiempo+=((zona[0]*zona[1]/10000)/velocidad)
    # poner el resultado en la ventana
    resultado = Label(ventana, text="El tiempo estimado es de "+str(tiempo)+" segundos", font=("Arial", 15), fg='black')
    resultado.pack(anchor=CENTER, expand=True)
    print("El tiempo estimado es de ",tiempo,"segundos")
tiempo_estimado(zonas)

ventana.mainloop()





   
    


    

