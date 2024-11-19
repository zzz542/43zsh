from django.contrib import admin
from .models import Music,Review
# Register your models here.
class MusicAdmin(admin.ModelAdmin):
    list_display = ('title','description')
    search_fields = ['title','description']
    list_editable = ('description',)

admin.site.register(Music,MusicAdmin)
admin.site.register(Review)