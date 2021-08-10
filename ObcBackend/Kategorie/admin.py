from django.contrib import admin
from Kategorie.models import Letter, Kategoria, Profil, Miasto

# Register your models here.
class LetterAdmin(admin.ModelAdmin):
    ordering = ['title']
class MiastoAdmin(admin.ModelAdmin):
    ordering = ['title']
class KategoriaAdmin(admin.ModelAdmin):
    ordering = ['title']

class ProfilAdmin(admin.ModelAdmin):
    ordering = ['title']
# site register

admin.site.register(Letter, LetterAdmin)

admin.site.register(Kategoria, KategoriaAdmin)
admin.site.register(Profil, ProfilAdmin)
admin.site.register(Miasto, MiastoAdmin)