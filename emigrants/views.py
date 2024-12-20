# from django.http import JsonResponse
# from django.shortcuts import render, get_object_or_404, redirect
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from django.utils import timezone
# from django.db.models import Count
# from .models import Emigrant
# from .forms import EmigrantForm, EmigrantFilterForm
# from django.db.models import Q
# from .filters import EmigrantFilter
#
# class EmigrantListView(ListView):
#     model = Emigrant
#     template_name = 'emigrants/emigrant_list.html'
#     context_object_name = 'emigrants'
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         filter_form = EmigrantFilterForm(self.request.GET)
#         if filter_form.is_valid():
#             filters = {k: v for k, v in filter_form.cleaned_data.items() if v}
#             queryset = queryset.filter(**filters)
#         return queryset
#
# class EmigrantDetailView(DetailView):
#     model = Emigrant
#     template_name = 'emigrants/emigrant_detail.html'
#     context_object_name = 'emigrant'
#
# class EmigrantCreateView(CreateView):
#     model = Emigrant
#     form_class = EmigrantForm
#     template_name = 'emigrants/emigrant_form.html'
#     success_url = '/emigrants/'
#
# class EmigrantUpdateView(UpdateView):
#     model = Emigrant
#     form_class = EmigrantForm
#     template_name = 'emigrants/emigrant_form.html'
#     success_url = '/emigrants/'
#
# class EmigrantDeleteView(DeleteView):
#     model = Emigrant
#     template_name = 'emigrants/emigrant_confirm_delete.html'
#     success_url = '/emigrants/'
#
# def emigrant_card(request, pk):
#     emigrant = get_object_or_404(Emigrant, pk=pk)
#     return render(request, 'emigrants/emigrant_card.html', {'emigrant': emigrant})
#
#
# def emigrant_reports(request):
#     # Создаем фильтр на основе запроса
#     filter_set = EmigrantFilter(request.GET, queryset=Emigrant.objects.all())
#     queryset = filter_set.qs  # Отфильтрованный QuerySet
#
#     # Получаем уникальные значения для национальностей и стран эмиграции
#     nationalities = Emigrant.objects.values_list('nationality', flat=True).distinct()
#     countries_of_emigration = Emigrant.objects.values_list('country_of_emigration', flat=True).distinct()
#
#     # Подсчитываем количество эмигрантов, соответствующих выбранным фильтрам
#     total_emigrants = queryset.count()
#
#     # Получаем список эмигрантов, соответствующих выбранным фильтрам
#     emigrants_list = queryset
#
#     # Группировка данных для отчетов
#     reports = {
#         'age_groups': list(
#             queryset.extra(select={
#                 'age_group': "CASE "
#                              "WHEN EXTRACT(YEAR FROM date_of_birth) >= EXTRACT(YEAR FROM CURRENT_DATE) - 18 THEN 'Моложе 18' "
#                              "ELSE 'Старше 18' END"
#             }).values('age_group').annotate(count=Count('id')).order_by('age_group')
#         ),
#         'gender': list(queryset.values('gender').annotate(count=Count('id')).order_by('-count')),
#         'education': list(queryset.values('education').annotate(count=Count('id')).order_by('-count')),
#         'nationality': list(queryset.values('nationality').annotate(count=Count('id')).order_by('-count')),
#         'marital_status': list(queryset.values('marital_status').annotate(count=Count('id')).order_by('-count')),
#         'preferred_countries': list(
#             queryset.values('country_of_emigration').annotate(count=Count('id')).order_by('-count')),
#     }
#
#     if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
#         return JsonResponse(reports)
#
#     return render(
#         request,
#         'emigrants/emigrant_reports.html',
#         {
#             'reports': reports,
#             'filter_set': filter_set,
#             'nationalities': nationalities,
#             'countries_of_emigration': countries_of_emigration,
#             'total_emigrants': total_emigrants,
#             'emigrants_list': emigrants_list,
#         }
#     )

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.utils import timezone
from django.db.models import Count
from .models import Emigrant
from .forms import EmigrantForm, EmigrantFilterForm
from django.db.models import Q
from .filters import EmigrantFilter
from django.db import OperationalError
from django.http import HttpResponseServerError
class HomeView(TemplateView):
    template_name = 'emigrants/home.html'
