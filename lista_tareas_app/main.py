"""
Aplicación de escritorio tipo To-Do List desarrollada en Python con Tkinter,
aplicando Programación Orientada a Objetos (POO), arquitectura modular por capas
y manejo de eventos de usuario (teclado y ratón).
"""

from servicios.tarea_servicio import TareaServicio
from ui.app_tkinter import AppTkinter


def main():
    # Instancia la capa de servicio
    servicio = TareaServicio()
    #Construye la UI inyectando el servicio.
    app = AppTkinter(servicio)
    # Arrancar el bucle de eventos a través del único método público
    app.run()


if __name__ == "__main__":
    main()