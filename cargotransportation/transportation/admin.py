from django.contrib import admin
from .models import *


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'link')
    list_display_links = ('id', 'name')


@admin.register(Cards_orders)
class Cards_ordersAdmn(admin.ModelAdmin):
    list_display = ('id', 'title', 'short_description', 'full_description', 'slug', 'image_card')
    list_display_links = ('id', 'title')


@admin.register(Type_transporation)
class Type_transporationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_type', 'description', 'image_type')
    list_display_links = ('id', 'title_type')


@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_client', 'number_telephone', 'email')
    list_display_links = ('id', 'name_client')
    ordering = ('name_client',)


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'number_telephone', 'salary', 'pasport', 'work_experience')
    list_display_links = ('id', 'first_name')
    ordering = ('last_name',)


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'registration_number', 'technical_condition', 'type_vehicle', 'load_capacity', 'insurance_information')
    list_display_links = ('id', 'model')


@admin.register(Incidents)
class IncidentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_incident', 'date_incident', 'time_incident', 'type_incident', 'description')
    list_display_links = ('id', 'name_incident')


@admin.register(Cargos)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_cargo', 'weight', 'type', 'dimensions', 'type_transportation', 'status')
    list_display_links = ('id', 'name_cargo')


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_order', 'date_order', 'period_execution', 'price_order', 'order_completion_status',
                    'point_departure', 'point_destination', 'additional_information')
    list_display_links = ('id', 'name_order')
