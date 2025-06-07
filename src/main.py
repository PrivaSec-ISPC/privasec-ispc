from app.puertas import *
from data.puertas import cargar_puertas
from app.eventos import *



def main():
    puertas = cargar_puertas()
    notificar_estado_puertas(puertas, hora)

    while True:
        accion = input(
            "Desea agregar una puerta (a), listar puertas (b), buscar puerta (c), eliminar puerta (d) o salir (e):"
        )

        if accion == "a":
            nombre = input("Ingresar el nombre de la puerta: ")
            agregar_puerta(puertas, nombre)

        if accion == "b":
            listar_puertas(puertas)

        if accion == "c":
            nombre = input("Ingresar el nombre de la puerta: ")
            buscar_puerta(puertas, nombre)

        if accion == "d":
            nombre = input("Ingresar el nombre de la puerta: ")
            eliminar_puerta(puertas, nombre)

        if accion == "e":
            break


if __name__ == "__main__":
    main()
