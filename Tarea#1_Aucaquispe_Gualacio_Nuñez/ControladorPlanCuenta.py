from DaoPlanCuenta import *
from ModeloPlanCuenta import *

class ControladorPlanCuenta:
    def __init__(self,planCuenta=None):
        self.p=planCuenta


    def Consultar(self,buscar):
        objDao=DaoPlanCuenta()
        return objDao.Consultar(buscar)

    def Ingresar(self,p):
        objDao=DaoPlanCuenta()
        return objDao.Ingresar(p)

    def Modificar(self,p):
        objDao=DaoPlanCuenta()
        return objDao.Modificar(p)

    def Eliminar(self,p):
        objDao=DaoPlanCuenta()
        return objDao.Eliminar(p)


'''ctr= ControladorPlanCuenta()
p = ModeloPlanCuenta(18,'04',3,'CAPITAL CONTABLE','A',True)
ctr.Eliminar(p)

gr =ctr.Consultar("")
print(gr)'''
