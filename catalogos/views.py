from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Pais
from django.db.models import Q
from .forms import PaisForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

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