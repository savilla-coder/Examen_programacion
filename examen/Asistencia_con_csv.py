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
