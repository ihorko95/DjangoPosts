from django.urls import path
from .views import *

urlpatterns = [
    path('', hello, name='post_list_url'),
    path('post/<str:slug>/', post_detail, name='post_detail_url')
]