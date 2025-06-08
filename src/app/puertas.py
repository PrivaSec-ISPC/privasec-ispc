import uuid
from data.config import guardar_puertas
from app.validaciones import validar_nombre


# nueva puerta
def nueva_puerta(nombre):
    id_puerta = str(uuid.uuid4())
    nueva_puerta = {"id": id_puerta, "nombre": nombre.capitalize(), "estado": False}

    return nueva_puerta


# agregar puerta
def agregar_puerta(puertas, nombre):
    mensaje_error = validar_nombre(nombre)
    if mensaje_error:
        print(mensaje_error)
        return

    for puerta in puertas:
        if puerta["nombre"].lower() == nombre.lower():
            print("La puerta ingresada ya esta registrada.")
            return

    puertas.append(nueva_puerta(nombre))
    guardar_puertas(puertas)
    print("La puerta fue agregada exitosamente.")


# listar puertas
def listar_puertas(puertas):
    if not puertas:
        print("No hay puertas agregadas.")
        return

    for puerta in puertas:
        print(f"{puerta["nombre"]} - {puerta["estado"]}")


# buscar puerta
def buscar_puerta(puertas, nombre):
    mensaje_error = validar_nombre(nombre)
    if mensaje_error:
        print(mensaje_error)
        return

    for puerta in puertas:
        if puerta["nombre"].lower() == nombre.lower():
            print(f"{puerta["nombre"]} - {puerta["estado"]}")
            return

    print(f"La puerta no fue encontrada.")


# eliminar puerta
def eliminar_puerta(puertas, nombre):
    mensaje_error = validar_nombre(nombre)
    if mensaje_error:
        print(mensaje_error)
        return

    for puerta in puertas:
        if puerta["nombre"].lower() == nombre.lower():
            puertas.remove(puerta)
            guardar_puertas(puertas)
            print(f"la puerta {puerta["nombre"]} fue eliminada correctamente.")
            return
    print(f"La puerta no ha sido encontrada.")
