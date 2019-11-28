from django.db import models
from django.urls.base import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Flat(models.Model):  # TODO Приделать slug и внедрить везде где нужно!!!!
    address = models.ForeignKey(
        "Address", verbose_name="Адрес", on_delete=models.PROTECT, null=True, blank=True)
    entrance = models.PositiveSmallIntegerField(
        "Номер подьезда", blank=False, default=1)
    number = models.PositiveSmallIntegerField(
        "Номер квартиры", blank=False, null=False, default=0)
    person = models.ForeignKey(
        "Person", verbose_name="Жилец", on_delete=models.PROTECT)
    active = models.BooleanField("Дежурит?")
    sqare = models.FloatField(
        "Площадь квартиры", blank=True, null=True)  # Площадь квартиры

    number.admin_order_field = 'number'

    class Meta:
        verbose_name = "Квартира"
        verbose_name_plural = "Квартиры"
        unique_together = ('number', 'address')

    def __str__(self):
        return f"Квартира №{self.number:<3} {'' if self.active else 'не'} дежурит"

    def get_update_url(self):
        return reverse('flat_update_url', kwargs={'id': self.id})


class Address(models.Model):
    street = models.ForeignKey("Street", verbose_name="Улица",
                               on_delete=models.PROTECT, null=True)
    home_number = models.PositiveSmallIntegerField(
        "Номер дома", blank=False, default=1)

    class Meta:
        verbose_name = "Адрес дома"
        verbose_name_plural = "Адреса домов"

    def __str__(self):
        return f'ул. {self.street.title}, д.{self.home_number}'


class Street(models.Model):
    title = models.CharField("Название улицы", max_length=100, blank=False)

    class Meta:
        verbose_name = 'улица'
        verbose_name_plural = 'улицы'

    def __str__(self):
        return f'ул. {self.title}'

    def __repr__(self):
        return f'{self.title}'


class Person(models.Model):
    fullname = models.CharField("Полное имя", max_length=50)
    # user = models.OneToOneField(
    #     User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Жилец"
        verbose_name_plural = "Жильцы"

    def __str__(self):
        fname = self.fullname.split(' ')
        return f"{fname[0]} {fname[1][0]}.{fname[2][0]}." if len(fname) == 3 else f"{self.fullname}"

    def __repr__(self):
        return super().__repr__()
        # return super().__reduce__()

    def get_update_url(self):
        return reverse('person_update_url', kwargs={'id': self.id})
