mi_diccionario = {}
import os
sw = True

def fnt_agregar(diccionario, nu_persona, nombre, placa, contacto, ruta, descripcion):
    if nu_persona == '' or nombre == '' or placa == '' or contacto == '' or ruta == '' or descripcion == '': 
        enter = input('Debe diligenciar toda la información solicitada <ENTER>')
    else:
        diccionario[nu_persona] = {'nombre': nombre, 'Placa': placa, 'Contacto': contacto, 'Ruta': ruta, 'Descripcion': descripcion}
        enter = input(f'\nLa persona {nombre} ha sido registrada con éxito <ENTER>')

def fnt_selector(op):
    if op == '1':
        os.system('cls')
        nombre = input('Nombre:  ')
        placa = input('Placa:  ')
        contacto = input('Contacto:  ')
        ruta = input('Ruta: ')
        descripcion = input('Descripcion de la carga: ')
        numero = input('Numero de registro: ')
        fnt_agregar(mi_diccionario, numero, nombre, placa, contacto, ruta, descripcion)
        
while sw == True:
    os.system('cls')
    opcion = input('1. Registrar\n2. Mostrar\n3. Salir\n-->  ')
    if opcion == '1':
        fnt_selector(opcion)
    elif opcion == '2':
        os.system('cls')
        print('\nCantidad de registros: ',len(mi_diccionario),'\n')
        for clave, valor in mi_diccionario.items():
            print(f"{clave}: {valor}")
        enter = input('\n\nPresione ENTER para continuar...')
    elif opcion == '3':
        sw = False