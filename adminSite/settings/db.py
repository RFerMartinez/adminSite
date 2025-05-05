from pathlib import Path

# path del directorio que contiene el archivo "manage.py"
BASE_DIR = Path(__file__).resolve().parent.parent

# Configuración para la Base de Datos por defecto (SQLite)
SQLITE3 = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Configuración para base de Datos PostgreSQL
POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '---',
        'USER': 'postgres',
        'PASSWORD': '---',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}