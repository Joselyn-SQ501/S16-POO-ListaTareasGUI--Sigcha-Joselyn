# Importación de librerías necesarias para la interfaz gráfica
import tkinter as tk
from tkinter import ttk, messagebox
from servicios.tarea_servicio import TareaServicio

# Paleta de colores y tipografía para la ui
COLORS = {
    "COLOR_BG"       : "#1E1E2E" ,  # Fondo principal (oscuro azulado)
    "COLOR_SURFACE"  : "#2A2A3E" ,  # Superficie de tarjetas / frames
    "COLOR_ACCENT"   : "#7034D7" ,  # Violeta — color de acento
    "COLOR_ACCENT2"  : "#A78BFA" ,  # Violeta claro — hover / completadas
    "COLOR_TEXT"     : "#E2E8F0" ,  # Texto principal
    "COLOR_MUTED"    : "#F2FFF6" ,  # Texto secundario / tareas completadas
    "COLOR_SUCCESS"  : "#1EA951" ,  # Verde — confirmación
    "COLOR_DANGER"   : "#D83939" ,  # Rojo — eliminar
    "COLOR_DONE_BG"  : "#006330" ,  # Fondo de fila completada
    "COLOR_PENDING" : "#690303",   # Fondo de fila pendiente
}

FONT_TITLE  = ("Courier New", 20, "bold")
FONT_LABEL  = ("Courier New", 11, "bold")
FONT_ENTRY  = ("Courier New", 11)
FONT_BTN    = ("Courier New", 10, "bold")
FONT_TABLE  = ("Courier New", 12, "bold")
FONT_HINT   = ("Courier New",  10)

