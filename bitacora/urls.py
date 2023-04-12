from django.urls import path
from bitacora.views.piloto.views import piloto_list


urlpatterns = [
    path('piloto/list/', piloto_list, name='piloto_list'),
]
