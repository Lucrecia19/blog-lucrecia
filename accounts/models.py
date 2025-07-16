from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100, blank=True)
    apellido = models.CharField(max_length=100, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio = models.TextField(blank=True)
    link = models.URLField(max_length=200, blank=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)

    def _str_(self):
        return f'Perfil de {self.user.username}'