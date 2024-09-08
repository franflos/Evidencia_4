CREATE DATABASE MaquinaBateriaDB;
USE MaquinaBateriaDB;

CREATE TABLE Baterias (
    id_BATERIAS INT AUTO_INCREMENT PRIMARY KEY,
    id_tamaño INT,
    cantidad INT DEFAULT 0,
    fecha_trituracion DATETIME DEFAULT CURRENT_TIMESTAMP,
      foreign key(id_tamaño) references tamaños(id_tamaño)
);
CREATE TABLE tamaños (
    id_tamaño INT AUTO_INCREMENT PRIMARY KEY,
    tamaño VARCHAR(20) NOT NULL
);
DROP TABLE tamaños;
DROP TABLE Baterias;