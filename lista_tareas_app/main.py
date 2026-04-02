"""
Aplicación de escritorio tipo To-Do List desarrollada en Python con Tkinter,
aplicando Programación Orientada a Objetos (POO), arquitectura modular por capas,
garantizando una correcta separación de responsabilidades.
Esta aplicación permite la gestión de tareas al permitir agregar, completar y eliminar
actividades de manera sencilla e intuitiva, proporcionando una experiencia de usuario
fluida, eficiente y mejorada.

Esta versión corresponde a una mejora del sistema base, incorporando:

- Manejo de eventos de teclado y ratón mediante .bind()
- Atajos de teclado para mejorar la interacción del usuario:
  * Enter → añadir tarea
  * Ctrl + C → marcar como completada
  * Ctrl + D / Delete → eliminar tarea
  * Escape → cerrar aplicación
- Feedback visual dinámico mediante una barra de eventos
- Actualización en tiempo real del estado de las tareas

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