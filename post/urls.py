from django.urls import path

from . import views

app_name = 'post'

urlpatterns = [
    path('', views.post_list, name='post'),
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('create/', views.PostCreate.as_view(), name='post_create'),
    path('update/<int:pk>', views.PostUpdate.as_view(), name='post_update'),
    path('delete/<int:pk>', views.PostDelete.as_view(), name='post_delete'),
    # TO UPLOAD MULTI PHOTOS #
    path('update/image<int:post_pk>', views.post_update_image, name='post_update_image'),
]