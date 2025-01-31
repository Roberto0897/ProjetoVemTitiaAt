from django.contrib import admin
from . import models


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ('name',)

admin.site.register(models.Cliente, ClienteAdmin)

