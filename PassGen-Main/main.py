import random 
import colorama
from colorama import Fore
import os
import time
import random

os.system('cls')


colorama.init()

auth = '''
  /$$$$$$              /$$     /$$      
 /$$__  $$            | $$    | $$      
| $$  \ $$ /$$   /$$ /$$$$$$  | $$$$$$$ 
| $$$$$$$$| $$  | $$|_  $$_/  | $$__  $$
| $$__  $$| $$  | $$  | $$    | $$  \ $$
| $$  | $$| $$  | $$  | $$ /$$| $$  | $$
| $$  | $$|  $$$$$$/  |  $$$$/| $$  | $$
|__/  |__/ \______/    \___/  |__/  |__/
                                        
                                        '''


print(Fore.RED + auth)

print(Fore.YELLOW + 'Bienvenido a PassGen, un programa developeado por GiroBro, el cual te generará contraseñas seguras Anti Brute-force.')
print('')
time.sleep(7)
print(Fore.GREEN + 'Como medida de seguridad anit db scam, una vez cierres el programa, las contraseñas generadas serán irrecuperables. Guardalas bien!')
print('')
time.sleep(10)
pasar = input(Fore.CYAN + 'Si leiste nuestros términos, presione enter.')
if pasar == '""':
    print(Fore.YELLOW + 'Gracias por confiar en nosotros.')
    time.sleep(1)
    print(Fore.GREEN + 'Accediendo al sistema...')
    time.sleep(3)


                                           

ascii1 = '''
                                 ____   _    ____ ____     ____ _____ _   _ 
                                |  _ \ / \  / ___/ ___|   / ___| ____| \ | |    byGiroBro :)
                                | |_) / _ \ \___ \___ \  | |  _|  _| |  \| |   
                                |  __/ ___ \ ___) |__) | | |_| | |___| |\  |  
                                |_| /_/   \_\____/____/   \____|_____|_| \_|   
                                             '''


os.system('cls')
print(Fore.BLUE + ascii1) 
print('')

print(Fore.GREEN + '                                     [1] Máxima Seguridad')
print('')
print(Fore.YELLOW + '                                         --------     [2] Máxima cortitud')
print('')
print(Fore.GREEN + '                                    [3] Números + simbolos    --------') 
print('')
print(Fore.YELLOW  + '                                    ----------   [4] Máxima largitud')
print('')
print(Fore.GREEN  + '                                    [5] Letras + Simbolos   ---------') 
print('')
print(Fore.YELLOW  + '                                     ---------  [6] Vocales')
print('')
print(Fore.GREEN + '                                     [7] Vocales + Mayus   -------')
print('')
print(Fore.YELLOW + '                                       --------- [8] Numeros + Vocales')
print('')
print(Fore.GREEN  + '                                  [9] Simbolos + Vocales    ----------')
print('')
print(Fore.YELLOW  + '                                     -----------  [10] Mayus + Números')
print('')
print('')

opcion = int(input(Fore.CYAN + '                                root@GiroBro> ')) 
print('') 

# DIGITOS

letras = 'abcdefghijklmnopqrstuvwxyz'
letras_mayus = 'ABCDEFGHIJQLMNOPQRSTUVWXYZ'
numeros = '12345678910'
vocales = 'aeiou'
simbolos = '^?¿¨Ç:;_`+¡!´/'

# CARACTERESs

normal = k = 10

# NUM PASS LARGA/CORTA

# CORTA
corta = k = 7

# LARGA
larga = k = 14

if opcion == 1:
    print(Fore.CYAN + '  Seleccionaste una contraseña segura.')
    time.sleep(1)
    pass1 = ''.join(random.choices(letras + letras_mayus + numeros + vocales + simbolos, k = normal))
    print('')
    print(Fore.GREEN + '  Cargando...')
    print('')
    time.sleep(3)
    print(Fore.BLUE + '  Una contraseña' + Fore.GREEN + ' [S] ' + Fore.BLUE + 'para usted: ' + Fore.YELLOW + pass1)
    time.sleep(2)
    salir = input(Fore.RED + '  Pulsa enter para retirarte.')
    time.sleep(2)
    if salir == '""':
        print(Fore.BLUE + 'Saliendo...')
        time.sleep(2)

if opcion == 2:
    print(Fore.CYAN + '  Seleccionaste Maxima cortitud.')
    time.sleep(1)
    pass2 = ''.join(random.choices(letras + letras_mayus + numeros + vocales + simbolos, k = corta))
    print('')
    print(Fore.GREEN + '  Cargando...')
    print('')
    time.sleep(3)
    print(Fore.BLUE + '  Una contraseña' + Fore.GREEN + ' [C] ' + Fore.BLUE + 'para usted: ' + Fore.YELLOW + pass2)
    time.sleep(2)
    salir = input(Fore.RED + '  Pulsa enter para retirarte.')
    time.sleep(2)
    if salir == '""':
        print(Fore.BLUE + 'Saliendo...')
        time.sleep(2)

if opcion == 3:
    print(Fore.CYAN + '  Seleccionaste simobolo + Números.')
    time.sleep(1)
    pass3 = ''.join(random.choices(numeros + simbolos, k = normal))
    print('')
    print(Fore.GREEN + '  Cargando...')
    print('')
    time.sleep(3)
    print(Fore.BLUE + '  Una contraseña' + Fore.GREEN + ' [S + N] ' + Fore.BLUE + 'para usted: ' + Fore.YELLOW + pass3)
    time.sleep(2)
    salir = input(Fore.RED + '  Pulsa enter para retirarte.')
    time.sleep(2)
    if salir == '""':
        print(Fore.BLUE + 'Saliendo...')
        time.sleep(2)


