from components.subtract import restar_huevos

def main():
    print("=== Calculadora Cuenta Huevos ===")
    total = int(input("Total de huevos que tienes: "))
    a_restar = int(input("¿Cuántos huevos quieres restar? "))
    restantes = restar_huevos(total, a_restar)
    print(f"Huevos restantes: {restantes}")

if __name__ == "__main__":
    main()
