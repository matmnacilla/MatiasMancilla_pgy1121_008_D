import funciones as fn
import numpy
import time

creativos=numpy.zeros((10,10),int)

while True:    
    
    opcion=fn.validar_op()
    if opcion == 1:
        cant_entradas=fn.val_entrada()
        print(fn.mostrar())
        time.sleep(3)
        for x in range (cant_entradas):
            fila=fn.validar_fila()
            columna=fn.validar_columnas()
            rut=fn.val_rut()
    elif opcion==2:
        print(fn.mostrar())
        time.sleep(4)
    elif opcion==3:
        print(sorted(fn.lista_rut))
    elif opcion==4:
       fn.ganancias()
    else:
        print("Gracias por su compra!!")
        print("ATTE: Matias Mancilla Olivares 11/07/2023")

