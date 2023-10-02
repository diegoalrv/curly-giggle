# Aplicación Dockerizada con FastAPI

Esta es una aplicación Dockerizada que incluye un servidor FastAPI y un script para obtener periódicamente nuevas URL de imágenes de una API de imágenes de perros y actualizar el servidor FastAPI.

## Requisitos previos

- [Docker](https://www.docker.com/get-started)

## Uso

1. Clona este repositorio en tu máquina local:

   ```
   git clone https://github.com/tuusuario/turepositorio.git
   cd turepositorio
   ```

2. Construye el contenedor Docker para la aplicación FastAPI:
    
    ```
    docker build -t fastapi-app .
    ```

3. Ejecuta el contenedor de la aplicación FastAPI:
    
    ```
    docker run -d -p 9001:900l fastapi-app
    ```

4. Accede a la aplicación FastAPI:

Abre un navegador web y ve a http://localhost:9001. Deberías ver la documentación de FastAPI donde puedes probar los endpoints.

5. Para comprobar nuevas URL de imágenes:

El script random_image_change.py se ejecuta periódicamente dentro del contenedor y actualiza la aplicación FastAPI con nuevas URL de imágenes cuando están disponibles.

## Endpoints:

/check_changes (GET): Comprueba si hubo cambios en la URL de la imagen. Devuelve {"changes_occurred": true} o {"changes_occurred": false}.

/get_new_image (GET): Obtiene la nueva URL de la imagen si hubo cambios. Devuelve {"image_url": "nueva_url_de_imagen"} o {"message": "No hay cambios en la imagen"}.

/update_image (POST): Actualiza la URL actual de la imagen. Envía un payload JSON {"new_image_url": "nueva_url_aqui"} a este endpoint para actualizar la URL de la imagen.