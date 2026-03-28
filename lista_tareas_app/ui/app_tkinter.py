# Importación de librerías necesarias para la interfaz gráfica
import tkinter as tk
from tkinter import ttk, messagebox
from servicios.tarea_servicio import TareaServicio

# Paleta de colores y tipografía para la ui
COLORS = {
    "COLOR_BG"       : "#1E1E2E" ,  # Fondo principal (oscuro azulado)
    "COLOR_SURFACE"  : "#2A2A3E" ,  # Superficie de tarjetas / frames
    "COLOR_ACCENT"   : "#7C3AED" ,  # Violeta — color de acento
    "COLOR_ACCENT2"  : "#A78BFA" ,  # Violeta claro — hover / completadas
    "COLOR_TEXT"     : "#E2E8F0" ,  # Texto principal
    "COLOR_MUTED"    : "#64748B" ,  # Texto secundario / tareas completadas
    "COLOR_SUCCESS"  : "#22C55E" ,  # Verde — confirmación
    "COLOR_DANGER"   : "#EF4444" ,  # Rojo — eliminar
    "COLOR_DONE_BG"  : "#1A2E1A" ,  # Fondo de fila completada
    "COLOR_PENDING" : "#2E1A1A",   # Fondo de fila pendiente
    "COLOR_ENTRY_BG" : "#313150",   # Fondo del campo de texto
}

FONT_TITLE  = ("Segoe UI", 20, "bold")
FONT_SUBTITLE  = ("Segoe UI", 16, "bold")
FONT_LABEL  = ("Segoe UI", 10, "bold")
FONT_ENTRY  = ("Segoe UI", 11)
FONT_BTN    = ("Segoe UI", 10, "bold")
FONT_TABLE  = ("Segoe UI", 10, "bold")
FONT_HINT   = ("Segoe UI",  9)

