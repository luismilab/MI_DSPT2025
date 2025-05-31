import csv
import random
import datetime

# --- Constantes y Listas de Datos ---
HOY = datetime.date(2025, 5, 29) # Fecha de referencia para cálculos de edad y fecha de alta
NOMBRE_ARCHIVO_CSV = 'personas_ficticias_espana.csv'
NUM_REGISTROS = 1000

NOMBRES_HOMBRE = ['Hugo', 'Martín', 'Daniel', 'Alejandro', 'Javier', 'Álvaro', 'David', 'Sergio', 'Manuel', 'Carlos', 'Pablo', 'Adrián', 'Diego', 'Marcos', 'Iván', 'Lucas', 'Mateo', 'Leo', 'Enzo', 'Mario', 'Gabriel', 'Samuel', 'Thiago', 'Bruno', 'Oliver', 'Álex']
NOMBRES_MUJER = ['Lucía', 'Sofía', 'Carla', 'María', 'Paula', 'Valeria', 'Alba', 'Julia', 'Noa', 'Emma', 'Claudia', 'Sara', 'Carmen', 'Irene', 'Marta', 'Laura', 'Ana', 'Elena', 'Aitana', 'Olivia', 'Chloe', 'Abril', 'Vega', 'Jimena', 'Candela', 'Triana', 'Vera']
APELLIDOS = ['García', 'Rodríguez', 'González', 'Fernández', 'López', 'Martínez', 'Sánchez', 'Pérez', 'Gómez', 'Martín', 'Jiménez', 'Ruiz', 'Hernández', 'Díaz', 'Moreno', 'Muñoz', 'Álvarez', 'Romero', 'Alonso', 'Gutiérrez', 'Navarro', 'Torres', 'Domínguez', 'Vázquez', 'Ramos', 'Gil', 'Ramírez', 'Serrano', 'Blanco', 'Molina', 'Morales', 'Suárez', 'Ortega', 'Delgado', 'Castro', 'Ortiz', 'Rubio', 'Marín', 'Sanz', 'Núñez', 'Iglesias', 'Medina', 'Garrido', 'Cortés', 'Castillo', 'Santos', 'Pascual', 'Herrero', 'Vega', 'Izquierdo', 'Benítez', 'Reyes', 'Fuentes', 'Soler', 'Vicente', 'Lorenzo', 'Gallego', 'Mora', 'Cabrera', 'Pardo', 'Rojas', 'Campos', 'Silva', 'Salas', 'Guerrero', 'Vidal', 'Peña', 'Flores', 'Cruz', 'Soto', 'Ríos', 'Luna', 'Prieto']

GENEROS_CON_PESOS = (['Hombre', 'Mujer', 'Otro'], [0.49, 0.49, 0.02])

DOMINIOS_EMAIL = ['example.com', 'mail.com', 'email.es', 'workmail.com', 'personal.es', 'inbox.org', 'company.net', 'mymail.es', 'domain.org']

TIPOS_CALLE = ['Calle', 'Avenida', 'Paseo', 'Plaza', 'Ronda', 'Camino', 'Bulevar', 'Glorieta']
NOMBRES_CALLE_GENERICOS = ['Principal', 'Mayor', 'del Sol', 'de la Luna', 'Nueva', 'Vieja', 'de las Flores', 'del Mar', 'Real', 'Constitución', 'Libertad', 'de la Estación', 'del Parque', 'Ancha', 'Estrecha', 'Gran Vía']

