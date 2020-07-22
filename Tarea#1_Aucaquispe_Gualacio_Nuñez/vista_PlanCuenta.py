import os
from ControladorPlanCuenta import  *
from ModeloPlanCuenta import ModeloPlanCuenta
from funciones import menu
ctr= ControladorPlanCuenta()

def Insertar(rango):
    for i in range(int(rango)):
        codigo= input('Ingrese Codigo: ')
        grupo = input('Ingrese Grupo: ')
        descripcion = input('Ingrese Descripcion: ')
        naturaleza = input("Ingrese Naturaleza [DEUDORA->D/ACREEDORA->A]: ")
        estado = input("Ingrese Estado [TRUE->1/FALSE->0]: ")
        if codigo.isdigit() and grupo.isdigit() and descripcion.isalpha() and naturaleza.isalpha() and estado.isdigit():
            modelo = ModeloPlanCuenta(codigo=codigo, idGrupo=grupo, desc=descripcion, naturaleza=naturaleza,
                                      estado=estado)
            if ctr.Ingresar(modelo):
                print("Registro grabado correctamente")
            else:
                print("Error al grabar el registro")
        else:
            print("Error en la lectura de datos")


def Modificar():
    id = input('Ingrese Id: ')
    codigo = input('Ingrese Codigo a modificar: ')
    grupo = input('Ingrese Grupo a modificar: ')
    descripcion = input('Ingrese Descripcion a modificar: ')
    naturaleza = input("Ingrese Naturaleza [DEUDORA->D/ACREEDORA->A] a modificar: ")
    estado = input("Ingrese Estado [TRUE->1/FALSE->0] a modificar: ")
    if id.isdigit() and codigo.isdigit() and grupo.isdigit() and descripcion.isalpha() and naturaleza.isalpha() and estado.isdigit():
        modelo = ModeloPlanCuenta(id=id, codigo=codigo, idGrupo=grupo, desc=descripcion, naturaleza=naturaleza,
                                  estado=estado)
        if ctr.Modificar(modelo):
            print("Registro Modificado correctamente")
        else:
            print("Error al Modificar el registro")
    else:
        print("Error en la lectura de datos")


def Eliminar():
    id = input('Ingrese Id: ')
    if id.isdigit():
        modelo = ModeloPlanCuenta(id=id)
        if ctr.Eliminar(modelo):
            print("Registro Eliminado correctamente")
        else:
            print("Error al Eliminar el registro")
    else:
        print("Error en la lectura de datos")


def Consultar():

    buscar = input('Ingrese nombre a buscar (SI DESEA CONSULTAR TODOS LOS REGISTROS, DEJAR EN BLANCO): ')
    if buscar.isalpha() or buscar=='':
        modelo = ctr.Consultar(buscar)
        print("ID    CODIGO    GRUPO    DESCRIPCION      NATURALEZA    ESTADO")
        for registo in modelo:
            print(
                '{:2}     {:2}        {:2}     {:20} {:12}  {:1}'.format(registo[0], registo[1], registo[2], registo[3],
                                                                         registo[4], registo[5]))
    else:
        print("Error en la lectura de datos")


def ejecutarPlanCuenta():
    while True:
        opc = str(menu(('INGRESAR', 'MODIFICAR','ELIMINAR','CONSULTAR', 'REGRESAR AL MENU PRINCIPAL'), 'MENÚ PLAN CUENTA'))
        if opc=='0':
            print('<<<INSERTAR DATOS>>>')
            valor=input('Ingrese cantidad de datos a ingresar ')
            if valor.isdigit():
                Insertar(valor)
            else:
                print("Error en la lectura de datos")
        elif opc=='1':
            print('<<<MODIFICAR DATOS>>>')
            Modificar()
        elif opc=='2':
            print('<<<ELIMINAR DATOS>>>')
            Eliminar()
        elif opc=='3':
            print('<<<CONSULTAR DATOS>>>')
            Consultar()
        elif opc=='4':
            break
        elif opc!='4':
            print('<<<Seleccione una opción correcta >>>')
        input("PRECIONE UNA TECLA PARA CONTINUAR...")
        os.system('cls')


