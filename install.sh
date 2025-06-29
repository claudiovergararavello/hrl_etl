#!/bin/bash

# Asegurar que el directorio sea propiedad del usuario airflow
chown -R airflow: /opt/airflow

# Paso 1: Instalar dependencias del sistema como root
apt-get update && apt-get install -y build-essential g++ gcc

# Paso 2: Cambiar a usuario 'airflow' y ejecutar el resto
su - airflow <<EOF
pip install --no-cache-dir -r /requirements.txt
airflow db migrate
airflow users create -u admin -p admin -r Admin -f Admin -l User -e admin@example.com
airflow standalone
EOF
