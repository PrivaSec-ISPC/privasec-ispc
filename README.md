
# Modulo Programador -  ( Primera Instancia )


### Automatización del Hogar

1. Luces inteligentes ( encender, apagar, cambiar intensidad o color )
2. Aire / Calefacción ( encender, ajustar temperatura )
3. Puertas inteligentes ( abrir / cerrar, bloquear / desbloquear )
4. Sistema de riego automático ( activar, programar días y horarios )

### Introducción

La automatización es el uso de tecnología para controlar y gestionar automáticamente distintos dispositivos y sistemas del hogar: luces, climatización, seguridad, etc.

La automatización de puertas inteligentes es una solución tecnológica que permite, el control de acceso a una determinada puerta de forma automática.

---

### Requerimientos funcionales del programa

- **Gestión de dispositivos**
    
    El programa debe permitir registrar dispositivos nuevos y estado inicial, con posibilidad de poder modificar las caracteristicas del dispositivo.
    
- **Control de Estado**
    
    El usuario puede ver el estado actual de todos los dispositivos registrados.
    
- **Automatización**
    
    Implementar reglas automáticas como el bloqueo / desbloqueo  automático de puertas.
    
- **Transparencia Algorítmica**
    
    El sistema contiene la documentación correspondiente de forma clara y concisa sobre como funcionan las automátizaciones.
    

### Problemáticas extras para elegir ( Automatización )

> " Se puede implementar un sistema de notificaciones automatizadas que funcione como recordatorio de seguridad. Por ejemplo, a las 12:00 p.m., el sistema podría enviar una alerta indicando: 'Todas las puertas están bloqueadas', brindando tranquilidad al usuario sobre el estado del hogar. ”  
“ 12pm -  Todas las puertas están bloqueadas ” → Ejemplo Notificación
> 

---

## Primera Instancia ( Agregar, Eliminar, Buscar, Listar )

### Gestionar los dispositivos

- Listar

```python
def listar_puertas(puertas):
    if not puertas:
        print("No hay puertas agregadas.")
        return

    for puerta in puertas:
        print(f"{puerta["nombre"]} - {puerta["estado"]}")
```

La función **listar_puertas** toma como parametro una lista de puertas ( dispositivos agregados por el usuario ) y muestra el nombre de la puerta, junto a su estado.

---

- Buscar

```python
def buscar_puerta(puertas, nombre):
    mensaje_error = validar_inputs(nombre)
    if mensaje_error:
        print(mensaje_error)
        return

    for puerta in puertas:
        if puerta["nombre"].lower() == nombre.lower():
            print(f"{puerta["nombre"]} - {puerta["estado"]}")
            return

    print(f"La puerta no fue encontrada.")
```

La función **buscar_puerta** toma como parametro una lista de puertas ( dispositivos agregados por el usuario ) y el nombre de una puerta específica. El usuario puede consultar el estado de esa puerta de manera individual.

---

- Agregar

```python
def agregar_puerta(puertas, nombre):
    mensaje_error = validar_inputs(nombre)
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
```

La función **agregar_puerta** toma como parametro una lista de puertas ( dispositivos agregados por el usuario ) y el nombre de una puerta específica. El usuario puede agregar una puerta a la lista, por default el valor del estado empieza en “False”.

---

- Eliminar

```python
def eliminar_puerta(puertas, nombre):
    mensaje_error = validar_inputs(nombre)
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
```

La función **eliminar_puerta** toma como parametro una lista de puertas ( dispositivos agregados por el usuario ) y el nombre de una puerta específica. El usuario puede eliminar una puerta específica de la lista.

---

- Validación

```python
def validar_inputs(nombre):
    if not nombre or not nombre.strip():
        return "El nombre no puede esta vacío"

    return None
```

La función **validar_inputs** toma como parametro el valor de un input ( nombre ). Atravez de esta función de momento podemos notifcar al usuario que el input no puede estar vacío, esta función busca aplicar el concepto de reutilización, ya que actualmente se utiliza en tres de las cuatro funciones del programa, evitando duplicar código, facilitando asi la lectura y posibles modificaciones futuras.

---

## Gestionar automatizaciones y estructuras de datos ( primera instancia JSON )

- Utilizaremos JSON como herramienta para la gestión momentanea de configuraciones y acceso, listar dispositivos, buscar dispositivos, agregar dispositos o eliminar dispositivos.
- JSON ofrece simplicidad, legibilidad y compatibilidad. Nos permite trabajar la información en estructuras de datos, facilitando el trabajo con datos estructurados, integrable en sistemas de automatización como el sistema de puertas inteligentes.
- Se realizará un menú por consola, donde pérmitiremos al usuario realizar acciones tales como, agregar, listar, buscar o eliminar dispositivos.

---

## Notificación Automática: Control de puertas ( Primera Instancia )

La automatización elegida en primera instancia, consiste en verificar el estado de todas las puertas gestionadas por el usuario, donde se emite una notificación según corresponda el horario establecido por el usuario.

En esta primera instancia el código no trabaja con bases de datos, sino trabaja con datos simulados por los desarrolladores.

Nuestra función se encarga de recorrer la lista donde se encuentran las puertas gestionadas  por el usuario y imprime de momento, el estado de todas las puertas, visualizando las puertas que están cerradas o abiertas

Esto nos permite aplicar conceptos básicos de lógica, listas, condicionales, y tipos de variables, buscando una posible solución a una situación real que más adelante con componente adicionales como almacenamiento de datos, podria escalarse a un sistema más completo 

```python
def notificar_estado_puertas(puertas, hora):
    tiempo = datetime.now().hour  # int
    print(tiempo)

    if hora == tiempo:
        for puerta in puertas:
            if puerta["estado"] == False:
                print(f"La puerta {puerta["nombre"]} está abierta")
            else:
                print(f"La puerta {puerta["nombre"]} está cerrada")
```

Para obtener el tiempo actual, se utiliza el módulo `datetime` de Python, que permite acceder a la fecha, la hora, los minutos, los segundos, entre otros datos relacionados con el tiempo.
Al trabajar con datos estructurados, es posible notificar al usuario el estado individual de cada puerta, indicando si está abierta o cerrada.