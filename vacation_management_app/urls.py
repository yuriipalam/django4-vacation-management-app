from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('vacation_request', views.vacation_request, name="vacation_request"),
    path('all_requests', views.requests_list, name="requests_list"),
]
