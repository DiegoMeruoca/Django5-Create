from django.contrib import admin
from .models import Categoria, Transacao  # Importa o model


admin.site.register(Categoria)  # Registra no admin
admin.site.register(Transacao)  # Registra no admin