# Ciudades con provincia y prefijo de CP. Ponderación especial para Bizkaia y Soria.
# Formato: (Ciudad, Provincia, Prefijo_CP)
UBICACIONES_BIZKAIA = [
    ('Bilbao', 'Bizkaia', '48'), ('Barakaldo', 'Bizkaia', '48'), ('Getxo', 'Bizkaia', '48'),
    ('Portugalete', 'Bizkaia', '48'), ('Santurtzi', 'Bizkaia', '48'), ('Basauri', 'Bizkaia', '48'),
    ('Sestao', 'Bizkaia', '48'), ('Galdakao', 'Bizkaia', '48'), ('Durango', 'Bizkaia', '48'),
    ('Erandio', 'Bizkaia', '48'), ('Amorebieta-Etxano', 'Bizkaia', '48'), ('Mungia', 'Bizkaia', '48')
]
UBICACION_SORIA = [('Soria', 'Soria', '42')]
OTRAS_UBICACIONES = [
    ('Madrid', 'Madrid', '28'), ('Barcelona', 'Barcelona', '08'), ('Valencia', 'Valencia', '46'),
    ('Sevilla', 'Sevilla', '41'), ('Zaragoza', 'Zaragoza', '50'), ('Málaga', 'Málaga', '29'),
    ('Murcia', 'Murcia', '30'), ('Palma', 'Islas Baleares', '07'), ('Las Palmas de Gran Canaria', 'Las Palmas', '35'),
    ('Alicante', 'Alicante', '03'), ('Córdoba', 'Córdoba', '14'), ('Valladolid', 'Valladolid', '47'),
    ('Vigo', 'Pontevedra', '36'), ('Gijón', 'Asturias', '33'), ('Vitoria-Gasteiz', 'Álava', '01'),
    ('A Coruña', 'A Coruña', '15'), ('Granada', 'Granada', '18'), ('Elche', 'Alicante', '03'),
    ('Santa Cruz de Tenerife', 'Santa Cruz de Tenerife', '38'), ('Pamplona', 'Navarra', '31'),
    ('Almería', 'Almería', '04'), ('Donostia-San Sebastián', 'Gipuzkoa', '20'), ('Santander', 'Cantabria', '39'),
    ('Castellón de la Plana', 'Castellón', '12'), ('Burgos', 'Burgos', '09'), ('Albacete', 'Albacete', '02'),
    ('Logroño', 'La Rioja', '26'), ('Badajoz', 'Badajoz', '06'), ('Salamanca', 'Salamanca', '37'),
    ('Huelva', 'Huelva', '21'), ('Lleida', 'Lleida', '25'), ('Tarragona', 'Tarragona', '43'),
    ('Cádiz', 'Cádiz', '11'), ('Jaén', 'Jaén', '23'), ('Ourense', 'Ourense', '32'), ('Lugo', 'Lugo', '27')
]

PROFESIONES = [
    'Ingeniero/a', 'Profesor/a', 'Médico/a', 'Diseñador/a', 'Administrativo/a', 'Fontanero/a',
    'Electricista', 'Autónomo/a', 'Estudiante', 'Jubilado/a', 'Contable', 'Abogado/a', 'Periodista',
    'Chef', 'Agricultor/a', 'Mecánico/a', 'Recepcionista', 'Dependiente/a', 'Limpiador/a',
    'Conductor/a', 'Músico/a', 'Artista', 'Programador/a', 'Científico/a', 'Bombero/a', 'Policía',
    'Marketing Digital', 'Analista de Datos', 'Consultor/a', 'Enfermero/a', 'Farmacéutico/a', 'Arquitecto/a'
]
NIVELES_ESTUDIOS = [
    'Sin estudios', 'Primaria', 'ESO', 'Bachillerato', 'Formación Profesional (Grado Medio)',
    'Formación Profesional (Grado Superior)', 'Grado Universitario', 'Máster', 'Doctorado'
]
ESTADOS_CIVILES = ['Soltero/a', 'Casado/a', 'Divorciado/a', 'Viudo/a', 'Pareja de hecho']

# --- Funciones de Generación ---

def generar_fecha_nacimiento():
    if random.random() < 0.70:  # 70% de probabilidad para edades entre 29 y 62
        edad = random.randint(29, 62)
    else: # 30% restante, distribuido entre 18-28 y 63-96
        if random.random() < 0.5:
            edad = random.randint(18, 28)
        else:
            edad = random.randint(63, 96)

    año_nacimiento = HOY.year - edad
    mes_nacimiento = random.randint(1, 12)

    if mes_nacimiento == 2: # Febrero
        es_bisiesto = (año_nacimiento % 4 == 0 and año_nacimiento % 100 != 0) or (año_nacimiento % 400 == 0)
        max_dias = 29 if es_bisiesto else 28
    elif mes_nacimiento in [4, 6, 9, 11]: # Meses con 30 días
        max_dias = 30
    else: # Meses con 31 días
        max_dias = 31
    dia_nacimiento = random.randint(1, max_dias)

    return datetime.date(año_nacimiento, mes_nacimiento, dia_nacimiento).strftime('%d-%m-%Y')

def generar_email(nombre, apellido1, apellido2):
    nombre_limpio = nombre.lower().split()[0].replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u').replace('ñ','n')
    apellido1_limpio = apellido1.lower().replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u').replace('ñ','n')
    return f"{nombre_limpio}.{apellido1_limpio}{random.randint(1,999)}@{random.choice(DOMINIOS_EMAIL)}"

def generar_telefono():
    return f"{random.choice(['6', '9', '7'])}{''.join([str(random.randint(0, 9)) for _ in range(8)])}"

def generar_direccion_calle():
    return f"{random.choice(TIPOS_CALLE)} {random.choice(NOMBRES_CALLE_GENERICOS)} {random.randint(1, 250)}"

def seleccionar_ubicacion():
    # Ponderación: ~20-25% Bizkaia, ~1-2% Soria, resto distribuido
    rand_val = random.random()
    if rand_val < 0.25: # Probabilidad para Bizkaia
        return random.choice(UBICACIONES_BIZKAIA)
    elif rand_val < 0.27: # Probabilidad para Soria (ajustada al espacio restante)
        return random.choice(UBICACION_SORIA)
    else:
        return random.choice(OTRAS_UBICACIONES)

