"""
Script para crear usuarios de prueba en la base de datos.
Ejecutar este script una sola vez para crear los usuarios de prueba.

Usuarios creados:
1. Administrador: admin@admin.cl / Administrador123?
2. Cliente: cliente@cliente.cl / Cliente123?
"""

import bcrypt
from datetime import date
from config import conectar_db
from src.Datos.usuario_repository import Usuario_Repository
from src.Logica_de_Negocio.usuarios_service import Usuario_Service
from src.Logica_de_Negocio.models.Cliente import Cliente

def crear_usuarios_prueba():
    # Inicializar repositorio y servicio
    usuario_repo = Usuario_Repository(conectar_db)
    usuario_serv = Usuario_Service(usuario_repo)
    
    print("=== Creando usuarios de prueba ===\n")
    
    # Usuario 1: Administrador
    print("1. Creando usuario Administrador...")
    try:
        # Verificar si ya existe
        if usuario_serv.obtener_usuario_por_email("admin@admin.cl"):
            print("El usuario administrador ya existe. Saltando...\n")
        else:
            # Hashear contraseña
            password_admin = "Administrador123?"
            password_hash_admin = bcrypt.hashpw(password_admin.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            
            # Crear objeto usuario
            admin = Cliente(
                id_cliente=None,
                rut="12345678-9",
                nombres="Admin",
                apellido_paterno="Sistema",
                apellido_materno="Principal",
                email="admin@admin.cl",
                contraseña_hash=password_hash_admin,
                telefono="+56 9 1234 5678",
                fecha_nacimiento=date(1990, 1, 1),
                fecha_registro=date.today(),
                rol="Administrador"
            )
            
            # Guardar en BD
            usuario_repo.create(admin)
            print("Usuario administrador creado exitosamente!")
            print(f"      Email: admin@admin.cl")
            print(f"      Password: {password_admin}\n")
    except Exception as e:
        print(f"Error al crear administrador: {e}\n")
    
    # Usuario 2: Cliente
    print("2. Creando usuario Cliente...")
    try:
        # Verificar si ya existe
        if usuario_serv.obtener_usuario_por_email("cliente@cliente.cl"):
            print("El usuario cliente ya existe. Saltando...\n")
        else:
            # Hashear contraseña
            password_cliente = "Cliente123?"
            password_hash_cliente = bcrypt.hashpw(password_cliente.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            
            # Crear objeto usuario
            cliente = Cliente(
                id_cliente=None,
                rut="98765432-1",
                nombres="Cliente",
                apellido_paterno="Prueba",
                apellido_materno="Test",
                email="cliente@cliente.cl",
                contraseña_hash=password_hash_cliente,
                telefono="+56 9 8765 4321",
                fecha_nacimiento=date(1995, 6, 15),
                fecha_registro=date.today(),
                rol="Cliente"
            )
            
            # Guardar en BD
            usuario_repo.create(cliente)
            print("Usuario cliente creado exitosamente!")
            print(f"      Email: cliente@cliente.cl")
            print(f"      Password: {password_cliente}\n")
    except Exception as e:
        print(f"Error al crear cliente: {e}\n")
    
    print("=== Proceso completado ===")
    print("\nPuedes iniciar sesión con cualquiera de estos usuarios:")
    print("  • Administrador: admin@admin.cl / Administrador123?")
    print("  • Cliente: cliente@cliente.cl / Cliente123?")

if __name__ == "__main__":
    try:
        crear_usuarios_prueba()
    except Exception as e:
        print(f"\nError general: {e}")
        import traceback
        traceback.print_exc()
