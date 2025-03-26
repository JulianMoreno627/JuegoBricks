import pytest
from src.GestorTareas import Tarea, GestorTareas

# Prueba 1: Crear una tarea
def test_crear_tarea():
    tarea = Tarea("Comprar leche", "Ir al supermercado", 2)
    assert tarea.titulo == "Comprar leche"
    assert tarea.descripcion == "Ir al supermercado"
    assert tarea.prioridad == 2
    assert tarea.completada is False

# Prueba 2: Marcar una tarea como completada
def test_marcar_completada():
    tarea = Tarea("Lavar el coche", "Usar agua y jabón", 3)
    tarea.marcar_completada()
    assert tarea.completada is True

# Prueba 3: Agregar una tarea al gestor
def test_agregar_tarea():
    gestor = GestorTareas()
    tarea = Tarea("Hacer ejercicio", "30 minutos de cardio", 1)
    gestor.agregar_tarea(tarea)
    assert len(gestor.tareas) == 1

# Prueba 4: Eliminar una tarea
def test_eliminar_tarea():
    gestor = GestorTareas()
    tarea = Tarea("Leer un libro", "Novela de ciencia ficción", 2)
    gestor.agregar_tarea(tarea)
    gestor.eliminar_tarea("Leer un libro")
    assert len(gestor.tareas) == 0
