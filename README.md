

## Instalación

### 1. Clonar repositorio

# Plantas Agriconecta

<img src="https://github.com/user-attachments/assets/161dd911-e035-487b-ad26-7fb4681db956" width="450" />

Plataforma digital para conectar agricultores y compradores en Guatemala.

<img src="https://github.com/user-attachments/assets/9c53beac-9e87-4df2-98b8-c68605bd8d54" />

---

## Tabla de Contenidos

- Descripción
- Características
- Tecnologías
- Requisitos Previos
- Instalación
- Configuración
- Uso
- Estructura del Proyecto
- API Endpoints
- Scripts Disponibles
- Testing
- Despliegue
- Contribución
- Autores
- Licencia

---

## Descripción

Agriconecta es una plataforma web que conecta directamente a agricultores guatemaltecos con compradores como restaurantes, tiendas y consumidores finales. El objetivo es eliminar intermediarios, mejorar precios y fomentar el comercio justo.

### Problemas que resuelve

- Dificultad de los agricultores para vender directamente
- Búsqueda de productos frescos y locales por parte de compradores
- Intermediarios que elevan precios y reducen ganancias

### Solución

La plataforma permite:

- Publicar y gestionar productos agrícolas
- Recibir pedidos en tiempo real
- Trazabilidad completa de pedidos
- Organización geográfica por departamento y municipio

---

## Características

### Agricultores

- Publicación de productos con fotos y descripciones
- Gestión de inventario en tiempo real
- Panel de ventas y estadísticas
- Notificaciones de pedidos
- Sistema de calificaciones

### Compradores

- Búsqueda y filtros avanzados
- Carrito de compras
- Productos por ubicación
- Interfaz responsive
- Contacto directo con productores

### Generales

- Autenticación JWT
- Sistema de ubicación nacional
- Notificaciones por correo
- Interfaz moderna

---

## Tecnologías

### Backend

- Python 3.11+
- Django 5
- Django REST Framework
- PostgreSQL 16
- JWT
- Pillow
- CORS Headers

### Frontend

- React 18
- TypeScript
- Vite
- React Router
- Axios
- CSS3

### DevOps

- Render
- Netlify o Vercel
- GitHub
- Gunicorn
- WhiteNoise

---

## Requisitos Previos

### Backend
- Python 3.11+
- pip
- PostgreSQL
- virtualenv

### Frontend
- Node 18+
- npm o yarn

### Herramientas
- Git
- VS Code
- Postman

---

## Instalación

### 1. Clonar repositorio

```bash
git clone [https://github.com/tu-usuario/agriconecta.git](https://github.com/DougO28/HuellitasBackend)
cd agriconecta

# Navegar a la carpeta del backend
cd backend

# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```bash

# Navegar a la carpeta del frontend (desde la raíz)
cd frontend

# Instalar dependencias
npm install
# o con yarn:
yarn install

Backend - Variables de Entorno

Crear un archivo .env en la carpeta backend/

# Django Settings
SECRET_KEY=tu-secret-key-super-segura-aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DB_NAME=agriconecta_db
DB_USER=postgres
DB_PASSWORD=tu_password
DB_HOST=localhost
DB_PORT=5432

# CORS Settings
CORS_ALLOWED_ORIGINS=http://localhost:5173,http://127.0.0.1:5173

# Email Settings (opcional)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=tu-email@gmail.com
EMAIL_HOST_PASSWORD=tu-password-de-app
EMAIL_USE_TLS=True

# Media Files
MEDIA_URL=/media/
MEDIA_ROOT=media/

# Production (solo para deployment)
RENDER_EXTERNAL_HOSTNAME=tu-app.onrender.com

Generar Secret Key
# En Python shell
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())

Frontend - Variables de Entorno

# API URL
VITE_API_URL=http://localhost:8000/api

# Production
# VITE_API_URL=https://tu-backend.onrender.com/api


Ejecutar Migraciones

# Asegúrate de estar en la carpeta backend con el venv activado
python manage.py makemigrations
python manage.py migrate

Carga de Datos Iniciales

