import os

from funciones import menu
from vista_PlanCuenta import ejecutarPlanCuenta
from vista_grupo import ejecutarGrupo


def ejecutarMenuPrincipal():
    while True:
        opc = str(menu(('GRUPO DE CUENTAS', 'PLAN DE CUENTAS', 'SALIR'), 'MENÚ PRINCIPAL'))
        if opc=='0':
            ejecutarGrupo()

        elif opc=='1':
            ejecutarPlanCuenta()
        elif opc=='2':
            print('<<<Gracias por usar el sistema!....>>>')
            input("PRECIONE UNA TECLA PARA CONTINUAR...")
            break
        elif opc!='2':
            print('<<<Seleccione una opción correcta >>>')
        input("PRECIONE UNA TECLA PARA CONTINUAR...")
        os.system('cls')



ejecutarMenuPrincipal()