# Clase que representa la interfaz gráfica del sistema
class AppTkinter:

    # Constructor de la clase de interfaz
    def __init__(self, servicio):
        # Recibe la capa de servicio para interactuar con la lógica del sistema
        self.servicio = servicio
        
        # Creación de la ventana principal
        self.root = tk.Tk()
        
        self._entry_tarea:  tk.Entry     = None  # type: ignore[assignment]
        self._tree:         ttk.Treeview = None  # type: ignore[assignment]
        self._lbl_contador: tk.Label     = None
        
        # Construye todos los elementos de la interfaz
        self._configurar_ventana()
        self._crear_ui()
        self._registrar_eventos()
        self._refrescar()

    # Método que inicia la ejecución de la interfaz
    def run(self):
        self.root.mainloop()


    def _configurar_ventana (self):
        self.root.title("Lista de Tareas")
        self.root.geometry("880x630")
        self.root.resizable(True, True)
        self.root.configure(bg=COLORS["COLOR_BG"])
        self.root.minsize(850, 610)

    # Método encargado de crear todos los componentes visuales
    def _crear_ui(self):

        self._crear_header()
        self._crear_seccion_entrada()
        self._crear_tabla_tareas()
        self._crear_barra_indicaciones()
    
    def _crear_header(self):
        header = tk.Frame(self.root, bg=COLORS["COLOR_BG"])
        header.pack(fill="x", padx=24, pady=(24, 8))

        tk.Label(
            header,
            text="📝LISTA DE TAREAS✍️",
            font=FONT_TITLE,
            fg=COLORS["COLOR_TEXT"],
            bg=COLORS["COLOR_BG"],
        ).pack(side="left")
        

        self._lbl_contador = tk.Label(
            header,
            text="",
            font=("Courier New", 11),
            fg=COLORS["COLOR_MUTED"],
            bg=COLORS["COLOR_BG"],
        )
        self._lbl_contador.pack(side="right", pady=6)
   
    def _crear_seccion_entrada(self):
        
        cont_input = tk.Entry(self.root, bg=COLORS["COLOR_BG"])
        cont_input.pack(fill="x", padx=24, pady=4)

        self.var_tarea = tk.StringVar()

        self._entry_tarea = tk.Entry(
            cont_input,
            textvariable=self.var_tarea,
            font=FONT_ENTRY,
            bg=COLORS["COLOR_ENTRY_BG"],
            fg=COLORS["COLOR_TEXT"],
            insertbackground=COLORS["COLOR_ACCENT2"],    # Color del cursor de texto
            relief="flat",
            bd=0,
        )
        self._entry_tarea.pack(side="left", fill="x", expand=True, ipady=8, padx=(0, 12)) 
     
        # Botones
        tk.Button(
            cont_input, 
            text="✚ Añadir tarea", 
            font= FONT_BTN, 
            bg=COLORS["COLOR_ACCENT"], 
            fg= "white", 
            activebackground=COLORS["COLOR_ACCENT2"], 
            activeforeground="white", 
            relief="flat", 
            cursor="hand2", padx=16, pady=8,command=self._agregar).pack(side="left", padx=(0, 10))
        tk.Button(
            cont_input, 
            text="✔ Marcar Completada", 
            font= FONT_BTN, 
            bg=COLORS["COLOR_SUCCESS"], 
            fg= "white", 
            activebackground="#16a34a", 
            activeforeground="white", 
            relief="flat", 
            cursor="hand2", padx=16, pady=8, command=self._completar).pack(side="left", padx=(0, 10))
        tk.Button(
            cont_input, 
            text="🗑 Eliminar", 
            font= FONT_BTN, 
            bg=COLORS["COLOR_DANGER"], 
            fg= "white", 
            activebackground="#b91c1c", 
            activeforeground="white", 
            relief="flat", cursor="hand2", padx=16, pady=8, command=self._eliminar).pack(side="right")
        
    def _crear_tabla_tareas(self):
        frame_lista = tk.Frame(self.root, bg=COLORS["COLOR_BG"])
        frame_lista.pack(fill="both", expand=True, padx=24, pady=8)
        
        # El estilo se extrae a un método propio para no sobrecargar este método
        self.__aplicar_estilo_treeview()

        # __tree se referencia en handlers, _registrar_eventos() y _refrescar_lista()
        self._tree = ttk.Treeview(
            frame_lista,
            columns=("id", "descripcion", "estado"),
            show="headings",
            style="Tareas.Treeview",
            selectmode="browse",
        )

        self._tree.heading("id", text="Id")
        self._tree.heading("descripcion", text="Descripción")
        self._tree.heading("estado", text="Estado")

        # Anchos de columna
        self._tree.column("id",  width=50,  anchor="center", stretch=False)
        self._tree.column("descripcion", minwidth=300, anchor="w")
        self._tree.column("estado", width=160, anchor="center", stretch=False)

        # Tag "pendiente": texto en ROJO + fondo rojizo oscuro
        self._tree.tag_configure(
            "pendiente",
            foreground=COLORS["COLOR_DANGER"],
            background=COLORS["COLOR_PENDING"],
        )
        # Tag "completada": texto en VERDE + fondo verdoso oscuro
        self._tree.tag_configure(
            "completada",
            foreground=COLORS["COLOR_SUCCESS"],
            background=COLORS["COLOR_DONE_BG"],
        )

        scrollbar = ttk.Scrollbar(frame_lista, orient="vertical", command=self._tree.yview)
        self._tree.configure(yscrollcommand=scrollbar.set)
        self._tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def __aplicar_estilo_treeview(self) -> None:
       
        style = ttk.Style()
        style.theme_use("default")
        style.configure(
            "Tareas.Treeview",
            background=COLORS["COLOR_SURFACE"],
            foreground=COLORS["COLOR_TEXT"],
            rowheight=38,
            fieldbackground=COLORS["COLOR_SURFACE"],
            font=FONT_TABLE,
            borderwidth=0,
        )
        style.configure(
            "Tareas.Treeview.Heading",
            background=COLORS["COLOR_ACCENT"],
            foreground="white",
            font=FONT_LABEL,
            relief="flat",
        )
        style.map(
            "Tareas.Treeview",
            background=[("selected", COLORS["COLOR_ACCENT"])],
            foreground=[("selected", "white")],
        )
    
    def _crear_barra_indicaciones(self):
        indications = tk.Frame(self.root, bg=COLORS["COLOR_BG"])
        indications.pack(fill="x", padx=24, pady=(4, 20))
        
        tk.Label(
            indications,
            text="↩ Enter para añadir   |   Doble clic para completar",
            font=FONT_HINT,
            fg=COLORS["COLOR_MUTED"],
            bg=COLORS["COLOR_BG"],
        ).pack(side="right")
    
    def _registrar_eventos(self):
        # Evento de doble click
        self._tree.bind("<Double-1>", self._doble_click)
        self._entry_tarea.bind("<Return>", self._on_enter)
        self.root.protocol ("WM_DELETE_WINDOW", self._cerrar_aplicacion)

   

    def _agregar(self):
        try:
            self.servicio.agregar_tarea(self.var_tarea.get())
            self.var_tarea.set("")
            self._refrescar()
        except Exception as e:
            messagebox.showerror("Entrada inválida", str(e), parent=self.root)
   
    def _on_enter(self, event):
        self._agregar()

    def _completar(self):
        id_tarea = self._get_selected()
        if id_tarea is None:
            return
        
        try:
            self.servicio.completar_tarea(id_tarea)
            self._refrescar()
        except KeyError as e:
            messagebox.showerror("Error", str(e), parent=self.root)

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
    
    
    def _doble_click(self, event):
        self._completar()

    def _cerrar_aplicacion(self):
        confirmado = messagebox.askyesno(
            "Salir de la aplicación",
            "¿Estás seguro de que deseas cerrar la aplicación?",
            parent=self.root,
        )
        if confirmado:
            self.root.destroy()

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

    def _refrescar(self):
        
        id_previo = self._get_selected(silencioso=True)
        
        for i in self._tree.get_children():
            self._tree.delete(i)

        tareas = self.servicio.listar_tareas()
        item_a_reseleccionar = None

        for tarea in tareas:
            if tarea.completada:
                estado_texto = "✔  Completada"
                tag = ("completada",)   # Verde
            else:
                estado_texto = "✗  Pendiente"
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
