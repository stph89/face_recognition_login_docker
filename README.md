# Facial Recognition and Login Facial System


[Stephany Valderrama](https://github.com/stph89)&nbsp;and [Wenya Li](https://github.com/wenlla)  &nbsp;

**Thanks to:**  [Aaron Moran](https://github.com/Moran98)&nbsp;, [Arnas Steponavicius](https://github.com/ArnasSteponavicius00)&nbsp;and [Thomas Kenny](https://github.com/KennyThomas).
**Modified code from those repositories**

![imagen](https://user-images.githubusercontent.com/110174766/217071499-439be897-c7de-4474-a0a7-bc9b03ed876b.png)


## Requirements

The requirements needed for this project are as follows :

* Python 3.8+

* Linux, Windows, MacOS

* Django

* Latest version of pip
  

## Installation
  
For run theses facial recognition demos, you require to install the following python module.

You can run `pip install requirements.txt`

```
pip3 install django
pip3 install numpy
pip3 install opencv-python
pip3 install Pillow
pip3 install face_recognition
```
  **Note:** Make sure you are using the latest version of pip.
* #### For Mac or Linux --> follow the instructions of [face_recognition docs](https://gist.github.com/ageitgey/629d75c1baac34dfa5ca2a1928a7aeaf)

* #### For Windows --> follow the instructions of [face_recognition docs](https://github.com/ageitgey/face_recognition/issues/175#issue-257710508)

**Note:** Currently the packages for `face_recognition` are not fully supported on Windows. 

## Estructura de este repositorio

| Carpeta                     | Folder / Fichero    | Descripción                                                                              |
|-----------------------------|---------------------|------------------------------------------------------------------------------------------|
| `facial_recognition_webcam` | `facial.py`         | Face recognition system on live video from a local webcam.                               |
|`facial_recognition_webcam`  | `/info_facial`      | Imágenes de referencia para reconocimiento facial múltiple.                              |
| `login_recognition_app`     | `/accounts`         | Codigo html para el registro de usuarios.                                                |
| `login_recognition_app`     | `/facialrecognition`| Configuracion de metodos, funciones y conexion entre modulos par despliegue en Django.   |
| `login_recognition_app`     | `~/ /media`         | Aquí se almacenan las imágenes de los usuarios registrados.                              |
| `login_recognition_app`     | `db.sqlite3`        | base de datos SQlite donde se guardan las migraciones de los nuevos usuarios registrados.|
| `login_recognition_app`     | `manage.py`         | Archivo principal para el funcionamiento del sistema de login.                           |
|                             | `.gitignore`        | Para ignorar los archivos sensibles como imégenes.                                       |
|                             | `requirements.txt`  | Librerías y paquetes utilizados par la creación de este proyecto.                        |
|                             | `README.md`         | Descripción de este repositorio                                                          |
           

## Demos with `face recognition` and `openCV` libraries.
We proposed two demos using [face recognition library](https://github.com/ageitgey/face_recognition):

 * **Simple sample of Face recognition system on live video from a local webcam.**
 
 * **Facial login web application with Django framework and sqlite databases.**
  
  
  
## Running the Face recognition system on live video from a local webcam
This is a face recognition system on live video from a local webcam.

1. Navigate to directory

	```
	$ cd \facial_recognition_webcam\
	```
2. Put into `\info_facial` folder the images of the persons that you want to recognize in this demo.

The image format could be `.jpg`, `.jpeg`, `.png`.

4. Run the application:

	```
	$ python facial.py 
	```
	
5. Look at the camera for take the picture to recognize faces and compare with the base images of the system.
	
7. Press `CTRL-C` to stop the process.

## Running the Facial login web application Locally

1. Navigate to directory

	```
	$ cd \login_recognition_app\facialrecognition
	```
  

2. Make migrations of the required models and tables needed to run the program.
	```
	$ python manage.py makemigrations
	```
  

3. Perform Migrations.

	```
	$ python manage.py migrate
	```


4. Create a super user to access administrator controls and dashboard.

	```
	$ python manage.py createsuperuser
	```
![Captura de Pantalla 2023-02-06 a las 15 41 45](https://user-images.githubusercontent.com/110174766/217022005-001a3eb1-740a-4be6-82ba-ad37103dcef3.png)



5. Run the program.

	```
	$ python manage.py runserver
	
	or
	
	$ python manage.py runserver --nothreading --noreload
	```

6. Make sure to navigate in your browser to `http://localhost:8000/` to view the application.

![imagen](https://user-images.githubusercontent.com/110174766/217067999-bd319b8e-af8b-4cbb-a7d7-f83b22477159.png)

  

7. To access the admin type the following into the browser while the server is running `http://localhost:8000/admin`. 
This page will display the database and allow the admin to edit user's accounts.

8. To access the register type, please write an `username` and upload a image of this user to register into the system.

![imagen](https://user-images.githubusercontent.com/110174766/217067598-3f40c0fa-5d2a-4294-ad05-dc5e64b23208.png)
![imagen](https://user-images.githubusercontent.com/110174766/217067656-456b2aec-3837-4415-a125-d45029e51aa7.png)


The images taken in registration process are saved in `\login_recognition_app\facialrecognition\media\images` --> These are our base images for the recognition process.

9. To login into the system, please click on `Login`, write the registered `username` and then look the camera for the login photo verification process. 


![imagen](https://user-images.githubusercontent.com/110174766/217068990-e27e177e-08e3-4d60-b941-6ea55fac71c0.png)

Then, press `Q` for take the picture for login.

![imagen](https://user-images.githubusercontent.com/110174766/217068434-498c596d-6a82-4677-8b57-5028ca9226a8.png)



If the detected face make match with a registered username, then you'll have a `Welcome` like this:

![imagen](https://user-images.githubusercontent.com/110174766/217067344-bb8112fa-65e3-478d-8886-db4b3a63f949.png)

  
10. Press `CTRL-C` to stop the process.