def emigrant_create(request):
    try:
        # Искусственно выбрасываем исключение
        raise Exception("Тестовое исключение для проверки обработки ошибок")

        if request.method == 'POST':
            form = EmigrantForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('emigrant_list')
        else:
            form = EmigrantForm()
        return render(request, 'emigrants/emigrant_form.html', {'form': form})
    except Exception as e:
        return render(request, 'emigrants/error.html', {
            'error_message': 'Произошла внутренняя ошибка сервера. Пожалуйста, попробуйте позже или обратитесь к администратору.',
            'error_details': str(e)
        }, status=500)

class EmigrantListView(ListView):
    model = Emigrant
    template_name = 'emigrants/emigrant_list.html'
    context_object_name = 'emigrants'

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_form = EmigrantFilterForm(self.request.GET)
        if filter_form.is_valid():
            filters = {k: v for k, v in filter_form.cleaned_data.items() if v}
            queryset = queryset.filter(**filters)
        return queryset

class EmigrantDetailView(DetailView):
    model = Emigrant
    template_name = 'emigrants/emigrant_detail.html'
    context_object_name = 'emigrant'

class EmigrantCreateView(CreateView):
    model = Emigrant
    form_class = EmigrantForm
    template_name = 'emigrants/emigrant_form.html'
    success_url = '/emigrants/'

class EmigrantUpdateView(UpdateView):
    model = Emigrant
    form_class = EmigrantForm
    template_name = 'emigrants/emigrant_form.html'
    success_url = '/emigrants/'

class EmigrantDeleteView(DeleteView):
    model = Emigrant
    template_name = 'emigrants/emigrant_confirm_delete.html'
    success_url = '/emigrants/'

def emigrant_card(request, pk):
    emigrant = get_object_or_404(Emigrant, pk=pk)
    return render(request, 'emigrants/emigrant_card.html', {'emigrant': emigrant})

def emigrant_reports(request):
    # Создаем фильтр на основе запроса
    filter_set = EmigrantFilter(request.GET, queryset=Emigrant.objects.all())
    queryset = filter_set.qs  # Отфильтрованный QuerySet

    # Получаем уникальные значения для национальностей и стран эмиграции
    nationalities = Emigrant.objects.values_list('nationality', flat=True).distinct()
    countries_of_emigration = Emigrant.objects.values_list('country_of_emigration', flat=True).distinct()

    # Подсчитываем количество эмигрантов, соответствующих выбранным фильтрам
    total_emigrants = queryset.count()

    # Получаем список эмигрантов, соответствующих выбранным фильтрам
    emigrants_list = queryset

    # Группировка данных для отчетов
    reports = {
        'age_groups': list(
            queryset.extra(select={
                'age_group': "CASE "
                             "WHEN EXTRACT(YEAR FROM date_of_birth) >= EXTRACT(YEAR FROM CURRENT_DATE) - 18 THEN 'Моложе 18' "
                             "ELSE 'Старше 18' END"
            }).values('age_group').annotate(count=Count('id')).order_by('age_group')
        ),
        'gender': list(queryset.values('gender').annotate(count=Count('id')).order_by('-count')),
        'education': list(queryset.values('education').annotate(count=Count('id')).order_by('-count')),
        'nationality': list(queryset.values('nationality').annotate(count=Count('id')).order_by('-count')),
        'marital_status': list(queryset.values('marital_status').annotate(count=Count('id')).order_by('-count')),
        'preferred_countries': list(
            queryset.values('country_of_emigration').annotate(count=Count('id')).order_by('-count')),
    }

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse(reports)

    return render(
        request,
        'emigrants/emigrant_reports.html',
        {
            'reports': reports,
            'filter_set': filter_set,
            'nationalities': nationalities,
            'countries_of_emigration': countries_of_emigration,
            'total_emigrants': total_emigrants,
            'emigrants_list': emigrants_list,
        }
    )




