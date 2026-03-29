"""
Aplicación de escritorio tipo To-Do List desarrollada en Python con Tkinter,
aplicando Programación Orientada a Objetos (POO), arquitectura modular por capas
y manejo de eventos de usuario (teclado para agregar tareas y ratón para interactuar).
Esta aplicación permite la gestión de tareas al permitir agregar, completar y eliminar
actividades de manera sencilla e intuitiva, proporcionando una experiencia de usuario
fluida y eficiente.
"""

# Importa la clase de servicio y la interfaz gráfica
from servicios.tarea_servicio import TareaServicio
from ui.app_tkinter import AppTkinter

# Función principal para iniciar la aplicación
def main():
    # Instancia la capa de servicio
    servicio = TareaServicio()
    # Construye la UI inyectando el servicio.
    app = AppTkinter(servicio)
    # Inicia la aplicación
    app.run()

# Punto de entrada del programa, que llama a la función main para iniciar el sistema
if __name__ == "__main__":
    main()