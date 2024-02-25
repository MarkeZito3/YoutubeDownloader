import keyboard
import downloader
import os
from colorama import init, Fore, Back, Style
import time
import sys

init(autoreset=True)  # Inicializar colorama

def imprimir_post_menu(seleccion):
    opciones = ["Descargar otro Video/Audio", "Exit"]
    os.system('cls')
    print("Selecciona una opción:")
    print("==================================")
    for i, opcion in enumerate(opciones):
        if i == seleccion:
            print(Fore.BLACK + Back.WHITE + " "+ opcion + " ")
        else:
            print(opcion)
    print("==================================\npress [q] to exit")
def imprimir_menu(opciones, seleccion):
    os.system('cls')
    print("Selecciona una opción:")
    print("==================================")
    for i, opcion in enumerate(opciones):
        if i == seleccion:
            print(Fore.BLACK + Back.WHITE + " "+ opcion + " ")
        else:
            print(opcion)
    print("==================================\npress [q] to exit")

def main():
    opciones = ["Video [720]", "Audio"]
    seleccion = 0

    url=True

    imprimir_menu(opciones, seleccion)

    while True:
        event = keyboard.read_event(suppress=True)
        
        if event.scan_code == 80: #up
            if seleccion >= len(opciones)-1:
                seleccion=len(opciones)-1
            else:
                seleccion +=1
            # print (seleccion)
        elif event.scan_code == 72: #down
            if seleccion <= 0:
                seleccion=0
            else:
                seleccion -=1 
            # print (seleccion)
        elif event.scan_code == 28: #enter
            print("Seleccionaste la opción:", opciones[seleccion])
            if seleccion == 0:
                try:
                    os.system("cls")
                    url = input("""Ingrese el URL: """)
                    if not downloader.ableToDownload(url):
                        os.system("cls")
                        print("================================================")
                        print("URL no vlálida, pruebe nuevamente con otro link uwu")
                        print("================================================")

                    else:
                        os.system("cls")
                        print("================================================")
                        print("\tDescargando video...")
                        print("================================================")
                        downloader.download_video(url)
                except Exception as e:
                    print("\nNombre del error: ", e)
                    print("================================================")
                    input("Press Enter to continue...")
            elif seleccion == 1:
                try:
                    os.system("cls")
                    url = input("""Ingrese el URL: """)
                    if not downloader.ableToDownload(url):
                        os.system("cls")
                        print("================================================")
                        print("URL no vlálida, pruebe nuevamente con otro link uwu")
                        print("================================================")
                    else:
                        os.system("cls")
                        print("================================================")
                        print("\tDescargando audio...")
                        print("================================================")
                        downloader.download_audio(url)
                except:
                    print("\nNombre del error: ", e)
                    print("================================================")
                    input("Press Enter to continue...")
        elif event.scan_code == 16: # q = for quit
            print("Saliendo del menú...")
            break
        
        imprimir_menu(opciones, seleccion)
        time.sleep(0.1)

if __name__ == "__main__":
    main()
