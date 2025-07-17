Proyecto Final - Blog Personal
Desarrollado por Lucrecia como entrega final para el curso de Python en Coderhouse.

📌 Descripción

Este proyecto es una aplicación web tipo blog, donde los usuarios pueden:

--Registrarse, iniciar y cerrar sesión.
-Ver y editar su perfil.
-Crear, leer, actualizar y eliminar páginas con contenido enriquecido.
-Buscar páginas por título.
-Ver una sección personalizada "Acerca de mí".
-Acceder a las funcionalidades desde una interfaz clara con navegación dinámica.

🚀 Cómo correr el proyecto
1. Cloná el repositorio:
'''bash
git clone https://github.com/Lucrecia19/blog-lucrecia
cd blog-lucrecia

2. Creá y activá un entorno virtual:

python -m venv venv
venv\Scripts\activate   # En Windows

3. Instalá las dependencias:

pip install -r requirements.txt

4. Aplicá las migraciones:

python manage.py migrate

5. Corré el servidor:

python manage.py runserver

6. Accedé desde tu navegador en http://127.0.0.1:8000/


🧪Usuario de prueba

-Usuario: prueba
Contraseña: coderhouse123


🛠 Requisitos técnicos

-Python 3.13.2
-Django 4.x
-django-ckeditor
-Uso de herencia de templates (base.html)
-CBVs, mixin y decoradores
-Archivos ignorados: db.sqlite3, _pycache_, media


📁 Estructura del proyecto

-accounts/: Registro, login, perfil y logout
-paginas/: CRUD de páginas
-templates/: Base de vistas HTML
-media/: Imágenes cargadas por usuarios (ignorada en Git)
-static/: Archivos estáticos

📽 Video demostración

-En el siguiente video se puede ver el funcionamiento del proyecto:

 https://youtu.be/7EGJk8VCygw