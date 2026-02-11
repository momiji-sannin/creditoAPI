# Django

Este es un repositorio contiene el desarrollo de una REST API la cual se conecta una base de datos (SQLite) para guardar información proporcionada por el usario a partir de archivos de un POST /applications/. También, tiene la posibilidad de subir archivos de imagen de comprobante de domicilio por medio POST /applications/*<app_id>*/documents. Por último, procesa y valida la informacion del usuario y genera un status de aprobación para préstamo bancario a través de un GET /getscore.


## Instalación

Para instalar el proyecto se necesita instalar la librería *pipenv* de Python usando el siguiente comando.

```bash
pipenv install django
```

Situarnos en la carpeta del repositorio y activar virtual por medio de:
```bash
cd \path\del\repositorio
 python -m pipenv shell  
```

Por último, instalamos las dependencias del proyecto en el archivo *requirements.txt*

```bash
pip install -r requirements.txt
```

## Correr Localmente 

Para correr el proyecto, nos conectamos al servidor de local mediante:

```
 python manage.py runserver   
```

Damos click en la URL que nos genera para conectarnos a la API. Para ver la documentación y el monitoreo de la misma, visitamos la ruta:

- (eg.) http://127.0.0.1:8000

## REST API

Esta applicacióm fue creada con ayuda del framework [*Django*](https://www.djangoproject.com/). Cuenta con las siguentes funciones principales:

### *Upload Application*
*URL:* `POST creditscore/applications/`

Se suben la informacion del cliente llenado una forma la cual pide los siguientes campos:
- nombre
- apellido
- edad
- género
- ingreso mensual
- rfc


### *Get Score*
*URL:* `GET creditscore/applications/<app_id>/getscore`

Regresa el si status del la aplicación, ya sea "Aprovado" o "Denegado".

### *Upload Image*
*URL:* `POST creditscore/applications/<app_id>*documents`

Sirve para subir un Comprobante de Domicilio


## Modelos de Datos

Para el diseño de la base de datos se considero que eran necesarias 4 tablas: 
- Clientes
- Aplicaciones
- Documentos
- Dirección

Ya que así se puede agregar información que sea relevante para los clientes y tener la posibilidad de añadir más campos en un futuro(eg. correo, edad, etc). Con una entidad de relación de uno a muchos con respecto a la de aplicaciones ya que existe la posibildad de que un mismo cliente pueda aplicar mas de una vez. Se mantuvo una relacion de 1 a 1 para las demas tablas para reducir las cantidad de informacion almacenada.

Para la primary key de las Applicaciones se decidió por usar UUID que se genera automaticámente al momento de subir una aplicacion, asi podria acceder a la consulta de su aplicacion sin dejarla expuesta.

Al momento de que un usario que haya hecho alguna aplicacion previamente, se podra actualizar su informacion sin duplicar informacion. Esto es posible al momento del POST/applications/ checar si el cliente ya existe comparando el RFC ya que único.