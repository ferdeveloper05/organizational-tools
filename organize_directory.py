import shutil
import time
from pathlib import Path

# generar reporte 

def validar_ruta(path_dir: Path) -> Path | None: 
    if path_dir.exists() and not path_dir.is_dir(): 
        return
    
    return path_dir  
    
    
def crear_directorios(path_validate_dir: Path, extensiones: dict[str: list[str]]): 
    print("Creando directorios para organizar los archivos...")
    for file in path_validate_dir.iterdir(): 
        for name, exten in extensiones.items(): 
            if file.suffix in exten:
                new_dir = path_validate_dir.parent / name
                new_dir.mkdir(exist_ok=True)
                shutil.move(file, new_dir)
    print("Moviendo los archivos a sus directorios correspondientes...")
    

def main(): 
    print("\n###################### ORGANIZADOR DE DIRECTORIOS ######################\n")
    time.sleep(1)
    
    print("Acontinuacion se le solicitara el nombre del directorio a ordenar.\n")
    print("Si no se ingresa un nombre de directorio el script se aplicará al directorio 'Downloads'\n")
    print("Luego se validara el nombre del directorio y se procedera a organizar el directorio\n")
    
    directory = input('Ingrese el nombre del directorio a ingresar: ') 
    option = directory if directory else "Downloads"
    path_validate = validar_ruta(Path.home() / option)
    
    time.sleep(1)
    
    print("Directorio validado correctamente!")
    time.sleep(1.5)
    
    crear_directorios(path_validate, extensiones)    


if __name__ == '__main__': 
    
    extensiones = {
        'Documents': ['.docx', '.pdf', '.txt', '.doc'], 
        'Pictures': ['.png', '.jpeg', '.jpg', '.gif', '.webp'], 
        'Code': ['.py', '.php', '.js', '.html', '.css'], 
        'Music': ['.mp3'],
        'Videos': ['.mp4'], 
        'Spreadsheets': ['.csv', '.xls', '.xlsx'],
        'Executables': ['.deb', '.exe']
    }
    
    main()