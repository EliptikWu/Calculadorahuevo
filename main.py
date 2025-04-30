from components.add import sumar_huevos
from components.subtract import restar_huevos
from components.division import dividir
from components.multiplication import multiplicar_huevos

def main():
    """Programa principal de la Calculadora Cuenta Huevos."""
    print("=== Calculadora Cuenta Huevos ===")
    while True:
        print("\nSeleccione una operación:")
        print("1. Sumar huevos")
        print("2. Restar huevos")
        print("3. Multiplicar huevos")
        print("4. Dividir huevos")
        print("5. Salir")
        opcion = input("Opción (1/2/3/4/5): ")

        if opcion == '5':
            print("¡Hasta luego!")
            break

        # Pedir entradas comunes
        total = input("Total de huevos que tienes: ")
        valor = input("Ingrese el valor para la operación: ")

        # Ejecutar la operación seleccionada
        if opcion == '1':
            resultado = sumar_huevos(total, valor)
        elif opcion == '2':
            try:
                resultado = restar_huevos(int(total), int(valor))
            except ValueError:
                resultado = "Error: Ingresa números enteros válidos"
        elif opcion == '3':
            try:
                resultado = multiplicar_huevos(int(total), int(valor))
            except ValueError:
                resultado = "Error: Ingresa números enteros válidos"
        elif opcion == '4':
            try:
                resultado = dividir(int(total), int(valor))
            except ValueError:
                resultado = "Error: Ingresa números enteros válidos"
        else:
            print("Opción inválida, por favor selecciona del 1 al 5.")
            continue

        print(f"Resultado: {resultado}")


if __name__ == "__main__":
    main()
