# ✅ Lista de Tareas — Tarea Semana 15

Aplicación de escritorio **To-Do List** desarrollada con **Python + Tkinter**,
siguiendo arquitectura modular por capas (Modelo → Servicio → UI).

---

## 📁 Estructura del proyecto

```
lista_tareas_app/
│
├── main.py                  # Orquestador y punto de arranque
├── modelos/
│   └── tarea.py             # Clase Tarea (id, descripcion, completada)
├── servicios/
│   └── tarea_servicio.py    # Lógica: agregar, completar, eliminar, listar
└── ui/
    └── app_tkinter.py       # Interfaz Tkinter + captura de eventos
```

---

## ▶️ Ejecutar en desarrollo

```bash
# 1. (Opcional) Crear entorno virtual
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. Sin dependencias externas — Tkinter viene con Python
python main.py
```

---

## 📦 Generar ejecutable con PyInstaller

```bash
# 1. Instalar PyInstaller
pip install pyinstaller

# 2. Compilar (sin consola, un solo archivo)
pyinstaller --noconsole --onefile --name TkMiApp main.py

# El ejecutable queda en:  dist/TkMiApp.exe  (Windows)
#                          dist/TkMiApp      (macOS / Linux)
```

> **Nota**: La carpeta `build/` y el archivo `.spec` son generados
> automáticamente y están excluidos del repositorio via `.gitignore`.

---

## 🎮 Funcionalidades

| Acción | Método |
|---|---|
| Añadir tarea | Botón **＋ Añadir** |
| Añadir tarea rápido | Tecla **Enter** en el campo de texto (`<Return>`) |
| Marcar completada | Botón **✔ Marcar Completada** |
| Marcar completada rápido | **Doble clic** sobre la tarea en la lista *(EXTRA)* |
| Eliminar tarea | Botón **🗑 Eliminar** (con confirmación) |

### Feedback visual
- Las tareas **completadas** se muestran en gris con fondo verde oscuro y el texto **"✔ Hecho"**.
- Las tareas **pendientes** se muestran en blanco con el texto **"○ Pendiente"**.
- El contador en el encabezado muestra `X pendiente(s) / Y total`.

---

## 👨‍💻 Eventos implementados con `.bind()`

```python
# Teclado — añadir tarea con Enter
self.entry_tarea.bind("<Return>", self._on_enter_presionado)

# Ratón — marcar completada con doble clic [EXTRA]
self.tree.bind("<Double-1>", self._on_doble_clic_lista)
```
