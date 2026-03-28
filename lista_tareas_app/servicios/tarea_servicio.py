from modelos.tarea import Tarea


class TareaServicio:

    def __init__(self):
        self._tareas: dict[int, Tarea] = {}
        self._contador = 1

    def agregar_tarea(self, descripcion: str):
        descripcion = (descripcion or "").strip()

        if not descripcion:
            raise ValueError("La descripción de la tarea no puede estar vacía.")

        tarea = Tarea(self._contador, descripcion)
        self._tareas[self._contador] = tarea
        self._contador += 1

    def completar_tarea(self, id_tarea: int):
        if id_tarea not in self._tareas:
            raise ValueError("La tarea no existe.")

        self._tareas[id_tarea].marcar_completada()

    def eliminar_tarea(self, id_tarea: int):
        if id_tarea not in self._tareas:
            raise ValueError("La tarea no existe.")

        del self._tareas[id_tarea]

    def listar_tareas(self):
        return list(self._tareas.values())