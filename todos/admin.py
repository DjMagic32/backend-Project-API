from django.contrib import admin
from .models import Todo

# Register your models here.
# Recordar siempre registrar el modelo de base de datos!!!
# Siempre se te olvida David!!!!

admin.site.register(Todo)
