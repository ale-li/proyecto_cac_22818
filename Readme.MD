# proyecto_cac_22818_G13
Abro la carpeta proyecto_cac_22818 en Visual Studio Code

Abro una terminal.

Verifico si está Python instalado y que versión es:
python --version

Para aislar el proyecto creo un entorno virtual que contenga una propia version de Python

Utilizar el módulo venv y crear la carpeta venv con el entorno virtual
python -m venv venv

Una vez que aparece la carpeta venv en VSCode pulso F1 y <Python: Select Interpreter> selecciono en entorno virtual (venv)
En terminal me tiene que mostrar el entorno virtual de trabajo. 
Sino en la terminal hay que ejecutar:
En CMD:
.\venv\Scripts\activate.bat

En Powershell:
.\venv\Scripts\activate.ps1

pip install -r requirements.txt

Creo la base de datos
python manage.py makemigrations
python manage.py migrate

Crear Superusuario de admin
python manage.py createsuperuser
usuario
algo@gmail.com
123

Ahora ya tengo el proyecto y voy a ejecutarlo:
python manage.py runserver



NOTA:
Si no se encuentra requirements.txt

Si quiero actualizar pip
.\venv\Scripts\python.exe -m pip install --upgrade pip

Ahora instalamos Django:
pip install django

Verifico la versión de Django:
django-admin --version

crear requirements.txt desde el entorno virtual
pip freeze > requirements.txt

