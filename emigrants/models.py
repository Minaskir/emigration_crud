from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re

def validate_name(value):
    """
    Валидатор для ФИО:
    - Проверяет, что значение начинается с большой букв.
    - Проверяет, что значение не содержит цифр.
    - Проверяет, что значение не пустое.
    """
    if not value:
        raise ValidationError('Это поле обязательно для заполнения.')
    if not value[0].isupper():
        raise ValidationError('Значение должно начинаться с большой буквы.')
    if not re.match(r'^[А-Яа-яёЁ\s-]+$', value):
        raise ValidationError('Значение должно содержать только буквы, пробелы или дефисы.')
    if len(value.replace(' ', '').replace('-', '')) < 2:
        raise ValidationError('Значение должно содержать не менее двух букв.')

class Emigrant(models.Model):
    last_name = models.CharField(max_length=100, verbose_name=_('Фамилия'), validators=[validate_name])
    first_name = models.CharField(max_length=100, verbose_name=_('Имя'), validators=[validate_name])
    middle_name = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('Отчество'), validators=[validate_name])

class Emigrant(models.Model):
    GENDER_CHOICES = [
        ('M', _('Мужской')),
        ('F', _('Женский')),
    ]
    MARITAL_STATUS_CHOICES = [
        ('single', _('Холост/Не замужем')),
        ('married', _('Женат/Замужем')),
        ('divorced', _('Разведен/Разведена')),
        ('widowed', _('Вдовец/Вдова')),
    ]
    EDUCATION_CHOICES = [
        ('none', _('Нет')),
        ('secondary', _('Среднее')),
        ('vocational', _('Среднее профессиональное')),
        ('higher', _('Высшее')),
    ]
    ACADEMIC_DEGREE_CHOICES = [
        ('none', _('Отсутствует')),
        ('bachelor', _('Бакалавр')),
        ('master', _('Магистр')),
        ('phd', _('Доктор наук')),
    ]
    NATIONALITY_CHOICES = [
        ('russian', _('Русский')),
        ('armenian', _('Армянин')),
        ('tatar', _('Татарин')),
        ('uzbek', _('Узбек')),
        ('dagestanez', _('Дагестанец')),
        ('chechenez', _('Чеченец')),
        # Добавьте другие национальности по необходимости
    ]
    PROFESSION_CHOICES = [
        ('engineer', _('Инженер')),
        ('doctor', _('Врач')),
        ('teacher', _('Учитель')),
        ('programmist', ('Программист')),
        ('test', _('Тестировщик')),
        ('povar', _('Повар')),
        # Добавьте другие профессии по необходимости
    ]
    COUNTRY_OF_EMIGRATION_CHOICES = [
        ('russia', _('Россия')),
        ('armenia', _('Армения')),
        ('tatarstan', _('Республика Татарстан')),
        ('uzbekistan', _('Узбекистан')),
        ('dagestan', _('Дагестан')),
        ('checnya', _('Чечня')),
        # Добавьте другие страны по необходимости
    ]

    last_name = models.CharField(max_length=100, verbose_name=_('Фамилия'), validators=[validate_name])
    first_name = models.CharField(max_length=100, verbose_name=_('Имя'), validators=[validate_name])
    middle_name = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('Отчество'), validators=[validate_name])
    date_of_birth = models.DateField(verbose_name=_('Дата рождения'))
    nationality = models.CharField(max_length=100, choices=NATIONALITY_CHOICES, verbose_name=_('Национальность'))
    education = models.CharField(max_length=100, choices=EDUCATION_CHOICES, verbose_name=_('Образование'))
    academic_degree = models.CharField(max_length=100, blank=True, null=True, choices=ACADEMIC_DEGREE_CHOICES, verbose_name=_('Ученая степень'))
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS_CHOICES, verbose_name=_('Семейное положение'))
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name=_('Пол'))
    profession = models.CharField(max_length=100, choices=PROFESSION_CHOICES, verbose_name=_('Профессия'))
    country_of_emigration = models.CharField(max_length=100, choices=COUNTRY_OF_EMIGRATION_CHOICES, verbose_name=_('Страна эмиграции'))
    reason_for_emigration = models.TextField(verbose_name=_('Причина эмиграции'))

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    def get_education_display(self):
        return dict(self.EDUCATION_CHOICES).get(self.education, self.education)

    def get_academic_degree_display(self):
        return dict(self.ACADEMIC_DEGREE_CHOICES).get(self.academic_degree, self.academic_degree)
    def get_profession_display(self):
        return dict(self.PROFESSION_CHOICES).get(self.profession, self.profession)
    def get_nationality_display(self):
        return dict(self.NATIONALITY_CHOICES).get(self.nationality, self.nationality)
    def get_country_of_emigration_display(self):
        return dict(self.COUNTRY_OF_EMIGRATION_CHOICES).get(self.country_of_emigration, self.country_of_emigration)