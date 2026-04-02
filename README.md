# 📝Aplicación GUI Lista de Tareas ✍️ con Eventos y Ejecutable

Aplicación de escritorio tipo *To-Do List* desarrollada con *Python + Tkinter*, aplicando:

- Programación Orientada a Objetos (POO)
- Arquitectura modular por capas (Modelo → Servicio → UI → main)
- Manejo de eventos de usuario (teclado y ratón)

Esta versión corresponde a una *evolución del sistema base (Semana 15)*, incorporando mejoras en la experiencia de usuario mediante:

- Implementación de *atajos de teclado*
- Feedback visual dinámico en tiempo real de los eventos o atajos
- Interacción más rápida, eficiente y accesible

La aplicación permite agregar, completar y eliminar tareas de forma sencilla, brindando una experiencia fluida y moderna.

---

## 🎯 Objetivo del Proyecto

Desarrollar una aplicación interactiva que permita gestionar tareas diarias, cumpliendo con los siguientes criterios:

- Separación de responsabilidades por capas  
- Interfaz gráfica funcional y reactiva  
- Manejo de eventos con `.bind()` (teclaro y ratón)  
- Incorporar *atajos de teclado* para mejorar la interacción
- Feedback visual claro y dinámico del estado de las tareas y acciones del usuario
- Reutilizar y mejorar el sistema desarrollado en la Semana 15


---

## 📁 Estructura del proyecto

```
S16-POO-ListaTareasGUI--Sigcha-Joselyn/ lista_tareas_app/
│
├── modelos/
│   └── tarea.py             # Clase Tarea (id, descripcion, estado_completado)
├── servicios/
│   └── tarea_servicio.py    # Lógica: agregar, completar, eliminar, listar
└── ui/
│    └── app_tkinter.py      # Interfaz Tkinter + captura de eventos y atajos
│
├── main.py                  # Orquestador y punto de arranque
│
├── README.md                # Documentación del proyecto
└── .gitignore               # Archivos y carpetas que Git debe ignorar
```
## 📦 Arquitectura por capas

### 📌 Modelos

Define la entidad Tarea.

✔️ Incluye:
- id  
- descripción  
- estado (completada o no)  

✔️ Implementa:
- Encapsulación  
- Properties (@property)  
- Validación de datos  

---

### ⚙️ Servicios

Contiene la lógica del sistema.

✔️ Funcionalidades:
- Agregar tareas  
- Marcar tareas como completadas  
- Eliminar tareas  
- Listar tareas  

✔️ Incluye:
- Validación de descripción vacía  
- Manejo de errores con excepciones  

---

### 🖥️ Interfaz Gráfica (UI)

Desarrollada con *Tkinter*.

✔️ Permite:
- Ingresar tareas  
- Visualizar tareas en Treeview  
- Seleccionar tareas  
- Ejecutar acciones mediante botones  

✔️ Componentes usados:
- Entry  
- Button  
- ttk.Treeview  
- messagebox  

---

## 🎮 Funcionalidades

| Acción | Método |
|---|---|
| Añadir tarea | Botón **＋ Añadir** |
| Añadir tarea rápido | Tecla **Enter** en el campo de texto|
| Marcar completada | Botón **✔ Marcar Completada** |
| Marcar completada rápido | **Doble clic** sobre la tarea en la lista|
| Atajo tarea completada | Teclas **Ctrl+C** sobre la tarea en la lista |
| Eliminar tarea | Botón **🗑 Eliminar** (con confirmación) |
| Atajo para eliminar tarea | Tecla **Delete / Ctrl + D** (con confirmación) |
| Atajo cerrar la aplicación | Tecla **Esc** (con confirmación) |
---

## 🎨 Feedback Visual

- 🔴 *Pendiente*
  - Texto rosa pastel 
  - Fondo rojizo oscuro  
  - Estado: ✗ Pendiente  

- 🟢 *Completada*
  - Texto verde pastel  
  - Fondo verdoso oscuro  
  - Estado: ✔ Completada  

- El contador en el encabezado muestra `X pendiente(s) / Y total`.
- Además existe un apartado de indicaciones sobre las acciones rápidas para el usuario y los atajos aplicados.

>✔️ Mejora la accesibilidad y reduce el uso del mouse  
>✔️ Optimiza la experiencia del usuario al identificar el estado de la tarea de forma visual clara.


---

## 👨‍💻 Eventos implementados con `.bind()`

```python
# Evento de teclado (Enter)
self._entry_tarea.bind("<Return>", self._on_enter)

# Evento de ratón (doble clic)
self._tree.bind("<Double-1>", self._doble_click)

# Evento de teclado (Ctrl+C) 
self.root.bind("<Control-c>", self._atajo_completar)
self.root.bind("<Control-C>", self._atajo_completar)
        
# Evento de teclado (Delete o Ctrl+D)
self.root.bind("<Delete>", self._atajo_eliminar)
self.root.bind("<Control-d>", self._atajo_eliminar)
self.root.bind("<Control-D>", self._atajo_eliminar)
       
# Evento de teclado (Escape)
self.root.bind("<Escape>", self._atajo_salir)

```
> ✔️ Cumple con los requisitos de eventos avanzados.

---

## 📋 Requisitos

- Python 3.10 o superior  
- Tkinter (incluido en Python)

## 🚀 Cómo Ejecutar el Programa en consola

1. **Obtener el enlace del repositorio.**
2. **Abrir un IDE:** PyCharm o Visual Studio Code.
3. **Clonar el repositorio:**
   ```bash
   git clone <url-del-repositorio>
   ```
4. **Ejecutar:**
   ```bash
   python main.py
   ```
5. Se abrirá la interfaz gráfica del sistema de tareas.

---
## 🚀 Evolución del sistema (Semana 16)

Esta versión representa una mejora del sistema desarrollado previamente, enfocada en la optimización de la interacción del usuario.

Se añadieron:

- Atajos de teclado para acciones principales
- Barra de eventos con mensajes en tiempo real
- Mayor fluidez en la navegación
- Mejora en la accesibilidad y usabilidad

>✔️ Se mantiene la arquitectura original sin alterar la separación de responsabilidades.

---

## 🧠 Buenas prácticas aplicadas

- ✔️ Programación Orientada a Objetos (POO)  
- ✔️ Encapsulación  
- ✔️ Separación por capas  
- ✔️ Inyección de dependencias  
- ✔️ Manejo de eventos  
- ✔️ Código modular  
- ✔️ Uso de ttk.Treeview con estilos 
- ✔️ Mejora de UX mediante atajos de teclado
- ✔️ Feedback en tiempo real por la barra de eventos.


---

## 🏁 Conclusión

Este proyecto implementa una aplicación GUI completa en Python, integrando:

- Arquitectura limpia  
- Interacción dinámica  
- Eventos de teclado y ratón (Atajos)
- Feedback visual claro  