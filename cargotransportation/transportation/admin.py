from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'link')
    list_display_links = ('id', 'name')

@admin.register(Cards_orders)
class Cards_ordersAdmn(admin.ModelAdmin):
    list_display = ('id', 'title', 'short_description', 'full_description', 'slug', 'image_card')
    list_display_links = ('id', 'title')

@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_client', 'number_telephone', 'adress', 'inn', 'email')
    list_display_links = ('id', 'name_client')
    ordering = ('name_client',)

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'number_telephone', 'salary', 'pasport', 'work_experience')
    list_display_links = ('id', 'first_name')
    ordering = ('last_name',)

# admin.site.register(Clients, ClientsAdmin)
# admin.site.register(Driver, DriverAdmin)
admin.site.register(Vehicle)
admin.site.register(Orders)
admin.site.register(Incidents)
admin.site.register(Transportation_categories)
admin.site.register(Cargo)


