from django.contrib.auth.models import User
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
    email = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Клиент'
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
        verbose_name = 'Водитель'
        verbose_name_plural = 'Водители'

    def __str__(self):
        return self.last_name + ' ' + self.first_name


class Cargo(models.Model):
    name_cargo = models.CharField(max_length=30, verbose_name="Название груза...")
    weight = models.CharField(max_length=30, verbose_name="Вес")
    type = models.CharField(max_length=30, verbose_name="Тип")
    dimensions = models.CharField(max_length=30, verbose_name="Габариты")
    type_transportation = models.CharField(max_length=30, verbose_name="Тип перевозки")

    class Meta:
        verbose_name = 'Груз'
        verbose_name_plural = 'Грузы'

class Cargos(models.Model):
    name_cargo = models.CharField(max_length=30, verbose_name="Название груза...")
    weight = models.CharField(max_length=30, verbose_name="Вес")
    type = models.CharField(max_length=30, verbose_name="Тип")
    dimensions = models.CharField(max_length=30, verbose_name="Габариты")
    type_transportation = models.CharField(max_length=30, verbose_name="Тип перевозки")
    status = models.CharField(max_length=30, verbose_name="Статус груза", blank=True, default="Не выполнен")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Груз'
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
        verbose_name_plural = 'Техники'


class Incidents(models.Model):
    name_incident = models.CharField(max_length=30, verbose_name="Название")
    date_incident = models.DateField(verbose_name="Дата")
    time_incident = models.TimeField(verbose_name="Время")
    type_incident = models.CharField(max_length=30, verbose_name="Тип")
    description = models.TextField(blank=True, verbose_name="Описание")

    class Meta:
        verbose_name = 'Происшествие'
        verbose_name_plural = 'Происшествия'


class Orders(models.Model):
    name_order = models.CharField(max_length=255, verbose_name="Название", default="Заказ")
    date_order = models.DateField(verbose_name="Дата", auto_now_add=True)
    period_execution = models.CharField(max_length=30, verbose_name="Срок выполнения", default="1 Неделя")
    price_order = models.CharField(verbose_name="Цена", max_length=10, default="0р.")
    order_completion_status = models.CharField(max_length=30, verbose_name="Статус выполнения", default="В обработке")
    point_departure = models.CharField(max_length=255, verbose_name="Точка отправки", default="Москва")
    point_destination = models.CharField(max_length=255, verbose_name="Точка доставки", default="Москва")
    additional_information = models.TextField(blank=True, verbose_name="Доп информация")

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
