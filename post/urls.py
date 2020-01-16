from django.urls import path

from . import views


app_name = 'post'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    # path('create/', views.PostCreate.as_view(), name='post_create'),
    path('create/', views.multi_upload, name='post_create'),
    path('update/<int:pk>', views.PostUpdate.as_view(), name='post_update'),
    path('delete/<int:pk>', views.PostDelete.as_view(), name='post_delete'),
    path('comment/<int:post_pk>/', views.comment_create, name='comment_create'),
    path('reply/<int:comment_pk>/', views.reply_create, name='reply_create'),
]