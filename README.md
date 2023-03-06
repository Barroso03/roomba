# roomba
Somos Jorge Barroso, Juan Navarro y María Rámon.


#   CÓDIGO:

```
from tkinter import *

ventana = Tk()
ventana.title("Roomba")
ventana.geometry("1000x1200")
botonenviar = StringVar()

largobjeto = Label(ventana, text="Largo del objeto:")
largobjeto.grid(row=0, column=0, sticky=W)
cuadrolargobjeto = Entry(ventana)
cuadrolargobjeto.grid(row=0, column=1)

alturaobjeto = Label(ventana, text="Altura del objeto:")
alturaobjeto.grid(row=1, column=0,sticky=W)
cuadroalturaobjeto = Entry(ventana)
cuadroalturaobjeto.grid(row=1, column=1)

largohabitacion = Label(ventana, text="Largo de la habitación:")
largohabitacion.grid(row=2, column=0, sticky=W)
cuadrolargohabitacion = Entry(ventana)
cuadrolargohabitacion.grid(row=2, column=1)

alturahabitacion = Label(ventana, text="Altura de la habitación:")
alturahabitacion.grid(row=3, column=0, sticky=W)
cuadroalturahabitacion = Entry(ventana)
cuadroalturahabitacion.grid(row=3, column=1)

posicionx1 = Label(ventana, text="Coordenada eje x primer punto:")
posicionx1.grid(row=4, column=0, sticky=W)
cuadroposicionx1 = Entry(ventana)
cuadroposicionx1.grid(row=4, column=1)

posiciony1 = Label(ventana, text="Coordenada eje y primer punto:")
posiciony1.grid(row=5, column=0, sticky=W)
cuadroposiciony1 = Entry(ventana)
cuadroposiciony1.grid(row=5, column=1)


def roomba():
    # si le das al boton enviar, se ejecuta esta funcion
    # se obtienen los datos de los cuadros de texto
    largobjeto = int(cuadrolargobjeto.get())
    alturaobjeto = int(cuadroalturaobjeto.get())
    largohabitacion = int(cuadrolargohabitacion.get())
    alturahabitacion = int(cuadroalturahabitacion.get())
    posicionx1 = int(cuadroposicionx1.get())
    posiciony1 = int(cuadroposiciony1.get())
    posicionx2 = posicionx1 + largobjeto
    posiciony2 = posiciony1 + alturaobjeto
    # se calcula la superficie a limpiar
    superficie = ((largohabitacion * alturahabitacion) - (largobjeto * alturaobjeto))/10000# m^2
    # se calcula el tiempo estimado
    velocidad= 2#m^2/s
    tiempo = superficie / velocidad
    # se muestra el resultado en la ventana
    resultado = Label(ventana, text="La superficie a limpiar es de " + str(superficie) + " m^2")
    resultado.grid(row=4, column=0, sticky=W)
    resultado = Label(ventana, text="El tiempo estimado es de " + str(tiempo) + " segundos")
    resultado.grid(row=5, column=0, sticky=W)
    # dibujamos la habitacion
    canvas = Canvas(ventana, width=largohabitacion, height=alturahabitacion)
    canvas.grid(row=7, column=0, sticky=W)
    # pinta el fondo de la habitacion
    canvas.create_rectangle(0, 0, largohabitacion, alturahabitacion, fill="white", outline="orange")
    # dibujamos el objeto
    canvas.create_rectangle(posicionx1, posiciony1,posicionx2,posiciony2, fill="brown", outline="orange")
    # en el rectangulo blanco pon objeto
    canvas.create_text(posicionx1 + largobjeto/2, posiciony1 + alturaobjeto/2, text="Objeto")
    # haz una linea horizontal
    canvas.create_line(0, posiciony1, largohabitacion, posiciony1, fill="orange")
    # encima de la linea horizontal pon la altura del objeto
    canvas.create_text(largohabitacion/2, posiciony1/2, text="Zona 1",fill="blue")
    # haz una linea vertical
    canvas.create_line(posicionx1, posiciony2, posicionx1, alturahabitacion, fill="orange")
    canvas.create_text(posicionx1/2, alturahabitacion/2, text="Zona 2",fill="blue")
    # haz una linea vertical
    canvas.create_line(posicionx2, posiciony2,posicionx2,alturahabitacion, fill="orange")
    canvas.create_text(posicionx2 + (largohabitacion-posicionx2)/2, alturahabitacion/2, text="Zona 3",fill="blue")
    canvas.create_text(posicionx1+(largobjeto/2),posiciony2+(alturahabitacion-posiciony2)/2 , text="Zona 4",fill="blue")
    # pon las medidas de la habitacion
    canvas.create_text(largohabitacion/2, alturahabitacion/2, text="Habitación",fill="black")
    canvas.create_text(largohabitacion/2, alturahabitacion/2 + 20, text=str(largohabitacion) + " x " + str(alturahabitacion) + " cm",fill="black")
    # pon las medidas del objeto
    canvas.create_text(posicionx1 + largobjeto/2, posiciony1 + alturaobjeto/2, text="Objeto",fill="black")
    canvas.create_text(posicionx1 + largobjeto/2, posiciony1 + alturaobjeto/2 + 20, text=str(largobjeto) + " x " + str(alturaobjeto) + " cm",fill="black")
    



botonenviar = Button(ventana, text="Enviar", command=roomba)
botonenviar.grid(row=6, column=0, sticky=W)









ventana.mainloop()
```

# SOLUCIÓN:
1. Captura en el momento que ejecutamos el código:

<img width="1008" alt="Captura de pantalla 2023-03-06 a las 16 30 26" src="https://user-images.githubusercontent.com/91721668/223156892-7bb80453-0190-4c1c-868e-95551ef512e5.png">

2. Captura una vez ya introducidos los datos de la interfaz con las respuestas a las preguntas requeridas:


<img width="1003" alt="Captura de pantalla 2023-03-06 a las 16 34 05" src="https://user-images.githubusercontent.com/91721668/223156944-bc60fadc-2a32-4e5a-8ffd-3a4bb2c75131.png">