# Cargar departamentos y municipios de Guatemala
python manage.py loaddata fixtures/ubicaciones.json

# Cargar categorías de productos
python manage.py loaddata fixtures/categorias.json

# Crear superusuario
python manage.py createsuperuser
```

### Uso Modo Dev

Backend (Django)

# Asegúrate de estar en la carpeta backend
cd backend

# Activar entorno virtual
source venv/bin/activate  # macOS/Linux
# o
venv\Scripts\activate  # Windows

# Ejecutar servidor de desarrollo
python manage.py runserver

# El servidor estará disponible en:
# http://localhost:8000
# Admin panel: http://localhost:8000/admin

Frontend  (React)

# Asegúrate de estar en la carpeta frontend
cd frontend

# Ejecutar servidor de desarrollo
npm run dev
# o
yarn dev

# El servidor estará disponible en:
# http://localhost:5173

### Modo Producción

Backend
# Recolectar archivos estáticos
python manage.py collectstatic --noinput

# Ejecutar con Gunicorn
gunicorn agriconecta.wsgi:application --bind 0.0.0.0:8000

Frontend

# Construir para producción
npm run build
# o
yarn build

# Los archivos optimizados estarán en la carpeta 'dist/'

## Estructura del Proyecto

```text
agriconecta/
│
├── backend/
│   ├── agriconecta/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │
│   ├── api/
│   │   ├── models/
│   │   │   ├── usuario.py
│   │   │   ├── producto.py
│   │   │   ├── pedido.py
│   │   │   └── ubicacion.py
│   │   │
│   │   ├── serializers/
│   │   ├── views/
│   │   ├── migrations/
│   │   └── urls.py
│   │
│   ├── media/
│   ├── fixtures/
│   ├── requirements.txt
│   └── manage.py
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── api/
│   │   ├── components/
│   │   ├── context/
│   │   ├── pages/
│   │   ├── styles/
│   │   ├── App.tsx
│   │   └── main.tsx
│   │
│   ├── .env
│   ├── package.json
│   ├── tsconfig.json
│   └── vite.config.ts
│
├── .gitignore
├── README.md
└── LICENSE
```



### Arquitectura del Backend

┌─────────────┐
│   Cliente   │
│  (Frontend) │
└──────┬──────┘
       │ HTTP Request
       ▼
┌─────────────┐
│    URLs     │  ← urls.py (Routing)
└──────┬──────┘
       │
       ▼
┌─────────────┐
│    Views    │  ← Lógica de negocio
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Serializers │  ← Validación y conversión
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Models    │  ← Interacción con BD
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  PostgreSQL │  ← Base de datos
└─────────────┘


### API Endpoints

Base URL
Development: http://localhost:8000/api
Production: https://backend.onrender.com/api   -- en este caso se usa el del servidor que vayan a utilizar, en mi caso fue render.

Autenticación

| Método | Endpoint | Descripción | Autenticación |
|--------|-----------|--------------|----------------|
| POST | /usuarios/register/ | Registrar nuevo usuario | No |
| POST | /usuarios/login/ | Iniciar sesión | No |
| GET | /usuarios/me/ | Obtener usuario actual | Sí |
| PUT | /usuarios/me/ | Actualizar perfil | Sí |

Productos

| Método | Endpoint | Descripción | Autenticación |
|--------|-----------|--------------|----------------|
| GET | /productos/ | Listar todos los productos | No |
| GET | /productos/{id}/ | Obtener producto específico | No |
| POST | /productos/ | Crear producto | Sí (Agricultor) |
| PUT | /productos/{id}/ | Actualizar producto | Sí (Dueño) |
| DELETE | /productos/{id}/ | Eliminar producto | Sí (Dueño) |
| GET | /productos/?categoria={id} | Filtrar por categoría | No |
| GET | /productos/?search={query} | Buscar productos | No |

Pedidos

| Método | Endpoint | Descripción | Autenticación |
|--------|-----------|--------------|----------------|
| GET | /pedidos/ | Listar mis pedidos | Sí |
| GET | /pedidos/{id}/ | Obtener pedido específico | Sí |
| POST | /pedidos/ | Crear nuevo pedido | Sí (Comprador) |
| PATCH | /pedidos/{id}/actualizar_estado/ | Actualizar estado | Sí (Agricultor) |
| DELETE | /pedidos/{id}/ | Cancelar pedido | Sí (Comprador) |

Ubicaciones

| Método | Endpoint | Descripción | Autenticación |
|--------|-----------|--------------|----------------|
| GET | /departamentos/ | Listar departamentos | No |
| GET | /municipios/ | Listar municipios | No |
| GET | /municipios/?departamento={id} | Municipios por departamento | No |

Categorías

| Método | Endpoint | Descripción | Autenticación |
|--------|-----------|--------------|----------------|
| GET | /categorias/ | Listar categorías | No |

### Autenticación JWT

Se incluye token en el header de cada petición autenticada

headers: {
  'Authorization': 'Bearer tu_token_aqui'
}

### Ejemplo de una petición

// Login
const response = await fetch('http://localhost:8000/api/usuarios/login/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    email: 'usuario@email.com',
    password: 'password123'
  })
});

const data = await response.json();
const token = data.token;

// Crear producto (con token)
const producto = await fetch('http://localhost:8000/api/productos/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${token}`
  },
  body: JSON.stringify({
    nombre: 'Tomates Cherry',
    descripcion: 'Tomates orgánicos',
    precio: 15.00,
    cantidad_disponible: 50,
    unidad_medida: 'libra',
    categoria: 1
  })
});



