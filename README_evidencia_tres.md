# Modulo Programador - ( Segunda Instancia )

### Introducción

A partir de la instancia anterior, donde se podía gestionar dispositivos (agregar, listar, buscar y eliminar) a través de un programa de consola, en esta nueva etapa se incorporaron funcionalidades que permiten determinar dicha gestión según el rol del usuario (admin o user)

Según los requerimientos funcionales definidos para esta instancia, se permite:

- El registro de nuevos usuarios y el inicio de sesión en el sistema.
- El acceso a funcionalidades específicas según el rol del usuario (admin o user).

---

### Requerimientos funcionales del programa

- **Gestión de usuarios**
    
    El programa deber permitir registrar nuevos usuarios y almacenar su información. Los usuarios podrán acceder a sus datos y gestionar sus dispositivos.
    
- **Gestión de dispositivos**
    
    El programa debe permitir registrar dispositivos nuevos y estado inicial, con posibilidad de poder modificar las caracteristicas del dispositivo.
    
- **Control de Estado**
    
    El usuario puede ver el estado actual de todos los dispositivos registrados.
    
- **Automatización**
    
    Implementar reglas automáticas como el bloqueo / desbloqueo  automático de puertas.
    
- **Transparencia Algorítmica**
    
    El sistema contiene la documentación correspondiente de forma clara y concisa sobre como funcionan las automátizaciones.
    

---

## Segunda Instancia ( Registro e Inicio de sesión )

- **Registro de Usuarios**

```python
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
```

La función registrar_usuarios toma como parametro una lista de usuarios , el nombre y la contraseña del usuario, donde se valida que los campos estén completos, y que el usuario ingresado se encuentre dentro de la lista de usuarios, permitiendo que el primer usuario registrado sea nombrado como “admin”.

---

- **Iniciar Sesión**

```python
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
```

La función iniciar_sesión toma como parametros una lista de usuarios, el nombre y la contraseña del usuario, donde se verifica que los datos seán validos y permita la entrada del usuario al menú correspondiente devolviendo un “True” o “False”.

---

## Segunda Instancia ( Validaciónes )

```python
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
```

Dentro de las validaciones no solo se mejoraron o agregaron requerimientos funcionalidades sino tambien, requerimientos no funcionales, donde las validaciones se trasladaron a un módulo separado, permitiendo mayor escalabilidad y eficiencia.

La función validar_contraseña toma como parametro la contraseña del usuario, donde verifica que los campos no esten vacios y que cumpla con la condición de tener al menos 8 caracteres. 

---

### Segunda Instancia (admin o user)

```python
# verificar estado
def verificar_estado(usuarios, nombre):
    for usuario in usuarios:
        if usuario["nombre"].lower() == nombre.lower():
            return usuario["estado"]
```

La función verficar_estado toma como parametro la lista de usuarios y el nombre del usuario, donde dependiendo del “estado”, en el menú  podrá accerder a determinadas funcionalidades del programa.

---

```python
# consultar datos personales
def consultar_datos_personales(usuarios, nombre):
    for usuario in usuarios:
        if usuario["nombre"].lower() == nombre.lower():
            return f"Usuario: {usuario["nombre"]} \nEstado: {usuario["estado"]}"
```

La función verficar_estado toma como parametro la lista de usuarios y el nombre del usuario, esta funcionalidad permite consultar los datos personales, donde puede observar su nombre y estado en el programa, está función a futuro permitira más información del usuario.

---

- **Modificar rol del usuario (admin)**

```python
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
```

La función modificar_rol_usuario toma como parametro una lista de usuarios y el nombre de usuario, donde permite cambiar el estado del usuario de “user” a “admin”, permitiendo que en el programa haya más administradores y eligiendo quien puede tener determinados accesos a las funcionalidades.

---

### Bloqueo Automatico: Control de puertas ( Segunda Instancia )

Para está evidencia elegimos cambiar de momento la automatización con el fin de que resulte más comprensible con lo realizado en bases de datos, La automatizacion de notificación automatica se realizara mas adelante

```python
# bloqueo automatico
def bloqueo_automatico(puertas):
    print("Sistema de seguridad PrivaSec en proceso.")

    time.sleep(5)
    for puerta in puertas:
        if puerta["estado"] == False:
            puerta["estado"] = True

    guardar_puertas(puertas)
    print("Sistema de seguridad PrivaSec finalizado. Puertas aseguradas.")
```

La función bloqueo automático toma como parametro la lista de puertas, donde el usuario atravez del menú puede activar el bloqueo automatico, para la demostración el bloqueo se ejecutara en 5 segundos, tener en cuenta que para el programa final, el bloqueo automático se ejecutara a los 60seg.