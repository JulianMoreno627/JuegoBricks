import pytest
from src.Biblioteca_Virtual import Libro, Biblioteca

# Prueba 1: Crear un libro
def test_crear_libro():
    libro = Libro("El principito", "Antoine de Saint-Exupéry", "123456")
    assert libro.titulo == "El principito"
    assert libro.autor == "Antoine de Saint-Exupéry"
    assert libro.isbn == "123456"  # ISBN sí existe ahora

# Prueba 2: Agregar un libro a la biblioteca
def test_agregar_libro():
    biblioteca = Biblioteca()
    biblioteca.agregar_libro("1984", "George Orwell", "654321")  # Se pasan los parámetros correctos
    assert len(biblioteca.libros) == 1

# Prueba 3: Buscar un libro existente
def test_buscar_libro_existente():
    biblioteca = Biblioteca()
    biblioteca.agregar_libro("Cien años de soledad", "Gabriel García Márquez", "789101")
    resultado = biblioteca.buscar_libro("Cien años de soledad")
    assert resultado is not None
    assert resultado.titulo == "Cien años de soledad"

# Prueba 4: Buscar un libro inexistente
def test_buscar_libro_inexistente():
    biblioteca = Biblioteca()
    resultado = biblioteca.buscar_libro("Libro Desconocido")
    assert resultado is None
