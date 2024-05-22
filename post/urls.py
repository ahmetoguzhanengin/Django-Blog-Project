
from django.urls import path
from .views import post_index, post_detail, post_create, post_update, post_delete

app_name = 'post'


urlpatterns = [
    path('index/', post_index, name = 'index'),
    path('create/', post_create, name = 'create'),
    path('<slug:slug>/', post_detail, name='detail'),

    path('<slug:slug>/update/', post_update, name = 'update'),
    path('<slug:slug>/delete/', post_delete, name = 'delete'),
]
