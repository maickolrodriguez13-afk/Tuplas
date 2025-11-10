# ==============================
# EJERCICIOS DE TUPLAS, LISTAS Y DICCIONARIOS
# ==============================

# ----------- Ejercicio 1: Tuplas -----------
vulnerabilidades = ('SQL Injection', 'Cross-Site Scripting', 'Buffer Overflow', 'Denegación de Servicio')

print("\n--- EJERCICIO 1: TUPLAS ---")
print("Segundo elemento:", vulnerabilidades[1])
print("Dos últimos elementos:", vulnerabilidades[-2:])

try:
    vulnerabilidades[0] = 'Inyección SQL'
except TypeError as e:
    print("Error al intentar modificar una tupla:", e)


# ----------- Ejercicio 2: Listas -----------
puertos_abiertos = [22, 80, 443, 8080]

print("\n--- EJERCICIO 2: LISTAS ---")
puertos_abiertos.append(21)
print("Lista tras agregar 21:", puertos_abiertos)

puertos_abiertos.remove(8080)
print("Lista tras eliminar 8080:", puertos_abiertos)

puertos_abiertos.sort()
print("Lista ordenada:", puertos_abiertos)


# ----------- Ejercicio 3: Diccionarios -----------
dispositivo_red = {
    'IP': '10.0.3.12',
    'Hostname': 'Firewall-Corp',
    'Estado': 'Activo'
}

print("\n--- EJERCICIO 3: DICCIONARIOS ---")
print("Hostname:", dispositivo_red['Hostname'])

dispositivo_red['Ubicación'] = 'Centro de Datos'
dispositivo_red['Estado'] = 'Inactivo'

print("Diccionario actualizado:")
for clave, valor in dispositivo_red.items():
    print(f"{clave}: {valor}")
