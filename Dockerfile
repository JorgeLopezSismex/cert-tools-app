# Usa la imagen oficial de Python 3.10.12
FROM python:3.10.12-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación al contenedor
COPY . .

# Expone el puerto 5000
EXPOSE 5000

# Establece el comando predeterminado para ejecutar la aplicación
CMD ["python", "run.py"]

