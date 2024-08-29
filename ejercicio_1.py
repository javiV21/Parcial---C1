class Paciente:
    def __init__(self, nombre, edad, motivo, fecha_consulta):
        self.nombre = nombre
        self.edad = edad
        self.motivo = motivo
        self.fecha_consulta = fecha_consulta
        self.consulta_asignada = True

class Doctor:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad
        self.disponible = True

class Secretaria:
    def __init__(self):
        self.pacientes = []
        self.sala_espera = []

    def registrar_paciente(self):
        while True:
            nombre = input("Ingrese el nombre del paciente: ")

            # Verificar si el paciente ya está registrado
            paciente_existente = next((p for p in self.pacientes if p.nombre == nombre), None)
            
            if paciente_existente:
                print(f"{nombre} ya tiene una consulta previa para el {paciente_existente.fecha_consulta}. Dirigiéndose a la sala de espera.")
                self.sala_espera.append(paciente_existente)
            else:
                edad = int(input("Ingrese la edad del paciente: "))
                motivo = input("Ingrese el motivo de la consulta: ")
                fecha_consulta = input("Ingrese la fecha de la consulta (DD/MM/AAAA): ")
                nuevo_paciente = Paciente(nombre, edad, motivo, fecha_consulta)
                self.pacientes.append(nuevo_paciente)
                print(f"Paciente {nombre} registrado con éxito y consulta asignada para el {fecha_consulta}.")

            otro_paciente = input("¿Desea registrar otro paciente? (s/n): ").strip().lower()
            if otro_paciente != 's':
                break

    def paciente_previamente_registrado(self):
        print("El paciente ha sido movido a la sala de espera.")
        # Regresar al menú sin hacer nada más
        return

    def mostrar_pacientes(self):
        print("Pacientes registrados:")
        for p in self.pacientes:
            print(f"- {p.nombre}, Motivo: {p.motivo}, Fecha de consulta: {p.fecha_consulta}")

def menu():
    secretaria = Secretaria()
    
    while True:
        print("\n--- Consultorio Médico ---")
        print("1. Registrar nuevo paciente")
        print("2. Paciente previamente registrado (Mover a sala de espera)")
        print("3. Mostrar pacientes registrados")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            secretaria.registrar_paciente()
        elif opcion == "2":
            secretaria.paciente_previamente_registrado()
        elif opcion == "3":
            secretaria.mostrar_pacientes()
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Iniciar el menú
menu()
