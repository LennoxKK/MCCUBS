from django.urls import path

from .views import personal_portfolio
urlpatterns = [
    path('',personal_portfolio),
]