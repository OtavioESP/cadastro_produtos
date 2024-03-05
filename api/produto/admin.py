from django.contrib import admin

from produto.models import Produto


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    pass
