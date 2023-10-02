import requests
import random
import time

# URL de la API de imágenes de perros
dogs_api = 'https://dog.ceo/api/breeds/image/random'

# URL de tu aplicación FastAPI
fastapi_url = 'http://localhost:9001'

while True:
    # Consultar la API de imágenes de perros
    response = requests.get(dogs_api)

    if response.status_code == 200:
        data = response.json()
        new_image_url = data.get("message")

        if new_image_url:
            # Enviar la nueva URL a la API de FastAPI
            payload = {"new_image_url": new_image_url}
            update_response = requests.post(fastapi_url + '/update_image', json=payload)

            if update_response.status_code == 200:
                print("Imagen actualizada correctamente:", new_image_url)
            else:
                print("Error al actualizar la imagen:", update_response.text)
        else:
            print("No se pudo obtener la URL de la imagen")
    else:
        print("Error al consultar la API de imágenes de perros")

    # Esperar un tiempo aleatorio entre 0 y 15 segundos antes de la próxima consulta
    time.sleep(random.randint(0, 30))
