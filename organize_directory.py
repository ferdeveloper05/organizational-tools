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
print(EXTENSIONES)

def validar_ruta(path_dir: Path) -> Path | None:
    """ Retorna la ruta solo si existe y es un directorio valido """
    if path_dir.exists() and path_dir.is_dir(): 
        return path_dir
    
    return None
    
    
def organizar_directorio(target_dir: Path): 
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
    
    print("Si no ingresa una ruta, se aplicará al directorio 'Downloads'.")
    
    directory_input = input('Ingrese el nombre del directorio: ').strip()
    name_dir = directory_input if directory_input else "Downloads"
    path_target = validar_ruta(Path.home() / name_dir)
    
    if not path_target:
        print(f"\nError: La ruta '{Path.home() / name_dir}' no existe o no es un directorio válido.")
        return
        
    print("\nDirectorio validado correctamente. Procesando...")
    organizar_directorio(path_target)
    print("\n¡Organización completada con éxito!")   


if __name__ == '__main__':     
    main()