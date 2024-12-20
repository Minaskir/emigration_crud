from django.urls import path
from .views import (
    EmigrantListView, EmigrantDetailView, EmigrantCreateView, EmigrantUpdateView, EmigrantDeleteView,
    emigrant_card, emigrant_reports, HomeView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),  # Главная страница
    path('emigrants/', EmigrantListView.as_view(), name='emigrant_list'),
    path('<int:pk>/', EmigrantDetailView.as_view(), name='emigrant_detail'),
    path('create/', EmigrantCreateView.as_view(), name='emigrant_create'),
    path('<int:pk>/update/', EmigrantUpdateView.as_view(), name='emigrant_update'),
    path('<int:pk>/delete/', EmigrantDeleteView.as_view(), name='emigrant_delete'),
    path('<int:pk>/card/', emigrant_card, name='emigrant_card'),
    path('reports/', emigrant_reports, name='emigrant_reports'),
]