import downloader
import os 

os.system("cls")
print("programa para descargar videos de youtube o directamente la música :D")
url = input("Ingrese la URL: ")
os.system("cls")
desicion = int(input("qué desea descargar:\npress:\n\t[1] video\n\t[2] audio\n\t[3] salir\nOpción: "))
os.system("cls")

if desicion == 1:
    downloader.download_video(url)
elif desicion == 2:
    downloader.download_audio(url)
else:
    input("Bye Bye puta\npress ENTER to leave")
    os.system("exit")