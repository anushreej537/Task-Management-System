from django.urls import path
from task_app import views

urlpatterns = [
    path('',views.home)
]
