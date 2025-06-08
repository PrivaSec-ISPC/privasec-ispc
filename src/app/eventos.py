import time
from data.config import guardar_puertas


# bloqueo automatico
def bloqueo_automatico(puertas):
    print("Sistema de seguridad PrivaSec en proceso.")

    time.sleep(5)
    for puerta in puertas:
        if puerta["estado"] == False:
            puerta["estado"] = True

    guardar_puertas(puertas)
    print("Sistema de seguridad PrivaSec finalizado. Puertas aseguradas.")
