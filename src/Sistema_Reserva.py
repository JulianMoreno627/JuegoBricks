# ==============================
# Código: Sistema de Reservas con Menú Interactivo
# ==============================

class Reserva:
    def __init__(self, cliente, fecha, hora, num_personas):
        self.cliente = cliente
        self.fecha = fecha
        self.hora = hora
        self.num_personas = num_personas
    
    def __str__(self):
        return f"Reserva de {self.cliente} para {self.num_personas} personas el {self.fecha} a las {self.hora}"


class SistemaReservas:
    def __init__(self):
        self.reservas = []
    
    def agregar_reserva(self, reserva):
        self.reservas.append(reserva)
    
    def cancelar_reserva(self, cliente, fecha, hora):
        self.reservas = [r for r in self.reservas if not (r.cliente.lower() == cliente.lower() and r.fecha == fecha and r.hora == hora)]
    
    def listar_reservas(self):
        return sorted(self.reservas, key=lambda r: (r.fecha, r.hora))
    
    def buscar_reserva(self, cliente):
        return [r for r in self.reservas if r.cliente.lower() == cliente.lower()]


def main():
    sistema = SistemaReservas()

    while True:
        print("\n📅 Sistema de Reservas 📅")
        print("1. Agregar reserva")
        print("2. Listar reservas")
        print("3. Buscar reserva por cliente")
        print("4. Cancelar reserva")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            cliente = input("Nombre del cliente: ")
            fecha = input("Fecha de la reserva (YYYY-MM-DD): ")
            hora = input("Hora de la reserva (HH:MM): ")
            num_personas = int(input("Número de personas: "))
            reserva = Reserva(cliente, fecha, hora, num_personas)
            sistema.agregar_reserva(reserva)
            print(f"✅ Reserva para {cliente} agregada.")

        elif opcion == "2":
            print("\n📋 Lista de Reservas:")
            reservas = sistema.listar_reservas()
            if reservas:
                for reserva in reservas:
                    print(reserva)
            else:
                print("No hay reservas registradas.")

        elif opcion == "3":
            cliente = input("Nombre del cliente a buscar: ")
            reservas = sistema.buscar_reserva(cliente)
            if reservas:
                for reserva in reservas:
                    print(reserva)
            else:
                print(f"No se encontraron reservas para {cliente}.")

        elif opcion == "4":
            cliente = input("Nombre del cliente: ")
            fecha = input("Fecha de la reserva (YYYY-MM-DD): ")
            hora = input("Hora de la reserva (HH:MM): ")
            sistema.cancelar_reserva(cliente, fecha, hora)
            print(f"❌ Reserva de {cliente} para el {fecha} a las {hora} cancelada.")

        elif opcion == "5":
            print("Saliendo del Sistema de Reservas...")
            break

        else:
            print("⚠️ Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
