# ==============================
# Código: Gestor de Tareas con Menú Interactivo
# ==============================

class Tarea:
    def __init__(self, titulo, descripcion, prioridad):
        self.titulo = titulo
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.completada = False
    
    def marcar_completada(self):
        self.completada = True

    def __str__(self):
        estado = "Completada" if self.completada else "Pendiente"
        return f"[{estado}] {self.titulo} - Prioridad: {self.prioridad}"


class GestorTareas:
    def __init__(self):
        self.tareas = []
    
    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
    
    def eliminar_tarea(self, titulo):
        self.tareas = [t for t in self.tareas if t.titulo.lower() != titulo.lower()]
    
    def listar_tareas(self):
        return sorted(self.tareas, key=lambda x: x.prioridad, reverse=True)
    
    def obtener_tarea(self, titulo):
        for tarea in self.tareas:
            if tarea.titulo.lower() == titulo.lower():
                return tarea
        return None


def main():
    gestor = GestorTareas()

    while True:
        print("\n📝 Gestor de Tareas 📝")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            titulo = input("Título de la tarea: ")
            descripcion = input("Descripción: ")
            prioridad = int(input("Prioridad (1-5): "))
            tarea = Tarea(titulo, descripcion, prioridad)
            gestor.agregar_tarea(tarea)
            print(f"Tarea '{titulo}' agregada.")

        elif opcion == "2":
            print("\n📋 Lista de Tareas:")
            tareas = gestor.listar_tareas()
            if tareas:
                for tarea in tareas:
                    print(tarea)
            else:
                print("No hay tareas registradas.")

        elif opcion == "3":
            titulo = input("Título de la tarea a completar: ")
            tarea = gestor.obtener_tarea(titulo)
            if tarea:
                tarea.marcar_completada()
                print(f"Tarea '{titulo}' marcada como completada.")
            else:
                print(f"No se encontró la tarea '{titulo}'.")

        elif opcion == "4":
            titulo = input("Título de la tarea a eliminar: ")
            gestor.eliminar_tarea(titulo)
            print(f"Tarea '{titulo}' eliminada.")

        elif opcion == "5":
            print("Saliendo del Gestor de Tareas...")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
