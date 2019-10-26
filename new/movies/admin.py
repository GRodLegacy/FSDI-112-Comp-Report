from django.contrib import admin

from .models import Genre, Movie, Serie

# Register your models here.
# So you can manage their data from the admin panel
# url/admin

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'in_stock', 'price' ) # properties that will be listed on the display table
    #exclude = ('in_stock',)
    fields = ('title', 'genre', 'in_stock', 'price', 'release_year')

class SerieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'season', 'episode', 'genre', 'price', 'in_stock')




admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Serie, SerieAdmin)
