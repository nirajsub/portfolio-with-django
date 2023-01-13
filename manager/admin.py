from django.contrib import admin
from .models import*

admin.site.register(
    [Planguage, Dtool, skills, Project, Contact, Framework, DataBase]
)