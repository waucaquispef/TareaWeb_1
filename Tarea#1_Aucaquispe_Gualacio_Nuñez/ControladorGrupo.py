from DaoGrupo import *

class ControladorGrupo:
    def __init__(self,grupo=None):
        self.g=grupo


    def Consultar(self,buscar):
        objDao=DaoGrupo()
        return objDao.Consultar(buscar)

    def Ingresar(self,g):
        objDao=DaoGrupo()
        return objDao.Ingresar(g)

    def Modificar(self,g):
        objDao=DaoGrupo()
        return objDao.Modificar(g)

    def Eliminar(self,g):
        objDao=DaoGrupo()
        return objDao.Eliminar(g)


'''grr = ModeloGrupo(4,'Ingreso')
ctr= ControladorGrupo()
ctr.Modificar(grr)

gr =ctr.Consultar("")
print(gr)
'''