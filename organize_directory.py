import shutil
from pathlib import Path

# generar reporte 

extensiones = {
    'Documents': ['.docx', '.pdf', '.txt', '.doc'], 
    'Pictures': ['.png', '.jpeg', '.jpg', '.gif', '.webp'], 
    'Code': ['.py', '.php', '.js', '.html', '.css'], 
    'Music': ['.mp3'],
    'Videos': ['.mp4'], 
    'Spreadsheets': ['.csv', '.xls', '.xlsx'],
    'Executables': ['.deb', '.exe']
}

EXTENSIONES: dict[str, str] = {
    ext: categoria
    for categoria, list_ext in extensiones.items()
    for ext in list_ext
}

def validar_ruta(path_dir: Path) -> Path | None:
    """ Retorna la ruta solo si existe y es un directorio valido """
    if path_dir.exists() and path_dir.is_dir(): 
        return path_dir
    
    return None
    
    
def crear_directorios(target_dir: Path): 
    print(f"Organizando archivos en: {target_dir}")
    
    for item in target_dir.iterdir():
        
        if item.is_dir(): 
            continue
         
        ext = item.suffix.lower()
        if ext in EXTENSIONES:
            categoria = EXTENSIONES[ext]
            dest_dir = target_dir / categoria
            dest_dir.mkdir(exist_ok=True)
            
            shutil.move(str(item), dest_dir / item.name)
            print(f"Movido: {item.name} -> {categoria}/")
    

def main(): 
    print("\n###################### ORGANIZADOR DE DIRECTORIOS ######################\n")
    
    print("Acontinuacion se le solicitara el nombre del directorio a ordenar.\n")
    print("Si no se ingresa un nombre de directorio el script se aplicará al directorio 'Downloads'\n")
    print("Luego se validara el nombre del directorio y se procedera a organizar el directorio\n")
    
    directory = input('Ingrese el nombre del directorio a ingresar: ') 
    option = directory if directory else "Downloads"
    path_validate = validar_ruta(Path.home() / option)
        
    print("Directorio validado correctamente!")
    
    crear_directorios(path_validate, extensiones)    


if __name__ == '__main__':     
    main()