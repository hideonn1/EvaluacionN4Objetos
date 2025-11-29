## Contexto general:

Este es un producto/proyecto para una agencia de viajes ficticia, realizado por 3 alumnos de primer año de Ingeniería en Informática de INACAP.


### Contexto académico:

Este proyecto corresponde a la asignatura **Programación Orientada a Objeto Seguro** en **INACAP, Chile**.

Su propósito es aplicar patrones de diseño y arquitectura en un sistema de gestión con base de datos MySQL.


### Sobre el programa

- El programa se ejecuta en la terminal
- El programa esta en español
- El programa esta en una version beta (Eso significa que esta en desarrollo activo. Algunas funciones puden cambiar en futuras versiones.)

### Los patrones de diseño y arquitectura utilizados son los siguientes:

1. Repository Pattern: Actúa como una capa intermedia entre la lógica de negocio del programa y el almacenamiento de datos en la DB, proporcionando una forma estructurada y estandarizada de acceder, administrar y manipular los datos. 

En este programa se encapsula completamente las operaciones sobre la base de datos en clases Repository, aislando así la lógica de negocio de los detalles de persistencia SQL.

    Ejemplo de uso:
    ```python
    repository = UserRepository()
    user = repository.get_user_by_email("admin@admin.cl")
    ```


2. Dependency Injection: Es la forma más común de inyección de dependencia, donde las dependencias que necesita una clase se proporcionan a través de su argumento de constructor. Las dependencias se pueden declarar como finales, lo que garantiza que se asignen una sola vez y no se puedan modificar después de la creación del objeto. 

En este programa, cada capa recibe sus dependencias a través del constructor (inyección manual). El controller recibe el service, el service recibe el repository, y el repository recibe la función de conexión a la base de datos.

    Ejemplo de uso:

    # main2.py líneas 18-20
    usuario_repo = Usuario_Repository(conectar_db)
    usuario_serv = Usuario_Service(usuario_repo)
    usuario_cont = Usuario_Controller(usuario_serv)


3. Template Method Pattern: Aprovecha las clases abstractas y la herencia para definir la estructura central de un algoritmo al tiempo que permite que las subclases implementen pasos específicos. Se declaran sin una implementación en la clase abstracta. Se requieren subclases para proporcionar implementaciones concretas.

    Ejemplo de uso:

        (Persona.py - Clase abstracta)
        from abc import ABC, abstractmethod

        class Persona(ABC):
            @abstractmethod
            def iniciar_sesion(self):
                pass
    
            @abstractmethod
            def validar_rut(self):
                pass

        (Cliente.py y Administrador.py heredan de Persona)


4. MVC (Model View Controller): Separa la lógica de negocio, la presentación y la interacción con el usuario a través de tres componentes interconectados (el modelo, la vista y el controlador). Por ejemplo, el controlador actúa como intermediario entre el modelo y la vista, recibiendo y procesando la información del usuario, y luego enviando la respuesta al usuario a través de la vista.

En el programa se implementa el MVC de la siguiente forma:

    Models en Logica_de_Negocio/models/
    Views en Presentacion/vista/
    Controllers en Presentacion/controlador/


### Para ejecutar el programa:
- Tener instalado Python 3.12.6
- Tener instalado MySQL (puede ser independiente o mediante XAMPP) 
- Tener instalado Git
- Tener una base de datos MySQL
- Clonar el repositorio en una carpeta local con el comando "git clone -b proyecto_antigravity_edition --single-branch https://github.com/hideonn1/EvaluacionN4Objetos.git"
- Abrir la terminal en la carpeta local de la clonación y ejecutar el comando "cd EvaluacionN4Objetos"
- Encender XAMPP y activar los servicios de Apache y MySQL, en el módulo de MySQL, presionar Admin para abrir phpMyAdmin e importar la base de datos. (El archivo de la base de datos se encuentra en EvaluacionN4Objetos/sql/proyecto_4_nuevo.sql)
- Ejecutar el archivo requeriments.txt con el comando "pip install -r requeriments.txt" para instalar las librerías necesarias
- Ejecutar el archivo main.py
- Seleccionar la opción 1 para iniciar sesión
- Iniciar sesión con las credenciales de prueba (Leer más abajo)

### Credenciales de acceso para los usuarios de prueba: 
### Para crear los usuarios de prueba, ejecutar el archivo crear_usuarios_prueba.py

Administrador: 
    email: admin@admin.cl
    password: Administrador123?

Cliente: 
    email: cliente@cliente.cl
    password: Cliente123?

<<<<<<< HEAD
    diegro@gmail.com  

### Fallos dentro del sistema:
# al crear reservas, admite input que no siguen el formato de fecha  
# revisar todo los controladores y vistas de reserva
# revisar todo los controladores y vistas de paquete

=======
### Autores

- Diego Agüero
- Pedro Lorca
- Juan Navarrete

### Fecha de entrega de la versión beta:

03 de Diciembre de 2025

### Licencia

Este proyecto está licenciado bajo la licencia MIT - véase el archivo LICENSE para detalles.
(puedes usarlo, modificarlo y distribuirlo libremente, siempre que mantengas el aviso de copyright original)
>>>>>>> 258871beb322e35e8da19fe55550d669f3ef2a43
