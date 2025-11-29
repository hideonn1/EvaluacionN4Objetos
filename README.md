# EvaluacionN4Objetos
Este es un producto/proyecto para una agencia de viajes ficticia, realizado por 3 alumnos de primer año de Ingeniería en Informática de INACAP.


# Por preguntar al profe 

- Al eliminar usuarios de la base de datos, es necesario borrar sus reservas o dejarlos como NULL
- Deberia existir la opcion de borrar/modificar reservas (para admin)
- Es necesaria una tabla que maneje fechas disponibles de destinos? o todos los destinos estan disponibles desde cualquier lado y tienen fechas disponibles sin restricciones


# Cambios a la base de datos

- Pais es un Int y debe ser un VARCHAR

### Para ejecutar el programa:
- Tener instalado Python 3.12.6
- Tener instalado MySQL
- Tener instalado Git
- Tener una base de datos MySQL
- Clonar el repositorio en una carpeta local con el comando "git clone -b proyecto_antigravity_edition --single-branch https://github.com/hideonn1/EvaluacionN4Objetos.git"
- Ejecutar el archivo requeriments.txt con el comando "pip install -r requeriments.txt" para instalar las librerias necesarias
- Ejecutar el archivo main.py
- Seleccionar la opcion 1 para iniciar sesion
- Iniciar sesion con las credenciales de prueba (Leer más abajo)

### Credenciales de acceso para los usuarios de prueba: 
### Para crear los usuarios de prueba, ejecutar el archivo crear_usuarios_prueba.py

Administrador: 
    email: admin@admin.cl
    password: Administrador123?

Cliente: 
    email: cliente@cliente.cl
    password: Cliente123?

    diegro@gmail.com  

### Fallos dentro del sistema:
# al crear reservas, admite input que no siguen el formato de fecha  
# revisar todo los controladores y vistas de reserva
# revisar todo los controladores y vistas de paquete

