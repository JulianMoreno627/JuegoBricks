import pytest
from src.Sistema_Reserva import Reserva, SistemaReservas

# Prueba 1: Crear una reserva
def test_crear_reserva():
    reserva = Reserva("Carlos Pérez", "2025-04-10", "18:30", 4)
    assert reserva.cliente == "Carlos Pérez"
    assert reserva.fecha == "2025-04-10"
    assert reserva.hora == "18:30"
    assert reserva.num_personas == 4

# Prueba 2: Agregar una reserva al sistema
def test_agregar_reserva():
    sistema = SistemaReservas()
    reserva = Reserva("Ana Gómez", "2025-05-15", "20:00", 2)
    sistema.agregar_reserva(reserva)
    assert len(sistema.reservas) == 1

# Prueba 3: Cancelar una reserva existente
def test_cancelar_reserva():
    sistema = SistemaReservas()
    reserva = Reserva("Luis Torres", "2025-06-20", "19:45", 3)
    sistema.agregar_reserva(reserva)
    sistema.cancelar_reserva("Luis Torres", "2025-06-20", "19:45")
    assert len(sistema.reservas) == 0

# Prueba 4: Buscar una reserva por cliente
def test_buscar_reserva():
    sistema = SistemaReservas()
    reserva1 = Reserva("Marta Ruiz", "2025-07-22", "21:00", 2)
    reserva2 = Reserva("Marta Ruiz", "2025-08-10", "19:00", 4)
    sistema.agregar_reserva(reserva1)
    sistema.agregar_reserva(reserva2)
    
    resultado = sistema.buscar_reserva("Marta Ruiz")
    assert len(resultado) == 2

