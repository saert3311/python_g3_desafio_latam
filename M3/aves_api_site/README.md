**Mini sitio de practica de acceso a apis**

Le dimos un twist a la forma de hacer el sitio, ya que aprovechamos a montar el template en flask para mostrar la información de la api https://aves.ninjas.cl/

Asi practicamos algo de manejo de templates para django

**Como usar**

Instala un ambiente virtual con:

    python -m venv venv
   
Recuerda activar el ambiente virtual

    venv/scripts/activate

Instalamos las dependencias del archivo requirements.txt

    pip install -r requirements.txt

Iniciamos el servidor flask para entrar a la web

    flask --app  birds run

Despues puedes acceder al sitio en la direccion http://127.0.0.1:5000/