from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from bitacora.forms import PilotoForm
from bitacora.models import *


def piloto_list(request):
    data = {

        'title': 'Listado Piloto',
        'pilotos': Piloto.objects.all()

    }
    return render(request, 'piloto/list.html', data)


class PilotoListView(ListView):
    model = Piloto
    template_name = 'piloto/list.html'

    # @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Piloto.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado Pilotos'
        print(reverse_lazy('piloto_list'))
        return context


class PilotoCreateView(CreateView):
    model = Piloto
    form_class = PilotoForm
    template_name = 'piloto/create.html'
    success_url = reverse_lazy('piloto_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación Piloto'
        return context
