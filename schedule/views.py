from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Schedule
from .forms import ScheduleCreateForm

class ScheduleListView(LoginRequiredMixin, ListView):
    model = Schedule
    template_name = 'schedule/schedule_list.html'
    context_object_name = 'schedule_list'
    #upcoming schedule
    queryset = Schedule.objects.order_by('date')

class ScheduleDetailView(LoginRequiredMixin, DetailView):
    model = Schedule
    template_name = 'schedule/_detail.html'

class ScheduleCreateView(LoginRequiredMixin, CreateView):
    model = Schedule
    form_class =  ScheduleCreateForm
    template_name = 'schedule/schedule_create.html'
    success_url = reverse_lazy('schedule:schedule')

class ScheduleUpdateView(LoginRequiredMixin, UpdateView):
    model = Schedule
    form_class =  ScheduleCreateForm
    template_name = 'schedule/schedule_create.html'
    success_url = reverse_lazy('schedule:schedule')

class ScheduleDeleteView(LoginRequiredMixin, DeleteView):
    model = Schedule
    success_url = reverse_lazy('schedule:schedule')
