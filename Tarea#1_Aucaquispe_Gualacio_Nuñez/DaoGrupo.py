from Conexion import Conector
class DaoGrupo(Conector):
    def __init__(self):
        super().__init__()

    def Consultar(self,buscar):
        result=False
        try:
            sql="select * from grupo where descripcion like '%"+ str(buscar) + "%' order by id"
            self.conectar()
            self.conector.execute(sql)
            result=self.conector.fetchall()
            self.conn.commit()
        except Exception as e:
            print("Error en la consulta de grupo",e)
            self.conn.rollback()
        finally:
            self.cerrar()
        return result

    def Ingresar(self,grupo):
        correcto=True
        try:
            sql="insert into grupo(descripcion) values(%s)"
            self.conectar()
            self.conector.execute(sql,(grupo.descripcion))
            self.conn.commit()
        except Exception as e:
            print("Error en insertar grupo", e)
            correcto=False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto

    def Modificar(self,grupo):
        correcto = True
        try:
            sql="update grupo set descripcion = %s where id = %s"
            self.conectar()
            self.conector.execute(sql,(grupo.descripcion,grupo.id))
            self.conn.commit()
        except Exception as e:
            print("Error en la Modificar grupo", e)
            correcto = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto


    def Eliminar(self,grupo):
        correcto =True
        try:
            sql='delete from grupo where id= %s'
            self.conectar()
            self.conector.execute(sql, (grupo.id))
            self.conn.commit()
        except Exception as e:
            print("Error en la Eliminación grupo", e)
            correcto = False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto

'''con = DaoGrupo()
grupo = con.Consultar("")
print(grupo)

for dato in grupo:
    print(dato[1])'''