ARG_Broker
Este proyecto, ARG_Broker, es una aplicación que simula la gestión de un broker financiero, permitiendo la compra y venta de acciones, manejo de portafolios de usuario y registro histórico de transacciones y cotizaciones de las acciones.

Descripción
ARG_Broker es una aplicación diseñada para facilitar la simulación de operaciones de trading, gestión de portafolios de usuarios, y acceso a información actualizada sobre precios de acciones. La base de datos MySQL incluida permite almacenar usuarios, acciones, transacciones, cotizaciones históricas y portafolios, relacionando toda esta información mediante consultas SQL y una lógica de backend implementada en Python.

Características
Usuarios: Registro y almacenamiento de datos personales de usuarios, tales como nombre, apellido, email y saldo.
Acciones: Registro de acciones disponibles para trading, con símbolos y precios de apertura y actuales.
Transacciones: Gestión de transacciones de compra y venta realizadas por usuarios.
Cotizaciones: Almacenamiento de precios históricos de acciones para facilitar el análisis de tendencia.
Portafolio de Usuarios: Almacenamiento y administración de las acciones actuales de cada usuario en su portafolio.
Estructura de la Base de Datos
Usuario: Información de usuarios registrados.
Accion: Información de las acciones disponibles.
Transaccion: Registro de las transacciones de compra y venta de acciones.
Cotizacion: Almacenamiento de precios históricos de acciones.
Portafolio: Relación entre usuarios y las acciones que poseen.
Configuración del Entorno
Requisitos Previos
Python 3.x
MySQL Server
Librerías de Python: mysql-connector-python
