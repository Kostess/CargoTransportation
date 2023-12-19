from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Clients)
admin.site.register(Driver)
admin.site.register(Vehicle)
admin.site.register(Orders)
admin.site.register(Incidents)
admin.site.register(Transportation_categories)
admin.site.register(Cargo)

class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
