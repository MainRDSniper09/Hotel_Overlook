# Django Hotel Overlook

Este es un sistema de gestión de hoteles desarrollado con **Django**.

## 📌 Requisitos

Asegúrate de tener instalado:
- **Python** (versión 3.13.2 o superior recomendada)
- **pip** y **virtualenv**
- **Git**

## 🚀 Instalación

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo
```

### 2️⃣ Crear un entorno virtual
```bash
python -m venv venv
```

### 3️⃣ Activar el entorno virtual
- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **Linux/Mac:**
  ```bash
  source venv/bin/activate
  ```

### 4️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```

## 🔧 Configuración

### 5️⃣ Aplicar migraciones
```bash
python manage.py migrate
```

### 6️⃣ Crear un superusuario
```bash
python manage.py createsuperuser
```
Ingresa un **nombre de usuario**, **correo electrónico** (opcional) y **contraseña**.

### 7️⃣ Correr el servidor
```bash
python manage.py runserver
```
Luego, abre [http://127.0.0.1:8000](http://127.0.0.1:8000) en tu navegador.

## 🛠 Funcionalidades

- **Administración de inventario** (productos, categorías, órdenes).
- **Sistema de autenticación** (registro, login, logout, perfiles).
- **Panel de administración de Django** para gestionar datos fácilmente.

## 📂 Estructura del Proyecto
```
📂 tu-repo/
├── dashboard/      # Aplicación principal
├── user/           # Gestión de usuarios
├── templates/      # Archivos HTML
├── static/         # Archivos CSS, JS, imágenes
├── db.sqlite3      # Base de datos SQLite (por defecto)
├── manage.py       # Archivo principal de Django
└── requirements.txt # Dependencias del proyecto
```

## 📝 Notas
- Para cerrar sesión, usa el botón de **Logout**, que realiza una petición **POST**.
- Si tienes problemas con la base de datos, intenta **eliminar `db.sqlite3` y volver a migrar**:
  ```bash
  rm db.sqlite3
  python manage.py migrate
  ```


