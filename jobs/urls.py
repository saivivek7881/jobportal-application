from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('<int:pk>/', views.job_detail, name='job_detail'),  # Detail page
    path('<int:pk>/apply/', views.apply_job, name='apply_job'),
    #path('<int:pk>/apply/', views.apply_job, name='apply_job'),
    path('application-success/', views.application_success, name='application_success'),

    path('add/', views.add_job, name='add_job'),
]