# =================================================================
# REGISTRO SIMPLE DE ASISTENCIA
# Script en Python para registrar, mostrar y eliminar la asistencia
# de personas usando un archivo de texto (asistencia.txt).
# =================================================================
#definimos el menu, ademas de poner un while para entrar en un bucle donde el usuario deba elegir las opciones 1, 2, 3 o 4
def menu():
    try:
      while True:
        print("-"*60)
        print("Bienvenido al Registrador S-S,por favor seleccione una opción ")
        print("1. Ingresar asistencia")
        print("2. Mostrar asistencia")
        print("3. Eliminar asistencia")
        print("4. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            ingreso_asistencia()
        elif opcion == "2":
            mostrar_asistencia()
        elif opcion == "3":
            eliminar_asistencia()
        elif opcion == "4":
            print("="*60)
            print("Muchas gracias por usar el Registrador S-S, Cerrando el programa")
            break
        else:
            print("Opción inválida. Por favor, ingrese de nuevo (1, 2, 3 o 4).")
    #Exception es para que salga error en la parte especifica del fallo 
    except Exception as e:
        print(f"Ocurrió un error inesperado en el menú: {e}")

# Bloque principal para ejecutar el menú
menu()
