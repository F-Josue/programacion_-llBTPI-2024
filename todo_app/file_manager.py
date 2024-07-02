from pathlib import Path
import json

ROOT_PATH = Path(__file__).resolve().parent

FILE_PATH = ROOT_PATH / 'datos.json'



DEAFULT_DATA = {
    'todos': []
}

def obtener_datos():
    with open(FILE_PATH) as datos_file:
        file_data = datos_file.read()
        
        print(file_data)
        if not file_data:
            return DEAFULT_DATA
        
        datos = json.loads(file_data)
        return datos
