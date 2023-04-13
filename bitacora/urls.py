from django.urls import path
from bitacora.views.piloto.views import *


urlpatterns = [
    path('piloto/list/', PilotoListView.as_view(), name='piloto_list'),
    path('piloto/list2/', piloto_list, name='piloto_list2'),
    path('piloto/add/', PilotoCreateView.as_view(), name='piloto_create'),
]
