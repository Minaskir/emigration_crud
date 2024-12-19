# from django import forms
# from django.utils.translation import gettext_lazy as _
# from .models import Emigrant
# from bootstrap_datepicker_plus.widgets import DatePickerInput
#
# class EmigrantFilterForm(forms.Form):
#     GENDER_CHOICES = Emigrant.GENDER_CHOICES
#     MARITAL_STATUS_CHOICES = Emigrant.MARITAL_STATUS_CHOICES
#     EDUCATION_CHOICES = Emigrant.EDUCATION_CHOICES
#     NATIONALITY_CHOICES = [(nationality, nationality) for nationality in Emigrant.objects.values_list('nationality', flat=True).distinct()]
#     COUNTRY_CHOICES = [(country, country) for country in Emigrant.objects.values_list('country_of_emigration', flat=True).distinct()]
#
#     gender = forms.ChoiceField(choices=GENDER_CHOICES, required=False)
#     marital_status = forms.ChoiceField(choices=MARITAL_STATUS_CHOICES, required=False)
#     education = forms.ChoiceField(choices=EDUCATION_CHOICES, required=False)
#     nationality = forms.ChoiceField(choices=NATIONALITY_CHOICES, required=False)
#     country_of_emigration = forms.ChoiceField(choices=COUNTRY_CHOICES, required=False)
#
# class EmigrantForm(forms.ModelForm):
#     class Meta:
#         model = Emigrant
#         fields = '__all__'
#         labels = {
#             'last_name': _('Фамилия'),
#             'first_name': _('Имя'),
#             'middle_name': _('Отчество'),
#             'date_of_birth': _('Дата рождения'),
#             'nationality': _('Национальность'),
#             'education': _('Образование'),
#             'academic_degree': _('Ученая степень'),
#             'marital_status': _('Семейное положение'),
#             'gender': _('Пол'),
#             'profession': _('Профессия'),
#             'country_of_emigration': _('Страна эмиграции'),
#             'reason_for_emigration': _('Причина эмиграции'),
#         }
#         widgets = {
#             'date_of_birth': DatePickerInput(options={
#                 'format': 'DD.MM.YYYY',
#                 'locale': 'ru',
#                 'showClose': True,
#                 'showClear': True,
#                 'showTodayButton': True,
#             }),
#             'academic_degree': forms.Select(choices=Emigrant.ACADEMIC_DEGREE_CHOICES),
#             'education': forms.Select(choices=Emigrant.EDUCATION_CHOICES),
#         }

from django import forms
from .models import Emigrant
from django.utils.translation import gettext_lazy as _
from bootstrap_datepicker_plus.widgets import DatePickerInput

class EmigrantFilterForm(forms.Form):
    GENDER_CHOICES = Emigrant.GENDER_CHOICES
    MARITAL_STATUS_CHOICES = Emigrant.MARITAL_STATUS_CHOICES
    EDUCATION_CHOICES = Emigrant.EDUCATION_CHOICES
    NATIONALITY_CHOICES = [(nationality, nationality) for nationality in Emigrant.objects.values_list('nationality', flat=True).distinct()]
    COUNTRY_CHOICES = [(country, country) for country in Emigrant.objects.values_list('country_of_emigration', flat=True).distinct()]

    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=False)
    marital_status = forms.ChoiceField(choices=MARITAL_STATUS_CHOICES, required=False)
    education = forms.ChoiceField(choices=EDUCATION_CHOICES, required=False)
    nationality = forms.ChoiceField(choices=NATIONALITY_CHOICES, required=False)
    country_of_emigration = forms.ChoiceField(choices=COUNTRY_CHOICES, required=False)

class EmigrantForm(forms.ModelForm):
    class Meta:
        model = Emigrant
        fields = '__all__'
        labels = {
            'last_name': _('Фамилия'),
            'first_name': _('Имя'),
            'middle_name': _('Отчество'),
            'date_of_birth': _('Дата рождения'),
            'nationality': _('Национальность'),
            'education': _('Образование'),
            'academic_degree': _('Ученая степень'),
            'marital_status': _('Семейное положение'),
            'gender': _('Пол'),
            'profession': _('Профессия'),
            'country_of_emigration': _('Страна эмиграции'),
            'reason_for_emigration': _('Причина эмиграции'),
        }
        widgets = {
            'last_name': forms.TextInput(attrs={'required': True}),
            'first_name': forms.TextInput(attrs={'required': True}),
            'middle_name': forms.TextInput(attrs={'required': True}),
            'date_of_birth': DatePickerInput(options={
                'format': 'DD.MM.YYYY',
                'locale': 'ru',
                'showClose': True,
                'showClear': True,
                'showTodayButton': True,
            }),
            'academic_degree': forms.Select(choices=Emigrant.ACADEMIC_DEGREE_CHOICES),
            'education': forms.Select(choices=Emigrant.EDUCATION_CHOICES),
        }