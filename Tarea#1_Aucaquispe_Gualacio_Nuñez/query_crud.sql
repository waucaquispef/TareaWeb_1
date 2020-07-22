CREATE DATABASE db_crud;

USE db_crud;

CREATE TABLE IF NOT EXISTS grupo(
id INT NOT NULL AUTO_INCREMENT,
descripcion VARCHAR(50),
PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS planCuenta(
id INT  NOT NULL AUTO_INCREMENT,
codigo VARCHAR(15) NOT NULL,
idGrupo  INT NOT NULL,
descripcion VARCHAR(100) NOT NULL,
naturaleza CHAR(1) NOT NULL,
estado BOOL,
PRIMARY KEY(id),
FOREIGN KEY(idgrupo) REFERENCES grupo(id)
);

INSERT INTO grupo(descripcion) VALUES('Activo');

SELECT * FROM grupo;

INSERT INTO planCuenta(codigo,idGrupo,descripcion,naturaleza,estado)
VALUES('01',1,'CAJA','D',TRUE);

SELECT * FROM planCuenta;

