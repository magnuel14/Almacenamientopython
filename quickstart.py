# libreria para autenticarse en el drive, se debe tener permisodel desarrollador 
# si no estas en la lista de usuarios aporbados va denegar su acceso
from pydrive.auth import GoogleAuth
#libreria para crear, modificar y eliminar contenio del dirve
from pydrive.drive import GoogleDrive
#fechas
from datetime import date
from datetime import datetime
from datetime import time


gauth = GoogleAuth()
gauth.LocalWebserverAuth() 
drive = GoogleDrive(gauth)

fecha = str(datetime.now())
exte='.mp4'
peatones='peatones'
circulos='circulos'
suma1= peatones + fecha + exte
suma2= circulos + fecha + exte


folderName = 'alma'  # Please set the folder name.

folders = drive.ListFile(
    {'q': "title='" + folderName + "' and mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()
for folder in folders:
    if folder['title'] == folderName:
        file1=drive.CreateFile({'title': suma1,'parents': [{'id': folder['id']}]}) 
        file1.SetContentFile('video_corto.mp4')
        file1.Upload()
        file2=drive.CreateFile({'title': suma2,'parents': [{'id': folder['id']}]}) 
        file2.SetContentFile('video_corto.mp4')
        file2.Upload()



'''
file1 = drive.CreateFile({'title': suma,'parents': [{'id': '1nCch1RByHVUNTGUBJPEsVJ1w86RKbhm1'}]})
file1.SetContentFile('video_corto.mp4') # Establecer el contenido del archivo a partir de una cadena dada


file1.Upload()


file1 = drive.CreateFile({'parents': [{'id': '1nCch1RByHVUNTGUBJPEsVJ1w86RKbhm1'}]})
file1 = drive.CreateFile({'title': suma})  # Create GoogleDriveFile instance with title 'Hello.txt'.
file1.SetContentFile('video_corto.mp4') # Establecer el contenido del archivo a partir de una cadena dada


file1.Upload()
'''
#Listar contenido del drive
'''
file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file1 in file_list:
  print('title: %s, id: %s' % (file1['title'], file1['id']))
  

file2 = drive.CreateFile({'parents': [{'id': '1nCch1RByHVUNTGUBJPEsVJ1w86RKbhm1'}]})

folderName = '###'  # Please set the folder name.

folders = drive.ListFile(
    {'q': "title='" + folderName + "' and mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()
for folder in folders:
    if folder['title'] == folderName:
        file2 = drive.CreateFile({'parents': [{'id': folder['id']}]})
        file2.SetContentFile('new_test.csv')
        file2.Upload()
folderName = 'alma'  # Please set the folder name.

folders = drive.ListFile(
    {'q': "title='" + folderName + "' and mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()
for folder in folders:
    if folder['title'] == folderName:
        file2 = drive.CreateFile({'title': suma})
        file2=drive.CreateFile({'parents': [{'id': folder['id']}]}) 
        file2.SetContentFile('video_corto.mp4')
        file2.Upload()
'''