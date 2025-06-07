from datetime import datetime


hora = 23


def notificar_estado_puertas(puertas, hora):
    tiempo = datetime.now().hour  # int
    print(tiempo)

    if hora == tiempo:
        for puerta in puertas:
            if puerta["estado"] == False:
                print(f"La puerta {puerta["nombre"]} está abierta")
            else:
                print(f"La puerta {puerta["nombre"]} está cerrada")
