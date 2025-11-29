# =================================================================
# REGISTRO SIMPLE DE ASISTENCIA
# Script en Python para registrar, mostrar y eliminar la asistencia
# Gestión de asistencia con CSV usando pandas
# =================================================================
#Añadimos librerias pandas para leer y crear un csv
import pandas as pd
import os # Importar el módulo os para verificar la existencia del archivo

# Nombre del archivo CSV
CSV_archivo = "asistencia.csv"

# Función para cargar los datos de asistencia desde el CSV
def cargar_asistencia_df():
    columnas_necesarias = ['nombre', 'apellido', 'estado', 'sexo']

    if os.path.exists(CSV_archivo):
        df = pd.read_csv(CSV_archivo)

        # Agregar columnas faltantes
        for columna in columnas_necesarias:
            if columna not in df.columns:
                df[columna] = pd.NA

        # Reordenar columnas por si el CSV está desordenado
        df = df[columnas_necesarias]

        return df
    else:
        return pd.DataFrame(columns=columnas_necesarias)

# Función para guardar los datos de asistencia en el CSV
def guardar_asistencia_df(df):
    df.to_csv(CSV_archivo, index=False)
    # Función para ingresar el sexo de la persona
def ingresar_sexo():
    sexo_opciones = {
        1: "Hombre",
        2: "Mujer",
        3: "Otro"
    }
    sexo = 0
    while sexo not in sexo_opciones:
        try:
            print("Ingrese el sexo de la persona:")
            print("1. Hombre")
            print("2. Mujer")
            print("3. Otro")
            sexo = int(input("Su opción: "))
            if sexo not in sexo_opciones:
                print("Opción inválida, intente de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número (1, 2 o 3).")
    return sexo_opciones[sexo]

# Ingreso de personas con nombre y apellido, ademas de su asistencia
def ingreso_asistencia():
    nombre = str(input("Ingrese su nombre: ")).strip().capitalize()
    apellido = str(input("Ingrese su apellido: ")).strip().capitalize()

    # Solicitar el sexo
    sexo_string = ingresar_sexo()

    print("-"*60)
    print("Ingrese si la persona está presente, llegó atrasado/a o ausente ")
    print("1. Presente")
    print("2. Atrasado/a")
    print("3. Ausente")

    estado_opciones = {
        1: "Presente",
        2: "Atrasado/a",
        3: "Ausente"
    }

    llegada = 0
    while llegada not in estado_opciones:
        try:
            llegada = int(input("Su opción: "))
            if llegada not in estado_opciones:
                print("Opción inválida, intente de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número (1, 2 o 3).")

    status_string = estado_opciones[llegada]
    print(f"Ingresado al sistema {nombre} {apellido} ({sexo_string}), asistencia: {status_string}")

    # Cargar el DataFrame existente
    df = cargar_asistencia_df()
    # Crear un nuevo DataFrame con la nueva entrada
    nueva_entrada = pd.DataFrame([{'nombre': nombre, 'apellido': apellido, 'estado': status_string, 'sexo': sexo_string}])

    # Concatenar la nueva entrada al DataFrame existente
    df = pd.concat([df, nueva_entrada], ignore_index=True)

    try:
        guardar_asistencia_df(df)
        print("Registro guardado exitosamente en asistencia.csv.")
    except IOError:
        print("Error al escribir en el archivo CSV de asistencia.")
def mostrar_asistencia():
    df = cargar_asistencia_df()

    if not df.empty:
        # Mostrar el DataFrame con un índice para el usuario (empezando desde 1)
        df_display = df.copy()
        df_display.index = df_display.index + 1 # Ajustar indice para mostrar
        print(df_display.to_string(index=True))
        print("-"*60)
        return df # Devolver el DataFrame original (con índices 0-basados) para uso interno
    else:
        print("No hay asistentes registrados aún.")
        return pd.DataFrame()
def eliminar_asistencia():
    df = mostrar_asistencia()
    if df.empty:
        return

    while True:
        try:
            seleccion_usuario = int(input("Ingrese el número del registro a eliminar (índice, 0 para cancelar): "))
            if seleccion_usuario == 0:
                print("Eliminación cancelada.")
                return

            # Convertir la selección del usuario (1) a un índice Dataframe (0)
            index_df = seleccion_usuario -1
            if index_df in df.index:
                # Obtener el registro antes de eliminarlo para el mensaje de confirmación
                registro_a_eliminar = df.loc[index_df]

                # Eliminar la fila por índice
                df = df.drop(index=index_df)

                try:
                    guardar_asistencia_df(df)
                    print(f"Registro '{registro_a_eliminar['nombre']} {registro_a_eliminar['apellido']}' eliminado exitosamente.")
                except IOError:
                    print("Error al escribir en el archivo CSV de asistencia después de eliminar.")
                return
            else:
                print("Número de registro inválido. Por favor, intente de nuevo (el índice mostrado).")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

        

#definimos el menu, ademas de poner un while para entrar en un bucle donde el usuario deba elegir las opciones 1, 2, 3 o 4
def menu():
    try:
      while True:
        print("-"*60)
        print("Bienvenido al Registrador S-S v2,por favor seleccione una opción ")
        print("1. Ingresar asistencia")
        print("2. Mostrar asistencia")
        print("3. Editar asistencia")
        print("4. Eliminar asistencia")
        print("5. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            ingreso_asistencia()
        elif opcion == "2":
            mostrar_asistencia()
        elif opcion == "3":
            editar_asistencia()
        elif opcion == "4":
            eliminar_asistencia()
        elif opcion == "5":
            print("="*60)
            print("Muchas gracias por usar el Registrador S-S, Cerrando el programa")
            break
        else:
            print("Opción inválida. Por favor, ingrese de nuevo (1, 2, 3, 4 o 5).")
    #Exception es para que salga error en la parte especifica del fallo 
    except Exception as e:
        print(f"Ocurrió un error inesperado en el menú: {e}")

# Bloque principal para ejecutar el menú
menu()
