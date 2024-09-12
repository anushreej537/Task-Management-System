from django.urls import path
from task_app import views

urlpatterns = [
    path('',views.home),
    path('addemp/',views.addemp),
    path('employee/',views.employee),
    path('project/',views.project)
]
