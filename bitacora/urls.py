from django.urls import path
from bitacora.views.piloto.views import *


urlpatterns = [
    path('piloto/list/', PilotoListView.as_view(), name='piloto_list'),
    path('piloto/add/', PilotoCreateView.as_view(), name='piloto_create'),
    path('piloto/edit/<int:pk>/', PilotoUpdateView.as_view(), name='piloto_update'),
    path('piloto/delete/<int:pk>/', PilotoDeleteView.as_view(), name='piloto_delete'),
]
