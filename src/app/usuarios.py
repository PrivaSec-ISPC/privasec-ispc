from data.config import guardar_usuarios
from app.validaciones import validar_nombre


# agregar usuario
def registrar_usuario(usuarios, nombre, contraseña):
    mensaje_error = validar_nombre(nombre)
    if mensaje_error:
        print(mensaje_error)
        return

    for usuario in usuarios:
        if usuario["nombre"].lower() == nombre.lower():
            print("El usuario ya existe.")
            return

    if not usuarios:
        usuarios.append(
            {"nombre": nombre.capitalize(), "estado": "admin", "contraseña": contraseña}
        )
    else:
        usuarios.append(
            {"nombre": nombre.capitalize(), "estado": "user", "contraseña": contraseña}
        )

    guardar_usuarios(usuarios)
    print("El usuario fue agregado exitosamente.")


# iniciar sesión
def iniciar_sesión(usuarios, nombre, contraseña):
    for usuario in usuarios:
        if (
            usuario["nombre"].lower() == nombre.lower()
            and usuario["contraseña"] == contraseña
        ):
            print("Inicio de sesión exitoso.")
            return True

    print("Usuario o contraseña incorrectos.")
    return False



# verificar estado
def verificar_estado(usuarios, nombre):
    for usuario in usuarios:
        if usuario["nombre"].lower() == nombre.lower():
            return usuario["estado"]


# consultar datos personales
def consultar_datos_personales(usuarios, nombre):
    for usuario in usuarios:
        if usuario["nombre"].lower() == nombre.lower():
            return f"Usuario: {usuario["nombre"]} \nEstado: {usuario["estado"]}"


# modificar roles de los usuarios
def modificar_rol_usuario(usuarios, nombre):
    for usuario in usuarios:
        if usuario["nombre"].lower() == nombre.lower():
            usuario["estado"] = "admin"
            guardar_usuarios(usuarios)
            print("Rol del usuario cambiado a Admin")
            return

    print("Usuario no encontrado")
    return
