


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
    print("La superficie a limpiar es de ",superficie,"m2")
superficie_a_limpiar(zonas)


   
    


    

