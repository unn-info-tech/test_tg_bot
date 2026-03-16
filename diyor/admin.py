from django.contrib import admin
from .models import Kitob

@admin.register(Kitob)
class KitobAdmin(admin.ModelAdmin):
    list_display = ('nom', 'muallif', 'nashr_yili', 'narx')
    search_fields = ('nom', 'muallif')
    list_filter = ('nashr_yili',)