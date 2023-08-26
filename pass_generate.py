import random
import string
from colorama import init, Fore
init(autoreset=True)

GREEN = "\033[92m"
BLUE = "\033[94m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
YELLOW = "\033[93m"
RESET = "\033[0m"
ROSA = "\033[91m\033[97m"

Letras = string.ascii_letters
numeros = string.digits
caracteres = string.punctuation

contra_aleatorio = []
largo_de_cadena = input (f"{Fore.LIGHTCYAN_EX}Indica el largo de la contrasena (en numeros):{Fore.RESET} ")
num = int(largo_de_cadena)
con_todo = input(f"{Fore.LIGHTCYAN_EX}Quieres que contenga numeros, letras y caracteres especiales?(solo si o no, en minuscula):{Fore.RESET} ")
if con_todo == "no":
    print(f"{Fore.LIGHTCYAN_EX}Selecciona la opcion que no quieres que contenga\n\nOpciones\n{Fore.RESET}")
    print(f"{Fore.LIGHTGREEN_EX}[1] Numeros {Fore.RESET}")
    print(f"{Fore.LIGHTGREEN_EX}[2] Letras{Fore.RESET}")
    print(f"{Fore.LIGHTGREEN_EX}[3] Caracteres especiales\n{Fore.RESET}")
    opcion = input(f"{Fore.LIGHTCYAN_EX}Selecciona la opcion:{Fore.RESET}")

if con_todo == "si":
    while len(contra_aleatorio) < num:
        categoria_aleatorio = random.choice([Letras, numeros, caracteres])
        contra_aleatorio.append(random.choice(categoria_aleatorio))
    contra_final = ''.join(contra_aleatorio)
    output = input(f"{Fore.LIGHTCYAN_EX}Quieres guardar el archivo?(solo si o no):{Fore.RESET} ")
    if output == "si":
        file_name = input(f"{Fore.LIGHTCYAN_EX}ingresa el nombre:{Fore.RESET} ")
    if output == "si":
        with open(f"{file_name}.txt", "w") as archivo:
            archivo.write(contra_final)
            print(f"{Fore.LIGHTCYAN_EX}Contrasena Guardada en {file_name}.txt{Fore.RESET}")
    elif output == "no":
        print(f"{Fore.LIGHTCYAN_EX}La contrasena es: {contra_final}{Fore.RESET}")
        
elif opcion == "1":
    while len(contra_aleatorio) < num:
        categoria_aleatorio = random.choice([Letras, caracteres])
        contra_aleatorio.append(random.choice(categoria_aleatorio))
    contra_final = ''.join(contra_aleatorio)
    output = input(f"{Fore.LIGHTCYAN_EX}Quieres guardar la contrasena en un archivo?(solo si o no):{Fore.RESET} ")
    if output == "si":
        file_name = input(f"{Fore.LIGHTCYAN_EX}Ingresa el nombre del archivo:{Fore.RESET} ")
    if output == "si":
        with open(f"{file_name}.txt", "w") as archivo:
            archivo.write(contra_final)
            print(f"{Fore.LIGHTCYAN_EX}Contrasena guardada en {file_name}.txt{Fore.RESET}")
    elif output == "no":
        print(f"{Fore.LIGHTCYAN_EX}La contrasena es: {contra_final}{Fore.RESET}")

elif opcion == "2":
    while len(contra_aleatorio) < num:
        categoria_aleatorio = random.choice([numeros, caracteres])
        contra_aleatorio.append(random.choice(categoria_aleatorio))
    contra_final = ''.join(contra_aleatorio)
    output = input(f"{Fore.LIGHTCYAN_EX}Quieres guardar la contrasena en un archivo?(solo si o no):{Fore.RESET} ")
    if output == "si":
        file_name = input(f"{Fore.LIGHTCYAN_EX}Ingresa el nombre del archivo:{Fore.RESET}")
    if output == "si":
        with open(f"{file_name}.txt", "w") as archivo:
            archivo.write(contra_final)
            print(f"{Fore.LIGHTCYAN_EX}La contrasena se guardo en {file_name}.txt{Fore.RESET}")
    elif output == "no":
        print(f"{Fore.LIGHTCYAN_EX}La contrasena es {contra_final} {Fore.RESET}")
        
elif opcion == "3":
    while len(contra_aleatorio) < num:
        categoria_aleatorio = random.choice([Letras, numeros])
        contra_aleatorio.append(random.choice(categoria_aleatorio))
    contra_final = ''.join(contra_aleatorio)
    output = input(f"{Fore.LIGHTCYAN_EX}Quieres guardar la contrasena en un archivo?(solo si o no):{Fore.RESET} ")
    if output == "si":
        file_name = input(f"{Fore.LIGHTCYAN_EX}Ingresa el nombre de el archivo:{Fore.RESET} ")
    if output == "si":        
        with open(f"{file_name}.txt", "w") as archivo:
            archivo.write(contra_final)
            print(f"{Fore.LIGHTCYAN_EX}La contrasena se guardo en {file_name}.txt{Fore.RESET}")
    elif output == "no":
        print(f"{Fore.LIGHTCYAN_EX}La contrasena es {contra_final}{Fore.RESET}")
        
        