def generar_codigo_postal(prefijo_provincia):
    return f"{prefijo_provincia}{''.join([str(random.randint(0,9)) for _ in range(3)])}"

def generar_ingresos(profesion, nivel_estudios):
    base_ingresos = random.randint(15000, 75000) # Rango base más ajustado

    if profesion == 'Estudiante' or nivel_estudios == 'Sin estudios':
        return random.randint(12000, 18000)
    if profesion == 'Jubilado/a':
        return random.randint(14000, 28000)

    if nivel_estudios in ['Doctorado', 'Máster'] or profesion in ['Médico/a', 'Ingeniero/a', 'Abogado/a', 'Arquitecto/a', 'Científico/a', 'Consultor/a']:
        base_ingresos = int(base_ingresos * random.uniform(1.1, 1.5))
    elif nivel_estudios in ['Primaria', 'ESO'] or profesion in ['Limpiador/a', 'Dependiente/a (sin especificar mucho)']:
         base_ingresos = int(base_ingresos * random.uniform(0.6, 0.9))

    return max(12000, min(80000, base_ingresos))


def generar_fecha_alta_sistema():
    dias_max_atras = 5 * 365 # Últimos 5 años
    dias_atras = random.randint(0, dias_max_atras)
    fecha_alta = HOY - datetime.timedelta(days=dias_atras)
    return fecha_alta.strftime('%d-%m-%Y')

# --- Script Principal ---
def main():
    datos_personas = []
    for i in range(NUM_REGISTROS):
        id_persona = i + 1

        genero_elegido = random.choices(GENEROS_CON_PESOS[0], weights=GENEROS_CON_PESOS[1], k=1)[0]
        if genero_elegido == 'Hombre':
            nombre = random.choice(NOMBRES_HOMBRE)
        elif genero_elegido == 'Mujer':
            nombre = random.choice(NOMBRES_MUJER)
        else: # Otro
            nombre = random.choice(NOMBRES_HOMBRE + NOMBRES_MUJER) # O una lista de nombres neutros si se tuviera

        apellido1 = random.choice(APELLIDOS)
        apellido2 = random.choice(APELLIDOS)
        fecha_nacimiento = generar_fecha_nacimiento()
        email = generar_email(nombre, apellido1, apellido2)
        telefono = generar_telefono()
        direccion_calle = generar_direccion_calle()

        ciudad_info = seleccionar_ubicacion()
        ciudad = ciudad_info[0]
        provincia = ciudad_info[1]
        codigo_postal = generar_codigo_postal(ciudad_info[2])

        pais = 'España'
        profesion = random.choice(PROFESIONES)
        nivel_estudios = random.choice(NIVELES_ESTUDIOS)
        estado_civil = random.choice(ESTADOS_CIVILES)
        numero_hijos = random.randint(0, 5)
        if fecha_nacimiento: # Evitar error si por alguna razón es None
            try:
                edad_actual = HOY.year - datetime.datetime.strptime(fecha_nacimiento, '%d-%m-%Y').year
                if edad_actual < 25 and numero_hijos > 1: # Jóvenes no suelen tener muchos hijos
                    numero_hijos = random.choice([0,1])
                if edad_actual < 18: # Asegurar que no haya hijos si es menor de edad (aunque el rango es 18+)
                    numero_hijos = 0
            except ValueError:
                pass # Si hay error en fecha, no ajustar hijos

        ingresos_anuales_euros = generar_ingresos(profesion, nivel_estudios)
        fecha_alta_sistema = generar_fecha_alta_sistema()

        datos_personas.append([
            id_persona, nombre, apellido1, apellido2, genero_elegido, fecha_nacimiento,
            email, telefono, direccion_calle, ciudad, provincia, codigo_postal, pais,
            profesion, nivel_estudios, estado_civil, numero_hijos, ingresos_anuales_euros,
            fecha_alta_sistema
        ])

    # Escribir a CSV
    encabezados = [
        'ID_Persona', 'Nombre', 'Apellido1', 'Apellido2', 'Genero', 'Fecha_Nacimiento',
        'Email', 'Telefono', 'Direccion_Calle', 'Ciudad', 'Provincia', 'Codigo_Postal', 'Pais',
        'Profesion', 'Nivel_Estudios', 'Estado_Civil', 'Numero_Hijos', 'Ingresos_Anuales_Euros',
        'Fecha_Alta_Sistema'
    ]

    with open(NOMBRE_ARCHIVO_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(encabezados)
        writer.writerows(datos_personas)

    print(f"Archivo '{NOMBRE_ARCHIVO_CSV}' generado con {NUM_REGISTROS} registros.")

if __name__ == '__main__':
    main()