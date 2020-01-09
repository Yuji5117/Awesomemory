from django.urls import path

from . import views



app_name = 'schedule'

urlpatterns = [
    path('', views.ScheduleListView.as_view(), name='schedule'),
    path('create/', views.ScheduleCreateView.as_view(), name='schedule_create'),
    path('update/<int:pk>/', views.ScheduleUpdateView.as_view(), name='schedule_update'),
    path('delete/<int:pk>/', views.ScheduleDeleteView.as_view(), name='schedule_delete'),
]