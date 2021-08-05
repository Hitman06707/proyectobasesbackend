from django.contrib import admin
from client.models import Pais

# Register your models here.
class PaisAdmin(admin.ModelAdmin):
    list_display = ('id_pais', 'codigo_postal', 'nombre', 'ciudad')
    #search_fields = ('ch_name_business', 'ch_tradename', 'ch_abbreviation')
    #resource_class = BusinessResource
    #inlines = [TemplateLookAndFeelInLine, ConfigSendMailInLine]


admin.site.register(Pais, PaisAdmin)
