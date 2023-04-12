from django.urls import path
from .views import holaView

urlpatterns = [
    path('', holaView, name='home')
]
