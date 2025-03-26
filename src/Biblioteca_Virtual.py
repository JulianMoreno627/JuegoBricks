class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.prestado = False

    def prestar(self):
        if not self.prestado:
            self.prestado = True
            return f"Libro '{self.titulo}' prestado con éxito."
        return f"El libro '{self.titulo}' ya está prestado."

    def devolver(self):
        if self.prestado:
            self.prestado = False
            return f"Libro '{self.titulo}' devuelto con éxito."
        return f"El libro '{self.titulo}' no estaba prestado."


class Biblioteca:
    def __init__(self):
        self.catalogo = []

    def agregar_libro(self, titulo, autor, anio):
        libro = Libro(titulo, autor, anio)
        self.catalogo.append(libro)
        return f"Libro '{titulo}' agregado a la biblioteca."

    def mostrar_catalogo(self):
        if not self.catalogo:
            return "La biblioteca no tiene libros."
        return "\n".join([f"{libro.titulo} - {libro.autor} ({libro.anio}) {'[Prestado]' if libro.prestado else ''}" for libro in self.catalogo])

    def prestar_libro(self, titulo):
        for libro in self.catalogo:
            if libro.titulo.lower() == titulo.lower():
                return libro.prestar()
        return f"El libro '{titulo}' no se encontró en la biblioteca."

    def devolver_libro(self, titulo):
        for libro in self.catalogo:
            if libro.titulo.lower() == titulo.lower():
                return libro.devolver()
        return f"El libro '{titulo}' no se encontró en la biblioteca."


def main():
    biblioteca = Biblioteca()
    
    while True:
        print("\n📚 Biblioteca Virtual 📚")
        print("1. Agregar libro")
        print("2. Mostrar catálogo")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            titulo = input("Título del libro: ")
            autor = input("Autor del libro: ")
            anio = input("Año de publicación: ")
            print(biblioteca.agregar_libro(titulo, autor, anio))

        elif opcion == "2":
            print("\n📖 Catálogo de la Biblioteca:")
            print(biblioteca.mostrar_catalogo())

        elif opcion == "3":
            titulo = input("Título del libro a prestar: ")
            print(biblioteca.prestar_libro(titulo))

        elif opcion == "4":
            titulo = input("Título del libro a devolver: ")
            print(biblioteca.devolver_libro(titulo))

        elif opcion == "5":
            print("Saliendo de la Biblioteca Virtual...")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
