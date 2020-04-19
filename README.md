# Minor1

<h3>About the Application</h3>
<p>This is an android bus tracking application which is made so that the college going students can know the live whereabouts 
of the bus so that they do not miss their bus. This will also avoid panic the students face and contribute in their mental well being.
The application also has voice notification support so the student need not look at the smartphone while walking for their stops avoiding the chances of accidents</p>

<h3>Screenshots</h3>
<img height=500 width=400 src="https://github.com/thesparkvision/Minor1/blob/master/add%20copy.png" alt="Admin Panel">
<h4>Fig.1 Admin Update Screen</h4><br>

<img height=500 width=400 src="https://github.com/thesparkvision/Minor1/blob/master/admin.png" alt="Main Admin screen">
<h4>Fig.2 Main Admin Screen</h4><br>

<img height=500 width=400 src="https://github.com/thesparkvision/Minor1/blob/master/forgot.png" alt="Forgot Password Screen">
<h4>Fig.3 Forgot Password Screen</h4><br>

<img height=500 width=400 src="https://github.com/thesparkvision/Minor1/blob/master/login%20copy.png" alt="Login Screen">
<h4>Fig.4 Login Screen</h4><br>

<img height=500 width=400 src="https://github.com/thesparkvision/Minor1/blob/master/map.png" alt="Home Screen">
<h4>Fig.5 Home Screen</h4><br>

<img height=500 width=400 src="https://github.com/thesparkvision/Minor1/blob/master/navbar.png" alt="Navigation Bar">
<h4>Fig.6 Navigation Bar</h4><br>


<h3>Technical Specifications</h3>
<p>This is a bus tracking application made using Python Kivy Framework and Firebase NoSQL database.
It also uses Google Maps API,OTP generator , email sending facility. 
The application also has voice notification facility using python packages.
The application has used all the CRUD operations for the admin panel and also an authentication mechanism to check whether the user is admin or client.
</p>

<h3>Necessary Requirements</h3>
<p>This application requires a Google Maps account using Credit card. Also a firebase database and a gmail id with password.
You have to do the necessary changes of this for successful execution of the application</p>

<h3>Installation Steps</h3>
<p>To run this application on Windows,
    
1. First install Python 3.5 or higher
    [Make sure you install Python in C:\Python\   as python has problem with space separated folders
     and make sure python is added to system path  and pip is checked in installation]

2. Go on cmd and type python --version to see if path is set.
    Type pip --version. If it is not installed,you have to install it manually from google by typing pip download

3. After pip is installed, type 
   python -m pip install --upgrade pip wheel setuptools virtualenv
 and execute on cmd

4. Then type
   python -m virtualenv kivy_venv on cmd

5. Then type kivy_venv\Scripts\activate , 
  [Your terminal should now preface the path with something like (kivy_venv), indicating that the kivy_venv environment is active. If it doesn’t say that, the virtual environment is not active.]

6. Installing the dependencies,
    run this command on cmd:
    python -m pip install docutils pygments pypiwin32 kivy_deps.sdl2==0.1.22 kivy_deps.glew==0.1.12

7. Then write python -m pip install kivy==1.11.1 and execute

8. After that, write pip install pyttsx3

9. Then , type python and a >>> prompt will appear ,type import kivy and press enter to check whether kivy is installed or not

10. Then write exit() and exit from python shell

11. Write garden install mapview

12. You are ready to run this application :)

    The demo admin login credentials are
       Username =0704ADMIN2019 ,
       Password=Admin@123

    The demo user credentials are 
       Username=0704USER2019 ,
       Password=User@123 
