import numpy
creativos=numpy.zeros((10,10),int)
lista_rut=[]
Platinum=120000
Gold=80000 
Silver=50000 
acumulador_pla=0
acumulador_gold=0
acumulador_sil=0
contador_pla=0
contador_gold=0
contador_sil=0
contador_tot=contador_gold+contador_pla+contador_sil
acumulador_tot=acumulador_gold+acumulador_pla+acumulador_sil

def mostrar_menu():
    print(""" 
1. Comprar entradas
2. Mostrar ubicaciones disponibles
3. Ver listado de asistentes
4. Mostrar ganancias totales
5. Salir
    """)

def validar_op ():
    while True:
        try:
            opc=int(input("\nIngrese opción:"))
            if opc in (1,2,3,4,5):
                return opc
            else:
                print("Error ingrese una de las opciones dadas!")
        except:
            print("Error debe ingrsar un número entero!")


def mostrar():
    print("\n\tASIENTOS\n")
    for x in range (10):
        print(f"Fila {x+1}:", end=" ")
        for y in range (10):
            print(creativos [x][y], end=" ")
        print()
        print()

def val_entrada():
    while True:
        try:
            cant_entrada=int(input("Ingrese la cantidad de entradas que desea comprar(máximo de entradas son 3!):"))
            if cant_entrada in (0,1,2,3):
                return cant_entrada
            else:
                print("ERROR, cantidad de entradas no apta!!")
        except:
            print("ERROR, debe ingresar un número entero postivo!!")
def val_rut():
    while True:
        try:
            rut=int(input("Ingrese su rut sin puntos y sin digito verificador:"))
            if len(str(rut)) == 8:
                lista_rut.append(rut)
                return rut
            else:
                print("ERROR, debe ingresar el rut como se le indica!")
        except:
            print("ERROR, debe ingresar número entero positivos!!")

def validar_fila():
    global acumulador_gold
    global acumulador_pla
    global acumulador_sil
    global contador_gold
    global contador_sil
    global contador_pla
    while True:
        try:
            fila=int(input("Ingrese fila que desea comprar:"))
            if fila in (1,2):
                acumulador_pla=acumulador_pla+Platinum
                contador_pla=contador_pla+1
                return fila
            elif fila in (3,4,5):
                acumulador_gold=acumulador_gold+Gold
                contador_gold=contador_gold+1
                return fila
            elif fila in (6,7,8,9,10):
                acumulador_sil=acumulador_sil+Silver
                contador_sil=contador_sil+1
                return fila  
            else:
                print("Error! debe ingresar una de las filas existentes!")
        except:
            print("ERROR, debe ingresar un número entero positivo!!")

def validar_columnas():
    while True:
        try:
            columna=int(input("Ingrese columna que desea comprar:"))
            if columna in (1,2,3,4,5,6,7,8,9,10):
                return columna
            else:
                print("Error! debe ingresar una de las columnas existentes!")
        except:
            print("ERROR, debe ingresar un número entero positivo!!")


def ganancias():
    print(" TIPO ENTRADA       |    CANTIDAD  |      TOTAL     |")
    print(f"PLATINUM {Platinum}      |{contador_pla}            |{acumulador_pla}        \t|")
    print(f"PLATINUM {Platinum}      |{contador_pla}            |{acumulador_pla}        \t|")
    print(f"PLATINUM {Platinum}      |{contador_pla}            |{acumulador_pla}        \t|")
    print(f"TOTAL                |{contador_tot}            |{acumulador_tot}           |")




