from django.contrib import admin
from django.urls import path, include
from .views import IndexView, LinterView
urlpatterns = [
    path('', IndexView.as_view()),
    path('linter/', LinterView.as_view())
]