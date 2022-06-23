from django.contrib import admin
from . models import *
# Register your models here.
class catadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(categ,catadmin)

class prodtadmin(admin.ModelAdmin):
    list_display = ['name','slug','desc','price','stock','available']
    list_editable = ['desc','price','stock','available']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(products,prodtadmin)


