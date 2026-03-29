# Importa el modelo existente del programa
from modelos.tarea import Tarea

# Clase encargada de la lógica del sistema
class TareaServicio:
    # Creación de un constructor vacío
    def __init__(self):
        self._tareas: dict[int, Tarea] = {} # Atributo privado que almacena las tareas registrados en un diccionario, cuya clave es el ID
        self._contador = 1 # Atributo privado que actúa como contador para asignar un ID único a cada tarea, iniciando en 1
    
    # Método para agregar una nueva tarea al sistema 
    def agregar_tarea(self, descripcion: str):
        descripcion = (descripcion or "").strip()
        
        # Validación  de que no esté vacía la tarea o solo con espacios
        if not descripcion:
            raise ValueError("La descripción de la tarea no puede estar vacía.")
        
        # Creación de la tarea
        tarea = Tarea(self._contador, descripcion)
        # Almacenamiento en el diccionario con su ID como clave y la tarea como valor
        self._tareas[self._contador] = tarea
        # Incrementa del contador e ID para la siguiente tarea
        self._contador += 1

    # Método para completar una tarea, cambiando su estado a completada
    def completar_tarea(self, id_tarea: int):
        # Validación de que la tarea exista en el sistema antes de marcarla como completada
        if id_tarea not in self._tareas:
            raise ValueError("La tarea no existe.")
        
        # Marca la tarea como completada utilizando el método de la clase Tarea
        self._tareas[id_tarea].marcar_completada()
    
    # Método para eliminar una tarea del sistema, validando que exista antes de eliminarla
    def eliminar_tarea(self, id_tarea: int):
        if id_tarea not in self._tareas:
            raise ValueError("La tarea no existe.")
        
        # Elimina la tarea del diccionario utilizando su ID como clave
        del self._tareas[id_tarea]
    
    # Método para listar todas las tareas registradas en el sistema, devolviendo una lista de objetos Tarea
    def listar_tareas(self):
        return list(self._tareas.values())