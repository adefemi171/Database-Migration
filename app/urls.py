from django.urls import path
from app import views

urlpatterns = [
    path('',views.index_page),
    path('api/v1/signup',views.index_page)
]