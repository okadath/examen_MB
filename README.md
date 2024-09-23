# examen
instrucciones para ejecutar el entorno
se uso la version de python 3.8, no deberia haber problemas con versiones superiores


## Instalacion

### Docker

crear el container con Docker Compose
```sh
docker compose build
```
y ejecutar el container 

```sh
docker compose up
```

abrirlo en la url `http://0.0.0.0:8000/`

### virtualenv

crear el entorno virtual e instalar dependencias
```sh
python -m venv env
source env/bin/activate
pip install -r requirements.txt 
```
y ejecutar el proyecto 

```sh
python manage.py runserver
```

abrirlo en la url `http://127.0.0.1:8000/`

### pipenv

crear el entorno virtual e instalar dependencias
```sh
pipenv shell --python=3.8
pipenv install
```
y ejecutar el proyecto 

```sh
python manage.py runserver
```

abrirlo en la url `http://127.0.0.1:8000/`

## proyecto


Swagger se muestra en la pagina principal para poder acceder a los endpoints con sencillez y poder probarlos, solo hay que hacer click en cada enpoint y ingresar los parametros.

La paginacion no es necesaria si hay pocos datos en la db(el valor de 10 es el tamaño por default de cada pagina), basta con colocar el valor de 1 si se desea probar este campo


![swagger](https://raw.githubusercontent.com/okadath/examen_MB/refs/heads/master/swagg.png)

### Filtro por edad

el campo para filtrar por edad minima es mimimum_age, en el endpoint se agrega al final de la url  `/?minimum_age=10`, en Swagger esta en el el campo "minimum_age" en su respectivo formulario
![swagger](https://raw.githubusercontent.com/okadath/examen_MB/refs/heads/master/filter.png)
