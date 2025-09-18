from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import CustomUserForm
from .models import CustomUser


class BirthdayListView(ListView):
    model = CustomUser
    template_name = 'home.html'
    context_object_name = 'users'


class BirthdayCreateView(CreateView):
    model = CustomUser
    form_class = CustomUserForm
    template_name = 'add_birthday.html'
    success_url = reverse_lazy('home')


class BirthdayUpdateView(UpdateView):
    model = CustomUser
    form_class = CustomUserForm
    template_name = 'add_birthday.html'
    success_url = reverse_lazy('home')


class BirthdayDeleteView(DeleteView):
    model = CustomUser
    template_name = 'delete_birthday.html'
    success_url = reverse_lazy('home')

