# Facial Recognition and Login Facial System


[Stephany Valderrama](https://github.com/stph89)&nbsp;and [Wenya Li](https://github.com/wenlla)  &nbsp;

[![Gitpod Ready-to-Code](https://img.shields.io/badge/Gitpod-Ready--to--Code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/Moran98/facial-recognition)

  

## Requirements

The requirements needed for this project are as follows :

* Python 3.8+

* Linux, Windows, MacOS

* Django

* Latest version of pip
  

## Installation
  
For run theses facial recognition demos, You required to install the following python module.


```
pip3 install django
pip3 install numpy
pip3 install opencv-python
pip3 install Pillow
pip3 install face_recognition
```
  **Note:** Make sure you are using the latest version of pip.
#### For Mac or Linux --> follow the instructions of [face_recognition docs](https://gist.github.com/ageitgey/629d75c1baac34dfa5ca2a1928a7aeaf)

#### For Windows --> follow the instructions of [face_recognition docs](https://github.com/ageitgey/face_recognition/issues/175#issue-257710508)

**Note:** Currently the packages for face_recognition are not fully supported on Windows. 


## Demos with `face recognition` and `openCV` libraries.
We proposed two demos using [face recognition library](https://github.com/ageitgey/face_recognition):

 **i. Simple sample of Face recognition system on live video from a local webcam.**
 
 **ii. Facial login web application with Django framework and my-sql databases.**
  
  
  
## Running the Face recognition system on live video from a local webcam
This is a face recognition system on live video from a local webcam.

1. Navigate to directory

	```
	$ cd \facial-recognition\facialrecognition
	```
2. Put into `info_facial` folder the images of the persons that you want to recognize in this demo.

4. Run the application:

	```
	$ python facial.py 
	```
	
5. Look at the camera for take the picture to recognize faces and compare with the base images of the system.
	
7. Press `CTRL-C` to stop the process.

## Running the Facial login web application Locally

1. Navigate to directory

	```
	$ cd \facial-recognition\facialrecognition
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
  

7. To access the admin type the following into the browser while the server is running `http://localhost:8000/admin`. 
This page will display the database and allow the admin to edit user's accounts.

8. To access the register type, please upload a image of the person to register and enter a username.

![Captura de Pantalla 2023-02-06 a las 16 08 46](https://user-images.githubusercontent.com/110174766/217021702-a0a3dc69-67a4-47fe-9fba-07145cca5a99.png)

9. To login into the system, please click on `Login` and then look the camera for the recognition process. 

Press `Q` for take the picture for login.
  
10. Press `CTRL-C` to stop the process.

Modified code from: [Aaron Moran](https://github.com/Moran98)&nbsp;, [Arnas Steponavicius](https://github.com/ArnasSteponavicius00)&nbsp;and [Thomas Kenny](https://github.com/KennyThomas)
