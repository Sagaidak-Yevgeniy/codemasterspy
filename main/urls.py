from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main_index'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
]
