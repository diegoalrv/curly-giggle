#!/bin/bash

# Ejecutar la aplicación FastAPI en segundo plano
uvicorn app:app --host 0.0.0.0 --port 9001 &

# Ejecutar el script random_image_change.py en segundo plano
python random_image_change.py

# Mantener el contenedor en ejecución
tail -f /dev/null
