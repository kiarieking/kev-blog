from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:id>/post_detail', views.post_detail, name='post_detail'),
    path('post_new', views.post_new, name='post_new'),
    path('<int:id>/edit', views.post_edit, name='post_edit')
]