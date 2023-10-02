# Usar la imagen base de Python 3.8
FROM python:3.8

# Establecer el directorio de trabajo en /app
WORKDIR /app

# Copiar el código de la aplicación FastAPI al contenedor
COPY . .

# Instalar las dependencias especificadas en requirements.txt
RUN pip install -r requirements.txt

# Exponer el puerto 9001 para que la aplicación FastAPI esté disponible desde fuera del contenedor
EXPOSE 9001

# Copiar el script de inicio al contenedor
COPY start.sh .

# Dar permisos de ejecución al script de inicio
RUN chmod +x start.sh

# Comando para ejecutar el script de inicio
CMD ["./start.sh"]