### Scripts Disponibles

### Backend
# Ejecutar servidor de desarrollo
python manage.py runserver

# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Cargar datos iniciales
python manage.py loaddata fixtures/ubicaciones.json

# Ejecutar tests
python manage.py test

# Recolectar archivos estáticos
python manage.py collectstatic

# Shell de Django
python manage.py shell

# Mostrar URLs disponibles
python manage.py show_urls

###Test Backend

# Todos los tests
python manage.py test

# Tests de una app específica
python manage.py test api

# Tests específicos con verbosidad
python manage.py test api.tests.test_models --verbosity=2

# Con coverage
coverage run --source='.' manage.py test
coverage report
coverage html  # Genera reporte HTML

###Frontend 

# Desarrollo
npm run dev          # Ejecutar servidor de desarrollo
npm run build        # Construir para producción
npm run preview      # Preview de build de producción
npm run lint         # Ejecutar linter

# Testing (si está configurado)
npm run test         # Ejecutar tests
npm run test:watch   # Tests en modo watch

###Frontend Testing

# Instalar dependencias de testing
npm install --save-dev vitest @testing-library/react @testing-library/jest-dom

# Ejecutar tests
npm run test

se debe actualizar settings.py

import os
from pathlib import Path

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost').split(',')

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}

crear build.sh

#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

Configurar en Render

Conecta tu repositorio de GitHub
Build Command: ./build.sh
Start Command: gunicorn agriconecta.wsgi:application
Agrega variables de entorno en el dashboard

Frontend - Netlify/Vercel
Netlify
bash# Instalar Netlify CLI
npm install -g netlify-cli

# Deploy
npm run build
netlify deploy --prod --dir=dist
Vercel
bash# Instalar Vercel CLI
npm install -g vercel

# Deploy
vercel --prod
Variables de Entorno en Producción
Backend (Render):

SECRET_KEY
DEBUG=False
ALLOWED_HOSTS
DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT
CORS_ALLOWED_ORIGINS

Frontend (Netlify/Vercel):

VITE_API_URL=https://tu-backend.onrender.com/api


###Autor
Equipo de Desarrollo
- Douglas Ortega - Desarrollador

- Contacto> douguiortega@gmail.com

###Agradecimiento
- A todas las personas que me confiaron e inspiraron este proyecto
- Recursos Utilizados
  - Django Documentation> https://docs.djangoproject.com/
  - React Documentation> https://react.dev/
  - MySQL Documentation> https://dev.mysql.com/doc/


<div align="center">
Hecho con el corazon para los agricultores de Guatemala
⬆ Volver arriba
</div>

