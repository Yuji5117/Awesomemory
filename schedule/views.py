from django.contrib import messages
from django.views import generic
from django.urls import reverse_lazy

from .models import Schedule
from .forms import ScheduleCreateForm

class ScheduleListView(generic.ListView):
    model = Schedule
    template_name = 'schedule/schedule_list.html'
    context_object_name = 'schedule_list'
    #upcoming schedule
    queryset = Schedule.objects.order_by('date')

class ScheduleDetailView(generic.DetailView):
    model = Schedule
    template_name = 'schedule/_detail.html'

class ScheduleCreateView(generic.CreateView):
    model = Schedule
    form_class =  ScheduleCreateForm
    template_name = 'schedule/schedule_create.html'
    success_url = reverse_lazy('schedule:schedule')

class ScheduleUpdateView(generic.UpdateView):
    model = Schedule
    form_class =  ScheduleCreateForm
    template_name = 'schedule/schedule_create.html'
    success_url = reverse_lazy('schedule:schedule')

class ScheduleDeleteView(generic.DeleteView):
    model = Schedule
    success_url = reverse_lazy('schedule:schedule')
