class Tarea:

    def __init__(self, id_tarea: int, descripcion: str):
        self.__id = id_tarea
        self.__descripcion = descripcion.strip()
        self.__completada = False

    # GETTERS
    @property
    def id(self):
        return self.__id

    @property
    def descripcion(self):
        return self.__descripcion

    @property
    def completada(self):
        return self.__completada

    # SETTER
    @descripcion.setter
    def descripcion(self, nueva_desc):
        if not nueva_desc.strip():
            raise ValueError("La tarea no puede estar vacía.")
        self.__descripcion = nueva_desc.strip()

    def marcar_completada(self):
        self.__completada = True

    def __repr__(self):
        estado = "✅" if self.completada else "❌"
        return f"[{estado}] ({self.__id}) {self.__descripcion}"
