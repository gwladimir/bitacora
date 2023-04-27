from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.views.decorators.csrf import csrf_exempt
from bitacora.forms import PilotoForm
from bitacora.models import Piloto
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class PilotoListView(ListView):
    model = Piloto
    template_name = 'piloto/list.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
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

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Piloto'
        context['entity'] = 'Pilotos'
        context['list_url'] = reverse_lazy('piloto_list')
        context['action'] = 'add'
        return context


class PilotoUpdateView(UpdateView):
    model = Piloto
    form_class = PilotoForm
    template_name = 'piloto/create.html'
    success_url = reverse_lazy('piloto_list')

    @method_decorator(login_required)
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
        context['title'] = 'Edición de Piloto'
        context['entity'] = 'Pilotos'
        context['list_url'] = reverse_lazy('piloto_list')
        context['action'] = 'edit'
        return context


class PilotoDeleteView(DeleteView):
    model = Piloto
    template_name = 'piloto/delete.html'
    success_url = reverse_lazy('piloto_list')

    @method_decorator(login_required)
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
        context['title'] = 'Emilinación de Piloto'
        context['entity'] = 'Pilotos'
        context['list_url'] = reverse_lazy('piloto_list')
        return context


class PilotoFormView(FormView):
    form_class = PilotoForm
    template_name = 'piloto/create.html'
    success_url = reverse_lazy('piloto_list')

    def form_valid(self, form):
        print(form.is_valid())
        print(form)
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        print(form.is_valid())
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Form | Piloto'
        context['entity'] = 'Pilotos'
        context['list_url'] = reverse_lazy('piloto_list')
        context['action'] = 'add'
        return context
