from django.contrib import admin
from gestorResultados.models import Canto, Baile, PlayBack, Conocimientos, Juegos, Barras

# Register your models here.

class Canto_admin(admin.ModelAdmin):

    list_display = ("jurado", "calificacion", "grado", "seccion")
    list_filter = ("grado", "seccion", "jurado")

class Baile_admin(admin.ModelAdmin):

    list_display = ("jurado", "calificacion", "grado", "seccion")
    list_filter = ("grado", "seccion", "jurado")

class Playback_admin(admin.ModelAdmin):

    list_display = ("jurado", "calificacion", "grado", "seccion")
    list_filter = ("grado", "seccion", "jurado")

class Conocimientos_admin(admin.ModelAdmin):

    list_display = ("calificacion", "grado", "seccion")
    list_filter = ("grado", "seccion")

class Juegos_admin(admin.ModelAdmin):

    list_display = ("calificacion", "grado", "seccion")
    list_filter = ("grado", "seccion")

class Barras_admin(admin.ModelAdmin):

    list_display = ("jurado", "calificacion", "grado", "seccion")
    list_filter = ("grado", "seccion", "jurado")

admin.site.register(Canto, Canto_admin)
admin.site.register(Baile, Baile_admin)
admin.site.register(PlayBack, Playback_admin)
admin.site.register(Conocimientos, Conocimientos_admin)
admin.site.register(Juegos, Juegos_admin)
admin.site.register(Barras, Barras_admin)