import shutil
import platform
from pathlib import Path


# extensiones 
# obtener directorio
# mover archivos 
# crear carpetas dependiendo de la extension
# generar reporte 
# interaccion con el usuario 
# carpeta especial dependiendo el nombre del archivo

def validar_ruta(path_dir: Path) -> Path | None: 
    if path_dir.exists() and not path_dir.is_dir(): 
        return
    
    return path_dir

def normalizar_extensiones(): 
    pass 

def crear_directorios(path_validate_dir: Path, extensiones: dict[str: list[str]]): 
    for file in path_validate_dir.iterdir(): 
        for name, exten in extensiones.items(): 
            if file.suffix in exten: 
                new_dir = path_validate_dir.parent / name
                new_dir.mkdir(exist_ok=True)
        
def ordenar_archivos(path_validate_dir: Path): 
    pass

extensiones = {
    'Documents': ['.docx', '.pdf', '.txt', '.doc'], 
    'Pictures': ['.png', '.jpeg', '.jpg', '.gif', '.webp'], 
    'Code': ['.py', '.php', '.js', '.html', '.css'], 
    'Music': ['.mp3'],
    'Videos': ['.mp4'], 
    'Spreadsheets': ['.csv', '.xls', '.xlsx'],
    'Executables': ['.deb', '.exe']
}

path_validate = validar_ruta(Path.home() / input('Ingrese el nombre del directorio a ingresar: '))

crear_directorios(path_validate, extensiones)