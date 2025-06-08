from app.puertas import listar_puertas, agregar_puerta, buscar_puerta, eliminar_puerta
from app.usuarios import (
    iniciar_sesión,
    verificar_estado,
    consultar_datos_personales,
    modificar_rol_usuario,
    registrar_usuario,
)
from data.config import cargar_puertas, cargar_usuarios
from app.eventos import bloqueo_automatico
from app.validaciones import validar_contraseña


def main():
    puertas = cargar_puertas()
    usuarios = cargar_usuarios()

    while True:
        accion = input("Desea iniciar sesión (1), registrar usuario (2) ó salir (3) ")

        if accion == "1":
            nombre = input("Ingresar nombre de usuario: ")
            contraseña = input("Ingresar contraseña: ")
            inicio_sesión = iniciar_sesión(usuarios, nombre, contraseña)

            if inicio_sesión == True:
                estado = verificar_estado(usuarios, nombre)

                if estado == "user":
                    while True:
                        accion = input(
                            "Desea consultar datos personales (1), configurar la automatización (2) , Permitir consultar puertas (3) o salir (4) "
                        )
                        if accion == "1":
                            print(consultar_datos_personales(usuarios, nombre))

                        if accion == "2":
                            accion = input("Desea activar el bloqueo automatico (s/n) ")
                            if accion == "s":
                                bloqueo_automatico(puertas)
                            if accion == "n":
                                continue

                        if accion == "3":
                            listar_puertas(puertas)

                        if accion == "4":
                            break

                if estado == "admin":
                    while True:
                        accion = input(
                            "Desea consultar automatizaciónes activas (1), Gestionar puertas (2) , Modificar rol de usuario (3) o salir (4) "
                        )
                        if accion == "1":
                            print(f"{"bloqueo automatico: Activado"}")

                        if accion == "2":
                            while True:
                                accion = input(
                                    "Desea agregar una puerta (1), listar puertas (2), buscar puerta (3), eliminar puerta (4) o salir (5):"
                                )
                                if accion == "1":
                                    nombre = input("Ingresar el nombre de la puerta: ")
                                    agregar_puerta(puertas, nombre)

                                if accion == "2":
                                    listar_puertas(puertas)

                                if accion == "3":
                                    nombre = input("Ingresar el nombre de la puerta: ")
                                    buscar_puerta(puertas, nombre)

                                if accion == "4":
                                    nombre = input("Ingresar el nombre de la puerta: ")
                                    eliminar_puerta(puertas, nombre)

                                if accion == "5":
                                    break
                        if accion == "3":
                            nombre = input(
                                "¿Que usuario quiere asignar como nuevo admin? "
                            )
                            modificar_rol_usuario(usuarios, nombre)
                        if accion == "4":
                            break

        if accion == "2":
            nombre = input("Ingresar nombre de usuario: ")
            while True:
                contraseña = input("Ingresar contraseña: ")
                if validar_contraseña(contraseña):
                    break
                else:
                    continue
            registrar_usuario(usuarios, nombre, contraseña)

        if accion == "3":
            break


if __name__ == "__main__":
    main()
