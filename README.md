# Facial Recognition and Login System


[Stephany Valderrama](https://github.com/stph89)&nbsp;and [Wenya Li](https://github.com/wenlla)  &nbsp;

[![Gitpod Ready-to-Code](https://img.shields.io/badge/Gitpod-Ready--to--Code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/Moran98/facial-recognition)

  

## Requirements

The requirements needed for this project are as follows :

* Python 3.8+

* Linux, Windows, MacOS

* Django

* Latest version of pip
  

## Installation
  

#### Installing Packages on Mac or Linux follow the instructions below

* https://gist.github.com/ageitgey/629d75c1baac34dfa5ca2a1928a7aeaf
  

Then you are required to install the following python module (Make sure you are using the latest version of pip):

```
pip3 install django
pip3 install opencv-python
pip3 install Pillow
pip3 install face_recognition
```
  

#### Installing Packages on Windows

Currently the packages for face_recognition are not fully supported on Windows, to get around this issue you must follows the instructions below.

* https://github.com/ageitgey/face_recognition/issues/175#issue-257710508

  

## Running the Application Locally

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

6. Make sure to navigate in your browser to 'http://localhost:8000/' to view the application.
  

7. To access the admin type the following into the browser while the server is running `http://localhost:8000/admin`. 
This page will display the database and allow the admin to edit user's accounts.

8. To access the register type, please upload a image of the person to register and enter a username.

![Captura de Pantalla 2023-02-06 a las 16 08 46](https://user-images.githubusercontent.com/110174766/217021702-a0a3dc69-67a4-47fe-9fba-07145cca5a99.png)

9. To login into the system, please click on `Login` and then look the camera for the recognition process. 

Press `Q` for take the picture for login.
  
10. Press `CTRL-C` to stop the process.

Modified code from: [Aaron Moran](https://github.com/Moran98)&nbsp;, [Arnas Steponavicius](https://github.com/ArnasSteponavicius00)&nbsp;and [Thomas Kenny](https://github.com/KennyThomas)
