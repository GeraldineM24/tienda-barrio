# Imagen base oficial de Python
FROM python:3.11-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar archivo de dependencias
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente
COPY src/ ./src/
COPY tests/ ./tests/

# Variable de entorno
ENV PYTHONPATH=/app

# Comando por defecto - ejecutar pruebas
CMD ["python", "-m", "pytest", "tests/", "-v"]