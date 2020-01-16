from django.urls import path

from . import views


app_name = 'accounts'

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name="signup"),
    path('profile/<int:pk>/', views.UserProfileView.as_view(), name="profile"),
    path('profile/<int:pk>/update/', views.UserProfileUpdateView.as_view(), name="update_profile"),
]