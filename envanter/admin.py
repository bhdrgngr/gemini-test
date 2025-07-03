from django.contrib import admin
from .models import Firma, Parca, Fotograf

class FotografInline(admin.TabularInline):
    model = Fotograf
    extra = 1  # Varsayılan olarak 1 ekstra fotoğraf yükleme alanı gösterir

@admin.register(Parca)
class ParcaAdmin(admin.ModelAdmin):
    inlines = [FotografInline]
    list_display = ('ad', 'firma', 'adet', 'renk', 'eklenme_tarihi')
    list_filter = ('firma', 'renk')
    search_fields = ('ad', 'firma__ad')

@admin.register(Firma)
class FirmaAdmin(admin.ModelAdmin):
    search_fields = ('ad',)

# Fotograf modelini doğrudan admin panelinde görmek isterseniz bu satırı ekleyebilirsiniz.
# admin.site.register(Fotograf)