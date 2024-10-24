CREATE DATABASE ARGBroker;


USE ARGBroker;



-- Tabla Usuario
CREATE TABLE Usuario (
    idUsuario INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    cuil INT(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    saldo DECIMAL(10, 2) DEFAULT 0,
    intentos_fallidos INT DEFAULT 0,
    hora_bloqueado DATETIME DEFAULT NULL
);

-- Tabla Accion
CREATE TABLE Accion (
    idAccion INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100),
    simbolo VARCHAR(10) UNIQUE,
    precio_apertura DECIMAL(10, 2),
    precio_actual DECIMAL(10, 2)
);

-- Tabla Transaccion
CREATE TABLE Transaccion (
    idTransaccion INT PRIMARY KEY AUTO_INCREMENT,
    idUsuario INT,
    idAccion INT,
    cantidad INT,
    precio DECIMAL(10, 2),
    tipoTransaccion ENUM('compra', 'venta'),
    comision DECIMAL(10, 2),
    fechaOperacion DATETIME,
    FOREIGN KEY (idUsuario) REFERENCES Usuario(idUsuario),
    FOREIGN KEY (idAccion) REFERENCES Accion(idAccion)
);

-- Tabla Cotizacion (historial de precios de acciones)
CREATE TABLE Cotizacion (
    idCotizacion INT PRIMARY KEY AUTO_INCREMENT,
    idAccion INT,
    fechaHora DATETIME,
    precio DECIMAL(10, 2),
    FOREIGN KEY (idAccion) REFERENCES Accion(idAccion)
);

-- Tabla Portafolio (relaciona a los usuarios con las acciones que poseen)
CREATE TABLE Portafolio (
    idPortafolio INT PRIMARY KEY AUTO_INCREMENT,
    idUsuario INT,
    idAccion INT,
    cantidad INT,
    FOREIGN KEY (idUsuario) REFERENCES Usuario(idUsuario),
    FOREIGN KEY (idAccion) REFERENCES Accion(idAccion)
);

-- 4. Insertar datos iniciales

-- Insertar usuarios
INSERT INTO Usuario (nombre, apellido, cuil, email, password, saldo) 
VALUES ('Alvaro', 'Benicio', 1, 'alvarobeniicio@gmail.com', 'd123', 50000.00),
       ('Maria', 'Lopez', 2, 'maria.lopez@gmail.com', 'd1234', 75000.00);

-- Insertar acciones
INSERT INTO Accion (nombre, simbolo, precio_apertura, precio_actual) 
VALUES ('Empresa A', 'EMP_A', 150.50, 160.75),
       ('Empresa B', 'EMP_B', 80.00, 82.30);

-- Insertar cotizaciones históricas
INSERT INTO Cotizacion (idAccion, fechaHora, precio) 
VALUES (1, '2024-10-01 10:00:00', 151.00),
       (1, '2024-10-02 10:00:00', 155.00),
       (2, '2024-10-01 10:00:00', 80.50),
       (2, '2024-10-02 10:00:00', 82.00);

-- Insertar transacciones
INSERT INTO Transaccion (idUsuario, idAccion, cantidad, precio, tipoTransaccion, comision, fechaOperacion) 
VALUES (1, 1, 100, 160.00, 'compra', 0.02, '2024-10-02 12:00:00'),
       (2, 2, 50, 82.00, 'venta', 0.02, '2024-10-03 14:00:00');

-- Insertar portafolio (relación entre usuario y acciones)
INSERT INTO Portafolio (idUsuario, idAccion, cantidad) 
VALUES (1, 1, 100),
       (2, 2, 50);

-- 5 de consultas SELECT

-- Mostrar todos los usuarios
SELECT * FROM Usuario;

-- Mostrar las transacciones de un usuario específico
SELECT tipoTransaccion, cantidad, precio, fechaOperacion 
FROM Transaccion 
WHERE idUsuario = 1;

-- Mostrar el portafolio de un usuario
SELECT u.nombre, a.nombre AS accion, p.cantidad 
FROM Usuario u
JOIN Portafolio p ON u.idUsuario = p.idUsuario
JOIN Accion a ON p.idAccion = a.idAccion
WHERE u.idUsuario = 1;

-- Mostrar las cotizaciones históricas de una acción
SELECT fechaHora, precio FROM Cotizacion WHERE idAccion = 1 ORDER BY fechaHora DESC;

-- Mostrar todas las acciones disponibles
SELECT nombre, simbolo, precio_actual FROM Accion;
