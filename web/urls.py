from django.urls import path
from . import views

urlpatterns = [
    # workarea
    path('admin/', views.workarea, name='workarea'),
    # website
    path('', views.home, name='home'),
]
