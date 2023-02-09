from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import StreamingHttpResponse
from accounts.forms import RegistrationForm
from accounts.forms import LoginForm
from .models import UserProfile
import face_recognition
# import requests
import cv2
import numpy as numpy
from PIL import Image as img, ImageDraw
import fnmatch
import os

# Instanciar la ruta del directorio
# rootDir = '../facialrecognition'

IMAGES_DIR = 'facialrecognition/media/images' # imágenes del login
VERIF_DIR = 'facialrecognition/media/verif' #imagenes del registro

user_photo = []
user_photo_name = []


def home(request):
    return render(request, 'accounts/home.html')

"""Método login
Paso 1: Solicitar username
Paso 2: Verificación de foto si username existe
Paso 3: Mensaje de error si no existe"""


def login(request):
    context = {}
    global userLoginName
    global users
    if request.method == "POST":
        form = LoginForm(request.POST, request.FILES)
        if form.is_valid():
            userName = form.cleaned_data.get("username")
            userLoginName = userName
            users = UserProfile.objects.filter(
                title=userLoginName)
            if users:
                return render(request, 'accounts/verifyLogin.html', context)
            #Si el nombre de usuario coincide con un nombre de la base de datos pasar a verificar foto

            else:
                form = LoginForm()
                errorMessage = "Error: Usuario aún no registrado."  # else return error message
                context = {'form': form, 'errorMessage': errorMessage, }
                return render(request, 'accounts/login.html', context)
            # Si el nombre de usuario NO coincide con un nombre de la base de datos pasar a verificar foto
    else:
        form = LoginForm()
        context['form'] = form
        return render(request, 'accounts/login.html', context)

"""Método register
Paso 1: Solicitar username para registrar
Paso 2: Subir imagen relacionada a este nuevo nombre de usuario
Paso 3: Mensaje de error si el usuario ya existe"""

def register(request):
    context = {}
    if request.method == "POST":
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            img = form.cleaned_data.get("images")
            errorname = UserProfile.objects.filter(title=name)
            if errorname:
                errorMessage = "Error: Este usuario ya existe."  # else return error message
                context = {'form': form, 'errorMessage': errorMessage, }
                return render(request, 'accounts/register.html', context)
            else:
                obj = UserProfile.objects.create(
                    title=name,
                    img=img
                )
                obj.save()
                print(obj)
                return render(request, 'accounts/home.html', context)

    else:
        form = RegistrationForm()
    context['form'] = form
    return render(request, 'accounts/register.html', context)

"""Método verifyPhoto
Paso 1: Se recorren todas las imágenes del directorio y se añaden a las listas
Paso 2: Se cargan las imágenes registradas en la base de datos
Paso 3: Mensaje de error si no se toma la foto
Paso 4: Si toma foto, hace el encoding, compara el encoding nuevo con el encoding 
de las fotos del registro y hace match con los nombres."""
def verifyPhoto(request):
    context = {}

    '''Se recorren todas las imágenes del directorio y se añaden a las listas
    '''
    print("Loading registered faces database!")
    for file in os.listdir(IMAGES_DIR):
        if file.endswith(('.jpg', '.jpeg', '.png')):
            image = face_recognition.load_image_file(f"{IMAGES_DIR}/{file}")
            name_face_encoding = face_recognition.face_encodings(image)
            if len(name_face_encoding) > 0:
                # encoding de todas las caras encontradas
                encoding = name_face_encoding[0]
                # se adicionan los encodings a la lista
                user_photo.append(encoding)
                # se adiciona el nombre de la foto a la lista
                user_photo_name.append(file)

            else:
                print("¡No se detectó un área de cara válida!")
                pass
            continue

    '''Aqui se decide a dónde se redigirá el ususario:
    if true - redirect to login
    if false - redirect to register
    
    Si se cumple o no el condicional de takePhotoLogin()
    '''

    if takePhotoLogin() is True:
        form = LoginForm()
        context = {'form': form,
                   'users': users,
                   }

        return render(request, 'accounts/loggedIn.html', context)
    else:
        form = LoginForm()
        context['form'] = form

        return redirect('/login')

"""Método takePhotoLogin
Paso 1: Se recorren todas las imágenes del directorio y se añaden a las listas
Paso 2: Se cargan las imágenes registradas en la base de datos
Paso 3: Mensaje de error si no se toma la foto"""
def takePhotoLogin():
    context = {}
    # Abrir la cámara para tomar la imagen
    capture = cv2.VideoCapture(0)
    # Create live feed to take image and save photo
    while True:
        ret, frame = capture.read()
        cv2.imshow("Take Verification picture", frame)
        if (cv2.waitKey(1) & 0xFF == ord('q')): #la foto se toma con la letra q
            cv2.imwrite(f"{VERIF_DIR}/photo.png", frame)
            break
    capture.release()
    cv2.destroyAllWindows()
    cv2.waitKey(1)
    # Se carga la imagen tomada
    ver_photo = face_recognition.load_image_file(f"{VERIF_DIR}/photo.png")
    # Se hace el encoding de la imagen
    ver_photo_enc = face_recognition.face_encodings(ver_photo)[0]

    # DEBUG print
    print(f"VERIFICATION PHOTO: {ver_photo}")
    print(f"VERIFICATION PHOTO ENC: {ver_photo_enc}")

    # obtener las ubicaciones de la foto de verificación cargada utilizada para la comparación
    ver_locs = face_recognition.face_locations(ver_photo)
    # encontrar las caras y los encodings
    ver_photo_enc = face_recognition.face_encodings(ver_photo, ver_locs)

    # comprobar si la foto de verificación coincide con una foto de usuario
    for (top, right, bottom, left), ver_photo_enc in zip(ver_locs, ver_photo_enc):
        matches = face_recognition.compare_faces(user_photo, ver_photo_enc)

    # Mostrar si se logea o no
    if True in matches:
        print("Thank you for logging in")
        return True
    else:
        print("FAILED")
        return False
