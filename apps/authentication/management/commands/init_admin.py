"""
Comando para inicializar un superusuario automáticamente
"""
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

User = get_user_model()

class Command(BaseCommand):
    help = 'Crea un superusuario si no existe ninguno'

    def handle(self, *args, **options):
        # Verificar si ya existe algún superusuario
        if User.objects.filter(is_superuser=True).exists():
            self.stdout.write(
                self.style.WARNING('Ya existe un superusuario. No se creó ninguno nuevo.')
            )
            return

        # Obtener credenciales desde variables de entorno o usar valores por defecto
        username = os.getenv('DJANGO_SUPERUSER_USERNAME', 'admin')
        email = os.getenv('DJANGO_SUPERUSER_EMAIL', 'admin@huellitas.com')
        password = os.getenv('DJANGO_SUPERUSER_PASSWORD', 'Huellitasadmin') 

        try:
            user = User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            self.stdout.write(
                self.style.SUCCESS(f'Superusuario "{username}" creado exitosamente')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error al crear superusuario: {str(e)}')
            )
