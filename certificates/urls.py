from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.certificate_detail, name='certificate_detail'),
]
