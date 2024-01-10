from django.db import models
from django.urls import reverse

class Menu(models.Model):
    name = models.CharField(max_length=60, verbose_name='Название')
    link = models.CharField(max_length=255, verbose_name='Ссылка')

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

class Cards_orders(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    short_description = models.CharField(max_length=255, blank=True, verbose_name='Краткое описание')
    full_description = models.TextField(blank=True, verbose_name='Полное описание')
    image_card = models.ImageField(upload_to='transporations/images/', verbose_name='Изображение')
    slug = models.SlugField(max_length=255, db_index=True, unique=True)

    class Meta:
        verbose_name = 'Карточка закоза'
        verbose_name_plural = 'Карточки закозов'

    def get_absolute_url(self):
        return reverse('service', kwargs={'name': self.slug})

    def __str__(self):
        return self.title

class Type_transporation(models.Model):
    title_type = models.CharField(max_length=60, verbose_name='Типы перевозок')
    description = models.TextField(blank=True, verbose_name='Описание')
    image_type = models.ImageField(verbose_name='Изображение')

    class Meta:
        verbose_name = 'Тип перевозок'
        verbose_name_plural = 'Типы перевозок'

    def __str__(self):
        return self.title_type

class Clients(models.Model):
    name_client = models.CharField(max_length=30, verbose_name='Имя клиента')
    number_telephone = models.CharField(max_length=30, verbose_name="Номер телефона")
    adress = models.CharField(max_length=30, verbose_name="Адрес")
    inn = models.IntegerField(default=0, verbose_name="ИНН")
    email = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Клиенты'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.name_client

class Driver(models.Model):
    first_name = models.CharField(max_length=30, verbose_name="Имя")
    last_name = models.CharField(max_length=30, verbose_name="Фамилия")
    number_telephone = models.CharField(max_length=30, verbose_name="Номер телефона")
    salary = models.IntegerField(default=0, verbose_name="Зарплата")
    pasport = models.CharField(max_length=30, verbose_name="Паспорт")
    work_experience = models.CharField(max_length=30, verbose_name="Опыт работы")

    class Meta:
        verbose_name = 'Водители'
        verbose_name_plural = 'Водители'

    def __str__(self):
        return self.last_name + ' ' + self.first_name

class Cargo(models.Model):
    weight = models.CharField(max_length=30, verbose_name="Вес")
    type = models.CharField(max_length=30, verbose_name="Тип")
    cargo_volume = models.CharField(max_length=30, verbose_name="Объем")
    cargo_value = models.IntegerField(default=0, verbose_name="Стоимость")
    dimensions = models.CharField(max_length=30, verbose_name="Габариты")

    class Meta:
        verbose_name = 'Грузы'
        verbose_name_plural = 'Грузы'

class Vehicle(models.Model):
    type_vehicle = models.CharField(max_length=30, verbose_name="Тип")
    registration_number = models.CharField(max_length=30, verbose_name="Регистрационный номер")
    technical_condition = models.CharField(max_length=30, verbose_name="Техническое состояние")
    model = models.CharField(max_length=30, verbose_name="Модель")
    load_capacity = models.CharField(max_length=30, verbose_name="Грузоподьемность")
    insurance_information = models.CharField(max_length=255, verbose_name="Инфо о страховке")

    class Meta:
        verbose_name = 'Техника'
        verbose_name_plural = 'Техника'

class Incidents(models.Model):
    name_incident = models.CharField(max_length=30, verbose_name="Название")
    date_incident = models.DateField(verbose_name="Дата")
    time_incident = models.TimeField(verbose_name="Время")
    type_incident = models.CharField(max_length=30, verbose_name="Тип")
    description = models.TextField(blank=True, verbose_name="Описание")

    class Meta:
        verbose_name = 'Происшествия'
        verbose_name_plural = 'Происшествия'

class Transportation_categories(models.Model):
    category_type = models.CharField(max_length=30, verbose_name="Тип категории")

    class Meta:
        verbose_name = 'Категории перевозок'
        verbose_name_plural = 'Категории перевозок'

class Orders(models.Model):
    name_order = models.CharField(max_length=255, verbose_name="Название")
    date_order = models.DateField(verbose_name="Дата")
    period_execution = models.CharField(max_length=30, verbose_name="Срок выполнения")
    price_order = models.IntegerField(default=0, verbose_name="Цена")
    order_completion_status = models.CharField(max_length=30, verbose_name="Статус выполнения")
    point_departure = models.CharField(max_length=255, verbose_name="Точка отправки")
    point_destination = models.CharField(max_length=255, verbose_name="Точка доставки")
    distance = models.IntegerField(default=0, verbose_name="Расстояние")
    additional_information = models.TextField(blank=True, verbose_name="Доп информация")
    

    class Meta:
        verbose_name = 'Заказы'
        verbose_name_plural = 'Заказы'