# Clase que representa la interfaz gráfica del sistema
class AppTkinter:

    # Constructor de la clase de interfaz
    def __init__(self, servicio):
        # Recibe la capa de servicio para interactuar con la lógica del sistema
        self.servicio = servicio
        
        # Inicializa la ventana principal y los componentes de la interfaz
        self.root = tk.Tk()
        self._entry_tarea:  tk.Entry     = None  
        self._tree:         ttk.Treeview = None  
        self._lbl_contador: tk.Label     = None
        self._lbl_evento: tk.Label     = None
        
        # Construye todos los elementos de la interfaz
        self._configurar_ventana()
        self._crear_ui()
        self._registrar_eventos()
        self._refrescar()

    # Método que inicia la ejecución de la interfaz
    def run(self):
        self.root.mainloop()

    # Método encargado de configurar las propiedades de la ventana principal
    def _configurar_ventana (self):
        self.root.title("Lista de Tareas")
        self.root.geometry("880x630")
        self.root.resizable(True, True)
        self.root.configure(bg=COLORS["COLOR_BG"])
        self.root.minsize(850, 610)

    # Método encargado de crear todos los componentes visuales
    def _crear_ui(self):
        
        # Cada sección de la interfaz se delega a un método propio para mantener este método limpio y legible
        self._crear_header()
        self._crear_seccion_entrada()
        self._crear_tabla_tareas()
        self._crear_barra_indicaciones()
        self._crear_barra_eventos()
    
    # Submétodo para crear el encabezado
    def _crear_header(self):
        header = tk.Frame(self.root, bg=COLORS["COLOR_BG"])
        header.pack(fill="x", padx=24, pady=(24, 8))
        
        # Título 
        tk.Label(
            header,
            text="📝LISTA DE TAREAS✍️",
            font=FONT_TITLE,
            fg=COLORS["COLOR_TEXT"],
            bg=COLORS["COLOR_BG"],
        ).pack(side="left")
        
        # Contador de tareas
        self._lbl_contador = tk.Label(
            header,
            text="",
            font=FONT_LABEL,
            fg=COLORS["COLOR_MUTED"],
            bg=COLORS["COLOR_BG"],
        )
        self._lbl_contador.pack(side="right", pady=6)
   
    # Submétodo para crear la sección de entrada de nuevas tareas y botones de acción
    def _crear_seccion_entrada(self):
        
        cont_input = tk.Frame(self.root, bg=COLORS["COLOR_BG"])
        cont_input.pack(fill="x", padx=24, pady=4)
        
        # Variable de control para el campo de entrada de texto
        self.var_tarea = tk.StringVar()
        
        # Campo de entrada que describe la tarea
        self._entry_tarea = tk.Entry(
            cont_input,
            textvariable=self.var_tarea,
            font=FONT_ENTRY,
            bg="white",
            fg=COLORS["COLOR_BG"],
            insertbackground=COLORS["COLOR_ACCENT2"],    # Color del cursor de texto
            relief="flat",
            bd=0,
        )
        self._entry_tarea.pack(side="left", fill="x", expand=True, ipady=8, padx=(0, 12)) 
     
        # Botones de acción para agregar, completar y eliminar tareas, cada uno con su propio estilo y color
        tk.Button(
            cont_input, 
            text="✚ Añadir tarea", 
            font= FONT_BTN, 
            bg=COLORS["COLOR_ACCENT"], 
            fg= "white", 
            activebackground=COLORS["COLOR_ACCENT2"], 
            activeforeground="white", 
            relief="flat",  
            padx=16, 
            pady=8,
            command=self._agregar).pack(side="left", padx=(0, 10))
        
        tk.Button(
            cont_input, 
            text="✔ Marcar Completada", 
            font= FONT_BTN, 
            bg=COLORS["COLOR_SUCCESS"], 
            fg= "white", 
            activebackground="#16a34a", 
            activeforeground="white", 
            relief="flat", 
            padx=16,
            pady=8,
            command=self._completar).pack(side="left", padx=(0, 10))
        
        tk.Button(
            cont_input, 
            text="🗑 Eliminar", 
            font= FONT_BTN, 
            bg=COLORS["COLOR_DANGER"], 
            fg= "white", 
            activebackground="#b91c1c", 
            activeforeground="white", 
            relief="flat",
            padx=16,
            pady=8,
            command=self._eliminar).pack(side="right")
    
    # Submétodo para crear la tabla que muestra las tareas, utilizando ttk.Treeview para una mejor apariencia y funcionalidad
    def _crear_tabla_tareas(self):
        frame_lista = tk.Frame(self.root, bg=COLORS["COLOR_BG"])
        frame_lista.pack(fill="both", expand=True, padx=24, pady=8)
        
        # El estilo se extrae a un método propio para no sobrecargar este método
        self.__aplicar_estilo_treeview()

        # Creación de la tabla con columnas necesarias para las tareas
        self._tree = ttk.Treeview(
            frame_lista,
            columns=("id", "descripcion", "estado"),
            show="headings",
            style="Tareas.Treeview",
            selectmode="browse",
        )
        
        # Configuración de los encabezados de columna
        self._tree.heading("id", text="ID")
        self._tree.heading("descripcion", text="Descripción")
        self._tree.heading("estado", text="Estado")
      
        # Anchos de columna y comportamiento de estiramiento
        self._tree.column("id",  width=50,  anchor="center", stretch=False)
        self._tree.column("descripcion", minwidth=300, anchor="w")
        self._tree.column("estado", width=160, anchor="center", stretch=False)

        # Tag "pendiente" coleareando con el color rojo para resaltar las tareas que aún no se han completado
        self._tree.tag_configure(
            "pendiente",
            foreground="#FFE4E4",
            background=COLORS["COLOR_PENDING"],
        )
        # Tag "completada" coloreando con el color verde para resaltar las tareas finalizadas
        self._tree.tag_configure(
            "completada",
            foreground="#daffe8",
            background=COLORS["COLOR_DONE_BG"],
        )
        
        # Agrega una barra de desplazamiento vertical para la tabla, vinculada a la vista del Treeview
        scrollbar = ttk.Scrollbar(frame_lista, orient="vertical", command=self._tree.yview)
        self._tree.configure(yscrollcommand=scrollbar.set)
        self._tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    # Método privado para aplicar estilos personalizados al Treeview
    def __aplicar_estilo_treeview(self) -> None:
        
        # Configuración de estilo general para el Treeview, incluyendo colores de fondo, texto, altura de filas y fuente
        style = ttk.Style()
        style.theme_use("default")
        style.configure(
            "Tareas.Treeview",
            background=COLORS["COLOR_SURFACE"],
            foreground=COLORS["COLOR_MUTED"],
            rowheight=38,
            fieldbackground=COLORS["COLOR_MUTED"],
            font=FONT_TABLE,
            borderwidth=0,
        )

        # Configuración de estilo para los encabezados de columna
        style.configure(
            "Tareas.Treeview.Heading",
            background=COLORS["COLOR_ACCENT2"],
            foreground=COLORS["COLOR_SURFACE"],
            font=FONT_TABLE,
            relief="flat",
        )

        # Configuración de estilo para la fila seleccionada
        style.map(
            "Tareas.Treeview",
            background=[("selected", COLORS["COLOR_ACCENT"])],
            foreground=[("selected", COLORS["COLOR_TEXT"])],
        )
    
    # Submétodo para crear una barra de indicaciones al pie de la interfaz, informando al usuario sobre atajos de teclado y acciones disponibles
    def _crear_barra_indicaciones(self):
        indications = tk.Frame(self.root, bg=COLORS["COLOR_BG"])
        indications.pack(fill="x", padx=24, pady=(4, 20))
        
        # Texto de indicaciones para el usuario
        tk.Label(
            indications,
            text="↩ Enter (añadir) | Doble clic o Ctrl+C (completar) | Ctrl+D/Delete (eliminar) | Esc (salir)",
            font=FONT_HINT,
            fg=COLORS["COLOR_MUTED"],
            bg=COLORS["COLOR_BG"],
        ).pack(side="right")
    
    # Barra de eventos para mostrar mensajes relacionados con las acciones del usuario, como confirmaciones o errores, proporcionando retroalimentación inmediata sobre las interacciones con la aplicación
    def _crear_barra_eventos(self):
        frame_evento = tk.Frame(self.root, bg=COLORS["COLOR_BG"])
        frame_evento.pack(fill="x", padx=24, pady=(0, 10))

        self._lbl_evento = tk.Label(
            frame_evento,
            text="Eventos del sistema aparecerán aquí...",
            font=FONT_HINT,
            fg=COLORS["COLOR_ACCENT2"],
            bg=COLORS["COLOR_BG"]
        )
        self._lbl_evento.pack(side="left")

    # Método encargado de registrar los eventos de usuario
    def _registrar_eventos(self):
        # Evento de doble click
        self._tree.bind("<Double-1>", self._doble_click)
        
        # Evento de presionar Enter en el campo de entrada para agregar la tarea
        self._entry_tarea.bind("<Return>", self._on_enter)
        
        # Evento de atajo de teclado para completar tarea con teclas Ctrl+C 
        self.root.bind("<Control-c>", self._atajo_completar)
        self.root.bind("<Control-C>", self._atajo_completar)
        
        # Evento de eliminar tarea seleccionada con Delete o Ctrl+D
        self.root.bind("<Delete>", self._atajo_eliminar)
        self.root.bind("<Control-d>", self._atajo_eliminar)
        self.root.bind("<Control-D>", self._atajo_eliminar)
       
        # Evento de cerrar aplicación con Escape
        self.root.bind("<Escape>", self._atajo_salir)
        
        # Evento de cierre de ventana para confirmar antes de salir de la aplicación
        self.root.protocol ("WM_DELETE_WINDOW", self._cerrar_aplicacion)
    
    # Eventos 
    
    # Evento para agregar tareas al presionar Enter
    def _on_enter(self, event):
        self._lbl_evento.config(text="Enter detectado → tarea añadida")
        self._agregar()

    # Evento para completar tareas al hacer doble clic sobre ellas en la tabla
    def _doble_click(self, event):
        self._lbl_evento.config(text="Doble clic → tarea completada")
        self._completar()

    # Evento para completar tareas con atajo de teclado Ctrl+C
    def _atajo_completar(self, event):
        if self.root.focus_get() == self._entry_tarea:
            return
        self._lbl_evento.config(text="Tecla Ctrl+C → completar tarea")
        self._completar()

    #   Evento para eliminar tareas con atajo de teclado Ctrl+D o Delete
    def _atajo_eliminar(self, event):
        if self.root.focus_get() == self._entry_tarea:
            return
        self._lbl_evento.config(text="Tecla Ctrl+D/Delete → eliminar tarea seleccionada")
        self._eliminar()

    #  Evento para cerrar la aplicación con atajo de teclado Escape, mostrando un mensaje de confirmación antes de proceder con el cierre
    def _atajo_salir(self, event):
        self._lbl_evento.config(text="Tecla Escape → cerrando aplicación")
        self._cerrar_aplicacion()
    
    # Evento para confirmar antes de cerrar la aplicación, evitando cierres accidentales y pérdida de datos no guardados
    def _cerrar_aplicacion(self):
        confirmado = messagebox.askyesno(
            "Salir de la aplicación",
            "¿Estás seguro de que deseas cerrar la aplicación?",
            parent=self.root,
        )
        if confirmado:
            self.root.destroy()

    # Método de acción para agregar tareas con sus debidas validaciones
    def _agregar(self):
        try:
            self.servicio.agregar_tarea(self.var_tarea.get())
            self.var_tarea.set("")
            self._refrescar()
        except Exception as e:
            messagebox.showerror("Entrada inválida", str(e), parent=self.root)
    
    # Método de acción para completar tareas, obteniendo la tarea seleccionada y manejando posibles errores
    def _completar(self):
        id_tarea = self._get_selected()
        if id_tarea is None:
            return
        
        try:
            self.servicio.completar_tarea(id_tarea)
            self._refrescar()
        except KeyError as e:
            messagebox.showerror("Error", str(e), parent=self.root)
    
    # Método de acción para eliminar tareas, solicitando confirmación al usuario antes de proceder con la eliminación y manejando posibles errores
    def _eliminar(self):

        id_tarea = self._get_selected()
        
        if id_tarea is None:
            return

        confirmado = messagebox.askyesno(
            "Confirmar eliminación",
            "¿Estás seguro de que deseas eliminar esta tarea?",
            parent=self.root,
        )

        if confirmado:
            try:

                self.servicio.eliminar_tarea(id_tarea)
                self._refrescar()
            
            except KeyError as e:
                messagebox.showerror("Error", str(e), parent=self.root)
    
    # Método privado para obtener la tarea seleccionada en la tabla, con opción de mostrar un mensaje de advertencia si no hay selección
    def _get_selected(self, silencioso: bool = False):
        seleccion = self._tree.selection()

        if not seleccion:
            if not silencioso:
                messagebox.showinfo(
                    "Sin selección",
                    "Por favor, selecciona una tarea de la lista.",
                    parent=self.root,
                )
            return None
        return int(seleccion[0])
    
    # Método privado para refrescar la tabla de tareas, eliminando todas las filas actuales y volviendo a cargar las tareas desde el servicio
    def _refrescar(self):
        
        id_previo = self._get_selected(silencioso=True)
        
        for i in self._tree.get_children():
            self._tree.delete(i)

        tareas = self.servicio.listar_tareas()
        item_a_reseleccionar = None

        for tarea in tareas:
            if tarea.completada:
                estado_texto = "✅  Completada"
                tag = ("completada",)   # Verde
            else:
                estado_texto = "❌  Pendiente"
                tag = ("pendiente",)    # Rojo
        
            iid = self._tree.insert(
                "",
                "end",
                iid=str(tarea.id),
                values=(tarea.id, tarea.descripcion, estado_texto),
                tags=tag,
            )
            if tarea.id == id_previo:
                item_a_reseleccionar = iid

        # Restaurar la fila que estaba seleccionada antes del refresco
        if item_a_reseleccionar:
            self._tree.selection_set(item_a_reseleccionar)
            self._tree.focus(item_a_reseleccionar)

        # Actualizar el contador del header
        pendientes = sum(1 for t in tareas if not t.completada)
        self._lbl_contador.config(
            text=f"{pendientes} pendiente(s)  /  {len(tareas)} total"
        )
