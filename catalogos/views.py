from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Pais
from .forms import PaisForm


class PaisListView(LoginRequiredMixin, ListView):
    model = Pais
    template_name = 'pais/pais_list.html'
    context_object_name = 'paises'
    login_url = reverse_lazy('login')


class PaisCreateView(LoginRequiredMixin, CreateView):
    model = Pais
    form_class = PaisForm
    template_name = 'pais/pais_form.html'
    success_url = reverse_lazy('pais_list')
    login_url = reverse_lazy('login')


class PaisUpdateView(LoginRequiredMixin, UpdateView):
    model = Pais
    form_class = PaisForm
    template_name = 'pais/pais_form.html'
    success_url = reverse_lazy('pais_list')
    login_url = reverse_lazy('login')


class PaisDeleteView(LoginRequiredMixin, DeleteView):
    model = Pais
    template_name = 'pais/pais_confirm_delete.html'
    success_url = reverse_lazy('pais_list')
    login_url = reverse_lazy('login')
