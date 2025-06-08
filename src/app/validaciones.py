#  validación de nombre
def validar_nombre(nombre):
    if not nombre or not nombre.strip():
        return "El nombre no puede estar vacío"

    return None


# Validación de contraseña
def validar_contraseña(contraseña):
    if not contraseña or not contraseña.strip():
        print("La contraseña no puede estar vacia")
        return False
    if len(contraseña) < 8:
        print("La contraseña debe tener al menos 8 caracteres.")
        return False
    return True


