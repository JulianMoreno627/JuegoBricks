class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn  # Asegúrate de que ISBN existe en la clase

    def __str__(self):
        return f"{self.titulo} de {self.autor} (ISBN: {self.isbn})"


class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, titulo, autor, isbn):
        """ Se espera recibir los parámetros y crear el objeto dentro de la función. """
        libro = Libro(titulo, autor, isbn)
        self.libros.append(libro)

    def buscar_libro(self, titulo):
        """ Se agrega el método que faltaba. """
        for libro in self.libros:
            if libro.titulo == titulo:
                return libro
        return None
