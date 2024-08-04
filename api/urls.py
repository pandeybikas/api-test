from django.urls import path
from .views import Student_view_base

urlpatterns = [
    path('', Student_view_base.as_view())
]
