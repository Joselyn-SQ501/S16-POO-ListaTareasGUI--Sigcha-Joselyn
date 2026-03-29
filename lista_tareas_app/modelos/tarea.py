# Clase que representa una tarea del sistema
class Tarea:
    
    # Constructor de la clase con datos y su tipo
    def __init__(self, id_tarea: int, descripcion: str):
        self._id = id_tarea # Atributo privado del identificador único de la tarea
        self._descripcion = descripcion.strip() # Atributo privado de la descripción de la tarea, sin espacios al inicio o final
        self._completada = False # Atributo privado que indica si la tarea está completada (inicialmente en False)

    # Métodos GETTERS que permiten acceder a los atributos privados de forma controlada
    @property
    def id(self):
        return self._id

    @property
    def descripcion(self):
        return self._descripcion

    @property
    def completada(self):
        return self._completada

    # Método SETTER que permiten modificar la descripción o tarea de forma controlada en caso de requerir una actualización
    @descripcion.setter
    def descripcion(self, nueva_desc):
        if not nueva_desc.strip():
            raise ValueError("La descripción de la tarea no puede estar vacía.")
        self._descripcion = nueva_desc.strip()
    
    # Método que marca la tarea como completada, cambiando su estado a True
    def marcar_completada(self):
        self._completada = True

    # Método que devuelve la información de la tarea
    def __repr__(self):
        estado = "✅" if self.completada else "❌"
        return f"[{estado}] ({self._id}) {self._descripcion}"
