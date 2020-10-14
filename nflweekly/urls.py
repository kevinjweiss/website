from django.urls import path
from . import views

urlpatterns = [
    path("", views.weekly_index, name="weekly_index"),
    path("<int:pk>/", views.weekly_detail, name="weekly_detail"),
]