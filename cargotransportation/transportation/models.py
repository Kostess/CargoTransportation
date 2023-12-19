from django.db import models

class Clients(models.Model):
    name_client = models.CharField(max_length=30)
    number_telephone = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    inn = models.IntegerField(default=0)
    email = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Клиенты'
        verbose_name_plural = 'Клиенты'

class Driver(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number_telephone = models.CharField(max_length=30)
    salary = models.IntegerField(default=0)
    pasport = models.CharField(max_length=30)
    work_experience = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Водители'
        verbose_name_plural = 'Водители'

class Cargo(models.Model):
    weight = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    cargo_volume = models.CharField(max_length=30)
    cargo_value = models.IntegerField(default=0)
    dimensions = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Грузы'
        verbose_name_plural = 'Грузы'

class Vehicle(models.Model):
    type_vehicle = models.CharField(max_length=30)
    registration_number = models.CharField(max_length=30)
    technical_condition = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    load_capacity = models.CharField(max_length=30)
    insurance_information = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Техника'
        verbose_name_plural = 'Техника'

class Incidents(models.Model):
    name_incident = models.CharField(max_length=30)
    date_incident = models.DateField()
    time_incident = models.TimeField()
    type_incident = models.CharField(max_length=30)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Происшествия'
        verbose_name_plural = 'Происшествия'

class Transportation_categories(models.Model):
    category_type = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Категории перевозок'
        verbose_name_plural = 'Категории перевозок'

class Orders(models.Model):
    name_order = models.CharField(max_length=255)
    date_order = models.DateField()
    period_execution = models.CharField(max_length=30)
    price_order = models.IntegerField(default=0)
    order_completion_status = models.CharField(max_length=30)
    point_departure = models.CharField(max_length=255)
    point_destination = models.CharField(max_length=255)
    distance = models.IntegerField(default=0)
    additional_information = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Заказы'
        verbose_name_plural = 'Заказы'




