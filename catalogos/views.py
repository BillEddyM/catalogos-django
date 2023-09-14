from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Pais, Departamento, Municipio
from django.db.models import Q
from .forms import PaisForm, DepartamentoForm, MunicipioForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy

class PaisListView(ListView):
    model = Pais
    template_name = 'pais/pais_list.html'
    context_object_name = 'paises'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Pais.objects.filter(Q(nombre__icontains=query) | Q(codigo__icontains=query))
        else:
            return Pais.objects.all()

class PaisCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Pais
    form_class = PaisForm
    template_name = 'pais/pais_form.html'
    success_url = reverse_lazy('pais_list')
    login_url = reverse_lazy('login')
    permission_required = 'catalogos.add_pais'

class PaisUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Pais
    form_class = PaisForm
    template_name = 'pais/pais_form.html'
    success_url = reverse_lazy('pais_list')
    login_url = reverse_lazy('login')
    permission_required = 'catalogos.change_pais'

class PaisDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Pais
    template_name = 'pais/pais_confirm_delete.html'
    success_url = reverse_lazy('pais_list')
    login_url = reverse_lazy('login')
    permission_required = 'catalogos.delete_pais'

class DepartamentoListView(ListView):
    model = Departamento
    template_name = 'departamento/departamento_list.html'
    context_object_name = 'departamentos'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Departamento.objects.filter(Q(nombre__icontains=query) | Q(codigo__icontains=query))
        else:
            return Departamento.objects.all()

class DepartamentoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Departamento
    form_class = DepartamentoForm
    template_name = 'departamento/departamento_form.html'
    success_url = reverse_lazy('departamento_list')
    login_url = reverse_lazy('login')
    permission_required = 'catalogos.add_departamento'

class DepartamentoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Departamento
    form_class = DepartamentoForm
    template_name = 'departamento/departamento_form.html'
    success_url = reverse_lazy('departamento_list')
    login_url = reverse_lazy('login')
    permission_required = 'catalogos.change_departamento'

class DepartamentoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Departamento
    template_name = 'departamento/departamento_confirm_delete.html'
    success_url = reverse_lazy('departamento_list')
    login_url = reverse_lazy('login')
    permission_required = 'catalogos.delete_departamento'

class MunicipioListView(ListView):
    model = Municipio
    template_name = 'municipio/municipio_list.html'
    context_object_name = 'municipios'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Municipio.objects.filter(Q(nombre__icontains=query) | Q(codigo__icontains=query))
        else:
            return Municipio.objects.all()

class MunicipioCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Municipio
    form_class = MunicipioForm
    template_name = 'municipio/municipio_form.html'
    success_url = reverse_lazy('municipio_list')
    login_url = reverse_lazy('login')
    permission_required = 'catalogos.add_municipio'

class MunicipioUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Municipio
    form_class = MunicipioForm
    template_name = 'municipio/municipio_form.html'
    success_url = reverse_lazy('municipio_list')
    login_url = reverse_lazy('login')
    permission_required = 'catalogos.change_municipio'

class MunicipioDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Municipio
    template_name = 'municipio/municipio_confirm_delete.html'
    success_url = reverse_lazy('municipio_list')
    login_url = reverse_lazy('login')
    permission_required = 'catalogos.delete_municipio'