if opcion == 4:
    print(Fore.CYAN + '  Seleccionaste Numeros + simbolos.')
    time.sleep(1)
    pass4 = ''.join(random.choices(numeros + simbolos, k = corta))
    print('')
    print(Fore.GREEN + '  Cargando...')
    print('')
    time.sleep(3)
    print(Fore.BLUE + '  Una contraseña' + Fore.GREEN + ' [N + S] ' + Fore.BLUE + 'para usted: ' + Fore.YELLOW + pass4)
    time.sleep(2)
    salir = input(Fore.RED + '  Pulsa enter para retirarte.')
    time.sleep(2)
    if salir == '""':
        print(Fore.BLUE + 'Saliendo...')
        time.sleep(2)

if opcion == 5:
    print(Fore.CYAN + '  Seleccionaste Letas + Simbolos.')
    time.sleep(1)
    pass5 = ''.join(random.choices(letras + simbolos, k = corta))
    print('')
    print(Fore.GREEN + '  Cargando...')
    print('')
    time.sleep(3)
    print(Fore.BLUE + '  Una contraseña' + Fore.GREEN + ' [L + S] ' + Fore.BLUE + 'para usted: ' + Fore.YELLOW + pass5)
    time.sleep(2)
    salir = input(Fore.RED + '  Pulsa enter para retirarte.')
    time.sleep(2)
    if salir == '""':
        print(Fore.BLUE + 'Saliendo...')
        time.sleep(2)


if opcion == 6:
    print(Fore.CYAN + '  Seleccionaste Vocales.')
    time.sleep(1)
    pass6 = ''.join(random.choices(vocales, k = corta))
    print('')
    print(Fore.GREEN + '  Cargando...')
    print('')
    time.sleep(3)
    print(Fore.BLUE + '  Una contraseña' + Fore.GREEN + ' [V] ' + Fore.BLUE + 'para usted: ' + Fore.YELLOW + pass6)
    time.sleep(2)
    salir = input(Fore.RED + '  Pulsa enter para retirarte.')
    time.sleep(2)
    if salir == '""':
        print(Fore.BLUE + 'Saliendo...')
        time.sleep(2)

if opcion == 7:
    print(Fore.CYAN + '  Seleccionaste Vocales + Mayus')
    time.sleep(1)
    pass7 = ''.join(random.choices(vocales + letras_mayus, k = corta))
    print('')
    print(Fore.GREEN + '  Cargando...')
    print('')
    time.sleep(3)
    print(Fore.BLUE + '  Una contraseña' + Fore.GREEN + ' [V + M] ' + Fore.BLUE + 'para usted: ' + Fore.YELLOW + pass7)
    time.sleep(2)
    salir = input(Fore.RED + '  Pulsa enter para retirarte.')
    time.sleep(2)
    if salir == '""':
        print(Fore.BLUE + 'Saliendo...')
        time.sleep(2)


if opcion == 8:
    print(Fore.CYAN + '  Seleccionaste Números + Vocales.')
    time.sleep(1)
    pass8 = ''.join(random.choices(numeros + vocales, k = corta))
    print('')
    print(Fore.GREEN + '  Cargando...')
    print('')
    time.sleep(3)
    print(Fore.BLUE + '  Una contraseña' + Fore.GREEN + ' [N + V] ' + Fore.BLUE + 'para usted: ' + Fore.YELLOW + pass8)
    time.sleep(2)
    salir = input(Fore.RED + '  Pulsa enter para retirarte.')
    time.sleep(2)
    if salir == '""':
        print(Fore.BLUE + 'Saliendo...')
        time.sleep(2)


if opcion == 9:
    print(Fore.CYAN + '  Seleccionaste Símbolos + Números.')
    time.sleep(1)
    pass9 = ''.join(random.choices(numeros + simbolos, k = corta))
    print('')
    print(Fore.GREEN + '  Cargando...')
    print('')
    time.sleep(3)
    print(Fore.BLUE + '  Una contraseña' + Fore.GREEN + ' [S + N] ' + Fore.BLUE + 'para usted: ' + Fore.YELLOW + pass9)
    time.sleep(2)
    salir = input(Fore.RED + '  Pulsa enter para retirarte.')
    time.sleep(2)
    if salir == '""':
        print(Fore.BLUE + 'Saliendo...')
        time.sleep(2)

if opcion == 10:
    print(Fore.CYAN + '  Seleccionaste Símbolos + Números.')
    time.sleep(1)
    pass10 = ''.join(random.choices(numeros + simbolos, k = corta))
    print('')
    print(Fore.GREEN + '  Cargando...')
    print('')
    time.sleep(3)
    print(Fore.BLUE + '  Una contraseña' + Fore.GREEN + ' [S + N] ' + Fore.BLUE + 'para usted: ' + Fore.YELLOW + pass10)
    time.sleep(2)
    salir = input(Fore.RED + '  Pulsa enter para retirarte.')
    time.sleep(2)
    if salir == '""':
        print(Fore.BLUE + 'Saliendo...')
        time.sleep(2)








    
