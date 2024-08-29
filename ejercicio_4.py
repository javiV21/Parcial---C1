class Animal:
    def __init__(self, identificacion, especie, edad, peso, area):
        self.identificacion = identificacion
        self.especie = especie
        self.edad = edad
        self.peso = peso
        self.area = area
        self.tratamiento = None

    def asignar_tratamiento(self, medicamento, dosis, frecuencia):
        self.tratamiento = {
            "medicamento": medicamento,
            "dosis": dosis,
            "frecuencia": frecuencia
        }

    def mostrar_datos(self):
        print(f"Numero de identificacion: {self.identificacion}")
        print(f"Especie del animal: {self.especie}")
        print(f"Edad del animal: {self.edad} años")
        print(f"Peso: {self.peso} kg")
        print(f"Área del zoológico: {self.area}")
        if self.tratamiento:
            print(f"Tratamiento: {self.tratamiento['medicamento']}")
            print(f"Dosis: {self.tratamiento['dosis']}")
            print(f"tiempo de pausa para nuevo tratamiento : {self.tratamiento['frecuencia']}")
        else:
            print("No se requiere tratamiento.")
        print("---------------------------")
        print()

class Zoologico:
    def __init__(self):
        self.animales = []

    def agregar_animal(self, animal):
        self.animales.append(animal)

    def listar_animales(self):
        if self.animales:
            print("\nLista de todos los animales en el zoológico:")
            for animal in self.animales:
                animal.mostrar_datos()
        else:
            print("\nNo hay animales registrados en el zoológico.")
    
    def listar_animales_en_tratamiento(self):
        print("\nAnimales en tratamiento:")
        en_tratamiento = False
        for animal in self.animales:
            if animal.tratamiento:
                animal.mostrar_datos()
                en_tratamiento = True
        if not en_tratamiento:
            print("No hay animales en tratamiento.")
        print()

zoologico = Zoologico()

Menu = 0
while Menu < 4:
    print("-----------------------")
    print(" * ZOOLÓGICO * ")
    print("-----------------------")
    print("1. Ingresar nuevo animal")
    print("2. Mostrar todos los animales")
    print("3. Mostrar animales en tratamiento")
    print("4. Salir")
    print("-----------------------------")
    
    op = input("Ingrese la operación que desea realizar: ")
    match op:
        case "1":
            especie = input("Ingrese la especie del animal: ")
            identificacion = input("Ingrese la identificacion del animal: ")
            while True:
                try:
                    edad = int(input("Ingrese la edad del animal (en años): "))
                    if(edad <= 0):
                        print("la edad debe ser mayor a cero")
                        continue
                    break
                except ValueError:
                    print("Error: la edad debe ser numérica. Por favor, intente de nuevo.")
            while True:
                try:
                    
                    peso = float(input("Ingrese el peso del animal (en kg): "))
                    if(peso <= 0):
                        print("el peso debe ser mayor a cero")
                        continue
                    break
                except ValueError:
                    print("Error: el peso debe ser numérico. Por favor, intente de nuevo.")
            area = input("Ingrese el área del zoológico donde se encuentra el animal: ")

            animal = Animal(identificacion, especie, edad, peso, area)
            
            tratamiento = input("¿El animal necesita tratamiento? (s/n): ")
            if tratamiento.lower() == 's':
                medicamento = input("Ingrese el nombre del medicamento: ")
                dosis = input("Ingrese la dosis: ")
                frecuencia = input("Ingrese el tiempo de pausa para un nuevo tratamiento: ")
                animal.asignar_tratamiento(medicamento, dosis, frecuencia)

            zoologico.agregar_animal(animal)
            
        case "2":
            zoologico.listar_animales()
            regresar_menu = input("¿Desea regresar al menú principal? (s/n): ")
            if regresar_menu.lower() != 's':
                print("Gracias por utilizar el sistema.")
                break

        case "3":
            zoologico.listar_animales_en_tratamiento()
            regresar_menu = input("¿Desea regresar al menú principal? (s/n): ")
            if regresar_menu.lower() != 's':
                print("Gracias por utilizar el sistema.")
                break
        
        case "4":
            print("Gracias por utilizar el sistema.")
            break

        case _:
            print("Operación inválida, por favor intente de nuevo.")
            continue

