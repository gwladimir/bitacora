from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from bitacora.forms import PilotoForm
from bitacora.models import Piloto


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
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Piloto.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado Pilotos'
        context['create_url'] = reverse_lazy('piloto_create')
        context['list_url'] = reverse_lazy('piloto_list')
        context['entity'] = 'Pilotos'
        return context


class PilotoCreateView(CreateView):
    model = Piloto
    form_class = PilotoForm
    template_name = 'piloto/create.html'
    success_url = reverse_lazy('piloto_list')

    def post(self, request, *arg, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    #     print(request.POST)
    #     form = PilotoForm(request.POST)
    #     if form.is_valid():
    #         form.save
    #         return HttpResponseRedirect(self.success_url)
    #     self.object = None
    #     context = self.get_context_data(**kwargs)
    #     context['form'] = form
    #     return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación Piloto'
        context['entity'] = 'Pilotos'
        context['list_url'] = reverse_lazy('piloto_list')
        context['action'] = 'add'
        return context


class PilotoUpdateView(UpdateView):
    model = Piloto
    form_class = PilotoForm
    template_name = 'piloto/create.html'
    success_url = reverse_lazy('piloto_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *arg, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición un Piloto'
        context['entity'] = 'Pilotos'
        context['list_url'] = reverse_lazy('piloto_list')
        context['action'] = 'edit'
        return context


class PilotoDeleteView(DeleteView):
    model = Piloto
    template_name = 'piloto/delete.html'
    success_url = reverse_lazy('piloto_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Emilinar un Piloto'
        context['entity'] = 'Pilotos'
        context['list_url'] = reverse_lazy('piloto_list')
        return context
