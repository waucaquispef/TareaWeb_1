class ModeloPlanCuenta:
    def __init__(self, id=0, codigo=0,idGrupo=0, desc='',naturaleza='',estado=True):
        self.id = id
        self.codigo=codigo
        self.idGrupo=idGrupo
        self.descripcion = desc
        self.naturaleza=naturaleza
        self.estado=estado
