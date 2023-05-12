from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    GENERO = (
        ('F', 'Femenino'),
        ('M', 'Masculino'),
        ('O', 'Otro'),
    )

    TIPO = (
        ('Medico', 'Medico'),
        ('Asistente', 'Asistente'),
        ('Secretaria', 'Secretaria'),
        ('Paciente', 'Paciente'),
    )

    #username = models.CharField('Nombre de usuario', max_length=20, unique=True)
    email = models.EmailField('Email', max_length=254, unique=True)
    telefono = models.CharField('Telefono', max_length=10, blank=True, null=True)
    full_name = models.CharField('Nombre completo', max_length=100, blank=True, null=True)
    tipo = models.CharField('Tipo de usuario', max_length=20, choices=TIPO, blank=True, null=True)
    genero = models.CharField('Genero', max_length=1, choices=GENERO, blank=True, null=True)
    dia_nac = models.DateField(blank=True, null=True)
    cod_registro = models.CharField('Codigo de registro', max_length=6, blank=True, null=True)
    num_registro = models.CharField('Numero de registro', max_length=6, blank=True, null=True)

    #Campos obligados por django
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['full_name',]

    object = UserManager()

    class Meta:
        verbose_name =  'Usuario'
        verbose_name_plural =  'Usuarios'


    def __str__(self):
        return self.full_name       

    def get_short_name(self):
        return self.email

    def get_full_name(self):
        return self.full_name
