from django.contrib import admin

from .models import Contato

from django.contrib import admin

from .models import Livros

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone')


admin.site.register(Contato, ContatoAdmin)


class LivrosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'assunto', 'editora', 'isbn', 'ano')


admin.site.register(Livros, LivrosAdmin)
# Register your models here.
