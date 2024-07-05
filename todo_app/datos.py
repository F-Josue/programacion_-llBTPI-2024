from uuid import uuid4
from file_manager import obtener_datos, sincronizar_todos

datos_guardados = obtener_datos()

_tareas = datos_guardados['todos']

def crear_tarea(titulo: str):
    nueva_tarea = {
        'id': str (uuid4()),
        'titulo': titulo,
        'completada': False
    }
    
    _tareas.append(nueva_tarea)
    
    sincronizar_todos(_tareas)
    
def obtener_todas_las_tareas():
    return _tareas 