from django.urls import path
from .views import GetAllContentView
urlpatterns=[
    path('GetAllContent',GetAllContentView.as_view())
]