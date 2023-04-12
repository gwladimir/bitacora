from django.shortcuts import render

from bitacora.models import Piloto


def piloto_list(request):
    data ={

        'title': 'Listado Piloto',
        'pilotos': Piloto.objects.all()

    }
    return render(request,'piloto/list.html', data)