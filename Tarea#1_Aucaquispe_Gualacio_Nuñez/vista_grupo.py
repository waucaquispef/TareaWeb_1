import os
from ControladorGrupo import *
from ModeloGrupo import ModeloGrupo
from funciones import menu
ctr= ControladorGrupo()

def Insertar(rango):
    for i in range(int(rango)):
        grupo= input('Ingrese Grupo: ')
        if grupo.isalpha():
            modelo= ModeloGrupo(desc=grupo)
            if ctr.Ingresar(modelo):
                print("Registro grabado correctamente")
            else:
                print("Error al grabar el registro")
        else:
            print("Error en la lectura de datos,intente nuevamente")




def Modificar():
    id = input('Ingrese Id: ')
    grupo = input('Ingrese grupo a modificar: ')
    if grupo.isalpha() and id.isdigit():
        modelo = ModeloGrupo(codigo=id, desc=grupo)
        if ctr.Modificar(modelo):
            print("Registro Modificado correctamente")
        else:
            print("Error al Modificar el registro")
    else:
        print("Error en la lectura de datos,intente nuevamente")



def Eliminar():
    id = input('Ingrese Id: ')
    if  id.isdigit():
        modelo = ModeloGrupo(codigo=id)
        if ctr.Eliminar(modelo):
            print("Registro Eliminado correctamente")
        else:
            print("Error al Eliminar el registro")
    else:
        print("Error en la lectura de datos,intente nuevamente")


def Consultar():

    buscar = input('Ingrese nombre a buscar (SI DESEA CONSULTAR TODOS LOS REGISTROS, DEJAR EN BLANCO): ')
    if buscar.isalpha() or buscar=='':
        modelo = ctr.Consultar(buscar)
        print("CODIGO     GRUPO")
        for registo in modelo:
            print('{:5}     {:3}'.format(registo[0], registo[1]))
    else:
        print("Error en la lectura de datos,intente nuevamente")


def ejecutarGrupo():
    while True:
        opc = str(menu(('INGRESAR', 'MODIFICAR','ELIMINAR','CONSULTAR', 'REGRESAR AL MENU PRINCIPAL'), 'MENÚ GRUPO'))
        if opc == '0':
            print('<<<INSERTAR DATOS>>>')
            valor = input('Ingrese cantidad de datos a ingresar ')
            if valor.isdigit():
                Insertar(valor)
            else:
                print("Error en la lecura")
        elif opc == '1':
            print('<<<MODIFICAR DATOS>>>')
            Modificar()
        elif opc == '2':
            print('<<<ELIMINAR DATOS>>>')
            Eliminar()
        elif opc == '3':
            print('<<<CONSULTAR DATOS>>>')
            Consultar()
        elif opc == '4':
            break
        elif opc != '4':
            print('<<<Seleccione una opción correcta >>>')
        input("PRECIONE UNA TECLA PARA CONTINUAR...")
        os.system('cls')




